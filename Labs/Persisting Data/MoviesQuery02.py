import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Auiliando a classe a converter um item DynamoDB para JSON.
class DecimalEncoder (json.JSONEncoder):
    def default(self,o):
        if isinstance(o,decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

table = dynamodb.Table('Movies')

print("Filmes de 1992 - titulos A-L, com gêneros e ator principal.") 

response = table.query(
    ProjectionExpression = "#yr, title, info.games, info.actors[0]",
    ExpressionAttributeNames = { "#yr" : "year"}, # Nomes de atributos de expressão apenas para expressão de projeção.
    KeyConditionExpression = Key('year').eq(1992) & Key('title').between('A','L')
)

for i in response[u'Items']:
    print(json.dumps(i,cls=DecimalEncoder))