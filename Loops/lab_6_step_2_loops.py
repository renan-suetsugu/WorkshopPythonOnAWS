# Importação Padrão
import argparse
import json

# Impotação de terceiros
import boto3

# Argumentos
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True
)

args = parser.parse_args()

# Funções
def open_input():
    """This function returns a dictionary containing the contents of the Input section in the input file"""
    with open(args.filename) as file_object:
        contents = json.load(file_object)
    return contents['Input']

# Função Boto3 para usar o Amazon Translate para tradução de texto e apenas retornar o texto traduzido
def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

# Adicionar um Loop para interar com o arquivo json.
def translate_loop():
    input_text = open_input()
    for item in input_text: #  Aqui, iteramos em todos os dicionários da lista de entrada
        translate_text(**item)
    
# Função principal - use para chamar as outras funções
def main():
    translate_loop()

if __name__ == "__main__":
    main()

# Para atualizar o respositório