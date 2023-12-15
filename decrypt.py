def decrypt(s1, s2):
    return ''.join([char1 + char2 for char1, char2 in zip(s1, s2)])

s1="NWO"
s2="ETN"

print(decrypt(s1,s2))