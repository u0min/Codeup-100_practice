# 30)  정수 1개 입력받아 그대로 출력하기3(설명)
'''
정수 1개를 입력받아 그대로 출력해보자.
단, 입력되는 정수의 범위는
-9,223,372,036,854,775,808 ~ +9,223,372,036,854,775,807 이다.

int 형으로 저장할 수 있는 범위를 넘어가는 정수 값을 저장하기 위해서는
보다 큰 범위를 저장할 수 있는 다른 데이터형을 사용해야 한다.

long long int 데이터형을 사용하면
-9,223,372,036,854,775,808 ~ +9,223,372,036,854,775,807 범위의 정수값을
저장시킬 수 있다.

입력예제 : -2147483649
출력예제 : -2147483649
'''
'''
a = int(input())
print(a)
'''
# 31)  10진 정수 1개 입력받아 8진수로 출력하기(설명)
'''
10진수를 입력받아 8진수(octal)로 출력해보자.
참고
%d(10진수 형태)로 입력받고,
%o를 사용해 출력하면 8진수(octal)로 출력된다.

입력예제 : 10
출력예제 : 12
'''
'''
a = int(input())
print('%o'%a)
'''
# 32)  10진 정수 입력받아 16진수로 출력하기1(설명)
'''
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

참고
%d(10진수 형태)로 입력받고
%x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.

입력예제 : 255
출력예제 : ff
'''
'''
a = int(input())
print('%x'%a)
'''
# 33)  10진 정수 입력받아 16진수로 출력하기2(설명)
'''
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

참고
%d(10진수 형태)로 입력받고
%X로 출력하면 16진수(hexadecimal) 대문자로 출력된다.

입력예제 : 255
출력예제 : FF
'''
'''
a = int(input())
print('%X'%a)
'''

# 34)  8진 정수 1개 입력받아 10진수로 출력하기(설명)
'''
8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.

참고
%o로 입력받으면 8진수로 인식시켜 저장시킬 수 있다.
%d로 출력하면 10진수로 출력된다.

입력예제 : 13
출력예제 : 11
'''
'''
a = int(input(),8)
print(a)
'''
# 35)  16진 정수 1개 입력받아 8진수로 출력하기(설명)
'''
16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.

참고
%x(영문자 소문자) 나 %X(영문자 대문자)로 입력 받으면
16진수로 인식시켜 저장시킬 수 있다. %o로 출력하면 8진수로 출력된다.

입력예제 : f
출력예제 : 17
'''
'''
a = int(input(),16)
print(format(a,"o"))
'''

# 36)  영문자 1개 입력받아 10진수로 출력하기(설명)
'''
영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.

참고
예를 들어 영문 대문자 "A"는 10진수 65를 의미하는 2진수 값으로 저장된다.

입력예제 : A
출력예제 : 65
'''
'''
a = ord(input())
print(a)
'''
# 37)  정수 입력받아 아스키 문자로 출력하기
'''
영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.

10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
단, 0 ~ 255 범위의 정수만 입력된다.

입력예제 : 65
출력예제 : A
'''
'''
a = int(input())
print(chr(a))
'''
# 38)  정수 2개 입력받아 합 출력하기1(설명)
'''
정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
(단, 입력되는 정수는 -1073741824 ~ 1073741824 이다.)


입력예제 : 123 -123
출력예제 : 0
'''

a = (input().split( ))
print(int(a[0])+int(a[1]))

# 38)  정수 2개 입력받아 합 출력하기2(설명)
'''
정수 2개를 입력받아 합을 출력해보자.
단, 입력되는 정수는 -2147483648 ~ +2147483648 이다.

참고
+ 연산자를 사용하면 된다.
단, 계산된 결과가 int 형으로 저장할 수 있는 범위를 넘어갈 수 있기 때문에 다른 데이터형을 사용해야 한다.

주의
int 데이터형은 %d로 입출력하고,
long long int 데이터형은 %lld로 입출력한다.



입력예제 : 2147483648 2147483648
출력예제 : 4294967296 
'''

a = (input().split( ))
print(int(a[0])+int(a[1]))
