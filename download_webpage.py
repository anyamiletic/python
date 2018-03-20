import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, user_agent = wswp, num_retries=2):
	print("Downloading: %s" % (url))
	request = urllib.request.Request(url)

	#add user agent
	request.add_header('User-agent', user_agent)

	try:
		html = urllib.request.urlopen(url).read()
	except (URLError, HTTPError,ContentTooShortError) as e:
		print("Download error: %s" % (e.reason))
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries-1)

	return html

def main():
	url = input("Unesite url: ")
	print(download(url))

if __name__ == "__main__":
	main()