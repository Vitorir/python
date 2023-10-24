seq1 = [1, 2, 3]
seq1.append([4, 5, 6])
print(seq1)

seq2 = seq1.copy()
seq2.append(['a', 'b', 'c'])
print(seq2)

seq1.insert(0, 'w')
print(seq1)

seq1.pop()