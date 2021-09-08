import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Auxilizando a classe para converter um item DynamoDB para JSON
class DecimalEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

fe = Key('year').between(1950,1959)
pe = "#yr, title, info.rating"
# Nomes de atributos de expressão apenas para expressão de projeção.
ean = {"#yr": "year",}
esk = None

response = table.scan(
    FilterExpression = fe,
    ProjectionExpression = pe,
    ExpressionAttributeNames = ean
)

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

while 'LastEvaluateKey' in response:
    response = table.scan(
        ProjectionExpression = pe,
        FilterExpression = fe,
        ExpressionAttributeNames = ean,
        ExclusiveStarKey = response['LastEvaluateKey']
    )

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))