from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())

#Commands to memorize:
#close=closes the file
#read=reads file
#readline=reads just one line of a text file
#truncate=empties the file
#write(stuff)=writes stuff to a file
