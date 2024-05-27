def triangularizacao_superior(A, b):
  n =

Entrada: A, b
Sa ́ıda: U, c
1: n ← tamanho(b) ▷ n poderia ser parˆametro de entrada
2: U ← A ▷ Copia (A, b) para (U, c)
3: c ← b
4: para k ∈ {1, 2, . . . , n 9 1} fa ̧ca
5: para i ∈ {k + 1, k + 2, . . . , n} fa ̧ca
6: sik ← uik/ukk ▷ uij s ̃ao os coeficientes de U
7: ci ← ci 9 sikck ▷ ci s ̃ao os coeficientes de c
8: para j ∈ {k, k + 1, . . . , n} fa ̧ca
9: uij ← uij 9 sikukj ▷ Os termos a
⋆
ij s ̃ao sobrescritos em U

10: fim para ▷ assim como b
⋆
i
s ̃ao sobrescritos em c (linha 7)

11: fim para
12: fim para
13: retorne U, c
