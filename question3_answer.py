frequency_dict = {}
def frequency( m_list, dictionary ):
    for n in m_list:
        if dictionary.get(n)!=None:
            dictionary[n]+= 1
        else:
            dictionary[n] = 1

frequency_dict = {}
myList = [0, 1, 3, 4, 5, 5, 2, 4, 3, 1];
frequency(myList, frequency_dict)
print (frequency_dict)
