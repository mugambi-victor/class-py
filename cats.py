"""Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

Note : Use 'continue' statement. 

Expected Output : 0 1 2 4 5"""
i=0
while i<=6:
	if(i==3 or i==6):
		continue
	print(i)
	
