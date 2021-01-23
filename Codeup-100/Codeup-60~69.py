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

a = input().split()
b = int(a[0])
c = int(a[1])

if b>c:
    print(b)
elif b<c:
    print(c)
        