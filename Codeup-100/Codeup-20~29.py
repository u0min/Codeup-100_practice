# CodeUp 기초 100제 풀기
# 20)  주민번호 입력받아 형태 바꿔 출력하기
'''
주민번호는 다음과 같이 구성된다.

XXXXXX-XXXXXXX

앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다.
주민번호를 입력받아 형태를 바꿔 출력해보자.
입력예시 : 000907-1121112 출력예시 : 0009071121112
'''
'''
answer = input().split("-")
print(answer[0], answer[1],sep="")
'''

# 21)  단어 1개 입력받아 그대로 출력하기(설명)
'''
1개의 단어를 입력받아 그대로 출력해보자.

한 단어가 입력된다.(단, 단어의 길이는 50자 이하이다.)

문자를 50개 저장하기 위해서는 char data[51] 로 선언하면 된다.

char data[51]="";
scanf("%s", data);

를 실행하면, data[51] 에 한 단어가 저장된다.
'''
'''
answer = input()
print(answer)
'''
# 22)  문장 1개 입력받아 그대로 출력하기(설명)
'''
공백 문자가 포함되어 있는 문장을 입력받고 그대로 출력하는 연습을 해보자.
'''
'''
answer = input()
print(answer)
'''
# 23)  실수 1개 입력받아 부분별로 출력하기(설명)
'''
공백 문자가 포함되어 있는 문장을 입력받고 그대로 출력하는 연습을 해보자.
'''
'''
answer = input()
answer = answer.split(".")
print(answer[0],answer[1],sep="\n")
'''
# 24)  단어 1개 입력받아 나누어 출력하기(설명)
'''
단어를 1개 입력받는다.

입력받은 단어(영어)의 각 문자를

한줄에 한 문자씩 분리해 출력한다.
입력예제 : Boy 
출력예제 :
'B'
'o'
'y'
'''
'''
answer = input()
for i in range(len(answer)):
    print("\'"+answer[i]+"\'")
'''
'''
a=input()
a=[print("'"+i+"'") for i in a]
'''

# 25)  정수 1개 입력받아 나누어 출력하기(설명)
'''
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

입력예제 : 75254
출력예제 :
[70000]
[5000]
[200]
[50]
[4]
'''
'''
n = input()
if 10000 <= int(n) < 100000:
    a1 = int(n[0])*10000
    a2 = int(n[1])*1000
    a3 = int(n[2])*100
    a4 = int(n[3])*10
    a5 = int(n[4])*1
print("["+str(a1)+"]","["+str(a2)+"]","["+str(a3)+"]","["+str(a4)+"]","["+str(a5)+"]",sep="\n")
'''

# 26)  시분초 입력받아 분만 출력하기(설명)
'''
입력되는 시:분:초 에서 분만 출력해보자.

입력예제 : 17:23:57
출력예제 : 23
'''
'''
n = input().split(":")
print(int(n[1]))
'''

# 27)  년월일 입력 받아 형식 바꿔 출력하기(설명)
'''
년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

년월일(yyyy.mm.dd)를 입력받아,

일월년(dd-mm-yyyy)로 출력해보자.

(단, 한 자리 일/월은 0을 붙여 두자리로, 년도도 0을 붙여 네자리로 출력한다.) 

입력예제 : 2014.07.15
출력예제 : 15-07-2014 
'''
'''
n = input().split(".")
print('%02d'%int(n[2]),'%02d'%int(n[1]),'%04d'%int(n[0]),sep="-")
'''
# 28)  정수 1개 입력받아 그대로 출력하기2(설명)
'''
정수 1개를 입력받아 그대로 출력해보자.
(단, 입력되는 정수의 범위는 0 ~ 4,294,967,295 이다.)

참고
-2147483648 ~ +2147483647 범위의 정수를 저장하고 처리하기 위해서는
int 형으로 변수를 선언하면 된다.(int 로 선언하고 %d로 받고 출력)

하지만 이 범위를 넘어가는 정수를 저장하기 위해서는
보다 큰 범위를 저장할 수 있는 다른 데이터형을 사용해야 정상적으로 저장시킬 수 있다.

unsigned int 데이터형을 사용하면 0 ~ 4294967295 범위의 정수를 저장할 수 있다. 

입력예제 : 2147483648
출력예제 : 2147483648
'''
'''
a = input()
print(a)
'''
# 29)  실수 1개 입력받아 그대로 출력하기2(설명)
'''
실수 1개를 입력받아 그대로 출력해보자.
(단, 입력되는 실수의 범위는 +- 1.7*10-308 ~ +- 1.7*10308 이다.)

참고
float 데이터형을 사용하면 +- 3.4*10-38 ~ +- 3.4*1038 범위의 실수를 저장할 수 있다.
(float 로 선언하고 %f로 입력 받아 출력하면 된다.)

입력된 실수를 소수점 이하 11자리까지 반올림하여 출력한다.

입력예제 : 3.14159265359
출력예제 : 3.14159265359
'''

a = float(input())
print(format(a,".11f"))
# print('%.11f' % float(a))


