# 80)  [기초-종합] 언제까지 더해야 할까?
'''
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지
계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더한다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.

입력예제 :
55

출력예제 : 
10
'''
'''
a = int(input())
b = 0

for i in range(a):
    if a>b:
        b+=i
    else:
        print(i-1)
        break
'''
'''
a = int(input()) #입력값 55
b = 0 #while 반복횟수
c = 0 #더한 결과값

while c<a: #더한 결과값이 55보다 크면 종료
    b+=1
    c+=b

print(b) #종료 되었을때 횟수
'''
#1회차 c(0)<55 , b=1 c=1
#2회차 c(1)<55 , b=2 c=3
#3회차 c(3)<55 , b=3 c=6
#4회차 c(6)<55 , b=4 c=10
#5회차 c(10)<55 , b=5 c=15
#6회차 c(15)<55 , b=6 c=21
#7회차 c(21)<55 , b=7 c=28
#8회차 c(28)<55 , b=8 c=36
#9회차 c(36)<55 , b=9 c=45
#10회차 c(45)<55 , b=10 c=55
#11회차 c(55)<55 성립 X 종료 print(b) = 10


# 81)  [기초-종합] 주사위를 2개 던지면?(설명)
'''
1부터 n까지, 1부터 m까지 숫자가 적힌
서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.

참고
중첩의 원리...
반복 실행 구조도 조건 실행 구조와 마찬가지로 중첩의 원리가 적용된다.
반복 실행 구조를 중첩하면 원하는 반복 구조를 다양하게 만들어 낼 수 있다.


입력예제 :
2 3

출력예제 : 
1 1
1 2
1 3
2 1
2 2
2 3
'''
'''
a = input().split()
b = int(a[0]) #2
c = int(a[1]) #3
d = 0

for i in range(b):
    for j in range(c):
        print(d+1,j+1)
    d+=1
'''    
''' # codeup 모범소스
a,b=input().split()

n=int(a)
m=int(b)

for i in range(1, n+1) : 
    for j in range(1, m+1) :
        print(i, j)
'''

# 82)  [기초-종합] 16진수 구구단?
'''
16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
영일(01)이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

입력예제 :
B

출력예제 : 
B*1=B
B*2=16
B*3=21
B*4=2C
B*5=37
B*6=42
B*7=4D
B*8=58
B*9=63
B*A=6E
B*B=79
B*C=84
B*D=8F
B*E=9A
B*F=A5
'''
'''
a = input()
if a=="A":
    b=10
elif a=="B":
    b=11
elif a=="C":
    b=12
elif a=="D":
    b=13
elif a=="E":
    b=14
elif a=="F":
    b=15
else:
    b=int(a)

for i in range(1,16):
    print("{0}*".format(a)+format(i,"X")+"="+format(i*b,"X"))
'''

# 83)  [기초-종합] 3 6 9 게임의 왕이 되자!(설명)
'''
3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.


입력예제 :
9

출력예제 : 
1 2 X 4 5 X 7 8 X
'''
'''
a = int(input())

for i in range(1,a+1):
    if i%3!=0:
        print(i,end=" ")
    if i%3==0:
        print("X",end=" ")
'''
''' # codeup 모범소스
a=input()

n=int(a)

for i in range(1, n+1) :
    if i%3==0 :
        print('X', end=' ')
    else :
        print(i, end=' ')
'''

# 84)  [기초-종합] 빛 섞어 색 만들기(설명)
'''
빨강(red), 초록(green), 파랑(blue) 빛을 섞어
여러 가지 빛의 색을 만들어 내려고 한다.

빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때,
(빛의 강약에 따라 0 ~ n-1 까지 n가지의 빛 색깔을 만들 수 있다.)

주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과
총 가짓 수를 계산해보자.


입력예제 :
2 2 2

출력예제 : 
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
8
'''
'''
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
print(a*b*c)
'''
''' # codeup 모범소스
a,b,c=input().split()

R=int(a)
G=int(b)
B=int(c)

c=0
for i in range(R) :
    for j in range(G) :
        for k in range(B) :
            c+=1
            print(i, j, k)

print(c)

'''

# 85)  [기초-종합] 소리 파일 저장용량 계산하기(설명)
'''
소리가 컴퓨터에 저장될 때에는 디지털 데이터화 되어 저장된다.

마이크를 통해 1초에 적게는 수십 번, 많게는 수만 번 소리의 강약을 체크해
그 값을 정수값으로 바꾸고, 그 값을 저장해 소리를 파일로 저장할 수 있다.

값을 저장할 때에는 비트를 사용하는 정도에 따라 세세한 녹음 정도를 결정할 수 있고,
좌우(스테레오) 채널로 저장하면 2배… 5.1채널이면 6배의 저장공간이 필요하고,
녹음 시간이 길면 그 만큼 더 많은 저장공간이 필요하다.

1초 동안 마이크로 소리강약을 체크하는 수를 h
(헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

한 번 체크한 결과를 저장하는 비트 b
(2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

좌우 등 소리를 저장할 트랙 개수인 채널 c
(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

녹음할 시간 s가 주어질 때,

필요한 저장 용량을 계산하는 프로그램을 작성해보자.

입력예제 :
44100 16 2 10

출력예제 : 
1.7 MB
'''
'''
a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

print("%.1f" %(a*b*c*d/8/1024/1024)+" MB")
'''
''' # codeup 모범소스
a,b,c,d=input().split()

H=int(a)
B=int(b)
C=int(c)
S=int(d)

print('%.1f MB' % (H*B*C*S/8/1024/1024))
'''

