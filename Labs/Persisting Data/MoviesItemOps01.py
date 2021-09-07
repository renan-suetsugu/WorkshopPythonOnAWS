import boto3
import json
import decimal

# Classe para ajudar a converter um item DynamoDB para Json.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder,self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

title = "The Big New Movie"
year = 2015

response = table.put_item(
    Item = {
        'year':year,
        'title':title,
        'info': {
            'plot':'Nothing happens at all.',
            'rating':decimal.Decimal(0)
        }
    }
)

print("Entrada de item concluída:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))