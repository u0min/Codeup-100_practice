# 60)  비트단위로 AND 하여 출력하기(설명)
'''
입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)

입력예제 : 3 5
출력예제 : 1
'''
'''
a = input().split()
b = int(a[0])
c = int(a[1])

x = b&c
print(int(x))
'''
# 61)  비트단위로 OR 하여 출력하기(설명)
'''
입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.

입력예제 : 3 5
출력예제 : 7
'''
'''
a = input().split()
b = int(a[0])
c = int(a[1])

x = b|c
print(int(x))
'''
# 62)  비트단위로 XOR 하여 출력하기(설명)
'''
입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise) 연산자 ^(xor, circumflex/caret, 서컴플렉스/카릿)를 사용하면 된다.

입력예제 : 3 5
출력예제 : 6
'''
'''
a = input().split()
b = int(a[0])
c = int(a[1])

x = b^c
print(int(x))
'''
# 63)  [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기(설명)
'''
입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

입력예제 : 123 456
출력예제 : 456
'''
'''
a = input().split()
b = int(a[0])
c = int(a[1])

if b>c:
    print(b)
elif b<c:
    print(c)
'''        

# 64)  [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기(설명)
'''
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

입력예제 : 3 -1 5
출력예제 : -1
'''
'''
a = input().split()
b = int(a[0])
c = int(a[1])
d = int(a[2])

if b<c<d or b<d<c:
    print(b)
elif c<b<d or c<d<b:
    print(c)
else:
    print(d)
'''
# 65)  [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)
'''
세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

입력예제 : 1 2 4
출력예제 : 
2
4

'''
'''
a = input().split()
b = int(a[0])
c = int(a[1])
d = int(a[2])

if b%2==0:
    print(b)
if c%2==0:
    print(c)
if d%2==0:
    print(d)
'''
# 66)  [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)
'''
세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

입력예제 : 1 2 8
출력예제 : 
odd
even
even

'''
'''
a = input().split()
b = int(a[0])
c = int(a[1])
d = int(a[2])

if b%2==0:
    print("even")
else: print("odd")
if c%2==0:
    print("even")
else: print("odd")
if d%2==0:
    print("even")
else: print("odd")
'''
# 67)  [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기(설명)
'''
정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

입력예제 : -2147483648
출력예제 : 
minus
even

'''
'''
a = int(input())

if a>0:
    print("plus")
else: print("minus")
if a%2==0:
    print("even")
else: print("odd")
'''
# 68)  [기초-조건/선택실행구조] 정수 1개 입력받아 평가 출력하기(설명)
'''
점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

평가 기준
점수 범위 : 평가
90 ~ 100 : A
70 ~  89 : B
40 ~  69 : C
0  ~  39 : D
로 평가되어야 한다.

입력예제 : 73
출력예제 : B

'''
'''
a = int(input())

if a>=90:
    print("A")
elif a>=70:
    print("B")
elif a>=40:
    print("C")
else:
    print("D")
'''
# 69)  [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(설명)
'''
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

입력예제 : A
출력예제 : best!!!

'''

a = input()

if a=="A":
    print("best!!!")
elif a=="B":
    print("good!!")
elif a=="C":
    print("run!")
elif a=="D":
    print("slowly~")
else:
    print("what?")

