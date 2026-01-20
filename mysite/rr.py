
n = int(input())
arr = map(int, input().split())
arr1=set(arr)
arr2=[]
arr2.extend(arr1)
a=max(arr1)
arr2.remove(a)
    
print("Runner up is:",max(arr2))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=0
    for i in student_marks[query_name]:
        a+=i
    b=f"{a/3:.2f}"
    print(b)