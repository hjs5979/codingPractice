n = int(input())

students = []

for _ in range(n):
    students.append(input().split())
    
students.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]), x[0]))

for student in students:
    print(student[0])
    
# 문자 역순(아스키 값 이용)
#sorted(a_counter,  key=lambda x: (-x[1], -ord(x[0])))
#=> [('d', 2), ('b', 2), ('s', 1), ('a', 1)]