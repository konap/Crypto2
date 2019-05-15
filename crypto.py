import re
import string
import codecs
from collections import Counter
alphabet = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж':6,
            'з': 7, 'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12,
            'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18
            }


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
    compr = [None] * 19
    for (shift) in range(19):
        counter = 0
        for i in range(len(text) - shift):
            if (text[i] == text[i + shift]):
                print('On shift=', shift, ' ', text[i], text[i + shift])
                counter += 1
                compr[shift] = counter
    compr[0]=0
    print (compr)
    return (compr.index(max(compr)))


if __name__ == '__main__':

        f = codecs.open('text.txt', 'r', 'utf_8_sig')
        words = f.read().lower().replace('[', '').replace(']', '')
        word = re.sub('[qwertyuiopasdfghjklzxcvbnm.,;0123456789_&?/\n"=<>=()!*]', '', words)
        key = 'крипта'
        print('Слово ', word)
        print ('', key)
        print (form_dict())

    # Закодировали буквы в цифры
        key_encoded = encode_val(key)
        value_encoded = encode_val(word)

        print ('Value=', value_encoded)
        print ('Key=', key_encoded)

    # сдвигаем
        shifre = full_encode(value_encoded, key_encoded)
        print   ('Шифр=', ''.join(decode_val(shifre)))
        print  ('Len:', FindLenKey(shifre))
        file = open('Cryptotext.txt', 'w')
        file.write(''.join(decode_val(shifre)))
        file.close()

        decoded = full_decode(shifre, key_encoded)
        print('Key:', key_encoded)
        print ('Decode list=', decoded)
        decode_word_list = decode_val(decoded)
        print ('Word=', ''.join(decode_word_list))
        f.close()