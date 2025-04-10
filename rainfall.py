numberofyears = int(input("Enter the period in years: "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
total= 0 
average = 0 
count = 0 
for years in range(numberofyears):
    for month in months:
       print('enter rainfall amount for the month of:    ', month)
       rainfall = input(int(input('Enter the rainfall amount:    ')))
count += 1
total =+ rainfall
average == total / ( 12 * numberofyears)
print('Number of months' , months.len*numberofyears)
print("Average: ", average)
print("total: ", total)
