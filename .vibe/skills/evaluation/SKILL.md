---
name: evaluation
description: Evaluate historical-language lemma and POS predictions against EACL 2026 gold-standard annotations.
---

# Historical NLP Evaluation

## Objective
Evaluate lemmatization and POS-tagging predictions
against gold-standard annotations.

## Supported languages
- GRC: Ancient Greek
- HYE: Classical Armenian
- KAT: Old Georgian
- SYC: Syriac

## Reference datasets
- `data/corpus/test_in-domain/{LANG}_test.tsv`
- `data/corpus/test_out-of-domain/{LANG}_test.tsv`

## Reference format
The reference TSV files contain:
- text_form
- form
- lemma
- pos

## Prediction format
The expected predictions contain:
- token
- lemma
- POS tag

## Evaluation procedure
1. Identify the language, model and experimental setting.
2. Load the model predictions.
3. Load the corresponding reference TSV.
4. Exclude the header from the reference data.
5. Verify token counts and alignment.
6. Detect missing, duplicated or malformed predictions.
7. Compare predicted lemmas against reference lemmas.
8. Compare predicted POS tags against reference POS tags.
9. Calculate exact-match accuracy for both tasks.
10. Report results by language and dataset partition.

## Metrics

Lemma accuracy:
Number of correctly predicted lemmas divided by
the number of evaluated tokens.

POS accuracy:
Number of correctly predicted POS tags divided by
the number of evaluated tokens.

Report the denominator and any exclusions.

## Experimental comparisons
Compare results across:
- Four historical languages
- Zero-shot and few-shot settings
- 5, 50 and 500 few-shot examples
- In-domain and out-of-domain test sets
- Different LLM providers and models

## Composite annotations
Preserve the project's `@` convention.

Do not split composite annotations into additional
tokens without an explicitly documented evaluation rule.

## Scientific constraints
- Never invent evaluation results.
- Never evaluate without actual predictions.
- Never modify gold-standard annotations.
- Never use gold-standard labels during prediction.
- Do not silently ignore missing predictions.
- Report alignment errors before calculating metrics.
- Distinguish exact-match evaluation from linguistic
  equivalence or normalized evaluation.

## Output
Produce an evaluation report containing:
- Language
- Model
- Experimental setting
- Dataset partition
- Number of evaluated tokens
- Lemma accuracy
- POS accuracy
- Alignment errors
- Methodological limitations
