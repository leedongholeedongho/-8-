engkor_dict = {}

eng = input("영어 단어:")

kor = input("한글 단어:")

while(eng !='' and kor !=''):
    engkor_dict[eng] = kor
    eng = input("영어 단어:")
    kor = input("한글 단어:")

print(engkor_dict)
