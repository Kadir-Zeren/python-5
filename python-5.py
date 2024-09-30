text = 'Clarusway'

text[0]

text[:5] + 'k' + text [-3:]

yeni_string = text[:5] + 'k' + text[-3:]

cumle = 'In God We Trust'

cumle.lower()
print(cumle)
yeni_cumle = cumle.lower()

't' in cumle
'R' in cumle
'trust' in cumle
'R' not in cumle

var_string = 'ClarusWay'
print(var_string. lower())
print(var_string)
var_string = 'Clarusway'.lower()
print(var_string)

text = 'AaBbCc'
print (text.lower())
text.startswith('a')
text.startswith('aa')
text.startswith('b', 2)

text = text.lower()

var_str = 'In God we Trust'
var_str.lower ( )
print(var_str)

cumle = 'In God We Trust'
print (cumle)
yeni_cumle = cumle.lower()

text = 'www.clarusway.com'
print(text.endswith('.com'))
print(text.startswith('http:'))

text = 'www.clarusway.com'
print(text.endswith('om'))
print(text.startswith('w'))

'abcdeabcde'.startswith('c', 2,8)

email = "clarusway@clarusway.com is my e-mail address"
print(email.startswith("@", 9))
print(email.endswith("-", 10, 32))

text = 'a b c d'
len (text)

text=  'www.clarusway.com'
print (text.endswith('.co'))
print (text.startswith('w.'))

text = """
Data preprocessing is an important task in text classification.
This program counts words in a sentence. It starts with space separated words."""
print("To count words in a sentence : ", text.count(" ") + 1)

text = 'abcdef'
text.startswith('b',-5)

text = 'abcabcabc'
text.find('ca')
text.find('klm')
text.rfind('a')
text.index('ca')

text = 'www.clarusway.com'
print(text.index('com'))
print(text.find('com'))

sentence = "I live and work in Virginia"
print(sentence.upper())
print(sentence.lower())
print(sentence.swapcase())
print(sentence) # note that, source text is unchanged

text = 'ClaRusWay'
text.upper()
text.lower()
text.swapcase()

text.replace('W', '***')
text.replace('W', '***' ).lower()
text.replace('W', '***').lower().upper ()

sentence = "I live and work in Virginia"
title_sentence = sentence.title()
print(title_sentence)
changed_sentence = sentence.replace("i", "+")
print(changed_sentence)
print(sentence) # note that, again source text is unchanged

text = 'the better the family, the better the society'

text = text.title()
print(text)

sentence = "I live and work in Virginia"
swap_case = sentence.swapcase()
print(swap_case)
print(swap_case.capitalize()) # changes 'i' to uppercase and
# the rest to lowercase

text = 'Sodome and Gomore'
text.replace('0', '0')

text = 'Sodome and Gomore'
text = text.replace('0', '0')
print(text)

isim = '    Ali    '
isim.strip()

meslek ='  \n codder \t  '
meslek.strip()
meslek.rstrip()

space_string = "listen first"
print(space_string.strip()) # removes all spaces from both sides

source_string = "interoperability"
print(source_string.strip("yi"))
# removes trailing "y" or "i" or "yi" or "iy" from both sides

text = 'abcdabcd'
text.strip('a')
text.strip('ab')
text.strip('ba')
text.strip('bad')
text.strip('badc')
text.strip('c')

print(None or 1)

a = " "
b = "False"
c = True
d = ""
print(a or b or c and not d)

bool('')
bool(' ')

print("None or True and 1")

A = True
B = False
logic = (A or B) and (not A)
print(logic)

{} or () or "" or 35 or False

source_string = "interoperability"
print(source_string.lstrip("in"))
# removes "i" or "n" or "in" or "ni" from the left side

space_string = "listen first"
print(space_string.rstrip()) # removes spaces from the right side

source_string = "interoperability"
print(source_string.rstrip("yt"))
# removes "y" or "t" or "yt" or "ty" from the right side

source_string = "interoperability"
print(source_string.rstrip("ty"))

text = 'tyou can learn almost everything in pre-classz'
text.strip('tz')
text.strip('tz').upper()
text.rstrip('z')
text.rstrip('z').lstrip('t')
text.rstrip('z').lstrip('t').upper ()
print(text.rstrip('z').lstrip('t'). upper())

text = text.rstrip('z').lstrip('t'). upper()
print(text)

text = 'In God wee Trust'
text.replace('wee', 'we')

text = 'In God wee Trust'
print(text.replace("ee", "e"))
text1 = text[:9]
text2 = text[10:]
print (text1 + text2)