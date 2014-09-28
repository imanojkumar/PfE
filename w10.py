# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
# for each of the messages. You can pull the hour out from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
# Note that the autograder does not have support for the sorted() function.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read();
lines=text.split("\n");

tmpStr = "From "
space = " "
tmp = ""
hour = []
h = {}
listTime = []

for string in lines:
	if string.startswith(tmpStr):
		adr = string[5:]
		x = adr.find(space)
		tmp = adr
		listAttr = tmp.split();
		listTime.append(listAttr[4])
for x in listTime:
	y = x[0:2]
	hour.append(y)

for l_key in hour:
	if l_key in h.keys():
		h[l_key]=h[l_key]+1
	else: 
		h[l_key]=1

for k, v in sorted(h.items()):
	print k,v