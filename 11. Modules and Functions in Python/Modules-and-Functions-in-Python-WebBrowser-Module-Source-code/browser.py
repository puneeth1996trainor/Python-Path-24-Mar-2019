import webbrowser
#
# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)
# chrome = webbrowser.get('/usr/bin/google-chrome %s').open_new_tab("https://www.python.org/")
googleChrome = webbrowser.get(using='google-chrome')
googleChrome.open("https://www.python.org/")
