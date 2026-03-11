import datetime
now=datetime.datetime.now()

if 3<= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

if 6<= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9<= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

if 12<= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

######

number=input("정수 입력> ")
number=int(number)

number=str(number)
last_character=number[-1]
last_number=int(last_character)

if last_number==0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")
    
if last_number==1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다")