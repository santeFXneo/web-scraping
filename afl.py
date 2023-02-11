from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)

article.download()




print("33333333333333", article.parse())

print("4444444444444444", article.authors)


print("5555555555555555555", article.publish_date)


print("666666666666666666666", article.text)


print(article.top_image)


print(article.movies)



