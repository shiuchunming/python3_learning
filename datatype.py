
def list():
    print("---List---")

    a_list = ['a']
    a_list = a_list + [2.0, 3]
    a_list.append([1, 2])
    a_list.extend(['four', '#'])
    a_list.insert(0, '1')
    print("List A: " + str(a_list))
    print("Length of list: " + str(len(a_list)))

    print("Slice List:" + str(a_list[1:3]))
    print("Slice List: " + str(a_list[3:]))

    b_list = a_list
    a_list.append(False)
    print("Copy by reference: " + str(a_list))
    print("Copy by reference: " + str(b_list))
    b_list = a_list[:]
    a_list.append("ABC")
    print("Copy by value: " + str(a_list))
    print("Copy by value: " + str(b_list))

def tuple():
    print("\n---Tuple---")

    a_tuple = ("a", "b", "mpilgrim", "z", "example")
    print("Tuple A: " + str(a_tuple))
    try:
        a_tuple.append(False)
    except AttributeError:
        print("Can't Append; Tuple is a immutable version of list")
    
    print(type((False)))
    print(type((False,)))

def set():
    print("\n---Set---")

    a_set = {1, 2}
    a_set.add(3)
    print("Set A: " + str(a_set))
    a_set.update({1, 2, 3, 4})
    a_set.update([1, 2, 3, 0])
    print("Set A: " + str(a_set))
    a_set.discard(10)
    try:
        a_set.remove(10)
    except:
        print("Element 10 does not exists in Set")

def dictionary():
    print("\n---dictionary---")

    a_dict = {'server': 'db.diveintopython3.org', 'database': 'oracle'}
    print(a_dict['server'])

if __name__ == '__main__':
    list()
    tuple()
    set()
    dictionary()