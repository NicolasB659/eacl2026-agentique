[![Hugging Face App](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-App-yellow)](https://huggingface.co/spaces/ENC-PSL/lrec2026-llm-annotator)

> **[May 22, 2026]**: An open and ready to use [webapp](https://huggingface.co/spaces/ENC-PSL/lrec2026-llm-annotator), based on this repo and the LREC Tutorial, is now available on Hugging Face (required an API key)!

### Lemmatization and POS-tagging of historical languages using LLM

This repository contains the experimental framework and code for the paper:

"Under-resourced studies of under-resourced languages: lemmatization and POS-tagging with LLM annotators for historical Armenian, Georgian, Greek and Syriac" (Vidal-Gorène et al., 2025).

**Abstract**: Low-resource historical languages pose persistent challenges for NLP tasks such as lemmatization and part-of-speech (POS) tagging. This project investigates the capacity of Large Language Models (LLMs), including GPT-4 variants and open-weight Mistral models, to address these tasks in zero-shot and few-shot settings. We focus on four diverse languages: Ancient Greek, Classical Armenian, Old Georgian, and Syriac.

#### Repository structure

```
├── data
│   ├── corpus              # Train/Test TSV files (in-domain and out-of-domain)
│   ├── prompt-templates    # Text templates for zero-shot and few-shot (5, 50, 500)
│   └── tagsets             # Language-specific POS tagsets
├── pie-baseline            # Configuration and models for the PIE baseline mentioned in the paper
├── results                 # Raw outputs of the paper
├── scripts                 # Core logic
│   ├── config.py           # Configuration (API keys, task definitions)
│   ├── main.py             # Execution script
│   └── utils.py            # Helper functions
├── requirements.txt
└── README.md
```

### EACL 2026 - Corpus

#### GRC (greek)
* GRC_train = John Anagnostes, De Thessalonica Capta, Chap. 1 - 14 (15th c. AD - Historiography - 4.700 words)
* GRC_test (in-domain) = John Anagnostes, De Thessalonica Capta, Chap. 1 - 14 (15th c. AD - Historiography - 300 words)
* GRC_test (out-of-domain) = Grégoire de Nazianze, Homily 1, Chap. 1 - 4 (4th c. AD - Patristics, Homiletic - 300 words)

#### HYE (armenian)
* HYE_train = Evagrius, Letters (13th cent. AD - epistolography, ascetism - 4.700 words)
* HYE_test (in-domain) = Evagrius, Letters (13th cent. AD - epistolography, ascetism - 300 words)
* HYE_test (out-of-domain) = Step'anos of Siwnik' (Dub.), The Genesis Commentary, 2.1.1. - 2.1.20 (8th-9th cent. AD - exegesis, theology - 300 words)

#### KAT (georgian)
* KAT_train = Anonymus - Conversion of the Kartli, Chap. 1, Tit. - Chap. 3, Par. 4 (5th-9th cent. AD - hagiography, historiography - 4.700 words)
* KAT_test (in-domain) = Anonymus - Conversion of the Kartli, Chap. 1, Tit. - Chap. 3, Par. 4 (5th-9th cent. AD - hagiography, historiography - 300 words)
* KAT_test (out-of-domain) = History of the Rechabites by Zosimus (Text 2, Chap. 1-10) (8th-10th cent. AD - hagiography, historiography - 300 words)

#### SYC (syriac)
* SYC_train = Jacob of Serugh, Homilies (5th-6th c. AD - patristics, homiletic - 4.000 words)
* SYC_test (in-domain) = Jacob of Serugh, Homilies (5th-6th c. AD - patristics, homiletic - 300 words)
* SYC_test (out-of-domain) = History of the Rechabites by Zosimus (Long Version), Chap. 1, Tit. - Chap. 1, Par. 3 (4th cent. AD - hagiography, pseudepigraphs - 300 words)

## How to use it
### Getting started

1. Installation 
```bash
git clone https://github.com/anonymous/EACL2026_historical_languages.git
cd EACL2026_historical_languages
pip install -r requirements.txt
```

2. Configuration
Edit the config.py file to include your API keys, select models and define your local file paths:

```json
OPENAI_API_KEY = "your_key_here"
MISTRAL_API_KEY = "your_key_here"

TASKS = [
    {
        "name": "Zero Shot Armenian",
        "template": "path/to/template.txt",
        "test_file": "path/to/test.tsv",
        "tagset": "path/to/tagset.txt",
        "models": [
            {"provider": "openai", "name": "gpt-4o-mini"},
            {"provider": "mistral", "name": "mistral-large-latest"}
        ]
    }
]
```

To adapt the code to your language, you will have to update the `tagset`, the `prompt` and samples to provide.

3. Usage
Run the main script to start the annotation process:
```bash
python main.py
```

### How to cite

```latex
@inproceedings{vidal-gorene-etal-2026-resourced,
    title = "Under-resourced studies of under-resourced languages: lemmatization and {POS}-tagging with {LLM} annotators for historical {A}rmenian, {G}eorgian, {G}reek and {S}yriac",
    author = "Vidal-Gor{\`e}ne, Chahan  and
      Kindt, Bastien  and
      Cafiero, Florian",
    editor = "Hettiarachchi, Hansi  and
      Ranasinghe, Tharindu  and
      Plum, Alistair  and
      Rayson, Paul  and
      Mitkov, Ruslan  and
      Gaber, Mohamed  and
      Premasiri, Damith  and
      Tan, Fiona Anting  and
      Uyangodage, Lasitha",
    booktitle = "Proceedings of the Second Workshop on Language Models for Low-Resource Languages ({L}o{R}es{LM} 2026)",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.loreslm-1.28/",
    doi = "10.18653/v1/2026.loreslm-1.28",
    pages = "324--334",
    ISBN = "979-8-89176-377-7",
}
```

### LREC Tutorial

This paper will also serve as a basis for a tutorial at LREC 2026: (https://floriancafiero.github.io/lrec2026-llm-as-annotator-tutorial/) [Under-Resourced Studies of Under-Resourced Languages].

#### Acknowledgements
This research was supported by the French National Research Agency (ANR), grant ANR-21-CE38-0006 (DALiH project), and conducted as part of the PSL Research University's Major Research Program CultureLab. We thank the GREgORI lab for data access.
