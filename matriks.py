matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])

for i in range(4):
        for j in range(4):
            if i==j:
                matriks[i][j]=j
            if i<j:
                matriks[i][j]=j+2
            if i>j:
                matriks[i][j]=j-1

for i in range(4):
        print(matriks[i])