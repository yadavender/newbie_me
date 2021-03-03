x = ("sexy titties")
print(f"i like {x} baby")

y = ['a','v','g','c']
y.sort()
print(y)

y={'yadav':'21','manu':'22'}
print(y['yadav'])

y={'yadav':'21','manu':'22'}
y['mama']= '50'
print(y)

y=['yadavender']
print(y[0] + " yadav")

test = open('test.txt')
test.seek(0)
print(test.read())

file='test.txt'
with open('test.txt') as file:
    contents = file.read()
print(contents)

y=int(input ("Enter the number:"))
x=y ** 0.5
print('Root of', y, 'is', x)

y=int(input ("Enter the number:"))
x=y ** 0.5
print('Root of', y, 'is', '{:.2f}'.format(x))

y=int(input ("Enter the number:"))
x=y ** 0.5
print('Root of', y, 'is', round(x,2))

for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
      print(i)

for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)

i=0
for i in range(0,20):
    print(i)

words=["hi","there","bro","4115"]
for word in words:
    print(word, "!")

words=["hi","there","bro","4115"]
for x in words:
    print(x, "!")

while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break

    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)

    elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = (num1 - num2)
        print("The answer is " + result)

    break



t='jack is a very ver type van'
for word in t.split():
    if word[0] == 'v':
       print(word)


r= (range(0,50))
for num in r:
    if num%3== 0:
        print(num)


r= 'print every word that has even number of letters'
r=r.split()
for word in r:
    if len(word)%2==0:
        print(word)


for num in range(1,100):
    if num%3==0 and num%5==0:
        print(num,'fizzbuzz')
    elif num%3==0:
        print(num, 'fizz')
    elif num%5==0:
          print(num ,'buzz')


x='print first letter of the words'
for word in x.split():
    print(word[0])

x='print first letter of the words'
y=[word[0] for word in x.split()]
print(y)


def a(name):
    call = 'hello' ' ' +name
    return call
print(a('jack'))

def num(x,y):
    if x%2==0 and y%2==0:
      if x > y:
          return y
      else:
          return x
    else :

         if x>y:
             return x
         else:
             return y


print(num(2,5))


def kuch(text):
  text=text.split()
  first= text[0]
  second=text[1]

  return first[0]==second[0]

print(kuch('hello hey'))

def kuch(text):
  text=text.split()


  return text[0][0]==text[1][0]

print(kuch('hello hey'))


def num(x,y):
    if x==20 or y==20:
        return 'true'
    elif x + y == 20:
        return 'true'
    else:
        return 'false'
print(num(9,11))

def name(text):
    first=text[0]
    inbtwn=text[1:2]
    third=text[2]
    rest=text[2:]
    return first.upper() + inbtwn  + third.upper() + rest
print(name('yadavender'))

def name(text):
    rev=text[::-1]
    return rev
print(name('yadav'))


def y(text):
    result = ''
    for char in text:
        result += char * 3
    return result


print(y('hello'))

---------------------------------------------
# creating class and methods

class Cirle():
    def __init__(self,rad):
        self.rad = rad

    def circum (self):
        return 2 * 3.14 * self.rad

C = Cirle(5)
print(C.circum())

-----------
class Cylinder():

    def __init__(self,rad,hi):
        self.rad = rad
        self.hi = hi

    def volume(self):
        return 3.14 * self.rad**2 * self.hi

Can = Cylinder(2,1)
print(Can.volume())

-------------------------------------------
#bank deposit and withdraw/using class and function
class Account:
    def __init__(self,owner,bal):
        self.owner = owner
        self.bal = bal

    def deposit(self,add):
        self.bal = self.bal + add
        print(add , " is added to bal")
        return self.bal

    def withdraw(self,cut):
        if cut > self.bal:
            print("amount exceeds balance")
        elif cut <= self.bal:
            self.bal = self.bal - cut
            print(cut,"is withrawn from bal")
            return self.bal


acct = Account('ram',100)
print("bal is" , acct.deposit(int(input("Enter amt to add:"))))
print("bal is" , acct.withdraw(int(input("Enter amt to withraw:"))))

--------------------------------------------
#dictionary iteration/iterate .defining class and function
class Fruit():

    def __init__(self):
        pass
    def nutrition(self,name):
        a = {'apple':'100 calories','pear':'200 calories'}
        for keys,values in a.items():
           if name in a.keys():
             print(name,"has",values)
             return



f = Fruit()
print(f.nutrition('apple'))

---------------------------------------------
#open file and write into file

f=open('abc.txt','a')
#print(f.read())
f.seek(2)
f.write('\n')
f.write('i am an albatross \n the quick brown fox jumped')
f.close()
-------------------------------------
#number of character in a text file

def char_count(text,char):
    count = 0
    for x in text:
        if x == char:
            count +=1
    return count

