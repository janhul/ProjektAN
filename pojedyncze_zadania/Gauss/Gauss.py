import numpy as np

n = 5

A = np.loadtxt('macierz.txt')
B = np.loadtxt('macierzPrawejStrony.txt')
C = np.zeros((n,n+1))
C[:, :n] = A
C[:, n] = B


def metoda_eliminacji_gaussa():
    n=5
    X = np.zeros(n)

    for s in range(0, n-1):
        for i in range(s+1, n):
            for j in range(s+1, n+1):
                C[i][j] = C[i][j] - C[i][s]/C[s][s]*C[s][j]

    X[n-1] = C[n-1][n]/C[n-1][n-1]

    for i in range(n-1, -1, -1):
        suma = 0
        for s in range(i+1, n):
            suma = suma + C[i][s]*X[s]
        X[i] = (C[i][n] - suma)/C[i][i]

    for i in range(0, n):
        print(X[i])



metoda_eliminacji_gaussa()
