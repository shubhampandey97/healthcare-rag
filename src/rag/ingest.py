"""Step 1: read PDFs page by page -> data/processed/pages.jsonl"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

# WHO Weekly Epidemiological Record: English column left, French column right.
# Measured gap between the columns: x = 270-290 on a 595-pt page -> split at 47 %.
GUTTER = 0.47
FR_WORDS = {"les", "des", "est", "une", "dans", "pour", "sont", "qui", "aux", "avec",
            "été", "être", "du", "au", "sur", "par", "ces", "le", "la"}
EN_WORDS = {"the", "and", "of", "is", "are", "with", "for", "which", "that", "by",
            "be", "this", "in"}


def clean_text(text: str) -> str:
    text = text.replace("­", "")  # soft hyphens
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)  # join words split across lines
    text = re.sub(r"[ \t]+", " ", text)  # collapse spaces
    text = re.sub(r"\n{3,}", "\n\n", text)  # at most one blank line
    return text.strip()


def repeated_lines(pages: list[str], min_share: float = 0.5) -> set[str]:
    """Lines found on at least half of the pages = running headers/footers."""
    n = len(pages)
    if n < 4:  # too few pages to tell boilerplate from content
        return set()
    counts: Counter[str] = Counter()
    for page in pages:
        counts.update({ln.strip() for ln in page.splitlines() if ln.strip()})
    return {ln for ln, c in counts.items() if c / n >= min_share}


def french_share(text: str) -> float:
    """Share of common function words that are French (0 = English, 1 = French)."""
    words = re.findall(r"[a-zà-ÿ]+", text.lower())
    fr = sum(w in FR_WORDS for w in words)
    en = sum(w in EN_WORDS for w in words)
    return fr / (fr + en) if fr + en else 0.0


def is_bilingual_doc(lefts: list[str], rights: list[str]) -> bool:
    """True if most pages have English on the left and French on the right."""
    hits = sum(french_share(r) > 0.6 and french_share(lt) < 0.2 for lt, r in zip(lefts, rights))
    return hits >= 0.5 * len(lefts)


def read_pdf(path: Path) -> tuple[list[dict], bool]:
    import pymupdf  # imported here so tests run without it

    with pymupdf.open(path) as doc:
        full, lefts, rights = [], [], []
        for page in doc:
            w, h = page.rect.width, page.rect.height
            full.append(page.get_text("text"))
            lefts.append(page.get_text("text", clip=pymupdf.Rect(0, 0, w * GUTTER, h)))
            rights.append(page.get_text("text", clip=pymupdf.Rect(w * GUTTER, 0, w, h)))

    bilingual = is_bilingual_doc(lefts, rights)
    raw = lefts if bilingual else full
    boiler = repeated_lines(raw)
    records = []
    for i, txt in enumerate(raw, start=1):
        kept = "\n".join(ln for ln in txt.splitlines() if ln.strip() not in boiler)
        text = clean_text(kept)
        records.append({"doc_id": path.stem, "page": i, "text": text,
                        "n_chars": len(text), "english_column_only": bilingual})
    return records, bilingual


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="data/raw")
    ap.add_argument("--out", default="data/processed/pages.jsonl")
    args = ap.parse_args()

    pdfs = sorted(Path(args.raw).glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {args.raw}")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for pdf in pdfs:
            recs, bilingual = read_pdf(pdf)
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
            near_empty = [r["page"] for r in recs if r["n_chars"] < 100]
            total = sum(r["n_chars"] for r in recs)
            french = round(sum(french_share(r["text"]) for r in recs) / len(recs), 2)
            print(f"{pdf.name}: {len(recs)} pages, {total:,} chars, bilingual={bilingual}, "
                  f"french_share={french}, near-empty pages: {near_empty[:10]}")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
