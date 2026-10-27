# Agent Instructions

## 1. Project Overview

This project investigates the use of Large Language Models (LLMs) for lemmatization and part-of-speech (POS) tagging of four historical languages:

- GRC: Ancient Greek
- HYE: Classical Armenian
- KAT: Old Georgian
- SYC: Syriac

## 2. Objectives

The agentic system aims to:

1. Inspect and prepare historical linguistic corpora.
2. Generate lemma and POS annotations using LLMs.
3. Validate annotations against language-specific tagsets.
4. Evaluate annotation quality against reference data.
5. Support reproducible zero-shot and few-shot experiments.

## 3. Agent Responsibilities

### Corpus Analyst
- Inspect TSV corpus structure.
- Identify languages and dataset partitions.
- Detect missing values and formatting problems.
- Preserve original corpus files.

### Linguistic Annotator
- Perform lemmatization and POS-tagging.
- Follow language-specific annotation guidelines.
- Reuse existing prompt templates.
- Support zero-shot and few-shot experiments.

### Annotation Validator
- Check annotation consistency.
- Verify POS tags against the appropriate tagset.
- Detect missing or malformed annotations.
- Report potential linguistic inconsistencies.

### Evaluation Agent
- Compare predicted annotations with gold-standard annotations.
- Calculate accuracy and other appropriate metrics.
- Report results by language and experimental setting.
- Distinguish in-domain and out-of-domain evaluation.

## 4. General Rules

- Never modify original corpus files without explicit authorization.
- Never invent missing linguistic data, reference annotations or tagsets.
- Preserve Unicode characters and original scripts.
- Use existing prompts and tagsets whenever available.
- Clearly distinguish model predictions from gold-standard annotations.
- Do not use test annotations as few-shot examples.
- Never commit API keys, credentials or sensitive configuration files.
- Document assumptions, errors and experimental limitations.

## 5. Reproducibility

All experiments should record:

- Language
- Model and provider
- Prompt template
- Zero-shot or few-shot setting
- Dataset partition
- Evaluation metrics
