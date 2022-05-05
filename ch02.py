#!/usr/bin/env python
# coding: utf-8

# # chapter02
# 
# ## 프로젝트 Lab1

# In[2]:


# 두 실수의 사칙연산과 표준 입력 연산식의 계산
num1 = float(input('첫 번째 수 입력 >> '))
num2 = float(input('두 번째 수 입력 >> '))
print('합:', num1 + num2)
print('차:', num1 - num2)
print('곱하기:', num1 * num2)
print('나누기:', num1 / num2)
expression = input('연산식 입력 >> ')
print('연산식:', expression, '결과:', eval(expression))


# ## 프로젝트 Lab2

# In[4]:


# 진수와 그에 맞는 정수를 입력받아 2진수, 8진수, 10진수, 16진수 출력
base = int(input('입력할 정수의 진수(base)는? '))
invar = input(str(base) + '진수 정수 입력 >> ')
data = int(invar, base) # 입력 문자열을 base 진수로 변환
# 여러 진수로 출력
print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))


# ## 도전 프로그래밍
# ### p.68

# 01

# In[2]:


string1 = input('문자열 1: ')
string2 = input('문자열 2: ')
print(string1, string2)
print(f'{string1}, {string2}')


# 02

# In[10]:


v = int(input('차의 속도를 입력(km) >> '))
mile = v / 1.61
print(v, '(km)은', mile, '마일(miles)이다.')


# 03

# In[11]:


n = int(input('아메리카노 몇 개 주문하세요? '))
price = n * 3500
print('총 가격은', price, '이다.')


# 04

# In[13]:


earth = int(input('알려진 지구 둘레: '))
c = 2 * 3.141592 * 6378.1
dis = earth - c
print('지구와 같은 원둘레: ', c)
print('차이: ', dis, '(km)')


# 05

# In[15]:


celsius = int(input('온도 입력 >> '))
fahrenhite1 = celsius * 9/5 +32 # 정확 계산 화씨 변환
print('<정확 계산> 섭씨: ', celsius, ',', '화씨: ', fahrenhite1)

fahrenhite2 = celsius * 2 + 30 # 약식 계산 화씨 변환
print('<약식 계산> 섭씨: ', celsius, ',', '화씨: ', fahrenhite2)

dis = fahrenhite1 - fahrenhite2
print('차이: ', dis)


# 06

# In[17]:


num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))
print(num1, '/', num2, '==>', num1 / num2)
print(num1, '%', num2, '==>', num1 % num2)
print(num1, '//', num2, '==>', num1 // num2)
print(num1, '**', num2, '==>', num1 ** num2)


# In[3]:


num1 = int(input('첫 번째 숫자: '))
num2 = int(input('두 번째 숫자: '))

print(f'{num1} / {num2} = {num1/num2: .2f}')
print(f'{num1} % {num2} = {num1%num2: .2f}')
print(f'{num1} // {num2} = {num1//num2: .2f}')
print(f'{num1} ** {num2} = {num1**num2: .2f}')


# 07

# In[24]:


f1 = float.fromhex(input('첫 번째 16진수 실수 입력 >> '))
f2 = float.fromhex(input('첫 번째 16진수 실수 입력 >> '))

print('실수1: ', f1, '실수2: ', f2)
print('합: ', f1 + f2)
print('차: ', f1 - f2)
print('곱하기: ', f1 * f2)
print('나누기: ', f1 / f2)


# In[14]:


hex1 = input('첫 번째 16진수: ')
hex2 = input('두 번째 16진수: ')

num1, num2 = int(hex1, 16), int(hex2, 16)
print('실수1: ', num1, '실수2: ', num2)
print('합: ', num1 + num2)
print('차: ', num1 - num2)
print('곱하기: ', num1 * num2)
print('나누기: ', num1 / num2)


# 08

# In[27]:


num = int(input('네 자릿수 정수 입력 >> '))
renum = (num // 1000) + (((num % 1000) // 100) * 10) + (((num % 100) // 10) * 100) + ((num % 10) * 1000)
print(renum)


# In[28]:


# 간단하게
num = int(input('네 자릿수 정수 입력 >> '))
print(int(str(num)[::-1]))

