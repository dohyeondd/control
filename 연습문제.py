# num = int(input("임의의 숫자를 입력하세요"))
#
# print(num, type(num),)

#1. 사용자로부터 값을 입력받아.
data = input("값을 입력하세요 :")
#2. 입력받은값에 100을 더함
#2-1, 입력받은 값에 100을 더할 때, 데이터 타입을 변환(문자열 - >숫자형)
data_2 = int(data) +100
#3. 더한 값이 150초과인 경우, 사용자 입력 값을 출력
if data_2 > 150:
        print(data)
#4. 더한 값이 150이하인 경우, 값이 모자랍니다를 출력
elif data_2<= 150 :
    print("값이 모자랍니다")

x = 4
if 5 < x < 10 :
    print(x)
else:
      print("no")

#and, or, 연산자
apple = '사과'
banana ='감자'
if apple =='사과' or banana =='바나나':
     print("문자열이 모두 정확합니다.")

var = [1,2,3]
if 3 in var :
    print("숫자 3이 var 변수에 있습니다.")



# 1. 사용자로 부터 입력받아
text = input("조회할 요소를 입력하세요 : ")
# 2. fruit 변수는 리스트
fruit = ["사과", "포도", "홍시"}
#3. 입력받은 값이 fruit에 요소로 있는지 확인
if text in fruit :
    print("정답입니다.")
    print("오답입니다.")

text = input("조회할 요소를 입력하세요 : ")
fruit = ["봄" : "딸기", "여름":"토마토","가을": "사과"
if text in fruit
    print("정답입니다.")
else :
    print("오답입니다")
