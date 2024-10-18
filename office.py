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
| 1)office      |
+--------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")


islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+-------------+---------+
| Column      | Type    |
+-------------+---------+
| 1)description | text    |
| 2)name        | text    |
| 3)email       | text    |
| 4)keyword     | text    |
| 5)latitude    | float   |
| 6)logitude    | float   |
| 7)office_id   | int(11) |
| 8)other       | text    |
| 9)phone1      | text    |
| 10)phone2      | text    |
+-------------+---------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")

islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
NULL""")
