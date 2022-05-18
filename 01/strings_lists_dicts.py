string = 'one two three'
print (string)

string2 = 'two'
list_of_word = string.split(" ")

print(type(list_of_word))
print(list_of_word)

for i in list_of_word:
    if i == string2:
        print (f'Нашли {string2}!')
        break

string3 = "123,123.45"
int_14  = 15
edited_string3 = string3.replace (",", "")
summa = float (edited_string3) + float (int_14)
print (summa)


#https://api.coindesk.com/v1/bpi/currentprice.json