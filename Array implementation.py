class array():
 def __init__(self):
     self.l=[]
 def insert_at_end(self,list,value):
     l=list
     l.append(value)
     return l
 def insert_at_beginning(self,list,value):
     l=list
     l.insert(0,value)
     return l
 def insert_at_middle(self,list,value,index):
     l=list
     l.insert(index,value)
     return l
 def _to_count(self,list):
     l=list
     l.count(list)
     return l
 def _to_pop(self,list):
     l=list
     l1=l.pop()
     return l1
 def _to_sort(self,list):
    l=list
    l.sort()
    return l
 def _to_find_length(self,list):
    l=list
    l1=len(l)
    return l1
 def _to_reverse(self,list):
    l=list
    l.reverse()
    return l
 def _to_display_thelist(self,list):
     l=list
     return l
 def _to_clear(self,list):
     l=list
     l.clear()
     return l
obj=array()
list=[21,32,45,65,99,72,33]
while(list):
    print("1.insert at end")
    print("2.insert at beginning")
    print("3.insert at middle")
    print("4.to count the list")
    print("5.to pop the list")
    print("6.to sort the list")
    print("7.to find the length of the list")
    print("8.to reverse the list")
    print("9.display the list")
    print("10.clear the list")
    print("11.PROGRAM EXIT")
    print("-----------------------------")
    choice=int(input("enter the choice: "))
    if choice==1:
        value=input("enter the value: ")
        result=obj.insert_at_end(list,value)
        print(result)
    elif choice==2:
        value=input("enter the value: ")
        result=obj.insert_at_beginning(list,value)
        print(result)
    elif choice==3:
        value=input("enter the value: ")
        pos=int(input("enter the position: "))
        result=obj.insert_at_middle(list,value,pos)
        print(result)
    elif choice==4:
        result=obj._to_count(list)
        print(result)
    elif choice==5:
        result=obj._to_pop(list)
        print(result)
    elif choice==6:
        result=obj._to_sort(list)
        print(result)
    elif choice==7:
        result=obj._to_find_length(list)
        print(result)
    elif choice==8:
        result=obj._to_reverse(list)
        print(result)
    elif choice==9:
        result=obj._to_display_thelist(list)
        print(result)
    elif choice==10:
        result=obj._to_clear(list)
        print(result)
    elif choice==11:
        print("program exit")
        break
