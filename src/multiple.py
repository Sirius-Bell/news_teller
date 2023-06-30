import pyttsx3
from newsapi import NewsApiClient


class Teller:

    def __init__(self, api_key: str, count: int = 2, country: str = "ru",
                 language: str = "ru") -> None:
        """
        Get news and tell news.
        :param api_key: str, api key from newsapi
        :param count: int, news count, default is 2
        :param country: str, country news
        :param language: str, language to tell
        """

        if language is None or api_key is None:
            raise ValueError

        self.lang_voice: str = language
        self.api_key: str = api_key
        self.tts = pyttsx3.init()
        self.tts.setProperty("voice", language)
        self.api = NewsApiClient(api_key=api_key)

        self.count = count
        self.country = country
        self.language = language

    def add_to_say(self, text: str) -> None:
        """"
        Add to query text
        :param text: str, some text to say
        """

        self.tts.say(text)

    def get_news(self) -> bool:
        """
        Get news and says it
        """

        top_headlines = self.api.get_top_headlines(country=self.country, language=self.language)

        for i in top_headlines['articles']:
            if self.count >= 2: break
            self.add_to_say(i['source']['name'])
            self.add_to_say(i['title'])
            self.add_to_say(i['description'])

            self.count += 1
        return True


if __name__ == "__main__":
    wrap = Teller(api_key=None, language=None)
    wrap.get_news()
    wrap.tts.runAndWait()
