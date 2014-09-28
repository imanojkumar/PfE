# Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the lines and compute the average 
# of those values and produce an output as shown below.
# When you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0;
s = 0;
k = len("X-DSPAM-Confidence: ")
    
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1;
        nline = float(line[k:])
        s = s + nline
 
print "Average spam confidence: " + str(s/count)