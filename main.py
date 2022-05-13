"""Вариант 27. Написать программу, которая читая последовательность чисел из файла, выводит на экран самую длинную последовательность четных чисел, ее длину и позицию с которой она началась.
Чтение посимвольно. Максимальный размер рабочего буфера для обработки - 100 символов (максимальная длина числа). Вывод результата работы программы осуществляется на экран.
"""
import os

more_max_buffer_len = False    # максимальный размер рабочего буфера
max_buffer_len = 100    # максимальный размер рабочего буфера
buffer_len = 1          # размер буфера чтения

work_buffer = ""                # рабочий буфер
number_flag = False             # флаг для проверки наличия цифер
even_number = False             # флаг для проверки четности числа
number = ""
array = []
position = 0                    # позиция
temp_position = 0               # временная позиция
lenght = 0                      # длина
temp_lenght = 0                 # временная длина

try:   
    with open("text.txt", "r") as file:         # открываем файл
        buffer = file.read(buffer_len)          # читаем первый блок
        if not buffer:                          # если файл пустой
            print ("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
            
        while buffer:                               # пока файл не пустой
            while (buffer<'0' or buffer>'9') and buffer:         # ищем цифры
                if(number != ""):           # проверка на наличие цифры
                    array.append(number)
                number = ""
                buffer = file.read(buffer_len)      # читаем очередной блок
                
            while (buffer >= '0' and buffer <= '9') and buffer:  #обрабатываем цифры
                number_flag = True
                number += str(buffer)           # складывание цифер в число
 
                work_buffer += buffer    
                if len(work_buffer) >= max_buffer_len :    # Если буфер переполнен и в нем нет цифр
                    print ("\nФайл text.txt содержит блок цифр, превышающий максимальный размер буфера = "+str(max_buffer_len)+ " символов.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
                    more_max_buffer_len = True
                buffer = file.read(buffer_len)  # читаем очередной блок
                
            if not buffer and len(work_buffer) >0 and not number_flag:       
                print ("\nхвост файла text.txt не содержит ни одной цифры.")
                break
                
            if more_max_buffer_len:
                break
         
            work_buffer = ""                                    # готовим новый цикл ввода
            number_flag = False

        if(number != ""):           # проверка на наличие цифры
            array.append(number)
            
        for i in range(0, len(array)):
            if int(array[i]) % 2 == 0:      # проверка на четность
                if not even_number:
                    temp_position = i+1
                even_number = True
                temp_lenght += 1 
            else:
                even_number = False
                temp_position = 0
                temp_lenght = 0
            if temp_lenght > lenght:            
                lenght = temp_lenght
                position = temp_position
                
        
        if lenght!= 0:
            del array[position+lenght-1:]      # удаление чисел после четной последовательности 
            del array[0:position-1]            # удаление чисел до четной последовательности
            print ("Последовательность четных чисел: ", array)
            print ("Длинна: ", lenght)
            print ("Позиция: ", position)
        else:
            print ("В данном файле четных последовательностей нет") 
                
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.") 
