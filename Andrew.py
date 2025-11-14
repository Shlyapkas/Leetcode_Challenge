class Task1071:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        common = set()
        str1l = list(str1)
        str2l = list(str2)

        for el1 in str1l:
            if el1 in str2l:
                common.add(el1)
        a = "".join(sorted(common))

        lst = list(str1.partition(a))
        lst1 = list(str2.partition(a))

        for el in lst:
            if el == "":
                lst.remove(el)

        for el in lst1:
            if el == "":
                lst1.remove(el)

        if lst[0] == lst1[0]:
            return "".join(sorted(common))
        else:
            return ""

print(Task1071.gcdOfStrings(123, "LEET", "CODE"))
