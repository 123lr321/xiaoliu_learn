class Test001:
    def length_of_last_word(self, s: str) -> int:
        k = len(s)
        while s[-1] == ' ':
            del s[-1]
        for i in range(k - 1, -1, -1):
            if s[i] == ' ':
                return k - i - 1


a = Test001()
print(a.length_of_last_word('qwe we'))
