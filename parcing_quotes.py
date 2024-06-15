import requests
from requests import Session
from bs4 import BeautifulSoup
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
conn = psycopg2.connect(
    dbname=os.getenv("DBNAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host="localhost"
)

cur = conn.cursor()
cur.execute(""" 
    CREATE TABLE Цитаты (
        id SERIAL PRIMARY KEY, 
        Цитата VARCHAR(5000), 
        Автор VARCHAR(255), 
        Дата_рождения VARCHAR(255), 
        Место_рождения VARCHAR(255)        
) """)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
session = requests.Session()
response = session.get("https://quotes.toscrape.com/login", headers=headers)
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("input", {"name": "csrf_token"})["value"]
data = {
    "csrf_token": token,
    "username": "username",
    "password": "password"
}
response = session.post("https://quotes.toscrape.com/login", data=data, headers=headers, allow_redirects=True)




url = "https://quotes.toscrape.com"
response1 = requests.get(url, headers=headers)
soup1 = BeautifulSoup(response1.text, "lxml")
data1 = soup1.find_all("div", class_="quote")

author_url_list = []


for count in range(1, 6):
    url = f"https://quotes.toscrape.com/page/{count}/"
    response1 = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(response1.text, "lxml")
    data1 = soup1.find_all("div", class_="quote")
    for i in data1:
        text = i.find("span", class_="text").text
        author = i.find("small", class_="author").text
        author_url = " https://quotes.toscrape.com" + i.find("a").get("href")
        author_url_list.append(author_url)
        for k in author_url_list:
            response2 = requests.get(k, headers=headers)
            soup2 = BeautifulSoup(response2.text, "lxml")
            data2 = soup2.find("div", class_="author-details")
            born = data2.find("span", "author-born-date").text
            location = data2.find("span", "author-born-location").text
            description = data2.find("div", "author-description").text
        print(text, author, born, location, description)
        cur.execute("INSERT INTO Цитаты (Цитата, Автор, Дата_рождения, Место_рождения) VALUES (%s, %s, %s, %s)", (text, author, born, location))
conn.commit()
cur.close()
conn.close()






