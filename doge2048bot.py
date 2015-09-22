# A bot that blindly plays 2048
# Henry Barrow 2015

from selenium import webdriver # Need to 'pip install selenium' first
from selenium.webdriver.common.keys import Keys

# Launch Firefox and 2048
browser = webdriver.Firefox()
browser.get('http://doge2048.com/')

def play2048():
	# locate grid, game-over, and score by css selectors
	elem = browser.find_element_by_css_selector('.game-container')
	GameOver = browser.find_element_by_css_selector('.game-message > p:nth-child(1)')
	scoreElem = browser.find_element_by_css_selector('.score-container')

	score = scoreElem.text.strip()
	print 'Now playing...'

	#blind logic
	while len(GameOver.text.strip()) == 0:
		elem.send_keys(Keys.DOWN)
		elem.send_keys(Keys.RIGHT)
		elem.send_keys(Keys.DOWN)
		elem.send_keys(Keys.LEFT)
		
		# Press UP only as necessary
		if score == scoreElem.text.strip():
			elem.send_keys(Keys.UP)
		score = scoreElem.text.strip()

	if score.find('\n') > 0:
		score = score[:score.find('\n')]
	print 'Game Over! Score = ' + score + '\n'
	return int(score)

# Play until target score is exceeded	
score = play2048()
while score < 10000:
	TryElem = browser.find_element_by_css_selector('.retry-button')
	TryElem.click()
	score = play2048()
	
