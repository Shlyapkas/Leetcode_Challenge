def mergeAlternately(word1: str, word2: str) -> str:
    # merged = word1 + word2
    word1 = list(word1)
    word2 = list(word2)
    merged_lst = []


    if len(word1) == len(word2):
        for item in range(0, len(word1)):
            merged_lst.append(word1[item])
            merged_lst.append(word2[item])
    else:
        if len(word1) > len(word2):
            for item in range(0, len(word2)):
                merged_lst.append(word1[item])
                merged_lst.append(word2[item])
            for item in range(len(word2), len(word1)):
                merged_lst.append(word1[item])
        else:
            for item in range(0, len(word1)):
                merged_lst.append(word1[item])
                merged_lst.append(word2[item])
            for item in range(len(word1), len(word2)):
                merged_lst.append(word2[item])

    merged = ""
    for item in merged_lst:
        merged += item
    return merged

print(mergeAlternately("abcd1", "pqr"))

