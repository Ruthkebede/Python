
#declare a function main 
#ask user to input score
#define grade range and print using the assigned format
#Call main function to display our final result.

def main():
    score1=float(input("Please enter Score 1: "))
    score2=float(input("Please enter Score 2: "))
    score3=float(input("Please enter Score 3: "))
    score4=float(input("Please enter Score 4: "))
    score5=float(input("Please enter Score 5: "))
    
    findaverage= averagescore(score1, score2, score3, score4, score5)

    
    grade1= lettergrade(score1)
    grade2= lettergrade(score2)
    grade3= lettergrade(score3)
    grade4= lettergrade(score4)
    grade5= lettergrade(score5)
    average_grade= lettergrade(findaverage)
    
    print("Score \t numeric grade \t Letter Grade \n")
    print("------------------------------------------")
    
    print("Score 1: " ,"\t", format(score1,".1f"), "\t\t", grade1)
    print("Score 2: " ,"\t", format(score2,".1f"), "\t\t", grade2)
    print("Score 3: " ,"\t", format(score3,".1f"), "\t\t", grade3)
    print("Score 4: " ,"\t", format(score4,".1f"), "\t\t", grade4)
    print("Score 5: " ,"\t", format(score5,".1f"), "\t\t", grade5)
    print("---------------------------------------------")
    print("Average score: ",format(findaverage,".1f"), "\t\t",average_grade)

def averagescore(score1,score2,score3,score4,score5):
    average= (score1 + score2 + score3 + score4 + score5)/5
    return average

def lettergrade(grade):
    if(grade< 60):
        return "F"
    elif(grade < 70):
        return "D"
    elif(grade< 80):
        return "C"
    elif(grade < 90):
        return "B"
    elif(grade < 101):
        return "A"

main()
