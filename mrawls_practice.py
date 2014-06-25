# Simple program to practice python things
# by Meredith Rawls
#
# OVERVIEW
# Read in a data table so it is a Python dictionary of lists.
# Read in Gettysburg address, count lines, words, and vowels.

from __future__ import print_function
import numpy as np

# Read in the file table.txt
# It is three comma-separated columns: RA, Dec, and Name
filename = '../SciCoder2014/Data/table.txt'
datatable = open(filename)
# assign the first line of the file to be the key names for a dictionary
# for funsies, ignore any rows commented out with '#'
line = datatable.readline()
while line[0] == '#':
	line = datatable.readline()
keylist = line.rstrip('\n').split(',') 
# define a dictionary with empty lists as values for now
#datadict = {keylist[0]:[], keylist[1]:[], keylist[2]:[]} # less generalized version
datadict = {key:[] for key in keylist} # MAGIC
# keeps reading file after the first line and saves the data as lists
# keep ignoring any rows commented out with '#'
for line in datatable:
	if line[0] == '#':
		continue
	line = line.rstrip('\n')
	values = line.split(',')
	for i in range(0,len(keylist)):
		datadict[keylist[i]].append(values[i])
datatable.close()
print('You read in a data file called {0}'.format(filename))
print('It is a dictionary of lists, which is rather silly.')
#print(datadict)
print('Here is the {0} column:'.format(keylist[0]))
print(datadict[keylist[0]])

# Read in the Gettysburg address file
# Count how many lines, words, and vowels there are
# Sort the words alphabetically and remove duplicates (yeah I didn't get to this part)
filename = '../SciCoder2014/Data/gettysburg_address.txt'
text = open(filename)
linecount = 0
wordcount = 0
charcount = 0
acount = 0; ecount = 0; icount = 0; ocount = 0; ucount = 0
for line in text:
	line = line.rstrip(' \n')
	words = line.split(' ')
	linecount = linecount + 1
	for word in words:
		wordcount = wordcount + 1
		for char in word:
			charcount = charcount + 1
			if char == 'a' or char == 'A': acount = acount + 1
			if char == 'e' or char == 'E': ecount = ecount + 1
			if char == 'i' or char == 'I': icount = icount + 1
			if char == 'o' or char == 'O': ocount = ocount + 1
			if char == 'u' or char == 'U': ucount = ucount + 1
print('In the Gettysburg address:')
print('There are {0} lines'.format(linecount))
print('There are {0} words'.format(wordcount))
#print('There are {0} letters'.format(charcount))
print('There are {0} a\'s, {1} e\'s, {2} i\'s, {3} o\'s, and {4} u\'s'
	.format(acount,ecount,icount,ocount,ucount))
print(' ')

# EXERCISE FROM TUESDAY
class VendingMachine(object):
    # At the moment, our VendingMachine can only have three things: water, iced tea, and soda. Sorry.
    def __init__(self):
        self.item = ['water', 'iced tea', 'soda']
        self.quantity = [0, 0, 0]
        self.price = [1.00, 1.00, 1.00]
    # Report how much of any item is in stock
    def stock(self, item='water'):
        if item == 'water':
                return self.quantity[0]
        if item == 'iced tea':
                return self.quantity[1]
        if item == 'soda':
                return self.quantity[2]
        else:
            print('Sorry, this vending machine doesn\'t have any {0}.'.format(item))
    # Add some number of one item to the machine, and reset the price.
    def restock(self, item='water', quantity=1, price=1.00):
        index = int(self.item.index(item))
        already_stocked = self.quantity[index]
        new_additions = quantity
        self.quantity[index] = already_stocked + new_additions
        self.price[index] = price
        print('There are now {0} {1}s priced at ${2} each.'.format(self.quantity[index], self.item[index], self.price[index]))
    # Dispense some quantity of items from the machine
    def vend(self, item='water', price_paid=1.00):
        index = int(self.item.index(item))
        already_stocked = self.quantity[index]
        price_cost = self.price[index] # THIS LINE BREAKS THINGS
        if already_stocked == 0:
            print('Sorry, there are no {0}s in stock.'.format(self.item[index]))
        elif price_paid < price_cost:
            print('Sorry, you paid ${0}, and a(n) {1} costs ${2}.'.format(price_paid, self.item[index], price_cost))
        else:
            self.quantity[index] = already_stocked - 1
            change = price_paid - price_cost
            print('Thanks for your purchase! Your change is ${0}.'.format(change))

# API provided by Demitri
print('Now it\'s Vending Machine time!')
vm = VendingMachine()
vm.restock("water", quantity=5, price=1.50)
vm.restock("iced tea", quantity=10, price=2.50)
vm.restock("soda", quantity=12, price=2.00)    
vm.vend("water", 1.50)
print(vm.stock("water")) # how many waters are left    
vm.vend("water", 1.25) # should fail, and return the money to the user
vm.vend("water", 1.75) # should work, and return 0.25 to the user