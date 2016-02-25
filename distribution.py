"""
distribution.py
Author: Payton
Credit: Avery, Daniel, Mr. Dennison

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
def compare(a, b):
    return b > a

o = str(input("Please enter a string of text (the bigger the better): "))
print('The distribution of character in "' + o + '" is: ')

orig = o.lower()
alph = "abcdefghijklmnopqrstuvwxyz"
results = []
listnum = []

for c in alph:
    r = orig.count(c)
    if not r == 0:
        t = (r*c)
        results.append(t)
        listnum.append(r)

lists=zip(listnum,results)
print(list(lists))

sorted(results, key=lambda listnum: listnum[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

def bsort(seq, cmp):
    sorted = False  
    while not sorted:
        sorted = True   
        for index, value in enumerate(seq): 
            if index > 0:                  
                if not cmp(seq[index-1], value):  
                    sorted = False         
                    seq[index-1], seq[index] = seq[index], seq[index-1] 
                    
bsort(results, compare)
print(results)
