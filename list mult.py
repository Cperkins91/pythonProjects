def get_list():
    print("Please enter a list of integers on one line seperated by commas")
    A = [int(i) for i in input().split(',')]
    return A
def display_list(A):
    print(A)
def calculate_list(A,B):
    #for i in range(len(A))
    C = [A[i]*B[i] for i in range(len(A))]
    return C
def calculate_list2(A,B):
    C= []
    for i in range(len(A)):
        C.append(A[i]*B[i])
    return C
a = get_list()
display_list(a)
b = get_list()
display_list(b)
print(calculate_list(a,b))
print(calculate_list2(a,b))