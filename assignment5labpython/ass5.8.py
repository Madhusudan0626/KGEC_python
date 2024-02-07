n = int(input("Enter the number of rows:")) 
m = int(input("Enter the number of columns:")) 
  
matrix = [] 

print("Enter values in matrix :") 
for i in range(n):
    data =[] 
    for j in range(m):
         data.append(int(input())) 
    matrix.append(data) 

for i in range(n): 
    for j in range(m): 
        print(matrix[i][j], end = " ") 
    print()

for i in range(n):
    sum = 0
    for j in range(m): 
        sum = sum + matrix[i][j]
    print('Sum of row',i+1,':',sum) 