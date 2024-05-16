import requests

# Discord token endpoint
token_url = 'https://discord.com/api/v9/oauth2/token'

# Client ID and secret obtained from Discord Developer Portal
client_id = '1237645699399680050'
client_secret = '9NYVrza7gmoXL7O3IKsrAHbVnBl9z8nf'
redirect_uri = 'http://localhost:4200/'  # Must match the redirect URI configured in your Discord application

# Authorization code obtained from the OAuth2 flow
authorization_code = 'oxU0ynrhqH5QFYdbFT6rvhSXciOaGb';

# POST request to exchange authorization code for access token
token_params = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
}

response = requests.post(token_url, data=token_params)
token_data = response.json()
print("token_data ==> ", token_data)
if 'access_token' in token_data:
    access_token = token_data['access_token']
    print(f"Access Token: {access_token}")
else:
    print("Failed to obtain access token")