f = open('abc.txt','r')
text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    per = 100 * char_count(text,char)/len(text)

    #print("{0} - {1}%".format(char, round(per, 2)))
    print(char, "-", round(per,2),"%")
-------------------------------------------------
# Inheritance
class SchoolMember():

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('member initiated: {}'.format(self.name))

    def tell (self):
        print('name:{} age: {}'.format(self.name,self.age), end=" ")

class Teacher(SchoolMember):

    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary

    def tell (self):
        SchoolMember.tell(self)
        print('salary: "{}"'.format(self.salary))

class Student(SchoolMember):

    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print('marks:"{}"'.format(self.marks))

t= Teacher('maya',40,30000)
s =Student('ajay',21,85)
print()
members = [t,s]

for x in members:
    x.tell()
------------------------------------------------
#number of upper and lower characters in a string
def character_check(s):
    lower = 0
    upper = 0

    for i in s:
        if i >='A' and i <='Z':
            upper += 1
        elif i >='a' and i <= 'z':
            lower += 1
    print("upper char are",upper)
    print("lower char are ",lower)
y = "HOW you Doing"
print(character_check(y))
---------------------------------------
#stone paper scissors game
#repeat untill valid entry


while True:
    player1 = input('Player 1 turn:')
    player1 = player1.upper()
    player2 = input('Player 2 turn:')
    player2 = player2.upper()
    a = ('ROCK,PAPER,SCISSORS')
    if player1 == player2:
        print('It,s a Tie.')

    elif player1=='ROCK':
        if player2=='PAPER':
            print('player2 wins')
        else:
            print('player1 wins')
        break
    elif player1=='PAPER':
        if player2=='ROCK':
            print('player1 wins')
        else:
            print('player2 wins')
        break
    elif player1=='SCISSORS':
        if player2=='PAPER':
            print('player1 wins')
        else:
            print('player2 wins')
        break
    elif player1 and player2 not in a:

        print('Please enter valid option')

----------------------------------------------------

a = ('india,china,pakistan,laos,cambodia')
a = a.split(',')
while True:

        n = input('enter a index/(exit):')
        if n.upper() == 'EXIT':
            print('exiting...')
            break
        try:
            if int(n) in range(0,len(a)):
                print(a[int(n)])

            elif int(n) not in range(0,len(a)):
                print('Enter a valid entry..')
        except ValueError:

             print('Integer or Exit only')
-------------------------------------------------------------------
#counting number of words characters and lines in files

f = open('newfile.txt','r+')
lines = f.readlines()
l = 0
w = 0
c = 0
for line in lines:
    l +=1
    c = c + len(line)
    words = line.split()
    w = w + len(words)

print('there are {} lines {} words {} characters'.format(l,w,c))


f.close()
-------------------------------------------------------------------
#working with csv files

import csv

with open('Stars.csv', 'r') as file:
    #fieldname = ['name', 'age', 'gender']
    read = csv.DictReader(file)
    for lines in read:
        print(lines['name'])
----------------------------------------------------
#using panda with csv file Dataframe(displaying all the columns)
import csv
import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
df = pd.read_csv('Stars.csv')
# print(df['name'])
# print(df[['name','age']])
# print(df.head(2))
# print(df.iloc[1:4])
for index, row in df.iterrows():
    print(index, row['name'])
---------------------------------------------
#write csv to excel
import csv
import pandas as pd
import numpy as np
import xlwt


df = pd.read_csv('Stars.csv')
print(df)
#sort by name
test = df.sort_values(['name'],ascending=True)
print(test)
# print top 2 lines
print(df.head(2))
#print bottom 2 lines
print(df.tail(2))
#specific search
print(df[df['name']=='yadav'])
#or
print(df[(df['age']>25) & (df['gender']=='male')])

test = df.loc[df['age']>24]
print(test)
#print row from 1 to 4
print(df.iloc[1:4])
writer = pd.ExcelWriter('excel1.xls')
df.to_excel(writer)
writer.save()
---------------------------------
# adding columns using pandas
import csv
import pandas as pd
import numpy as np
import xlwt

df = pd.read_csv('star.csv',delimiter=',')
#df['age_total']= df['age']
# print(df.head(2))
print(df,'\n')
df['total']= df['name'].astype(str) + df['age'].astype(str)
writer = pd.ExcelWriter('star.xls')
df.to_excel(writer)
# df.to_excel(writer,index=False)
writer.save()
print(df)
------------------------------------
#using matplolibf for data plot chart

