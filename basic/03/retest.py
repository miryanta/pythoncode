import re

# p = re.compile('ab*')

# m = p.match('ac')
# print(m)

# m1 = p.search('babbbc')
# print(m1)

# m2 = re.search('ab*', 'bacc')
# print(m2)

email = input("email 입력")
p = re.compile('[a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,5}')
result = p.match(email)
print(result)