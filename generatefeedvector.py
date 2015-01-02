import feedparser
import re


# Returns title and dictionary of word counts for and RSS feed
def getwordcounts(url):
    # Parse the feed
    data = feedparser.parse(url)
    wordCount = {}

    # Loop over all the entries
    for entry in data.entries:
        if 'summary' in entry:
            summary = entry.summary
        else:
            summary = entry.description

        # Extract a list of words
        words = getwords(entry.title + ' ' + summary)
        for word in words:
            wordCount.setdefault(word, 0)
            wordCount[word] += 1
    return data.feed.title, wordCount


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']