# 86)  [기초-종합] 소리 파일 저장용량 계산하기(설명)
'''
이미지가 컴퓨터에 저장될 때에도 디지털 데이터화 되어 저장된다.

가장 기본적인 방법으로는 그림을 구성하는 한 점(pixel, 픽셀)의 색상을
빨강(r), 초록(g), 파랑(b)의 3가지의 빛의 세기 값으로 따로 변환하여 저장하는 것인데,

예를 들어 r, g, b 각 색에 대해서 8비트(0~255, 256가지 가능)씩을 사용한다고 하면,

한 점의 색상은 3가지 r, g, b의 8비트+8비트+8비트로 총 24비트로 표현해서
총 2^24 가지의 서로 다른 빛의 색깔을 사용할 수 있는 것이다.

그렇게 저장하는 점을 모아 하나의 큰 이미지를 저장할 수 있게 되는데,
1024 * 768 사이즈에 각 점에 대해 24비트로 저장하면 그 이미지를 저장하기 위한
저장 용량을 계산할 수 있다.

이렇게 이미지의 원래(raw) 데이터를 압축하지 않고 그대로 저장하는 대표적인 이미지 파일이
*.bmp 파일이며, 비트로 그림을 구성한다고 하여 비트맵 방식 또는 래스터 방식이라고 한다.

이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.

예를 들어
일반적인 1024 * 768 사이즈(해상도)의 각점에 대해
24비트(rgb 각각 8비트씩 3개)로 저장하려면 1024 * 768 * 24 bit의 저장 용량이 필요하다.

입력예제 :
1024 768 24

출력예제 : 
2.25 MB
'''
'''
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
'''
''' # codeup 모범소스
print("%.2f MB" %(a*b*c/8/1024/1024))

a,b,c=input().split()

W=int(a)
H=int(b)
B=int(c)

print('%.2f MB' % (W*H*B/8/1024/1024))
'''

# 87)  [기초-종합] 여기까지! 이제 그만~(설명)
'''
1, 2, 3 ... 을 순서대로 계속 더해나갈 때,
그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더한다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.

하지만, 이번에는 그 때의 합을 출력해야 한다.

예를 들어 57을 입력하면
1+2+3+...+8+9+10=55에 다시 11을 더해 66이 될 때,
그 값 66이 출력되어야 한다.

입력예제 :
57

출력예제 : 
66
'''
'''
a = int(input()) #입력값
b = 0 #출력값
c = 1 #더한값

while a>b:
    b+=c
    c+=1
    
print(b)
'''

''' # codeup 모범소스
a=input()

n=int(a)

s=0
i=1
while s<n :
   s+=i
   i+=1

print(s)

'''
# 88)  [기초-종합] 3의 배수는 통과?(설명)
'''
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
3의 배수인 경우는 출력하지 않도록 만들어보자.

예를 들면,
1 2 4 5 7 8 10 11 13 14 ...
와 같이 출력하는 것이다.

입력예제 :
10

출력예제 : 
1 2 4 5 7 8 10
'''
'''
a = int(input())
b = 0

while a>b:
    b+=1
    if b%3!=0:
        print(b,end=" ")
'''

# 통과라서 continue를 사용한듯
''' # codeup 모범소스
a=input()

n=int(a)

for i in range(1, n+1) :
    if i%3==0 :
        continue 
    print(i, end=' ')
'''

# 89)  [기초-종합] 수 나열하기1
'''
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(series)이라고 한다.

예를 들어
1 4 7 10 13 16 19 22 25 ... 은
1부터 시작해 이전에 만든 수에 3을 더해 다음 수를 만든 수열이다.
이러한 것을 수학에서는 앞뒤 수들의 차이가 같다고 하여

등차(차이가 같다의 한문 말) 수열이라고 한다.
수열을 알게 된 영일이는 갑자기 궁금해졌다.

"그럼.... 123번째 나오는 수는 뭘까?"

영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
n번째 수를 출력하는 프로그램을 만들어보자.


입력예제 :
1 3 5

출력예제 : 
13
'''
'''
a,b,c = input().split()
a = int(a) #시작값
b = int(b) #등차
c = int(c) #몇번째


for i in range(1,c+1):
    if i==c:
        print(a)
    a+=b    
'''

''' # codeup 모범소스
a,d,n=input().split()

A=int(a)
D=int(d)
N=int(n)

for i in range(N-1) :
    A = A + D

print(A)
'''