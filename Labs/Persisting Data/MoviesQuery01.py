import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Auxiliar classe para converter um item DynamoDB para JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

print("Filmes de 1985")

response = table.query(
    KeyConditionExpression = Key('year').eq(1985)
)

for i in  response['Items']:
    print(i['year'],":",i['title'])