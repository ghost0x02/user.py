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
| 1)employee    |
+--------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")


islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+---------------+-------------+
| Column        | Type        |
+---------------+-------------+
| 1)name          | varchar(40) |
| 2)address       | text        |
| 3)department_id | int(11)     |
| 4)email         | text        |
| 5)employee_id   | int(11)     |
| 6)image         | text        |
| 7)keyword       | text        |
| 8)phone_no      | text        |
+---------------+-------------+""")


print("LÜTFEN BİR SEÇENEK GİRİN")

islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+--------------+
| name         |
+--------------+
| Mr. Shafique |
+--------------+""")

if islemno == "2":

   print("""
+---------+
| address |
+---------+
| Horizon |
+---------+""")

if islemno == "3":

   print("""
+---------------+
| department_id |
+---------------+
| 5             |
+---------------+""")

if islemno == "4":

   print("""
+-----------------------------+
| email                       |
+-----------------------------+
| mshafique@horizonoil.com.pk |
+-----------------------------+""")

if islemno == "5":

   print("""
+-------------+
| employee_id |
+-------------+
| 8           |
+-------------+""")

if islemno == "6":

   print("""
+-----------------------------------+
| image                             |
+-----------------------------------+
| uploads/employee/Mr. Shafique.jpg |
+-----------------------------------+""")

if islemno == "7":

   print("""
+---------+
| keyword |
+---------+
| CFO     |
+---------+""")

if islemno == "8":

   print("""
+-------------+
| phone_no    |
+-------------+
| 03224596364 |
+-------------+""")
