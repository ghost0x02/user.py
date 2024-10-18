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
| 1)depratment  |
+--------------+""")

print("LÜTFEN BİR SEÇENEK GİRİN")


islemno = input("root@XEN-web:~ ")

if islemno == "1":

   print("""
+---------------+-------------+
| Column        | Type        |
+---------------+-------------+
| name          | NULL 00     |
| department_id | int(11)     |
+---------------+-------------+""")

print("""Bekleyin "department_id" verisine yönlendiriliyorsunuz...""")

time.sleep(5)

print("Bekleyin...")

time.sleep(2)

print("""
+---------------+
| department_id |
+---------------+
| 4             |
| 6             |
| 7             |
| 8             |
| 9             |
| 10            |
| 11            |
| 12            |
| 13            |
| 14            |
+---------------+""")
