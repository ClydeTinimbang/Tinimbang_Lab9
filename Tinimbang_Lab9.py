rows = int(input("Enter the number of rows for the triangle: "))

number = 1  
row = 1  

while row <= rows:
    col = 1  
    
    while col <= row:
        print(number, end=" ")  
        number += 1  
        col += 1  
    
    print()  
    row += 1  