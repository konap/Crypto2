# -*- coding: utf8 -*-

import re
from collections import Counter

Frequen = {'ъ': 0.00013830785331953106, 'э': 0.0008997139736559186, 'ф': 0.0027782768267330545, 'щ': 0.0030242366689765504,
             'ц': 0.005840298630894838, 'ю': 0.00650474666849176, 'ш': 0.00790065788910847, 'ж': 0.009028508528033719,
             'ч': 0.009090533183903817, 'й': 0.010245475051829798, 'х': 0.01124713759777795,
             'ь': 0.01570150598716161, 'з': 0.016815811011586492, 'б': 0.01707175183293552,
             'ы': 0.019110723278780155, 'я': 0.02011737631428107, 'г': 0.022619037434375062, 'у': 0.02482697259793479,
             'п': 0.02533885424063285, 'к': 0.026031106434309472, 'м': 0.03279464563246613, 'д': 0.0363293380899828,
             'р': 0.040220494086982805, 'л': 0.04666535488084137, 'в': 0.05032908713965101, 'т': 0.052996147342065265,
             'н': 0.05412542383514844, 'с': 0.057152512212440866, 'а': 0.07837777720743612, 'е': 0.08712040197680421,
             'и': 0.09196402855130366, 'о': 0.11031120692851053}

alphabet = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж': 6,
            'з': 7, 'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12,
            'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18,
            'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24,
            'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30,
            'я': 31}

def form_dict():
    d = {0: 'а', 1: 'б', 2: 'в', 3: 'г', 4: 'д', 5: 'е', 6: 'ж', 7: 'з', 8: 'и', 9: 'й',
         10: 'к', 11: 'л', 12: 'м', 13: 'н', 14: 'о', 15: 'п', 16: 'р', 17: 'с',
         18: 'т', 19: 'у', 20: 'ф', 21: 'х', 22: 'ц', 23: 'ч', 24: 'ш', 25: 'щ',
         26: 'ъ', 27: 'ы', 28: 'ь', 29: 'э', 30: 'ю', 31: "я"}
    return d


# кодируем слова в буквы
def encode_val(word):
    list_code = []
    lent = len(word)
    d = {0: 'а', 1:'б',  2: 'в', 3: 'г', 4:'д', 5:'е', 6:'ж', 7:'з', 8:'и', 9:'й',
         10:'к', 11:'л', 12:'м', 13:'н', 14:'о', 15:'п', 16:'р', 17:'с',
         18:'т', 19:'у', 20:'ф', 21:'х', 22:'ц', 23:'ч', 24:'ш', 25:'щ',
         26:'ъ', 27:'ы', 28:'ь', 29:'э', 30:'ю', 31:"я"}

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
                list_code.append(value)
    return list_code


def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0
    for i in value:
        dic[full] = [i, key[iter]]
        full = full + 1
        iter = iter + 1
        if (iter >= len_key):
            iter = 0

    return dic


def full_encode(value, key):
    dic = comparator(value, key)
    print ('Compare full encode', dic)

    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0] + dic[v][1]) % len(d)
        lis.append(go)
    return lis

def full_decode(value, key):
    dic = comparator(value, key)

    print('Deshifre=', dic)
    d = form_dict()  # получаем словарь кода

    lis = []
    for v in dic:
        go = (dic[v][0] - dic[v][1] + len(d)) % len(d)
        lis.append(go)
    return lis


def decode_val(list_in):
    list_code = []
    lent = len(list_in)

    d = form_dict()  # получаем словарь кода

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
                list_code.append(d[value])
    return list_code


def FindLenKey(text):
    compr = [None] * 34
    for (shift) in range(34):
        counter = 0
        for i in range(len(text) - shift):
            if (text[i] == text[i + shift]):
               # print('On shift=', shift, ' ', text[i], text[i + shift])
                counter += 1
                compr[shift] = counter
      #  print('Index:', shift, '=', compr[shift])
    compr[0]=0
    print (compr)
    return (compr.index(max(compr)))


def getNthSubkeysLetters(nth, keyLength, message):
    # Returns every nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

   i = nth - 1
   letters = []
   while i < len(message):
        letters.append(message[i])
        i += keyLength
   return ''.join(letters)

def Frequency (data):
    c = Counter()
    dict = {}
    for x in data:
        c += Counter(x.strip())
        dict[x]=0
    total =  (sum(c.values()))
    for obj in dict:
        dict[obj] = c[obj] / total

    return dict


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def Blocks(text, keylen):
    Blocks = [None]*keylen
    for i in range (keylen):
        Blocks[i] = getNthSubkeysLetters(i+1,keylen,text)
      #  print('Block #', i ,Blocks[i])
    return (Blocks)


def KeyValue (Blocks, keylen):
    KeyValue = [None]*keylen
    for i in range(keylen):
        text = Blocks[i]
        #print ('Current Text:', text)
        letterfrequency = Frequency(text)
        #print(i, '=', alphabet.get(keywithmaxval(letterfrequency)))
        #print("Frequency Letter in text: ",i,  sorted(letterfrequency.items(), key=operator.itemgetter(1)))
        KeyValue[i]=((alphabet.get(keywithmaxval(letterfrequency))-14) % 32)
    return (KeyValue)

def Index(text):
    compr = [None] * 32
    for (shift) in range(32):
        counter = 0
        for i in range(len(text) - shift):
            if (text[i] == text[i + shift]):
                # print('On shift=', shift, ' ', text[i], text[i + shift])
                counter += 1
                compr[shift] = counter / len(text)
    #    print ('Index:', shift, '=', compr[shift])
    print(compr)
    return (compr.index(max(compr)))

def M (text, i):
    sum = 0
    for j in range (len(text)):
       # print (Frequen.get(text[j]),'*', (word.count(text[i+j])))
        sum += Frequen.get(text[j]) * (word.count(text[(i+j)%32]))
       # print  (sum)
    return sum

if __name__ == '__main__':
    f = open('Sifr.txt', 'r')
    words = f.read().lower().replace('[', '').replace(']', '')
    word = re.sub('[qwertyuiopasdfghjklzxcvbnm.,;0123456789_&?/\n"=<>=()!*]', '', words)
    a = FindLenKey(word)
    print ('Len Key', a)
    #b = FindLenKey(word)
    #c = Index2(b)
   # print('Index', textlen)


    print('a = ', word.count('а'))
   # print(alphabet.get(key1))
    Tex = Blocks(word, a)
    for i in range(17):
         print('Stesp #',i, M(Tex[i], i))
    Key = KeyValue(Tex, a)
    print (Key)
    # [2, 5, 13, 5, 22, 8, 0, 13, 17, 10, 8, 9, 10, 19, 6, 28, 22] => [2, 5, 13, 5, 22, 8, 0, 13, 17, 10, 8, 9, 10, 19, 15, 5, 22]
    Key = [2, 5, 13, 5, 22, 8, 0, 13, 17, 10, 8, 9, 10, 19, 15, 5, 22]
    print ('Key', decode_val(Key))

    shifre =  encode_val(word)
    decoded = full_decode(shifre, Key)
    print ('Decode list=', decoded)
    decode_word_list = decode_val(decoded)
    print ('Word=', ''.join(decode_word_list))
    f.close()




