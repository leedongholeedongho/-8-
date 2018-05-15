num = int(input("점수:"))

if(num<=100 and num>=90):
    print(num, ":", "A")

elif(num<=89 and num>=80):
    print(num, ":", "B")

elif(num<=79 and num>=70):
    print(num, ":", "C")

elif(num<=69 and num>=60):
    print(num, ":", "D")

elif(num<=59 and num>=0):
    print(num, ":", "F")

else:
    print("입력 가능한 점수 범위는 0~100 입니다")
    
     
