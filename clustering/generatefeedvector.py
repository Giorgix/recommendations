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


apcount = {}
wordCounts = {}
feedlist = [line for line in file('feedlist.txt')]
for feedurl in feedlist:
    try:
        title, wordCount = getwordcounts(feedurl)
        wordCounts[title] = wordCount
        for word, count in wordCount.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
    except:
        print 'Failed to parse feed %s' % feedurl

wordlist = []
for word, blogCount in apcount.items():
    frac = float(blogCount) / len(feedlist)
    if frac > 0.1 and frac < 0.5:
        wordlist.append(word)

out = file('blogdata.txt', 'w')
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
for blog, wordCount in wordCounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wordCount:
            out.write('\t%d' % wordCount[word])
        else:
            out.write('\t0')
    out.write('\n')
