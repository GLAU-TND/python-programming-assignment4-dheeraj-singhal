lst = eval(input())
k = int(input())
my_dict = {}

for i, j in lst:
    if i in my_dict:
        my_dict[i].add(j)
    else:
        my_dict[i] = {j}
similar_pairs = {}
websites = list(my_dict.keys())

for i in range(len(websites) - 1):
    for j in range(i+1, len(websites)):
        similar_pairs[(websites[i], websites[j])] = len(my_dict[websites[i]] & my_dict[websites[j]]) / len(my_dict[websites[i]] | my_dict[websites[j]])

for i in sorted(similar_pairs, key=similar_pairs.get, reverse=True)[:k]:
    print(i)
