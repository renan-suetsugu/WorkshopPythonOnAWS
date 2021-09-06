# Importações Padrões
import argparse
import json

# Importação do logging
import logging

# Importação de terceiros
import boto3
from botocore.exceptions import ClientError

# Definindo o arquivo de log e seu padrão. O padrão é 'Warning'
logging.basicConfig(filename='translate.log',level=logging.DEBUG)

# Argumentos
parser = argparse.ArgumentParser(description="Fornece tradução entre um idioma de origem e outro do mesmo grupo de idiomas.")
parser.add_argument(
    '--file',
    dest='filename',
    help="O caminho para o arquivo de entrada. O arquivo válido deve ser json",
    required=True
)

args = parser.parse_args()

# Funções

# Abrir o arquivo de entrada para obter o json
def open_input():
    try:
        with open(args.filename) as file_object:
            contents = json.load(file_object)
            return contents['Input']
    except FileNotFoundError as e:
        logging.warning("Erro {}. Desculpe, o arquivo de entrada não foi encontrado, verifique e tente novamente".format(e))
   

# Função boto3 para usar no Amazon Translate para traduzir o texto e apenas retornar o texto traduzido.
def translate_text(**kwargs):
    try:
        client = boto3.client('translate')
        response = client.translate_text(**kwargs)
        print(response['TranslatedText'])
    except ClientError as e:
        logging.warning("Botocore generated an error {}".format (e))

# Adicionando um Loop para iterar com o arquivo json

def translated_loop():
    try:
        input_text = open_input()
        for item in input_text:
            if input_validation (item) == True:
                translate_text(**item)
            else:
                raise SystemError
    except:
        logging.warning("Um erro causou falha na tradução, verifique os logs para obter mais detalhes.")
# Adicionando a validação da entrada como uma função aqui

def input_validation(item):
    try:
        languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF",
                "nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it",
                "ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es",
                "sw","sv","tl","ta","th","tr","uk","ur","vi"
                ]
        json_input=item
        SourceLanguageCode = json_input['SourceLanguageCode']
        TargetLanguageCode = json_input['TargetLanguageCode']

        if SourceLanguageCode == TargetLanguageCode:
            print ("O SourceLanguageCode é o mesmo que o TargetLanguageCode - Nada a ser feito")
            return False
        elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
            print("Nem o SourceLanguageCode e TargetLanguageCde são válidos - Finalizando")
            return False
        elif SourceLanguageCode not in languages:
            print("O SourceLanguageCode não é valido - Finalizando")
            return False
        elif TargetLanguageCode not in languages:
            print("O TargetLanguageCode não é válido - Finalizando")
            return False
        elif SourceLanguageCode in languages and TargetLanguageCode in languages:
            print("O SourceLanguageCode e TargetLanguageCode são válidos - Processando")
            return True
        else:
            print("Há um problema")
            return False
    except:
        loggin.warning("Um erro não esperado ocorreu.")
# Função principal - use para chamar outras funções
def main():
    translated_loop()

if __name__ == "__main__":
    main()
