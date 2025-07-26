import requests

def get_top_track(artist):
    API_KEY = "2b393e1db024a7d4a9c5449aefe8bd7e"
    url = "http://ws.audioscrobbler.com/2.0/"

    params = {
        "method": "artist.gettoptracks",
        "artist": artist,
        "api_key": API_KEY,
        "format": "json",
        "limit": 1,
    }

    response = requests.get(url, params = params)

    if response.status_code == 200:
        data = response.json()
        try:
            top_track = data["toptracks"]["track"][0]["name"]
            return top_track
        except (KeyError, IndexError):
            return "Artist not found or top tracks not available"
    else:
        return "API request failed"

if __name__ == "__main__":
    print(get_top_track("Coldplay"))
