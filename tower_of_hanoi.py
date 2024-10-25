########################################################
#                                                      # 
#                   EXPERIMENT 4                       # 
#                  Tower Of Hanoi                      # 
#             Nathan Cordeiro 22co09                   #
#                                                      #
########################################################

def move(a,b):
    print("Move",a, "to", b)
def TowerofHanoi(n,A,B,C):
#if we have only one disk then we can directly transfer it to the destination
    if (n==1):
        move(A,C)
    else:
        TowerofHanoi(n-1, A, C, B)
        move(A,C)
        TowerofHanoi(n-1,B,A,C)

n = int(input("Enter the number of disks:"))
TowerofHanoi(n, "A", "B", "C")