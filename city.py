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
| 1)city        |
+--------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")


islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print(""" 
+--------------+-------------+
| Column       | Type        |
+--------------+-------------+
| 1)description  | text        |
| 2)city_id      | int(11)     |
| 3)city_name    | varchar(20) |
| 4)image        | text        |
| 5)keywords     | text        |
| 6)provience_id | int(11)     |
+--------------+-------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")


islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+------------------------+
| description            |
+------------------------+
| Saleem Filling Station |
+------------------------+""")


if islemno == "2":

   print("""
+---------+
| city_id |
+---------+
| 11      |
+---------+""")


if islemno == "3":

   print("""
+----------------------+
| city_name            |
+----------------------+
| NULL                 |
+----------------------+""")

if islemno == "4":

   print("""
+---------+
| image   |
+---------+
| NULL    |
+---------+""")


if islemno == "5":

   print("""
+----------+
| keywords |
+----------+
| NULL     |
+----------+""")




if islemno == "6":

   print("""
+--------------+
| provience_id |
+--------------+
| 11           |
+--------------+""")

