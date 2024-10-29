#WAP to fill letter in templete given below
# letter = '''
# Dear <|Name|>,
# Your are selected!
# <|Date|>
# '''

letter = '''
Dear <|Name|>,
Your are selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Kaushal").replace("<|Date|>","2050"))