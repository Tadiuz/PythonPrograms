from faker import Faker

import pandas as pd

import csv




fake = Faker()

Names = [fake.name() for i in range(100)]

ipv4 = [fake.ipv4() for i in range(100)]

language_name = [fake.language_name() for i in range(100)]

last_name = [fake.last_name() for i in range(100)]

password = [fake.password() for i in range(100)]

address = [fake.address() for i in range(100)]



# First Method using pandas
dict = {'Names': Names, 'Last Name': last_name, 'ipv4': ipv4, 'language name': language_name, 'password': password}
df = pd.DataFrame(dict)


#Using CSV library

headers  = ["Names", "Last Name", "ipv4", "language name", "password"]

name = "csv_library.csv"


with open (name, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(headers)
    csvwriter.writerows(list(zip(Names,last_name,  ipv4, language_name, password)))


#Using pure python

headers_str = '"' + '","'.join(headers) + '"'
with open("pure1" + name, 'w', newline="") as file:
    file.write(headers_str)
    file.write("\n")
    for i in list(zip(Names,last_name,  ipv4, language_name, password)):
        line = '"' + '","'.join(i) + '"'
        file.writelines(line)
        file.write("\n")



#read csv pure python
import time

n = []
with open("pure1" + name, 'r', newline="") as file:
    l = [line.rstrip().split(',') for line in file]




rows = []
with open("pure1" + name, 'r' ) as file:
    csvreader = csv.reader(file)

    l = [line for line in csvreader]




print(l)







