
def encode(source):
    ascii_values = [ord(character) for character in source]
    ##print(ascii_values)
    a = 3
    chr_code = ""
    for i in ascii_values:
        a += 1
        # #print(a)
        chr_code = chr_code+chr(int(i-7-a))
        # #print(chr_code)
    return chr_code
# source = "emily"
# en_code=encode(source)

def decode(en_code):
    ascii_values = [ord(character) for character in en_code]
    ##print(ascii_values)
    a = 3
    ##print(a)
    ori_code = ""
    for i in ascii_values:
        a += 1
        ori_code = ori_code + chr(int(i+7+a))
        #print(ori_code)
    return ori_code
# print(en_code)
# print(decode(en_code))

