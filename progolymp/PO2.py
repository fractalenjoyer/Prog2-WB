import re
input("Antal ord ? ")
print(re.sub(r"[aeiouy]([^aeiouy\s]{2})", r"\1", input("Mening ? "))[::-1])