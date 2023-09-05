import pickle

fh = open("vdstates", "rb")
contents = pickle.load(fh)
fh.close()

print("File COntent: ", contents)
print("File Type: ", type(contents))