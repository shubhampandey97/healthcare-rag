# Sources

All documents were downloaded on 2026-11-10 into `data/raw/` (not stored in git).
To rebuild the data, download each file from its link and save it under the file name shown.

| File name | Document | Publisher | Version / status | Pages | Link |
|---|---|---|---|---|---|
| who_table1_routine_2025-12.pdf | Table 1: Summary of WHO Position Papers – Recommendations for Routine Immunization | WHO | December 2025 | 13 | https://www.who.int/publications/m/item/table-1-who-recommendations-for-routine-immunization |
| who_measles_pp_2017.pdf | Measles vaccines: WHO position paper | WHO (Weekly Epidemiological Record) | April 2017, English/French | 24 | https://www.who.int/publications/i/item/who-wer9217-205-227 |
| who_hepb_pp_2017.pdf | Hepatitis B vaccines: WHO position paper | WHO (Weekly Epidemiological Record) | July 2017, English/French | 24 | https://www.who.int/publications/i/item/WER9227 |
| who_hpv_pp_2022.pdf | Human papillomavirus vaccines: WHO position paper | WHO (Weekly Epidemiological Record) | December 2022, English/French; replaces the 2017 paper | 28 | https://who.int/publications/i/item/who-wer9750-645-672 |
| fda_pccp_ai_final.pdf | Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions | US FDA | Final guidance | 49 | https://www.fda.gov/media/166704/download |
| fda_ai_lifecycle_draft_2025.pdf | Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations | US FDA | DRAFT guidance, January 2025 (not for implementation) | 67 | https://www.fda.gov/media/184856/download |
| gmlp_principles_2021.pdf | Good Machine Learning Practice for Medical Device Development: Guiding Principles | FDA, Health Canada, UK MHRA | October 2021 | 2 | https://www.fda.gov/media/153486/download |
| pccp_principles_2023.pdf | Predetermined Change Control Plans for Machine Learning-Enabled Medical Devices: Guiding Principles | FDA, Health Canada, UK MHRA | October 2023 | 2 | https://www.fda.gov/media/173206/download |
| transparency_principles_2024.pdf | Transparency for Machine Learning-Enabled Medical Devices: Guiding Principles | FDA, Health Canada, UK MHRA | June 2024 | 4 | https://www.fda.gov/media/179269/download |
| mdcg_2025-6.pdf | MDCG 2025-6 / AIB 2025-1: FAQ on Interplay between the MDR & IVDR and the Artificial Intelligence Act | European Commission (MDCG + AI Board) | June 2025 | 27 | https://health.ec.europa.eu/document/download/b78a17d7-e3cd-4943-851d-e02a2f22bbb4_en?filename=mdcg_2025-6_en.pdf |

## Notes
- The WHO position papers print English and French side by side; the ingestion step keeps the English column only.
- `fda_ai_lifecycle_draft_2025.pdf` is a draft. Answers based on it must not be presented as a final FDA requirement.
- The earlier WHO link `cdn.who.int/.../table_1_january_2025_web_english.pdf` no longer works (BlobNotFound); WHO replaced it with the December 2025 version.
