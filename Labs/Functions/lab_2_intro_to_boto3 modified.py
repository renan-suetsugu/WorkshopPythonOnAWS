import boto3

client = boto3.client('translate')


def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) #Este código está dentro da função e irá imprimir o conteúdo da variável "response"

translate_text() # Essa linha chamará a nossa função, sem ela o Python não fará nada.