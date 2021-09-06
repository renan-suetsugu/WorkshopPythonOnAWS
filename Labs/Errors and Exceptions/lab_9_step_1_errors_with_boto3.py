import logging
import boto3
import botocore.exceptions import ClientError

try:
    client = boto3.client('translate')
    <snip>
except ClientError as e:
    logging.warning("Erro! Código utilizando boto3{}".format(e))

# REVISAR
