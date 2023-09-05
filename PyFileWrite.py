# Modes
# w = write Mode
# r = Read Mode
# a = Append Mode

fh = open("FileExample.txt", "w")

fh.write("Welcome To FIle Handling In Python.\n")
fh.write("This is second line.\n")
fh.write("Always close the file once the job is done")

fh.close()