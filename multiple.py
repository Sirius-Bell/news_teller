import pyttsx3
from newsapi import NewsApiClient

RU_LANG_VOICE = ""
API_KEY = ""
tts = pyttsx3.init()
tts.setProperty("voice", RU_LANG_VOICE)
api = NewsApiClient(api_key=API_KEY)

def add_to_say(text):
	"""" ADD TO QUERY, SAY SOMETHING """
	tts.say(text)

def get_news():
	""" GET NEWS AND ADD TO SAY TO QUERY """
	count = 0
	top_headlines = api.get_top_headlines(country='ru', language='ru')

	for i in top_headlines['articles']:
		if count >= 2:
			break

		add_to_say(i['source']['name'])
		add_to_say(i['title'])
		add_to_say(i['description'])

		count += 1

get_news()

tts.runAndWait()