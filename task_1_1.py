# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
#https://drive.google.com/open?id=1q-mWRzF8zqPoq5o1FmqUIeqdl7rG3LUF
a=int(input('Введите трехзначное число:'))
a1=a//100
a2=(a-a1*100)//10
a3=a-(a1*100+a2*10)
s=a1+a2+a3
print('сумма цифр s=' + str(s))
