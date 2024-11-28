F=[0]*100
def init():
    F[1]=1
    F[2]=1
    for i in range(3,93):
        F[i]=F[i-1]+F[i-2]
init()
print(F[90])