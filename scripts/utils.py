import csv
import requests
import openai
from string import Template

def load_prompt_template(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    context = lines[0].strip().split('=', 1)[1].strip().strip("'")
    prompt_raw = ''.join(lines[1:]).strip()
    return context, Template(prompt_raw)

def load_test_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        return "\n".join([row[1] for row in reader])

def load_tagset(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read().strip()

def call_openai(model, messages, temperature=0.2):
    try:
        params = {"model": model, "messages": messages}
        if "o1" not in model:
            params["temperature"] = temperature
        
        response = openai.ChatCompletion.create(**params)
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"OpenAI Error ({model}): {e}"

def call_mistral(model, api_key, api_url, messages, temperature=0.2):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {"model": model, "messages": messages, "temperature": temperature}
    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        return f"Mistral Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Mistral Connection Error: {e}"
