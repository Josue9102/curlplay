import requests

class Game:
    def __init__(self, url):
        self.url = url

    def load_game(self):
        # Simulate loading the game via the URL
        response = requests.get(self.url)
        if response.status_code == 200:
            print("Game loaded successfully.")
            # Here you would have logic to handle the actual game file
        else:
            print("Failed to load the game from the provided URL.")
