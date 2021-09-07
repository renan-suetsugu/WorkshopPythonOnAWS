import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName = 'Movies',
    KeySchema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH' #Chave de partição
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # Chave de classificação
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName':'year',
            'AttributeType':'N'
        },
        {
            'AttributeName':'title',
            'AttributeType':'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print ("Table status:",table.table_status)