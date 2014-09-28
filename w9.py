# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number 
# of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person 
# who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count 
# of the number of times they appear in the file. After the dictionary is produced, the program reads through 
# the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

text = handle.read()
lines=text.split("\n");

tmpStr = "From "
space = " "
tmp = ""
mail = dict();

for string in lines:
	if string.startswith(tmpStr):
		adr = string[5:]
		x = adr.find(space)
		tmp = adr[:x]
		if tmp in mail:
			mail[tmp]=mail[tmp]+1
		else:
			mail[tmp]=1            

#print mail
email = ""
count = 0
for key in mail.keys():
	if mail[key]> count:
		count = mail[key]
		email = key

print email, count