import urllib
url = 'http://export.arxiv.org/api/query?search_query=ti:"reinforcement learning"&sortBy=lastUpdatedDate&sortOrder=descending&start=0&max_results=10'
data = urllib.urlopen(url).read()
print data