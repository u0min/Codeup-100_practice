# CodeUp 기초 100제 풀기
# 10)  정수 1개 입력받아 그대로 출력하기(설명)
'''
정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후
변수에 저장되어 있는 값을 그대로 출력해보자.

'''
'''
answer = input()
answer = int(answer)
print(answer)
'''

# 11)  문자 1개 입력받아 그대로 출력하기(설명)
'''
문자형(char)으로 변수를 하나 선언하고, 변수에 문자를 저장한 후
변수에 저장되어 있는 문자를 그대로 출력해보자.

'''
'''
answer = input()
print(answer)
'''

# 12)  실수 1개 입력받아 그대로 출력하기(설명)
'''
실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후
저장되어 있는 실수값을 출력해보자.
** Python 자릿수도 맞춰줘야함
'''
'''
answer = float(input())
print("%f" %answer)
'''

# 13)  정수 2개 입력받아 그대로 출력하기(설명)
'''
정수(int) 2개를 입력받아 그대로 출력해보자.
#입력 예시가 '1 2' 인데 int형이 아님
'''
'''
answer = input().split()
answer[0] = int(answer[0])
answer[1] = int(answer[1])
print(answer[0], answer[1], sep=" ")

# answer = input()
# print(answer) #이렇게만 해도 됨
'''

# 14)  문자 2개 입력받아 순서 바꿔 출력하기(설명)
'''
2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
#입력 예시 : A b 출력예시 : b A
'''
'''
answer = input().split()
print(answer[1], answer[0], sep=" ")
'''

# 15)  실수 입력받아 둘째 자리까지 출력하기(설명)
'''
실수(float) 1개를 입력받아 저장한 후,
저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여
소수점 이하 둘 째 자리까지 출력하시오.

'''
'''
answer = float(input())
print(format(answer,".2f"))
#round 사용하면 1.00 일때 1이나옴
'''

# 17)  정수 1개 입력받아 3번 출력하기(설명)
'''
int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.
입력예시 : 125 출력예시 : 125 125 125
'''
'''
answer = int(input())
print(answer,answer,answer,sep=" ")
'''

# 18)  시간 입력받아 그대로 출력하기(설명)
'''
어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
입력예시 3:16 출력 예시 3:16
'''
'''
answer = input()
print(answer)
'''

# 19)  연월일 입력받아 그대로 출력하기
'''
년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
입력예시 2013.8.5 출력 예시 2013.08.05
'''
'''
answer = input().split(".")
print(str(answer[0]).zfill(4),str(answer[1]).zfill(2),str(answer[2]).zfill(2),sep=".")
'''