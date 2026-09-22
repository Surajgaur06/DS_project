def jaccard_index(str1, str2):
    set1, set2 = set(str1.lower().split()), set(str2.lower().split())

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    return len(intersection) / len(union)


s1 = "data science is fun"
s2 = "Science makes data useful"

print("Jaccard Index:", jaccard_index(s1, s2))