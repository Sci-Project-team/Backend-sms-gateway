import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
import time
import random
import string

def random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def main():
    # Defining the host is optional and defaults to http://localhost:8000
    # See configuration.py for a list of all supported configuration parameters.
    configuration = openapi_client.Configuration(
        host = "http://localhost:8000"
    )

    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        auth_api = openapi_client.AuthenticationApi(api_client)
        sms_api = openapi_client.SMSApi(api_client)

        # 1. Register a new user
        username = random_string()
        password = "testpassword"
        email = f"{username}@example.com"
        user_create = openapi_client.UserCreate(username=username, password=password, email=email, full_name="Test User")

        try:
            print("1. Registering a new user...")
            api_response = auth_api.register_auth_register_post(user_create)
            print("User registered successfully:")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->register_auth_register_post: %s\n" % e)
            return

        # 2. Login with the new user
        try:
            print("\n2. Logging in...")
            # The login endpoint expects form data, which the client handles
            login_response = auth_api.login_auth_login_post(username=username, password=password)
            print("Login successful:")
            pprint(login_response)
            access_token = login_response['access_token']
        except ApiException as e:
            print("Exception when calling AuthenticationApi->login_auth_login_post: %s\n" % e)
            return

        # 3. Configure API client with the access token
        configuration.access_token = access_token
        
        # We need to create new api instances with the updated configuration
        # or update the existing ones. The generated client seems to use the config from when it was created.
        # So lets create a new client context
    
    # Re-enter context with updated configuration for authenticated requests
    with openapi_client.ApiClient(configuration) as api_client:
        sms_api_auth = openapi_client.SMSApi(api_client)

        # 4. Send an SMS
        # Note: Sending an SMS might require a real GSM module unless simulation is enabled.
        # This example assumes the API is running in simulation mode or with hardware.
        sms_create = openapi_client.SmsCreate(phone_number="+1234567890", message="Hello from the Python SDK's test case!")

        try:
            print("\n3. Sending an SMS...")
            api_response = sms_api_auth.send_sms_sms_post(sms_create)
            print("SMS sent successfully:")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SMSApi->send_sms_sms_post: %s\n" % e)
            


if __name__ == "__main__":
    main() 