class Node:
    def __init__ (self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__ (self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self, value):
        new_node= Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    def pop_first(self):
        if self.head==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.length-=1
        if(self.length==1):
            self.tail=None
        return temp
    def get(self, index):
        if index<0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set_value(self, index, value):
        temp=self.get(index)
        if temp:
            temp.value=value       
            return True
        return False
    def insert(self,index,value):
        if index<0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node=Node(value)
        temp = self.get(index-1)     
        new_node.next = temp.next
        temp.next=new_node
        self.length+=1
        return True
    def remove(self,index):
          if index<0 or index >= self.length:
            return None
          if index==0:
            self.pop_first
          if index == self.length-1:
              self.pop  
          prev=self.get(index-1)
          temp=prev.next
          prev.next = temp.next
          temp.next=None
          self.length -=1
          return temp
    def reverse(self):
        temp = self.head
        self.head=self.tail
        self.tail=temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after


#test
mi_lista = LinkedList(2)
mi_lista.append(3)
mi_lista.append(4)
mi_lista.append(5)
mi_lista.append(6)
mi_lista.append(7)

mi_lista.prepend(1)

mi_lista.print_list()
mi_lista.pop_first()
print("Lista nueva")
mi_lista.print_list()
mi_lista.set_value(0,4)
print("Lista nueva")
mi_lista.print_list()
mi_lista.insert(3,10)
mi_lista.print_list()
print("Lista nueva quitando el 2do")
mi_lista.remove(1)
mi_lista.print_list()
mi_lista.reverse()
print("Lista nueva inversa")
mi_lista.print_list()

