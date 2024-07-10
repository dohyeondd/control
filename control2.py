#1. 사용자로부터 문자 메세지 입력받기
data = input("문자메세지를 입력하세요.")
#2. 입력받은 문자메세지 길이
len_data = len(data)
#3. 20글자 초과 시 100원 출력
if len_data>20 :
        print("요금은 100원 입니다.")
#4. 20글자 이하 시50원
if len_data<=50 :
        print("요금은 50원 입니다.")



num = int(input("점수를 입력하세요."))
print("데이터 타입 변환 전:", num, type(num))
num = int(num)
if 81 <= num <= 100 :
        print("A")
elif 61 <= num <= 80 :
        print("B")

print(10%2)

data = input("숫자를 입력하세요.")

if data %2 ==0 :
    print("2로 나누었을 때 나머지가 0이므로, 짝수입니다.")
else :
    print("나머지가 존재하므로, 홀수입니다.")
