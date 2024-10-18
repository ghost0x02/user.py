from colorama import Fore, Style
import time


print(Fore.RED + """
   _____ ____    __
  / ___// __ \  / /
  \__ \/ / / / / /
 ___/ / /_/ / / /___
/____/\___\_\/_____/
                    """)
time.sleep(1)

print("""
 +--------------+
| 1)news         |
+--------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")


islemno = input("root@XEN-web:~ ")

print("""
+-------------+-------------+
| Column      | Type        |
+-------------+-------------+
| 1)description | text        |
| 2)name        | varchar(60) |
| 3)status      | int(11)     |
| 4)image       | text        |
| 5)keyword     | text        |
| 6)news_id     | int(11)     |
+-------------+-------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")

islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| THE COMPANY IS GOING TO LAUNCH THEIR FURNACE OIL IN THE MARKET                                                                                             |
| NEWLY PAINTED OIL TANKERS OF HORIZON OIL COMPANY. IT IS MOST AUSPICIOUS COLOR MATCHING AND DESIGN OF HORIZON LORRY. TANKERS ARE MOVING ACROSS THE COUNTRY. |
| the HORIZON oil is offering quality fuel at standard pricing .the quantity of HSD and PMG is avaliabe                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+""")

if islemno == "2":

   print("""
+---------------------+
| name                |
+---------------------+
| Horizon Oil Company |
| HORIZON OIL TANKERS |
| NEW PRICE           |
---------------------+""")

if islemno == "3":

   print("""
+----------+
| status   |
+----------+
| 1        |
| -1       |
| -1       |
+----------+""")

if islemno == "4":

   print("""
+--------------------------------------+
| image                                |
+--------------------------------------+
| uploads/news/Horizon Oil Company.png |
| uploads/news/HORIZON OIL TANKERS.jpg |
| uploads/news/NEW PRICE.jpg           |
+--------------------------------------+""")

if islemno == "5":

   print("""
+------------------------------+
| keyword                      |
+------------------------------+
| HORIZON FURNACE OIL          |
| DESIGN OF HORIZON OIL TANKER |
| Pricing of HSD and PMG       |
+------------------------------+""")

if islemno == "6":

   print("""
+---------+
| news_id |
+---------+
| 6       |
| 7       |
| 16      |
+---------+""")
