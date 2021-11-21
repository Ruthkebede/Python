
#First ask how many days the user worked.
#It is knows that the user's first day salary was one penny.
#assign value to the variables.
#use a for loop to include all the days worked and show increment.
#creat a formula that allows us to calculate the doubling behavior.
# finally, print the value in the form of dollars and cents.




num_of_days_worked=int(input("How many days have you worked: "))
daily_pay=0.01
tot_pennies=0
print('Day Pennies','\n', '-------------')

for specificDay in range(num_of_days_worked):
    pennies_day=(2 ** specificDay)*daily_pay
    tot_pennies= tot_pennies + pennies_day
    print(specificDay + 1,'\t','$',pennies_day)
    
tot_pay= tot_pennies
print("The total salary for",num_of_days_worked,"days is:$",tot_pay)
