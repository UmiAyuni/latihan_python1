def seqSearch(data, key):
pos = [ ]

for i in range(len(data)):
    if data[i]==key:
        pos.append(i+1)
    if len(pos)>0:
        print('data', key, 'sebanyak', len(pos), 'ditemukan di posisi',pos)
    else:
        print('data tidak ditemukan')

    return pos
data=[10, 4, 9, 1, 15, 7]
seqSearch(data,15)