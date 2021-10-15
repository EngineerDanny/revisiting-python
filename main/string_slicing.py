#[start:stop:step]

name = "Danny Agyapong"

first_char = name[0]
init_name  = name[0:3] #first index is inclusive and last index is exclusive
init_name  = name[:3] #same logic as 👆
last_name  = name[6:] 
reverse_name = name[::-1]

# print(first_char )
# print(init_name )
# print(last_name )
# print(reverse_name )


#using slice function instead, with a comma inplace of a column

m_first_char = name[slice(1,-1)]
# init_name  = name[0:3] #first index is inclusive and last index is exclusive
# init_name  = name[:3] #same logic as 👆
# last_name  = name[6:] 
# reverse_name = name[::-1]

print(m_first_char )


