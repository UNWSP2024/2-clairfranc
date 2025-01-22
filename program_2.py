# Program 2, Claire Francis, Jan 21, 2025

def average_age():
    # Get User Input
    age1 = int(input("insert age1 here:"))
    age2 = int(input("insert age2 here:"))
    age3 = int(input("insert age3 here:"))
    age4 = int(input("insert age4 here:"))
    age5 = int(input("insert age5 here:"))

    # Sum ages
    sum_ages = age1+age2+age3+age4+age5

    #Average the ages
    average_ages = sum_ages/5

    #Print the results
    print(average_ages)

# Line which calls the above function
average_age()
