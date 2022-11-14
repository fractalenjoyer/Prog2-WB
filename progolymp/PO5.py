import re
word = "ppotatiss"

def test(x: str) -> bool:
    return not re.search(r"[aeiouy][^aeiouy\s]{2}", x)

def mask(char, mask):
    return char if mask == "1" else ""

mutations = 0

for i in range(1, 2**len(word)):  
    tmp = "".join(map(mask, word, format(i, f"0{len(word)}b")))
    if test(tmp):
        mutations += 1

print(mutations)