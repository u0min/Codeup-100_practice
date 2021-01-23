# 70)  [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)
'''
월이 입력될 때 계절 이름이 출력되도록 해보자.

예
월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall


입력예제 : 12
출력예제 : winter

'''
'''
a = int(input())

if a==12 or a==1 or a==2:
    print("winter")

if a==3 or a==4 or a==5:
    print("spring")

if a==6 or a==7 or a==8:
    print("summer")

if a==9 or a==10 or a==11:
    print("fall")
'''
# 71)  [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1(설명)
'''
0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.

입력예제 : 7 4 2 3 0 1 5 6 9 10 8
출력예제 : 
7
4
2
3

'''

a = input().split()

for i in a:
    if int(i)==0:
        break
    print(i)