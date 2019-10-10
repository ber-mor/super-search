import webbrowser
import os

os.system('mode con: cols=50 lines=5')

search_engines = {
		'gg': 'https://www.google.com/search?q=',
		'yt': 'https://www.youtube.com/results?search_query=', 
		'ml': 'https://listado.mercadolibre.com.mx/',
		'az': 'https://www.amazon.com.mx/s?k=',
		'bl': 'https://borderlands.fandom.com/wiki/Special:Search?query='
	}

while(True):
	# Removes unnecesary spaces 
	raw_search = ' '.join(input('Search here: ').split())

	# Asks for input again if the first one was empty or it was just spaces
	while raw_search == '':
		raw_search = ' '.join(input('Nice try. Try again: ').split())	
	
	# Removes key from original search string, including the space after it  
	search = ' '.join(raw_search.split()[1:])

	# Gets key from original search string
	search_key = raw_search.split()[0]

	if search_key in search_engines.keys():
		webbrowser.open_new(search_engines[search_key]+search)
	else:
		# Default case: opens google search if search engine was not specified
		webbrowser.open_new(search_engines['gg']+raw_search)