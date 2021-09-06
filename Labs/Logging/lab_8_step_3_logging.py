# Importações padrões
import argparse
import json

# Importações de terceiros
import boto3

# Argumentos
parser = argparse.ArgumentParser(description="Fornecer tradução entre um idioma de origem e outro do mesmo conjunto de idiomas.")
parser.add_argument(
    '--file',
    dest = 'filename',
    help = "O caminho para o arquivo de entrada. O arquivo válido deve ser json.",
    required = True
)

args = parser.parse_args()

# Funções

# Abrir o arquivo de entrada para obter o Json
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input']

# Função boto3 para usar o Amazon Translate para traduzir o texto e apenas retonar o texto traduzido
def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

# Adicionando um loop para iterar sobre o arquivo json

def translate_loop():
    input_text = open_input()
    for item in input_text:
        if input_validation(item) == True:
            translate_text(**item)
        else:
            raise SystemError

# Aqui adicionaremos nossa validação de entrada como uma função
def input_validation(item):
    languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF",
                "nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it",
                "ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es",
                "sw","sv","tl","ta","th","tr","uk","ur","vi"
                ]
    json_input = item
    SourceLanguageCode = json_input['SourceLanguageCode']
    TargetLanguageCode = json_input['TargetLanguageCode']

    if SourceLanguageCode == TargetLanguageCode:
        print("O SourceLanguageCode pe o mesmo que o TargetLanguageCode - Nada a ser feito")
        return False
    elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
        print("Nem o SourceLanguageCode e TargetLanguageCode são válidos - Finalizando")
        return False
    elif SourceLanguageCode not in languages:
        print('O SourceLanguageCode não é válido - Finalizando')
        return False
    elif TargetLanguageCode not in languages:
        print("O TargetLanguageCode não é válido - Finalizando")
        return False
    elif SourceLanguageCode in languages and TargetLanguageCode in languages:
        print(" O SourceLanguageCode e o TargetLanguageCode são válidos - Processando")
        return True
    else:
        print("Há um problema!")
        return False


# Função principal - usada para chamar outras funções

def main():
    translate_loop()

if __name__ == "__main__":
    main(    )

