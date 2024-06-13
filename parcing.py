import requests
from bs4 import BeautifulSoup
from time import sleep
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
conn = psycopg2.connect(
        dbname=os.getenv("DBNAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host="localhost",
    )
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS Товары (
        id SERIAL PRIMARY KEY,
        название VARCHAR(255),
        цена VARCHAR(50),
        описание TEXT
    )
""")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
def get_url():
    for count in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="w-full rounded border")
        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url

for k in get_url():
    response = requests.get(k, headers=headers)
    sleep(3)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="my-8 w-full rounded border")
    name = data.find("h3", class_="card-title").text
    price = data.find("h4", class_="my-4 card-price").text
    description = data.find("p", class_="card-description").text
    print(name + "\n" + price + "\n" + description + "\n\n")
    cur.execute("INSERT INTO Товары (название, цена, описание) VALUES (%s, %s, %s)", (name, price, description))
conn.commit()
cur.close()
conn.close()