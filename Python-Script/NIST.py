# -----------------
# (Not finish) Below is a Python script that interacts with the OpenAI GPT-4 API to analyze data to find common vulnerabilities

import openai
import time
import csv

ChatGPT_API_KEY = "xxxxxxxxxxxxxxxxxxxx" # https://platform.openai.com/api-keys)
GPT_MODEL = "gpt-4-0125-preview" # API Models: https://platform.openai.com/docs/models/continuous-model-upgrades

def get_csv_contents(file_path):
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data
    except Exception as e:
       print(f"Error:\n\n{e}\n\n——————————")

def get_tsv_contents(input_file_path):
    all_rows = []
    with open(input_file_path, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')
        for row in reader:
            all_rows.append('\t'.join(row))
    return '\n'.join(all_rows)
            
def get_text_contents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def create_prompt(attack_type, nist_framework):
    return f'''

def ask_chatgpt(key, model, prompt):
   # Plug the API key into the openai object
    openai.api_key = key

    print("Asking ChatGPT.")

    while True:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response = response.choices[0].message.content
            return response

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying...")
            time.sleep(1)  # Pause for a second before retrying

def clean_up_response(response):
    cleaned_response = response.replace('\n','')
    return cleaned_response

def dump_contents_to_text_file(new_file_name, contents):
    try:
        with open(new_file_name, 'w') as file:
            file.write(contents)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# ----- SCRIPT RUNS HERE ----- #
