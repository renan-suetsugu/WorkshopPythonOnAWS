import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.create_table(
    TableName = 'Movies',
    KeySchema = [
        {
            'AttibuteName': 'year',
            'KeyType': 'HASH' #Chave de partição
        },
        {
            'AttibuteName': 'title',
            'KeyType': 'RANGE'  # Chave de classificação
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName':'year',
            'AttibuteType':'N'
        },
        {
            'AttributeName':'title',
            'AttibuteType':'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print ("Table status:",table.table_status)