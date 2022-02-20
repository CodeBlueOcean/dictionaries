# # # Dictionary 
# # [1]
# # dictionary = {
# #     'a' : 1,
# #     'b' : 2
# # }

# # print(dictionary['c'])

# Dictionary 
dictionary = {
    'a' : 1,
    'b' : 2,
    'x' : 3
}

print(dictionary['b'])

# another example Dictionary 
dictionary = {
    'a' : [1,2,3], 
    'b': 'hello', 
    'x' : True
}

my_list = [{ 
    'a' : [1,2,3], 
    'b': 'hello', 
    'x' : True
},
{
    'a': [4,5,6],
    'b': 'hello',
    'c': True
}
]
print(my_list[0]['a'][2])
# above code grab the first {}, 'a', index 2 
print(dictionary['a'][1])


