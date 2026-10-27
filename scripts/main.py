import openai
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
    prompt_text = template.safe_substitute(HYE_test=test_data, HYE_tagset=tagset_data)

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
            print(call_openai(model_name, messages))
            
        elif provider == "mistral":
            messages = [
                {"role": "system", "content": context},
                {"role": "user", "content": prompt_text}
            ]
            print(call_mistral(model_name, config.MISTRAL_API_KEY, config.MISTRAL_API_URL, messages))

if __name__ == "__main__":
    for task in config.TASKS:
        process_task(task)
