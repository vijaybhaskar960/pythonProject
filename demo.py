# def count_duplicate_values(dictionary):
#     duplicate_count = {}
#     for value in dictionary.values():
#         if value in duplicate_count:
#             duplicate_count[value] += 1
#         else:
#             duplicate_count[value] = 1
#     return {k:v for k, v in duplicate_count.items() if v > 1}
#
# example_dictionary = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
#
# print(count_duplicate_values(example_dictionary))
#
# import calendar
#
# year = 2023
# month = 1
#
# # Print the calendar
# print(calendar.month(year, month))
#
#
# from selenium import webdriver
#
# d = webdriver.Chrome(executable_path=r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
# d.get('https://www.amazon.in/')
# d.maximize_window()
# d.save_screenshot(r'C:\Users\Vijay Bhaskar Reddy\OneDrive\Desktop\Python_Notepad++\vijay.png')
#


fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

