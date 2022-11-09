from random import randint

goal = randint(0, 100)
print(goal)
flag = False
n = 1
attempt = []
while True:
    attempt.append(input("Введите число от 0 до 100:\n"))
    try:
        attempt[0] = int(attempt[0])
    except:
        print("Введите число!!!")
        del attempt[0]
        continue
    if attempt[0] > 100 or attempt[0] < 0:
        print("Вне диапазона!")
        del attempt[0]
        continue
    break
if attempt[0] == goal:
    print("Вы победили! Вау! С первой попытки!\n")
else:
    if abs(attempt[0] - goal) > 10:
        print("Холодно!")
    else:
        print("Тепло!\n")
    while flag == False:
        attempt.append(input(f"У вас {n+1} попытка. Ввод:\n"))
        try:
            attempt[n] = int(attempt[n])
        except:
            print("Введите число!!!")
            del attempt[n]
            continue
        if attempt[n] > 100 or attempt[n] < 0:
            print("Вне диапазона!")
            del attempt[n]
            continue
        if attempt[n] == goal:
            print(f"Вы угадали с {n+1} попытки! Поздравляем!\n")
            break
        if abs(attempt[n]-goal) < abs(attempt[n-1]-goal):
            print("Теплее!")
        elif abs(attempt[n]-goal) > abs(attempt[n-1]-goal):
            print("Холоднее!")
        else:
            print("Вы ввели то же число!")
        n+=1
input()