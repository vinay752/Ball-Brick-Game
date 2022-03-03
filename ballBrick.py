#Function to construct matrix before bricks are constructed
def matrixConstruction(N):
    k=[]
    for i in range(N):
        k.append([])
        for j in range(N):
            if i==0:
                k[i].append("W")
            elif j==0 or j==N-1:
                k[i].append("W")
            elif i==N-1 and j==N//2:
                k[i].append("o")
            elif i==N-1:
                k[i].append("G")
            else:
                k[i].append(" ")
    return k
#Function to implement bricks in empty matrix
def brickImp(matrix):
    BrickPositionX,BrickPositionY,BrickType=map(str,input("Enter the brick's position and brick type: ").split())
    BrickPositionX=int(BrickPositionX)
    BrickPositionY=int(BrickPositionY)
    if BrickType.isdigit():
        BrickType=int(BrickType)
    matrix[BrickPositionX][BrickPositionY]=BrickType
    if input("Do you want to continue(Y or N)?")=='Y':
        brickImp(matrix)
    return matrix
#Function to print matrix constructed with bricks
def printMatrix(N):
    for i in range(N):
        z=""
        for j in range(N):
            if j==N-1:
                z+=str(matrix[i][j])
            elif len(str(matrix[i][j]))==1:
                z+=str(matrix[i][j])+" "
            else:
                z+=str(matrix[i][j])
        print(z)
def traverse(N,ballCount):
    directionOfBall=input("Enter the direction in which the ball need to traverse: ")
    I=matrix[N-1].index('o')
    if directionOfBall=='ST':
        for i in range(N-2,-1,-1):
            if matrix[i][I]!=" ":
                if matrix[i][I]==1:
                    matrix[i][I]=" "
                    break
                elif matrix[i][I]=="DE":
                    for l in range(1,N-2):
                        matrix[i][l]=" "
                    break
                elif matrix[i][I]=="DS":
                    DS=matrix[i].index('DS')-1
                    for l in range(0,3):
                        matrix[i+1][DS+l]=" "
                        matrix[i][DS+l]=" "
                        matrix[i-1][DS+l]=" "
                    break
                elif matrix[i][I]=="B":
                    matrix[i][I]=" "
                    for l in range(1,N-2):
                        if l%2==1 and matrix[-1][I+int(l/2+1/2)]!="_":
                            matrix[-1][I+int(l/2+1/2)]="_"
                            printMatrix(N)
                            break
                        elif l%2==0 and matrix[-1][I-int(l/2)]!="_":
                            matrix[-1][I-int(l/2)]="_"
                            break
                        else:
                            pass
                    break
                elif matrix[i][I]=='W':
                    break
                else:
                    matrix[i][I]-=1
                    break
    elif directionOfBall=='LD':
        ballCount-=1
        for i in range(N-2,-1,-1):
            if matrix[i][I-1]!=" ":
                if matrix[i][I-1]==1:
                    matrix[i][I-1]=" "
                    if matrix[-1][I-1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I-1]="o"
                    break
                elif matrix[i][I-1]=="DE":
                    for l in range(1,N-2):
                        matrix[i][l]=" "
                    if matrix[-1][I-1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I-1]="o"
                    break
                elif matrix[i][I-1]=="DS":
                    DS=matrix[i].index('DS')-1
                    for l in range(0,3):
                        matrix[i+1][DS+l]=" "
                        matrix[i][DS+l]=" "
                        matrix[i-1][DS+l]=" "
                    if matrix[-1][I-1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I-1]="o"
                    break
                elif matrix[i][I-1]=='W':
                    if matrix[-1][I-1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I-1]="o"
                    break
                else:
                    matrix[i][I-1]-=1
                    if matrix[-1][I-1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I-1]="o"
                    break
    else:
        ballCount-=1
        for i in range(N-2,-1,-1):
            if matrix[i][I+1]!=" ":
                if matrix[i][I+1]==1:
                    matrix[i][I+1]=" "
                    if matrix[-1][I+1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I+1]="o"
                    break
                elif matrix[i][I-1]=="DE":
                    for l in range(1,N-2):
                        matrix[i][l]=" "
                    if matrix[-1][I+1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I+1]="o"
                    break
                elif matrix[i][I-1]=="DS":
                    DS=matrix[i].index('DS')-1
                    for l in range(0,3):
                        matrix[i+1][DS+l]=" "
                        matrix[i][DS+l]=" "
                        matrix[i-1][DS+l]=" "
                    if matrix[-1][I+1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I+1]="o"
                    break
                elif matrix[i][I+1]=='W':
                    if matrix[-1][I+1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I+1]="o"
                    break
                else:
                    matrix[i][I+1]-=1
                    if matrix[-1][I+1]!="W":
                        matrix[-1][I]="G"
                        matrix[-1][I+1]="o"
                    break
    printMatrix(N)
    return ballCount
N=int(input("Enter the size of the NxN matrix: ")) #matrix of NxN
matrix=matrixConstruction(N) #Function calling to build empty NxN matrix with Walls, Ground and ball
matrix=brickImp(matrix) #Function calling to implemnet bricks in above constructed matrix
ballCount=int(input("Enter ball count: "))
printMatrix(N) #Function calling to print above matrix with bricks
print("Ball count is {}.\n".format(ballCount))
while ballCount>0:
    ballCount=traverse(N,ballCount)
    count=0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if matrix[i][j]==" ":
                count+=1
    if count==pow(N-2,2):
        print("You win HURRAY..!!")
        break
    else:
        print("Ball count is {}.\n".format(ballCount))               
