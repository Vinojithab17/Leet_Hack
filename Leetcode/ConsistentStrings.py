
def countConsistentStrings(allowed: str, words: list[str]) -> int:
    dic = {}
    count = 0
    for i in allowed:
        dic[i] = i
    print(dic)
    for i in words:
        print(i)
        for j in range(len(i)):
            print(j)
            if i[j] not in dic:
                break
            elif (j == len(i)-1):
                count += 1
            else: continue
    return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

print(countConsistentStrings(allowed,words))
