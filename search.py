import webbrowser
import os

os.system('mode con: cols=50 lines=5')

while(True):

	# Removes unnecesary spaces 
	raw_search = ' '.join(input('Search here: ').split())

	# Asks for input again if the first one was empty or just spaces
	while raw_search == '':
		raw_search = ' '.join(input('Nice try. Try again: ').split())	
	
	# Removes first 3 characters from the original string: 2 from id and 1 space
	search = raw_search[3:]

	search_engines = {
		'gg': 'https://www.google.com/search?q=',
		'yt': 'https://www.youtube.com/results?search_query=', 
		'ml': 'https://listado.mercadolibre.com.mx/',
		'az': 'https://www.amazon.com.mx/s?k=',
		'bl': 'https://borderlands.fandom.com/wiki/Special:Search?query='
	}

	for se in search_engines:
		# Compares the current key with the 2 first characters of the search string
		if se == raw_search[:2]:
			# Opens new tab with composed link	
			webbrowser.open_new(search_engines[se]+search)	
			break

		# Compares the current key with the last one of the dict
		elif se == list(search_engines.items())[-1][0]:
			#Opens default google search if search engine wasn't specified
			webbrowser.open_new(search_engines['gg']+raw_search)
