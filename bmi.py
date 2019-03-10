weight = input('Enter your weight(kg): ')
height = input('Enter your height(cm): ')
weight = float(weight)
height = float(height)
bmi = weight/((height/100)**2)
print('your bmi is: ', bmi)

if bmi < 18.5:
    print('you are too thin')
elif bmi >=18.5 and bmi <24:
    print('you have an normal style')
elif bmi >=24 and bmi < 27:
    print('you are heavy')
elif bmi >=27 and bmi < 30:
    print('you are a little fat')
elif bmi >=30 and bmi < 35:
    print('you are fat')
else:
    print('you are very fat')