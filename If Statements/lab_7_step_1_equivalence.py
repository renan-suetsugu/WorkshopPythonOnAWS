import json

# Isso usa uma string json como entrada
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

json_input = json.loads(json_string) # Nós usamos vargas enquanto carregamos de uma string.

# Definimos duas variáveis para armazenar o código de idioma de uma entrada.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# A declaração IF verifica para ver se o código de idioma é o mesmo do código de origem
if SourceLanguageCode == TargetLanguageCode:
    print ("O código de idioma de origem é o mesmo que o código de idioma alvo - finalizando")
else:
    print("Os códigos de idioma de origem e o idioma alvo são diferentes - processando")

# Para atualizar o respositório