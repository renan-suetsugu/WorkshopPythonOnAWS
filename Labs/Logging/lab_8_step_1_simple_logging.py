import json

# Usaremos uma String Json como entrada
json_string = """
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

# Definimos duas variáveis para armazenar o código de idioma da entrada.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# A declaração If verifica se o código do idioma é o mesmo que o do código de origem.
if SourceLanguageCode == TargetLanguageCode:
    print("O código do SourceLanguageCode é o mesmo que o TargetLanguageCode - finalizando")
else:
    print("Os códigos de SourceLanguageCode e o TargetLanguageCode são diferentes - processando")


    