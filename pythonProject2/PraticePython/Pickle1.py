import pickle
student = {'name': "Vaishu&Vijay",
           "Department":"IT",
           'Salary':'90k',
           'list': [20,50,95,89,20,78]
           }
# Convert to binary
student_binary = pickle.dumps(student)
#print(student_binary)

# write binary mode
file = open("Pickle.txt", 'wb')
#fdata = file.write(student_binary)
pickle.dump(student,file)
file.close()