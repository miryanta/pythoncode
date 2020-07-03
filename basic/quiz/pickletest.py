import pickle

data = {1:'python', 2:'you need'}
#type dict
print(type (data))

#save file
with open("test.pickle",'wb') as f:
    pickle.dump(data,f)

