if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() 
    
    markslist = student_marks[query_name]
    total=float(sum(markslist))
    avg = float(total/3)
    
    print('{0:.2f}'.format(avg))
