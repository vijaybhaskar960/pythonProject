import re

n = "VijayVishu Reddy's"
r = re.search("\w+\s\w+",n)

print(r.group())
