import webbrowser, sys
import pyperclip # May need to install with 'pip install pyperclip'

sys.argv # ['mapit.py', '870', 'Valencia', 'St']

# Check if command line arguments were passed
if len(sys.argv) > 1:
	# ['mapit.py', '870', 'Valencia', 'St'] -> '870 Valencia St'
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()
	

url = ('https://www.google.com/maps/place/' + address)
webbrowser.get('windows-default').open(url)