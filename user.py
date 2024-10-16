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
| 1)user         |
+--------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")


islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+-------------+-------------+
| Column      | Type        |
+-------------+-------------+
| 1)description | text      |
| 2)email       | text      |
| 3)firstname   | varchar(20) |
| 4)image       | text        |
| 5)keyword     | text        |
| 6)lastname    | varchar(20) |
| 7)password    | text        |
| 8)user_id     | int(11)     |
| 9)username    | varchar(40) |
+-------------+-------------+

""")
print("LÜTFEN BİR SEÇENEK GİRİN")

islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+---------------+
| description   |
+---------------+
| nothing       |
|
+---------------+""")

if islemno == "2":

   print("""
+-----------------------+
| email                 |
+-----------------------+
| abdulrazak@orizol.com |
|
+-----------------------+""")

if islemno == "3":

   print("""
+-----------+
| firstname |
+-----------+
| Rehana    |
| abdul     |
+-----------+""")

if islemno == "4":

   print("""
+--------------------------+
| image                    |
+--------------------------+
| uploads/users/Rshafi.jpg |
| uploads/users/abdul.png  |
+--------------------------+""")

if islemno == "5":

   print("""
+---------+
| keyword |
+---------+
| Rs      |
| a       |
+---------+""")

if islemno == "6":

   print("""
+----------+
| lastname |
+----------+
| Shafi    |
| razak    |
+----------+""")

if islemno == "6":

   print("""
+------------------+
| password         |
+------------------+
| Abdul@123456789! |
|
+------------------+""")

if islemno == "7":

   print("""
+---------+
| user_id |
+---------+
| 1       |
| 4       |
+---------+""")


if islemno == "7":

   print("""
+----------+
| username |
+----------+
| NULL     |
| NULL     |
+----------+ NULL :( """)
