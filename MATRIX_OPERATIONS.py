import numpy as np
n=int(input("Enter the number of Rows\n"))
m=int(input("Enter the number of Columns\n"))
a=[]
for i in range(n):
    a.append([0] * m )
for i in range (n):
    for j in range(m):
        print("Enter Element In:",[i,j])
        a[i][j] = int(input())
print("The Matrix is:"),
print(np.matrix(a))
dt="\n\t\t\t1:DETERMINANT\n\t\t\t2:RANK\n\t\t\t3:MATRIX RAISED TO POWER\n\t\t\t4:INVERSE\n\t\t\t5:NORM\n\t\t\t6:TRANSPOSE\n\t\t\t7:TRACE" 
print(dt)
while True:
	d=input("\nCHOOSE THE REQUIRED OPERATION OR ELSE ENTER 000 TO CLOSE THE PROGRAM:")
	if d==1:
		if n==m:
			print("\nDETERMINANT OF MATRIX IS:"),
			print(np.linalg.det(a))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX FOR DET")
	elif d==2:
		  print("\nRANK OF THE GIVEN MATRIX IS:"),
		  print(np.linalg.matrix_rank(a))
	elif d==3:
		p=input("enter power:")
		print("\nTHE RESULT MATRIX IS:")
		print(np.linalg.matrix_power(a,p))
	elif d==4:
		print("\nINVERSE MATRIX IS:")
		print(np.linalg.inv(a))
	elif d==5:
		print("\nNORM OF MATRIX IS:")
		print(np.linalg.norm(a))
	elif d==6:
		print("\nTRANSPOSE OF MATRIX IS:")
		print(np.transpose(a))
	elif d==7:
		if n==m:
			print("\nTRACE OF MATRIX IS:"),
			print(np.trace(a))
		else:
			print("please enter square matrix")
	elif(d==000):
		print("\nPROGRAM ENDED")
		break


	
 
