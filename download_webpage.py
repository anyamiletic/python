import re

import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, user_agent = 'wswp', num_retries=2, charset='utf-8'):
	print("Downloading: %s" % (url))
	request = urllib.request.Request(url)

	#add user agent
	request.add_header('User-agent', user_agent)

	try:
		resp = urllib.request.urlopen(url)
		cs = resp.headers.get_content_charset()

		if not cs:
			cs = charset

		html = resp.read().decode(cs)
	except (URLError, HTTPError,ContentTooShortError) as e:
		print("Download error: %s" % (e.reason))
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries-1)

	return html

def crawl_sitemap(url):
	#first we download the sitemap
	sitemap = download(url)

	#extract the links
	links = re.findall('<loc>(.*?)</loc>', sitemap)

	#enter each of the links
	for link in links:
		html = download(link)
		print("entering: %s" % (link))

def main():
	url = input("Unesite url: ")
	crawl_sitemap(url)

if __name__ == "__main__":
	main()