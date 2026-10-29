import openai
import os
import config
from utils import (
    load_prompt_template, load_test_content, 
    load_tagset, call_openai, call_mistral
)

def process_task(task_cfg):
    print(f"\n{'='*10} EXÉCUTION : {task_cfg['name']} {'='*10}")
    
    context, template = load_prompt_template(task_cfg['template'])
    test_data = load_test_content(task_cfg['test_file'])
    tagset_data = load_tagset(task_cfg['tagset'])
    prompt_text = template.safe_substitute(LANG_test=test_data, LANG_tagset=tagset_data)

    for model_info in task_cfg['models']:
        provider = model_info['provider']
        model_name = model_info['name']
        
        print(f"\n[Modèle: {model_name}]")
        
        if provider == "openai":
            openai.api_key = config.OPENAI_API_KEY
            if "o1" in model_name:
                messages = [{"role": "user", "content": f"{context}\n\n{prompt_text}"}]
            else:
                messages = [
                    {"role": "system", "content": context},
                    {"role": "user", "content": prompt_text}
                ]
            prediction = call_openai(model_name, messages)
            
        elif provider == "mistral":
            messages = [
                {"role": "system", "content": context},
                {"role": "user", "content": prompt_text}
            ]
            prediction = call_mistral(model_name, config.MISTRAL_API_KEY, config.MISTRAL_API_URL, messages)
        
        # Sauvegarde des résultats dans results/{LANG}/
        # Extrait le code langue (ex: "GRC - Zero Shot" -> "GRC")
        lang_code = task_cfg['name'].split()[0]
        # Nettoie le nom du modèle pour le nom de fichier
        safe_model_name = model_name.replace('/', '_').replace('-', '_')
        # Extrait le nom du template (ex: "GRC-prompt-zero-shot_template.txt" -> "GRC-prompt-zero-shot")
        template_name = os.path.basename(task_cfg['template']).replace('_template.txt', '')
        # Extrait le partition (in-domain ou out-of-domain)
        partition = "in-domain" if "in-domain" in task_cfg['test_file'] else "out-of-domain"
        
        output_filename = f"results/{lang_code}/{safe_model_name}_{template_name}_test_{partition}_result.txt"
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(prediction)
        
        print(f"✅ Résultats sauvegardés dans : {output_filename}")
        print(prediction)

if __name__ == "__main__":
    for task in config.TASKS:
        process_task(task)
