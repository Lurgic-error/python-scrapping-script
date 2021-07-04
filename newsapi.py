import newsapi

# Init
# habari = NewsApiClient(api_key='a94eb0bf40fb4673b027dbd81b20e736')

# /v2/top-headlines
# top_headlines = habari.get_top_headlines(q='bitcoin',
#                                          sources='bbc-news,the-verge',
#                                          category='business',
#                                          language='en',
#                                          country='us')

# # /v2/everything
# all_articles = habari.get_everything(q='bitcoin',
#                                      sources='bbc-news,the-verge',
#                                      domains='bbc.co.uk,techcrunch.com',
#                                      from_param='2017-12-01',
#                                      to='2017-12-12',
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)

# # /v2/sources
# sources = habari.get_sources()

print(newsapi.NewsApiClient)
