from rag.ingest import clean_text, french_share, is_bilingual_doc, repeated_lines

EN = "The vaccine is recommended for all children and the schedule is flexible."
FR = "Le vaccin est recommandé pour tous les enfants dans les pays et la vaccination des filles."


def test_joins_word_split_across_lines():
    assert clean_text("vacci-\nnation") == "vaccination"


def test_collapses_whitespace():
    assert clean_text("a   b\n\n\n\nc") == "a b\n\nc"


def test_detects_running_header():
    pages = [f"WHO Guideline\nbody {i}" for i in range(4)]
    assert repeated_lines(pages) == {"WHO Guideline"}


def test_short_document_keeps_everything():
    assert repeated_lines(["x", "x"]) == set()


def test_french_share_separates_languages():
    assert french_share(EN) < 0.2
    assert french_share(FR) > 0.6
    assert french_share("") == 0.0


def test_bilingual_doc_detected_even_if_some_pages_miss():
    lefts = [EN] * 4
    rights = [FR, FR, FR, EN]  # last page: right column is English references
    assert is_bilingual_doc(lefts, rights)


def test_english_two_column_doc_not_clipped():
    assert not is_bilingual_doc([EN] * 4, [EN] * 4)
