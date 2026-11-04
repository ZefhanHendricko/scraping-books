\# Web Scraping Books dengan Python



\## Deskripsi



Project ini merupakan implementasi web scraping menggunakan bahasa pemrograman Python. Proses scraping menggunakan library Requests untuk mengambil halaman website dan BeautifulSoup4 untuk melakukan parsing HTML.



Website yang digunakan adalah \*\*Books to Scrape\*\*, yaitu website yang menyediakan data buku untuk latihan web scraping.



Data yang berhasil dikumpulkan meliputi judul buku, harga, rating, ketersediaan, dan URL buku.



\## Tujuan



Project ini bertujuan untuk:



1\. Mempelajari konsep dasar web scraping.

2\. Menggunakan Requests untuk mengambil data dari website.

3\. Menggunakan BeautifulSoup4 untuk membaca struktur HTML.

4\. Mengambil informasi buku secara otomatis.

5\. Menyimpan hasil scraping dalam format CSV.

6\. Menggunakan Git dan GitHub untuk mengelola project.



\## Teknologi



Project ini menggunakan:



\- Python

\- Requests

\- BeautifulSoup4

\- CSV

\- Git

\- GitHub



\## Data yang Dikumpulkan



| Data | Keterangan |

|---|---|

| Judul | Judul buku |

| Harga | Harga buku |

| Rating | Rating buku |

| Ketersediaan | Status ketersediaan buku |

| URL | URL halaman buku |



\## Proses Scraping



Alur proses scraping:



```text

Website Books to Scrape

&#x20;       ↓

Requests

&#x20;       ↓

Mengambil HTML

&#x20;       ↓

BeautifulSoup4

&#x20;       ↓

Parsing HTML

&#x20;       ↓

Mengambil data buku

&#x20;       ↓

CSV

&#x20;       ↓

GitHub

```



\## Cara Menjalankan Project



\### 1. Clone repository



```bash

git clone URL\_REPOSITORY

```



\### 2. Masuk ke folder



```bash

cd scraping-books

```



\### 3. Membuat virtual environment



```bash

python -m venv .venv

```



\### 4. Mengaktifkan virtual environment pada Windows



```powershell

.venv\\Scripts\\Activate.ps1

```



\### 5. Install library



```bash

pip install -r requirements.txt

```



\### 6. Menjalankan scraper



```bash

python scraper.py

```



\## Hasil Scraping



Program menghasilkan \*\*20 data buku\*\*.



Hasil scraping disimpan pada:



```text

data/books.csv

```



File CSV berisi kolom:



```text

judul

harga

rating

ketersediaan

url

```



\## Struktur Project



```text

scraping-books/

│

├── data/

│   └── books.csv

│

├── .venv/

│

├── .gitignore

├── README.md

├── requirements.txt

└── scraper.py

```







Project ini berhasil melakukan web scraping menggunakan Python, Requests, dan BeautifulSoup4. Data buku berhasil diambil dari website Books to Scrape dan disimpan dalam format CSV. Git dan GitHub digunakan untuk menyimpan serta mengelola source code dan hasil project.

