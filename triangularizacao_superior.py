def copia(A, b):
  n = len(A)
  U = []
  for i in range(0, n):
    linha = []
    linha.copy
    for j in range(0, n):
      linha.append(A[i][j])
    B.append(linha)

  return B

def pivoteamento(A, b, k):
  maiorElem = A[k][k]
  maiorIndc = k
  for i in range(0, len(A)):
    if (A[i][k] > maiorElem):
      maiorIndc = i

  tempA = A[k]
  A[k] = A[maiorIndc]
  A[maiorIndc] = tempA

  tempB = b[k]
  b[k] = b[maiorIndc]
  b[maiorIndc] = tempB

  return A, b

def triangularizacao_superior(A, b):
  n = len(b)

  U = A
  c = b.copy

  for k in range(0, n):
    
    for i in range(k+1, n):
      U, c = pivoteamento(U, c, k)
      s = U[i][k] / U[k][k]
      
      for j in range(k, n):
        U[i][j] = U[i][j] - s * U[k][j]

      c[i] = c[i] - s * c[k]

  return U, c

U, c = triangularizacao_superior([[0, 2, 5], [2, 1, 1], [3, 1, 0]], [1, 1, 2])
print(U)
print(c)
