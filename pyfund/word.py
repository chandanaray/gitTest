#!/usr/bin/env python3
"""Retrieve and print words from a URL.
Usage:
	python3 word.py <URL>"""

import sys
from urllib.request import urlopen


def fetch_word(url):
	"""Fetch a list of words from given URL.

		Args:
			url: The URL of a UTF-8 test document.

		Returns:
			A list of string cointaining the words from
			the document.
	"""
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words


def print_item(items):
	"""Print items one per line.
	Args :
		An iterable series of printable items.
	"""
	for item in items:
		print(item)


def main(url):
	"""Print each word from the url.

	Args:
		url:The URL of the document to be printed.
	"""
	word = fetch_word(url)
	print_item(word)


if __name__ == '__main__':
	main(sys.argv[1])
