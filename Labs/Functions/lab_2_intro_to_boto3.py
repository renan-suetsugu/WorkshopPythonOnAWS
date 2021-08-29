import boto3

client = boto3.client('translate')

### Add the new text below this line ###

def translate_text(): # A função foi declarada usando def, nome, parentêsis para parametos e dois pontos
    response = client.translate_text(
        Text='I am learnin to code in AWS', # Foi atribuido o valor da string para a variável texto
        SourceLanguageCode='en', # Usamos um código da documentação de duas letras para o idioma (en = Inglês)
        TargetLanguageCode='fr' #  Usamos um código da documentação de duas letras para o segundo idioma (fr = Francês)
    )