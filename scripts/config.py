OPENAI_API_KEY = ""
MISTRAL_API_KEY = ""
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

TASKS = [
    {
        "name": "Zero Shot",
        "template": "/path/to/template.txt",
        "test_file": "/path/to/test/file.tsv",
        "tagset": "/path/to/tagset.txt",
        "models": [
            {"provider": "openai", "name": "gpt-4o-mini"},
            {"provider": "openai", "name": "o1-mini"},
            {"provider": "mistral", "name": "mistral-large-latest"}
        ]
    },
    {
        "name": "Few Shot",
        "template": "/Users/nostradamus/Documents/.../HYE-prompt-few-shot-500_template.txt",
        "test_file": "/Users/nostradamus/Documents/.../HYE_test.tsv",
        "tagset": "/Users/nostradamus/Documents/.../HYE_tagset.txt",
        "models": [
            {"provider": "openai", "name": "gpt-4o-mini"},
            {"provider": "mistral", "name": "open-mistral-nemo"}
        ]
    }
]
