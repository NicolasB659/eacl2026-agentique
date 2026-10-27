import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

TASKS = [
    {
        "name": "GRC - Zero Shot",
        "template": "data/prompt-templates/GRC-prompt-zero-shot_template.txt",
        "test_file": "data/corpus/test_in-domain/GRC_test.tsv",
        "tagset": "data/tagsets/GRC_tagset.txt",
        "models": [
            {"provider": "mistral", "name": "mistral-large-latest"}
        ]
    }
]
