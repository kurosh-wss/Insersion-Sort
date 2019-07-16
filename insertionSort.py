import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple



# !!!!!    phase 1    !!!!!


# implementation of insertion sort
def insertionSort(lon): # lon ==>> list of numbers
    for i in range(1, len(lon)):
        key = lon[i]
        j = i-1

        while (j>=0 and lon[j]>key):
            lon[j+1] = lon[j]
            j -= 1
        
        lon[j+1] = key




# generating list of random numbers

def numberGenerator(numberOfLists, minRange, maxRange, m, n): # a, b, c ==>> length of the numbers in three lists
    mainList = []
    for i in range(numberOfLists):
        subList = []
        listRange = random.randint(minRange, maxRange)
        for k in range(listRange):
            subList.append(random.randint(m, n))
        mainList.append(subList)
    return mainList



# implementing the insert method

def insert(number, array): # inserting a number in its sorted position in the given sorted list(array)
    a = 0
    b = 1
    if len(array) is 0:
        array.append(number)
        return
    if array[0] == number:
        array.insert(0, number)
        return

    for i in range(len(array)):
        if array[i] == number:
            array.insert(i, number)
            return
        elif array[i] > number:
            array.insert(i, number)
            return






# !!!!!!!   phase 2   !!!!!!!!!!





# implementing doubly linked list(dll) 
# implementing doubly linked list(dll) 

class Node:

    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class dll:
    
    counter = 0 

    def __init__(self):
        self.head = None

    # adding a node at first
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        
        if self.head is not None:
            self.head.prev = newNode
        
        self.head = newNode
        self.counter += 1

    # adding node at the end
    def append(self, newData):
        newNode = Node(newData)
        newNode.next = None
        
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.counter += 1
            return

        lastNode = self.head
        while (lastNode.next is not None):
            lastNode = lastNode.next
            
        lastNode.next = newNode

        newNode.prev = lastNode
        self.counter += 1
        return

    # adding a node after a given node
    def insertAfter(self, prevNode, newData):
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        
        if (newNode.next is not None):
            newNode.next.prev = newNode

    def delete(self, targetNode):
        if self.head is None:
            return
        
        temp = self.head
        while (temp.next is not targetNode):
            temp = temp.next

        if (temp.next.next is None):
            temp.next = None
            return
        temp.next.next.prev = temp
        temp.next = temp.next.next

    

    # finding a number in the linked list if it exists
    def crawler(self, number):
        temp = self.head
        i = 0
        while (i != number and temp.next is not None):
            temp = temp.next
            i += 1
        return temp

    # inserting a node with binary search
    def inserting(self, number):
        firstIndex = 0
        lastIndex = self.counter

        if (self.counter is 0):
            self.append(number)
            return

        while (firstIndex <= lastIndex):
            middle = firstIndex + (lastIndex - firstIndex) / 2
            helpNode = self.crawler(middle)

            if ((helpNode.data > number and helpNode.prev is None)):
                self.push(number)
                self.counter += 1
                return
            
            elif ((helpNode.data < number and helpNode.next is None)):
                self.append(number)
                self.counter += 1
                return

            elif ((helpNode.data == number) or (helpNode.data < number and helpNode.next.data > number)):
                self.insertAfter(helpNode, number)
                self.counter += 1
                return

            elif (helpNode.data < number and helpNode.next is not None):
                firstIndex = middle + 1
            elif (helpNode.data > number and helpNode.prev is not None):
                lastIndex = middle - 1


    # insertion sort with linked list

    def insertionSort(self):
        sortedLL = dll()
        temp = self.head
        sortedLL.append(temp.data)
        while(temp.next is not None):
            sortedLL.inserting(temp.next.data)
            temp = temp.next
        self.head = sortedLL.head

    def toList(self):
        numbers = [] 
        temp = self.head
        while (temp is not None):
            numbers.append(temp.data)
            temp = temp.next
        return numbers

    def printer(self, node):
        while (node is not None):
            print(node.data)
            node = node.next




# comparing...






def first(lists, a, b):
    result = []
    numbers = numberGenerator(lists, a, b, 10, 1000)
    STL = [] # simple times list
    CTL = [] # complicated times list
    
    numbers.sort(key = lambda s:len(s))

    numbersLength = []
    for i in numbers:
        length = len(i)
        numbersLength.append(length)


    temp = numbers

    for i in range(lists):
        start = time.clock()
        insertionSort(temp[i])
        end = time.clock()
        STL.append(end - start)


    for i in range(lists):
        start = time.clock()
        ll = dll()
        for j in range(len(numbers[i])):
            ll.append(numbers[i][j])
        ll.insertionSort()
        end = time.clock()
        CTL.append(end - start)

    result.append(STL)
    result.append(CTL)
    result.append(numbersLength)
    return result



def second(lists, a, b):
    result = []
    numbers = numberGenerator(lists, a, b, 10, 1000)
    numbers.sort(key = lambda s:len(s))
    STL = [] # simple times list
    CTL = [] # complicated times list
    numbersLength = []
    for i in numbers:
        length = len(i)
        numbersLength.append(length)

    temp = numbers
    for i in range(lists):
        start = time.clock()
        l = []
        for j in range(len(temp[i])):
            insert(j, l)
        end = time.clock()
        STL.append(end - start)

    for i in range(lists):
        start = time.clock()
        ll = dll()
        for j in range(len(numbers[i])):
            ll.inserting(numbers[i][j])
        end = time.clock()
        CTL.append(end - start)

    result.append(STL)
    result.append(CTL)
    result.append(numbersLength)
    return result


# plotting...

def plotting(mainList):
    

    col1 = (mainList[0])
    col2 = (mainList[1])

    ind = np.arange(len(mainList[-1])) 
    width = 0.5

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, col1, width,
                    color='SkyBlue', label='Simple')
    rects2 = ax.bar(ind + width/2, col2, width,
                    color='IndianRed', label='Linked List')

    ax.set_ylabel('Times Lists')
    ax.set_title('Time Table for Linked List and Simple Insertion Sort')
    ax.set_xticks(ind)
    testsList = []
    for i in mainList[-1]:
        testsList.append(i)

    ax.set_xticklabels(tuple(testsList))
    ax.legend()



    def autolabel(rects, xpos='center'):


        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom')


    autolabel(rects1, "left")
    autolabel(rects2, "right")

    plt.show()


plotting(first(100, 1000, 2000))
plotting(second(100, 1000, 20000))