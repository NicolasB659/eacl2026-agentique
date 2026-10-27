---
name: pos-tagging
description: Assign part-of-speech tags to historical language tokens using language-specific tagsets.
user-invocable: true
---

# Historical Language POS Tagging

## Objective
Assign a grammatical category to each token.

## Procedure
1. Identify the language.
2. Load the corresponding POS tagset.
3. Read the available annotation guidelines and prompts.
4. Analyze each token in its linguistic context.
5. Assign only tags authorized by the tagset.
6. Preserve token order and the required output format.
7. Report uncertain annotations.

## Constraints
- Never invent grammatical labels.
- Never modify the original corpus.
- Report missing tagsets rather than guessing.
