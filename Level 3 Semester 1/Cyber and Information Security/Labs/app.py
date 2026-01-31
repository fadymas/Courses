def reverse(word:str):
    return word[::-1]

#cyzer
def shift(key: int,plain_text:str):
    cypher_text=""
    for i in plain_text:
        if(i.isupper()):
            C = (ord(i)+key-65) % 26 + 65
        else:
            C = (ord(i)+key-97) % 26 + 97
        c = chr(C)
        cypher_text+= c
    print(cypher_text)
shift(4,"abcd")

# monoalphabetic
def mono(plain_text):
    dic = {"a":"c","b":"x","c":"a"}
    cypher_text=""
    for i in plain_text:
        cypher_text+=dic.get(i)
    return cypher_text

