# TASK1

# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]

# num1 = int(input("1-ci eded: "))
# num2 =int(input("2-ci eded: "))
# num3 =int(input("3-cu eded: "))
# num4 =int(input("4-cu eded: "))
# num5=int(input("5-ci eded: "))
# list = [num1, num2, num3, num4, num5]
# print(list)

# list.sort()
# print(list)


# TASK2
# Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 



# sentence = str(input(" cumleni daxil edin: "))
# result = "".join((sorted(sentence)))
# print(result)


# TASK3
# Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13

# tebrikler . 4 cehdde 13 reqemeni tapdiz


# n = 13
# count = 0
# while True :
#     number = int(input("ededi tap: "))
#     count+=1
#     if number == n:
#         print(f"Doğrudur. {count} addimda tapdiniz")
#         break
        

# TASK4


# 1 ile 100 arasinda sade ededleri print edin. (for loops)
# for i in range(2,100):
#             x = False
#             for j in range(2,i):
#                 if i % j == 0:
#                     x = True
#                     break
#             if x == False:
#                 print (i)