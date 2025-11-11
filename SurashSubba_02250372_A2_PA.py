
def linear_search():
    while True:
        
        print( )
        print("Use This")
        print("02250371 02250372 02250373 02250374 02250375 02250376 02250377 02250378 02250379 02250380 02250381 02250382 02250383 02250384 02250385 02250386 02250387 02250388 02250389 02250390")
        print( )
        try:
            student_ids = list(map(int, input("Enter student IDs separated by space: ").split()))
            break  # valid input, exit loop
        except ValueError:
            print("Error: Only numbers are allowed. Please try again.")

    #split() break it into seperate strings
                                            #map means :Apply the int() function to every element in numbers

    while True:
        try:
            target_id = int(input("Enter the Student ID you want to search: "))
            break
        except ValueError:
            print("Error: Only numbers are allowed. Please try again.")


    print("Student IDs:", student_ids)
    print("Search for:,", target_id)


    for i in range(0,len(student_ids)):
        if (student_ids[i] == target_id):
            return f"Student ID {target_id} Found At Position {i+1}"
    return "Student ID not Found"
   
#print(linear_search())
 
def binarysearch():

    print( )
    print("Use This")
    print("18.5 15.0 19.5 17.0 16.5 14.0 20.0 13.5 18.0 16.0 19.0 15.5 17.5 14.5 12.0 19.7 18.2 16.8 15.2 17.8")
    print( )
    

    while True:
        try:
            test_scores = list(map(float, input("Enter test scores separated by space: ").split()))
            break
        except ValueError:
            print("Error: Only numbers (integers or decimals) are allowed. Please try again.")

    while True:
        try:
            target_score = float(input("Enter the test score you want to search: "))
            break
        except ValueError:
            print("Error: Only numbers(integer or decimal) are allowed. Please try again.")

    # Binary search requires a sorted list
    test_scores.sort()
    print("Sorted scores:", test_scores)
    print("Search for:", target_score)

    low = 0
    high = len(test_scores) - 1


    while low <= high:
        mid = (low + high) // 2

        if test_scores[mid] == target_score:
            return f"Score {target_score} found at position {mid + 1} "

        elif test_scores[mid] < target_score:
            low = mid + 1
        else:
            high = mid - 1

    return f"Score {target_score} not found"

#print(binarysearch())

def display_menu():
    while True:
        print("\n=== Searching Algorithms Menu ===")
        print("Select a search operation (1-3):")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Exit program")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            print("Result:", linear_search())

        elif choice == 2:
            print("Result:", binarysearch())

        elif choice == 3:
            print("Thank you for using the search program!")
            break

        else:
            print("Error: Please select a number between 1 and 3.")
            continue

        # Ask if user wants to perform another search
        again = input("Would you like to perform another search? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the search program!")
            break

# Run the menu
if __name__ == "__main__":
    display_menu()