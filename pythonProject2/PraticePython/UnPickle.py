import pickle

data = {}
file = open("Pickle.txt", 'rb')
data = pickle.load(file)
file.close()
print(data)
print(data['list'])
print(data['name'])
print(data['Salary'])

