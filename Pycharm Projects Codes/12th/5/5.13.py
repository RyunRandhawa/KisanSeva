import pickle
string="This is my first line. This is second line."
with open("myfile.info","wb") as fh:
    pickle.dump(string, fh)