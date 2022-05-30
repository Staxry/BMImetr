import requests
from pyfiglet import Figlet

preview_text = Figlet(font='epic')
print(preview_text.renderText('Jirometr'))

name  = str(input('Ведите ваше имя: '))

height =  float(input('Введите ваш рост в сантиметрах(Пример:1.50): '))

weight = int(input('Введите ваш весь в КГ: '))

bmi = weight / (height ** 2) #bmi-индекс массы тела.


print(name, 'Индекс массы вашего тела равен: ' + str(bmi))

if bmi < 18.5:
    print(name, 'У тебя Анарексия,иди ешь!!!')
elif bmi <25:
    print(name, 'Поздравляю, у тебя нет лишнего веса!!!=)')
else:
    print(name, 'Ты жирный иди срочно в качалку!!!')










