from pprint import pprint


class LongestKeyDict(dict):
    def longest_key(self):
        # zwracac najdłuzszy klucz w słowniku
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


# print(len(None))  # TypeError: object of type 'NoneType' has no len()

art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 7
art['siedem'] = 9
art['zen'] = 1
print(art.longest_key())  # abraham
pprint(art)
pprint(art.longest_key())
# {'abraham': 7, 'siedem': 9, 'tomasz': 12, 'zen': 1}
# 'abraham'
