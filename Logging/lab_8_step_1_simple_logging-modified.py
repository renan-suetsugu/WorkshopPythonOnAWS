# Importando o Logging
import logging
import json

# Usaremos uma String Json como entrada
json_string = """
{
    "Input":[
        {
            "Text":"I am learning to code in AWS",
            "SourceLanguageCode":"en",
            "TargetLanguageCode":"en"
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
    logging.warning("O código do SourceLanguageCode é o mesmo que o TargetLanguageCode - finalizando") 
    # Vamos printar no console que o nível padrão é o Warning
else:
    logging.info("Os códigos de SourceLanguageCode e o TargetLanguageCode são diferentes - processando")
    # Não vamos printar no console, porque este é inferior ao Warning
# Para atualizar o respositório