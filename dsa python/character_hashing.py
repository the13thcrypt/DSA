'''
ascii code for small characters is 97 to 122
ascii code for capital characters is 65 to 90'''
S="azyaysydayysyadyaaaa"
q=["a","y","s","d"]
hash_list=[0]*26
for char in S:
    ascii_value=ord(char)
    index=ascii_value-97
    hash_list[index]+=1
for char in q:
    ascii_value=ord(char)
    index=ascii_value-97
    print(hash_list[index])