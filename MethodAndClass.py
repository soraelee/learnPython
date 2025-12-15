# ==================================================================
# 기본 구문
# def 함수 이름(매개변수):
#       처리할 로직
#           return 출력값
# ==================================================================


def sum1(a, b):
    return a + b

a = sum1(3, 2)

def sum1_1(a, b):
    return a, b, a+b

d, e, f = sum1_1(1, 2);
print(d, e, f)

g = sum1_1(1, 2)

def sum2(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else :
        print('숫자를 입력하십시오.')

sum2(3, 2)
sum2('b', 2)

# =============================================================
# 함수의 input으로 여러개의 값을 입력하고 싶은데, 변수를 그만큼 늘려줘야 하는가?
# =============================================================

def sum3(*args):  # arguments의 줄임말, 받으면 튜플로 받아들인다. 
    return sum(args), type(args)

sum3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 함수를 만들 때 하나의 변수 + 튜플을 받으려면 반드시 순서를 지켜야 함
def exer(name, *args):
    print(name)
    print(len(args))
    print(type(args))

exer("이상훈", 1, 2, 3, 4 ,5 )

## 딕셔너리도 함수의 input으로 넣을 수 있으며 문자 앞에 ** 두개를 붙여야 함
def mean1(**kwargs):       # kwargs : keyword argument의 줄임말
    print(type(kwargs))
    return sum(kwargs.values())

mean1(a=1, b=2);

# =================================================================
# 클래스
# =================================================================

class coin:
    def __init__(self, name):
        self.name = name
        self.shares = 0

    def buy(self, shares):
        self.shares+=shares
        print(self.name + " 코인 {}개 매수 완료".format(shares))

    def sell(self, shares):
        self.shares-=shares
        print(self.name + " 코인 {}개 매도 완료".format(shares))

    def balance(self):
        print("현재 " + self.name + " 코인은 {}개 보유중입니다.".format(self.shares))

# 클래스의 상속
class add_coin(coin):
    def sell_all(self):
        self.shares = 0
        print(self.name + " 코인 전량 매도 완료")

eos = add_coin("EOS")
eos.buy(3)
eos.sell_all()
eos.balance()

eth = coin("ETH")
eth.buy(5)
eth.buy(4)
eth.buy(3)
eth.sell(7)
eth.balance()

doge = coin("doge")
doge.buy(3)

# 예제 2
# 튜플은 수정이 불가능 -> 리스트로 바꿔서 생각
class squid_game:
    def __init__(self, *args):
        self.data = list(args)[0]       ## 리스트로 변환
        print("참가자 명단은 아래와 같습니다. \n"+str(self.data))

    def check(self):
        print(self.data)
        print(type(self.data))

        return self.data
    
    def fail (self, *args):
        self.data = [x for x in self.data if x not in list(args)[0]]
        print(args)
        print(type(self.data))
        return self.data
    

    def fail2(self, * args):
        print(len(args))
        for i in range(0, len(args)):
            print(args[i])
            self.data.remove(args[i])

        return self.data
    
    def night_random_fight(self, num):
        for i in range(num):
            j = self.data.pop()
            print('{}번째 참가자 사망'.format(j))
        return self.data
    
first_list = list(range(1, 51))
first_comp = squid_game(first_list)

a = first_comp.check()
import random
first_dead_list = random.sample(first_list, 10)

first_live_list = first_comp.fail(first_dead_list)

# 과제
# 계산기 만들기
# 클래스 + 함수 강의에서 무ㅗ건 나옴
# class명 : cal, 덧셈함수 add, 뺄셈함수 sub 두개만 만들기

class cal :
    def __init__(self):
        self.result = 0
        
    def add(self, a) :
        self.result += a
        return self.result
    
    def sub(self, a) :
        self.result -= a
        return self.result
    
a = cal()
a.sub(3)
a.add(5)

