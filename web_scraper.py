import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("books_rated.csv", "w", newline="") as file:
     writer = csv.writer(file)
     writer.writerow(["Title", "Price", "Rating"])

     for book in books:
         title = book.h3.text
         price = book.find("p", class_="price_color").text
         price = float(price.replace("£", "").replace("Â", "").strip())
         rating = book.find("p", class_="star-rating")["class"][1] 
         writer.writerow([title, price, rating])


print("Books saved to csv!")

 
