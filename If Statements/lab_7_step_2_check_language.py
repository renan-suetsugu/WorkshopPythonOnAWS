import json

# Uma lista de idiomas definidas suportadas pelo Amazon Translate
languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

# Aqui usamos uma string Json como entrada
json_string="""
{
    "Input":[
        {
            "Text":"I am learning to code in AWS",
            "SourceLanguageCode":"en",
            "TargetLanguageCode":"fr"
        }      
    ]
}
"""

json_input = json.loads(json_string)

# Extraindo o SourceLanguageCode e TargetLanguageCode do JSon
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# Usando uma declaração If-else para verificar se o SourceLanguageCode está na lista de idiomas
if SourceLanguageCode in languages:
    print("O SourceLanguageCode é válido - processando")
else:
    print("O SourceLanguageCode não é válido - finalizando")

# Para atualizar o respositório