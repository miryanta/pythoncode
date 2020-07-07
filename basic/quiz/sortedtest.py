myList = [4,2,3,5,1]
myList.sort()
print(myList)

myDic = {1:1,3:3,2:2}
myDic.sort()
print(myDic)

#str
sorted("hello")


#list
sorted([5,2,1,3,4])
sorted([[2,1,3],[3,2,1],[1,2,3]])

#set
sorted({3,2,1})

#tuple
sorted((3,2,1))


#dict
sorted({3:1,2:3,1:4})

#value값dmf rlwnsdmfh wjdfuf
#dict
myDict = {3:1,2:3,1:4}

#[(3,1),(2,3),(1,4)]
sorted(myDict.items(), key=lambda  x: x[1])


#2번째 문자 기준으로 정렬
sorted(['abc', 'bac', 'pythong'], key=lambda x:x[1])

#내림차순
sorted(['abc', 'bac', 'pythong'], key=lambda x:x[1], reverse=True)