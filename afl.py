from newspaper import Article

url = 'https://www.afr.com/markets/equity-markets/retail-stocks-hit-with-reality-check-as-hawkish-rba-spoils-results-20230209-p5cjc2'
article = Article(url)

article.download()




print("33333333333333", article.parse())

print("4444444444444444", article.authors)


print("5555555555555555555", article.publish_date)


print("666666666666666666666", article.text)


print(article.top_image)


print(article.movies)



