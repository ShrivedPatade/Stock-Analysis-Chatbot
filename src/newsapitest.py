from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='16cf89e0dc4d423780887e4f0272dd6f')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          page=2)

# /v2/everything
all_articles = newsapi.get_everything(q='ongc',
                                      from_param='2026-01-12',
                                      to='2026-01-17',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
print([x['title'] for x in all_articles['articles']], sep='\n')