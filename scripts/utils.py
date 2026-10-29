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
    # ===== MODE SIMULATION (sans appel API réel) =====
    # Génère une réponse factice au format TSV pour tester la logique
    # Format attendu : token\tlemma\tPOS tag
    
    # Extrait les tokens de la dernière ligne du prompt (pour simulation)
    last_message = messages[-1]['content']
    lines = last_message.split('\n')
    
    # Filtre les lignes qui contiennent des mots grecs (ou autre langue)
    import re
    tokens = []
    for line in lines:
        # Nettoie la ligne et extrait les mots (simplifié)
        cleaned = re.sub(r'[\x00-\x1F\x7F-\xFF]', '', line)  # Supprime les caractères non-ASCII (temporaire)
        if cleaned.strip() and not cleaned.strip().startswith('---') and not cleaned.strip().startswith('You are'):
            tokens.append(cleaned.strip())
    
    # Génère une réponse TSV simulée (1 lemme + POS par token)
    fake_response = "token\tlemma\tPOS tag\n"
    greek_words = ["πολλοὶ", "μήπω", "τοὺς", "πολεμίους", "εἰσιέναι", "ἐκεῖθεν", "Τὸ", "δ´", "ἦν"]
    lemmas = ["πολύς", "μήπω", "ὁ", "πολέμιος", "εἴσειμι", "ἐκεῖθεν", "ὁ", "δέ", "εἰμί"]
    pos_tags = ["A", "I+Adv", "DET", "A", "V", "I+Adv", "DET", "I+Part", "V"]
    
    for i, token in enumerate(greek_words[:10]):  # Limite à 10 tokens pour la simulation
        fake_response += f"{token}\t{lemmas[i]}\t{pos_tags[i]}\n"
    
    return fake_response.strip()
    # ===== FIN MODE SIMULATION =====

def call_mistral(model, api_key, api_url, messages, temperature=0.2):
    # ===== MODE SIMULATION (sans appel API réel) =====
    # Retourne une réponse factice au format TSV pour tester la logique
    # Format attendu : token\tlemma\tPOS tag
    
    # Génère une réponse TSV simulée avec des données réalistes
    fake_response = "token\tlemma\tPOS tag\n"
    greek_words = ["πολλοὶ", "μήπω", "τοὺς", "πολεμίους", "εἰσιέναι", "ἐκεῖθεν", "Τὸ", "δ´", "ἦν", "ἀλλά"]
    lemmas = ["πολύς", "μήπω", "ὁ", "πολέμιος", "εἴσειμι", "ἐκεῖθεν", "ὁ", "δέ", "εἰμί", "ἄλλος"]
    pos_tags = ["A", "I+Adv", "DET", "A", "V", "I+Adv", "DET", "I+Part", "V", "DET"]
    
    for i in range(10):
        fake_response += f"{greek_words[i]}\t{lemmas[i]}\t{pos_tags[i]}\n"
    
    return fake_response.strip()
    # ===== FIN MODE SIMULATION =====
