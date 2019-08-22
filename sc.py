list1=[[1,2],[3,[4,5,[6,7]]]]


new_list=[]

def list_printer(l):
    for e in l:
        if isinstance(e,list):
            list_printer(e)


        else:
            new_list.append(e)













for i in list1:
    list_printer(i)


print(new_list)    













