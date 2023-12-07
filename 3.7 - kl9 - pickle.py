import pickle

# biblioteka do łatwiejszego zapisywania obiektów do pliku

lista = [1, 2, 3, 4, 5]
print(type(lista))  # <class 'list'>

# context managera
# usprawnia dziłąnie np z plikami, dba o obsługe błedów
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('lista.txt', "w") as fh:  # filehandler zapisujemy w fh
    fh.write(str(lista))

with open('lista.txt', "r") as file:
    data = file.read()

print(data)
print(type(data))  # <class 'str'>
print(data[0])  # [

with open('lista.pickle', "wb") as f:
    pickle.dump(lista, f)

with open("lista.pickle", "rb") as fh:
    p = pickle.load(fh)

print(p)
print(type(p))  # <class 'list'>
print(p[0])  # 1

lista_ser = pickle.dumps(lista)
print(lista_ser)  # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
print(pickle.loads(lista_ser))  # [1, 2, 3, 4, 5]
# 13:25
