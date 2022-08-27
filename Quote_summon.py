import requests


class SummonQuote:
    """Summons a Breaking Bad quote."""

    def __init__(self):
        """Makes an API call."""

        url = 'https://api.breakingbadquotes.xyz/v1/quotes'
        self.r = requests.get(url)

    def fetch_quote(self):
        """Takes an unformatted quote."""
        self.response_list = self.r.json()
        return self.response_list[0]

    def create_random_quote(self):
        """Takes the data from a JSON file and turns it into a formatted quote."""
        # print(f"Status code: {self.r.status_code}")

        response_dict = self.fetch_quote()
        quote = response_dict['quote']
        author = response_dict['author']
        return f'''"{quote}" - {author}'''
