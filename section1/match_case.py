#match-case (switch): alt to many elif statement
# cleaner code
# the default case id _

def day_of_week(day):
    match day:
        case 1:
            return "It is Monday"
        case 2:
            return "It is Tuesday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is Saturday"
        case 7:
            return "It is Sunday"
        case _:
            return "Not a valid day"


print(day_of_week(int(input("Enter the day of the week:"))))