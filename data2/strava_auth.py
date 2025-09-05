import requests
import json

# ==============================
# CONFIGURATION
# ==============================
CLIENT_ID = "175523"  # Replace with your client_id
CLIENT_SECRET = "aa5a2db82ff6c3d26f47d82829e8dc7858f72fed"  # Replace with your client_secret
REFRESH_TOKEN = "6622bf77cd84f507a84c1bf5404da2dbc4765064"  # Replace with your refresh_token

# ==============================
# STEP 1: Refresh Access Token
# ==============================
def refresh_access_token():
    url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        tokens = response.json()
        print("✅ New Access Token Retrieved!")
        print(json.dumps(tokens, indent=4))
        return tokens["access_token"]
    else:
        print("❌ Error refreshing token:", response.text)
        return None

# ==============================
# STEP 2: Get Athlete Profile
# ==============================
def get_athlete(access_token):
    url = "https://www.strava.com/api/v3/athlete"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        athlete = response.json()
        print("👟 Athlete Profile:")
        print(json.dumps(athlete, indent=4))
    else:
        print("❌ Error fetching athlete:", response.text)


if __name__ == "__main__":
    token = refresh_access_token()
    if token:
        get_athlete(token)
