n, n_t, k, k_t = 0, 0, 0, -1
array = []

with open("C:/python/laba_2/in.txt", "r") as f:
    array = f.read().split()

for i in range(0, len(array)):
    if int(array[i]) % 2 == 0:
        n_t += 1
        if k_t == -1:
            k_t = i
    else:
        n_t = 0
        k_t = -1
    if n_t > n:
        n = n_t
        k = k_t


if n != 0:
    del array[k+n:]
    del array[0:k]

    print ("Последовательность четных чисел: ", array)
    print ("Длинна: ", n)
    print ("Позиция: ", k)
else:
    print ("В данном файле четных последовательностей нет")