import csv
import pandas as pd
import numpy as np
import xlwt
from matplotlib import pyplot as plt
x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)
plt.plot(x, y)
plt.title('test plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
print(plt.show())
------------------------------------------------------------
#basic tkinter program
from tkinter import *

root = Tk()
root.title('something stupid')
e = Entry(root)
e.pack()
def bttn():
    mylabel = Label(root, text=e.get())
    mylabel.pack()


my_button = Button(root, text='click me!!!', command=bttn, fg='purple').pack()
root.mainloop()
--------------------------------------------------------------
# simple calculator in tkinter
from tkinter import *


root = Tk()
root.title('Calculator')
e = Entry(root, width= 30, borderwidth= 5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady= 10)
def bttn(number):
   current = e.get()
   e.delete(0,END)
   e.insert(0,str(current)+ str(number))

def bttnclr():
   e.delete(0, END)

def bttnplus():
   first_number= e.get()
   global f_num
   global factor
   factor = 'plus'
   f_num = float(first_number)
   e.delete(0, END)


def bttnmul():
   first_number = e.get()
   global f_num
   global factor
   factor = 'multiply'
   f_num = float(first_number)
   e.delete(0, END)


def bttndivide():
   first_number = e.get()
   global f_num
   global factor
   factor = 'divide'
   f_num = float(first_number)
   e.delete(0, END)

def bttnsubstract():
   first_number = e.get()
   global f_num
   global factor
   factor = 'substract'
   f_num = float(first_number)
   e.delete(0, END)

def bttnequal():
   second_number= e.get()
   e.delete(0, END)
   if factor == 'plus':
      e.insert(0, f_num + float(second_number))
   if factor == 'multiply':
      e.insert(0, f_num * float(second_number))
   if factor == 'divide':
      e.insert(0, f_num / float(second_number))
   if factor == 'substract':
      e.insert(0, f_num - float(second_number))

button1= Button(root, text='1', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(1))
button2= Button(root, text='2', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(2))
button3= Button(root, text='3', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(3))
button4= Button(root, text='4', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(4))
button5= Button(root, text='5', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(5))
button6= Button(root, text='6', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(6))
button7= Button(root, text='7', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(7))
button8= Button(root, text='8', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(8))
button9= Button(root, text='9', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(9))
button0= Button(root, text='0', padx=28, pady=10, borderwidth= 2, command=lambda: bttn(0))
buttonmultiply= Button(root, text='*', padx=28, pady=10, borderwidth= 2, command=bttnmul)
buttondivide= Button(root, text='/', padx=28, pady=10, borderwidth= 2, command=lambda: bttndivide())
buttonsubstract= Button(root, text='-', padx=28, pady=10, borderwidth= 2, command= bttnsubstract)
buttonplus= Button(root, text='+', padx=28, pady=10, borderwidth= 2, command= bttnplus)
buttonequal= Button(root, text='=', padx=28, pady=10, borderwidth= 2, command= bttnequal, bg='green')
buttonclear= Button(root, text='Clear', padx=15, pady=10, borderwidth=2, command= bttnclr, bg='red')

button1.grid(row= 3,column= 0)
button2.grid(row= 3,column= 1)
button3.grid(row= 3,column= 2)

button4.grid(row= 2,column= 0)
button5.grid(row= 2,column= 1)
button6.grid(row= 2,column= 2)

button7.grid(row= 1, column= 0)
button8.grid(row= 1, column= 1)
button9.grid(row= 1, column= 2)

button0.grid(row= 4, column= 0)

buttonplus.grid(row= 4, column=1)
buttonequal.grid(row= 5, column=2)
buttonclear.grid(row= 6, column=0)

buttonmultiply.grid(row=5, column=1)
buttondivide.grid(row=4, column=2)
buttonsubstract.grid(row=5, column=0)

root.mainloop()
----------------------------------------------------
# create random password
import random
import string


def gen_password():
    length = int(input('How strong/long password do you want(3-15):      '))
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;:/!@#$%^&*123456789"
    password = ""
    for i in range(length):
        password += (random.choice(char))

    return password


print(gen_password())
---------------------------------------------------------
# guess the randomly generated number

import random
def guessing_game():
    number = random.randint(0, 101)
    print(number)

    while True:
        guess = int(input('Guess the number:  '))

        if (guess > number):
            print('high')
            if abs(guess - number) < 10:
                print('just right')
        elif (guess < number):
            print('low')
            if abs(guess - number) < 10:
                print('just right')
        elif guess == number:
            print('CORRECT')
            break

print(guessing_game())
-----------------------------------------------------------------------------------------
# ordering in a restaurant from menu
import time
def restaurant():
    total = 0
    your_order = []
    while True:
        menu = {'snacks': 10, 'mainFood': 50, 'drinks': 5, 'sweets': 20}
        for keys, values in menu.items():
            print(keys, values)
        demand = input('\nOrder your food from menu: ')
        if not demand:
            return (f'your total is--{total}')
            break
        if demand not in menu.keys():
            print('Read the menu again Please!!')

        if demand in menu.keys():
            price = menu[demand]
            total += price
            your_order += demand

print(restaurant())
--------------------------------------------------------------------------------------------------------------------------
#



