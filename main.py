import os
from google.cloud import secretmanager

def access_secret_version(secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{os.getenv('GCP_PROJECT')}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name=name)
    payload = response.payload.data.decode("UTF-8")
    return payload

def hello_world(request):
    secret_id = "dsfsdf"
    secret_value = access_secret_version(secret_id, version_id="1")
    return f"Secret value: {secret_value}"
