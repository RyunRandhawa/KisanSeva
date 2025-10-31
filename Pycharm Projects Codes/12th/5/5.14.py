import pickle
st=""
with open("myfile.info", "rb") as fh:
    st=pickle.load(fh)
    lst=st.split('o')
    print(lst[0])