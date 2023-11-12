#list 
listValue = list()
def list_save(list1):
    listvar = list1
    
    listValue.insert(0,listvar)

    print(listValue)
    pass
l = list()
for i in range(0,10):
    list_save(i)
    l.insert(0,i)

print(l)
