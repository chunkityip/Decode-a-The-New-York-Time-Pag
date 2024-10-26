from bs4 import BeautifulSoup
import requests
import csv

url = requests.get('https://www.nytimes.com', timeout=60).text
#To get url code from NewYorkTime(NYT) webiste by using the requests library
#To get the url code from response object , add text
#https://2.python-requests.org/en/master/user/quickstart/#response-content

soup = BeautifulSoup(url, 'lxml')
# lxml is a library that processing XML and HTML

tag = soup.findAll('h2')
# I found out that all news title in NYT website are using h2
#<h2 class="css-1qwxefa esl82me0">
#<span...........>Deficit Will Reach $1 Trillion Next Year, Budget Office Predicts</span>
#</h2>
#The reason of using h2 but not sapn is because span tag is for Big news. I want to print all the news

file = open('news.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Today news at New York Time:'])

for article in tag:
    news = article.text
    print(news)

    writer.writerow([news])
file.close()

#print all the news into csv file call news.csv
