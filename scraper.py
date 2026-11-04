import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"


def scrape_books():
    print("Mengambil data dari website...")

    response = requests.get(URL)

    if response.status_code != 200:
        print("Gagal mengambil halaman.")
        print("Status code:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    data = []

    for book in books:
        title = book.h3.a["title"]

        price = book.select_one(".price_color").text.strip()

        # Memperbaiki karakter mata uang Pound
        price = price.replace("Ã‚Â£", "£")
        price = price.replace("Â£", "£")

        availability = book.select_one(
            ".availability"
        ).text.strip()

        rating = book.select_one(
            "p.star-rating"
        )["class"][1]

        book_url = book.h3.a["href"]

        data.append({
            "judul": title,
            "harga": price,
            "rating": rating,
            "ketersediaan": availability,
            "url": book_url
        })

    return data


def save_to_csv(data):
    with open(
        "data/books.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        fieldnames = [
            "judul",
            "harga",
            "rating",
            "ketersediaan",
            "url"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    books = scrape_books()

    if books:
        save_to_csv(books)

        print()
        print("Scraping berhasil!")
        print("Jumlah data:", len(books))
        print("Data disimpan di data/books.csv")
    else:
        print("Tidak ada data yang berhasil diambil.")
