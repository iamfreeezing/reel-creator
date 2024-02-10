import requests
lang = "en"                #hi = hindi, en = english
                            
                            
def translate_text(textconv, lang):             #returns translated text

    url = "https://google-translate-v21.p.rapidapi.com/translate"

    payload = {
        "text_to_translate": textconv,
        "dest": lang
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "921238bc85msh6ad9d991942dfe0p1a19b9jsn46c619809b96",
        "X-RapidAPI-Host": "google-translate-v21.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return (response.json()['translation'])
