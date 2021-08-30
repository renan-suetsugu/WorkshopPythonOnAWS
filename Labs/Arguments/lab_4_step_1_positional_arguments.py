import boto3

def translate_text(text, source_languague_code, target_language_code):
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text,
        SourceLanguageCode = source_languague_code,
        TargetLanguageCode = target_language_code
    )
    print(response)

def main():
    translate_text('I am learningto code in AWS','en','fr')

if __name__=="__main__":
    main()