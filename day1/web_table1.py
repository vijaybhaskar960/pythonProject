# Count the number of rows and columns in table
# Read specific row and Column
# Read all rows and columns data
# Read data based on condition

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
d = webdriver.Chrome()

d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
# Count the number of rows and columns in table

rows = len(d.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(rows)

Columns = len(d.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))
print(Columns)
# Read specific row and Column

specific  = d.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
print(specific)

# Read all rows and columns data

for r in range(2,rows+1):
    for c in range(1,Columns+1):
        data = d.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end= " ")

    print()

# Read data based on condition

for r in range(2,rows+1):
    authorname = d.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname== "Mukesh":
        bookname = d.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = d.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname,"    ",authorname,"     ",price)
d.close()
