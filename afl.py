from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)

download = article.download()
print(download)
print(article.html)



print(article.authors)


print(article.publish_date)


print(article.text)


print(article.top_image)


print(article.movies)



