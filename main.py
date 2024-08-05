
import os
from google.cloud import secretmanager

def access_secret_version(secret_id, version_id="latest"):
    # Create a Secret Manager client
    client = secretmanager.SecretManagerServiceClient()
    
    # Construct the resource name of the secret version
    project_id = "kilo-gcp"  # Use the actual project ID
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    
    # Access the secret version
    response = client.access_secret_version(name=name)
    
    # Extract and return the secret payload
    payload = response.payload.data.decode("UTF-8")
    return payload

def hello_world(request):
    # The ID of the secret to access
    secret_id = "dsfsdf"  # Update this to your secret ID
    
    # Access the secret value
    secret_value = access_secret_version(secret_id, version_id="1")
    
    # Return the secret value
    return f"Secret value: {secret_value}"
