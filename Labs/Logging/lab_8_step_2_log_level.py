# Importando Logging
import logging
import json

# Definir o nível de lofo em uma configuração básica. Isso significa que vamos capturar todas as nossas entradas de Log e não apenas o Warning ou superior.
logging.basicConfig(filename='example.log',level=logging.DEBUG)

# Vamos usar uma string Json como entrada.
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"fr",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

# Definir duas variáveis para armazenar o código do idioma da entrada.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# A declaração If verificará se o código do idioma é o mesmo do código de origem.
if SourceLanguageCode == TargetLanguageCode:
    logging.warning("O código do SourceLanguageCode é o mesmo do TargetLanguageCode - Finalizando")
    # Isso irá printar no console já que o nível padrão é aviso.
else:
    logging.info("Os códigos do SourceLanguageCode e TargetLanguageCode são diferentes - Processando")
    # Isso não será impresso no console, por causa que é inferior ao aviso.

