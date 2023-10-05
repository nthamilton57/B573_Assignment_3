#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#create a function that will generate a certain number of fibonacci numbers
def fib_nums(num):
    #if the number is 0 then it will ask for a positive integer. This doesnt really apply to this assignment as the number will be predefined in the code.
    if int(num) == 0:
        num = input("Please enter a positive integer.   ")
    
    #If the number is equal to 1, then the sequence will just be an array of 1 using the built in ones feature of np
    if int(num) == 1:
        fib_seq = np.ones(1,1)
        return fib_seq
    
    #If the number is greater than 1, set num1 and num2 equal to 1 and create an empty array for fib_seq and set our counter, n, to 0
    if int(num) > 1:
        num1, num2 = 1,1
        fib_seq = np.array([])
        n = 0
        
        #While counter number is less than the number of fibonacci numbers we want, we will append a number.
        while n < int(num):
            fib_seq = np.append(fib_seq, num1)
            
            #Update is a number that is used to redefine number 2 which is used to update number 1. it itself is never appended though
            update = num1 + num2
            #redefine number 1 as number 2 which will be appended in the next cycle
            num1 = num2
            #num2 is redifined as update
            num2 = update
            #increase our counter
            n += 1
            
        #fib_seq = np.array(fib_seq)
        #return the sequence
        return fib_seq


#define a function that will generate the quotient list of fibonacci numbers
def fib_quot(array):
    #generate an array with just one one
    fib_quot = np.ones((1,1))
    #set counter equal to 0
    n = 0
    #if length of array is 1, then the already defined array will be returned
    if len(array) == 1:
        return fib_quot
    #otherwise we will append values
    else:
    #while the counter is less than the length of the array - 1 (to account for the fact that we are dividing one number by the previous so we cant go to the absolute last number)
        while n < len(array)-1:
            #append the quotient of one number and the one before it
            fib_quot = np.append(fib_quot, array[n+1]/array[n])
            #increase the counter
            n += 1
    #return the array
    return fib_quot


#define a function that will generate the difference list of fibonacci numbers
def fib_dif(array):
    #create an empty array
    fib_dif = np.array([])
    #set counter equal to 0
    n=0
    #while the counter number is less than the number of fibonacci numbers we want, we will append a number.
    while n < len(array):
        #if the numbers we want is less than or equal to one, we will append a 0 and increase the counter
        if n <=1:
            fib_dif = np.append(fib_dif,0)
            n += 1
        #otherwise, we will append the difference between the element of an array and the previous element and increase our counter
        else:
            fib_dif = np.append(fib_dif, array[n]-array[n-1])
            n += 1
    #return the array
    return fib_dif

#here we create an array of 20 numbers and then use that array to create an additional array for the quotient and the difference array
Fib_Seq = fib_nums(20)
Fib_Quot = fib_quot(Fib_Seq)
Fib_Dif = fib_dif(Fib_Quot)



#create a y axis array that will just have the index of each number in each sequence (with indexing starting at 1)
##create a counter list that is empty
counterlist = np.array([])
#use a for loop in the length of the fibs_np array
for i in range(1,len(Fib_Seq)+1):
    #append the number to the new array
    counterlist = np.append(counterlist, i)

#Create a graph of all arrays together with their index
#we will create subplots with 1 row and 3 columns
fig, axes = plt.subplots(1, 3)
#main title
fig.suptitle('Possible Convergence in Fibonacci Sequence and Its Derivatives')
#main xlable
fig.supxlabel('Index of Sequence')
#main ylabel
fig.supylabel('Value of Number in Sequence')

#create the first graph in the leftmost slot with counterlist and fibonacci sequence
axes[0].plot(counterlist, Fib_Seq)
#set the individual title
axes[0].set_title('Fib_Seq')
#set the y label that will be ued for the whole figure
#axes[0].set_ylabel('Value of Number in Sequence')

#create the second graph in the middle slot with counterlist and fibonacci sequence quotients
axes[1].plot(counterlist, Fib_Quot, color = 'red')
#set the individual title
axes[1].set_title('Fib_Quot')
#set the xlabel that will be used for the whole figure
#axes[1].set_xlabel('Index of Sequence')

#create the third graph in the rightmost slot with counterlist and fibonacci sequence differences
axes[2].plot(counterlist, Fib_Dif, color = 'green')
#set the individual title
axes[2].set_title('Fib_Dif')

#to make sure there is no overlap
plt.tight_layout()

#Discuss the convergence of the graphs
print("Based on the graphs, both the difference and quotient arrays do converge. The Fibonacci sequence however will infinitely increase. The Fib_Quot array appears to converge to 1.61803 while the Fib_Dif array appears to converge to 0.")

#show the graph
plt.show()
