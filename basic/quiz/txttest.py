# f = open("test.txt", 'w')
# f.write("txt파일 생성")
# f.close()


f = open("test.txt", "r")

while line:
    line = f.readline()
    print(line)
line = f.readline()
type(line)
print(line)
f.close()