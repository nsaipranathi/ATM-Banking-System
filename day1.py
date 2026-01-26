
project = float(input("Enter project marks : "))
internal = float(input("Enter internal marks : "))
external = float(input("Enter external marks : "))

total_score = (project * 0.70) + (internal * 0.10) + (external * 0.20)

print("Total Score:", total_score)


if external < 50 and internal < 50 and project < 50:
    print("Result: FAIL")
       
    
    if total_score >= 90:
        print("A")
    elif total_score >= 70:
        print("B")
    elif total_score >= 50:
        print("C")
else:
    if project<50:
        print("you have failed in project")
    if internal<50:
        print("you have failed in internal")
    if external<50:
        print("you have failed in external")          
              
       
