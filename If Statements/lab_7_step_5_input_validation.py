# Importações padrões
import argparse
import json

# Importação de terceiros
import boto3

# Argumentos
parser = argparse.ArgumentParser(description="Fornece tradução entre um idioma de origem e outra do mesmo conjunto de idiomas")
parser.add_argument(
    '--file',
    dest='filename',
    help="O caminho para a entrada de arquivos. O arquivo válido deve ser Json",
    required=True
)

args = parser.parse_args()

# Funções

# Abra o arquivo de entrada para obter o Json.
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input'] #Entender este input

# Função boto3 para usar o Amazon Translate para traduzir o texto e retornar o Texto traduzido.
# Entender como funciona o **kwargs
def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

# Adicionando um Loop para iterar com o arquivo json.
def translate_loop():
    input_text = open_input()
    for item in input_text:
        if input_validation(item) == True:
            translate_text(**item)
        else:
            raise SystemError

# Adicionando nossa validação de entrada de uma função aqui.
def input_validation(item):
    languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF",
                "nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it",
                "ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es",
                "sw","sv","tl","ta","th","tr","uk","ur","vi"
                ]
    json_input=item
    SourceLanguageCode = json_input['SourceLanguageCode']
    TargetLanguageCode = json_input['TargetLanguageCode']
    
    if SourceLanguageCode == TargetLanguageCode:
        print("O SourceLanguageCode é o mesmo que o TargetLanguageCode - nada a ser feito")
        return False
    elif SourceLanguageCode not in languages and TargerLanguageCode not in languages:
        print ("Nem o SourceLanguageCode e TargetLanguageCode são válidos - finalizando")
        return False
    elif SourceLanguageCode not in languages:
        print("O SourceLanguageCode não é válido - Finalizando")
        return False
    elif TargetLanguageCode not in languages:
        print("O TargetLanguageCod  e não é válido - Finalizando")
        return False
    elif SourceLanguageCode in languages and TargetLanguageCode in languages:
        print("O SourceLanguageCode e o TargetLanguageCode são válidos - Processando")
        return True
    else:
        print("Há um problema")
        return False

# Função principal - usado para chamar outras funções
def main():
    translate_loop()

if __name__=="__main__":
    main()

# Para atualizar o respositório