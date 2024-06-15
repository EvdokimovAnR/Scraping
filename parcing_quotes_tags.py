import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import psycopg2
from dotenv import load_dotenv
import os
from time import sleep
import time

start_time = time.time()

load_dotenv()
conn = psycopg2.connect(
    dbname=os.getenv("DBNAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host="localhost"
)

cur = conn.cursor()
cur.execute(""" 
    CREATE TABLE Цитаты_по_тегам (
        id SERIAL PRIMARY KEY, 
        Цитата VARCHAR(5000), 
        Автор VARCHAR(255), 
        Дата_рождения VARCHAR(255), 
        Место_рождения VARCHAR(255)        
) """)



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
url = "https://quotes.toscrape.com"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
data = soup.find_all("span", class_="tag-item")
url_tag_list = []
url_author_list = []
for i in data:
    sleep(3)
    url_tag = url + i.find("a", class_="tag").get("href")
    url_tag_list.append(url_tag)
for k in url_tag_list:
    response1 = requests.get(k, headers=headers)
    soup1 = BeautifulSoup(response1.text, "lxml")
    data1 = soup1.find_all("div", class_="quote")
    # quote = data1.find("span", class_="text").text
    for l in data1:
        quote = l.find("span", class_="text").text
        author = l.find("small", class_="author").text
        author_relative_url = l.find("a").get("href")
        url_author = urljoin(k, author_relative_url)
        url_author_list.append(url_author)
        for s in url_author_list:
            sleep(3)
            response2 = requests.get(s, headers=headers)
            soup2 = BeautifulSoup(response2.text, "lxml")
            data2 = soup2.find("div", class_="author-details")
            born_date = data2.find("span", class_="author-born-date").text
            born_location = data2.find("span", class_="author-born-location").text
        print(quote, author, born_date, born_location)
        cur.execute("INSERT INTO Цитаты_по_тегам (Цитата, Автор, Дата_рождения, Место_рождения) VALUES (%s, %s, %s, %s)", (quote, author, born_date, born_location))
conn.commit()
cur.close()
conn.close()
end_time = time.time()

execution_time = end_time - start_time

print("Время выполнения: ", execution_time)










