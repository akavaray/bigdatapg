input_a=float(input("첫번쨰 숫자> "))
input_b=float(input("두번째 숫자> "))

print("덧셈 결과:", input_a+input_b)
print("뺄셈 결과:",input_a-input_b)
print("곱셈 결과:",input_a*input_b)
print("나눗셈 결과:",input_a/input_b)

output_a=str(52)
output_b=str(52.273)

print(type(output_a),output_a)
print(type(output_b),output_b)

#연습문제
#\n
#12

inch=int(input("인치입력>"))
centimeter=inch*2.54
print(inch,"인치는",centimeter,"cm")

#####

kg=int(input("킬로그램입력>"))
pound=kg*2.20462262
print(kg,"kg은",pound,"파운드")

#####

half=int(input("반지름입력>"))
leng=half*4*3.14
width=half**2*3.14
print(half,"반지름인 원의 둘레는",leng,"넓이는",width)