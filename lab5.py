import random

a = [round(random.uniform(1, 20), 2) for _ in range(10)]
print("Массив a:", a)


avg = sum(a) / len(a)
print("орташа арифметическое:", avg)

if avg in a:
    print(":", avg)
else:
    print("нет.")

A = [[random.randint(1, 50) for _ in range(4)] for _ in range(4)]
print("\nМатрица A:")
for row in A:
    print(row)

diagonal = [A[i][i] for i in range(4)]
print("бас:", diagonal)


max_diag = max(diagonal)
print("улкен диагонал:", max_diag)
