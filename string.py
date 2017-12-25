s = 'A'
print("length of s: " + str(len(s)))

list = ['A', 'a', 'c']
print("List: " + str(list).strip('[]'))
print("1st: {0[0]}, 2nd: {0[1]}, 3rd: {0[2]}".format(list))
print("1st: {0[0]}, 2nd: {0[1]}, 3rd: {0[2]}".format(list).lower())
print("Count of 'A' or 'a': " + str("1st: {0[0]}, 2nd: {0[1]}, 3rd: {0[2]}".format(list).lower().count('a')))

query = 'user=super&database=db121&password=me!=me'
a_list = query.split('&')
print("Split: " + str(a_list))

a_list_of_list = [v.split('=', 1) for v in a_list if '=' in v]
print("Split again: " + str(a_list_of_list))


