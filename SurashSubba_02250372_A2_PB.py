# === Sorting Functions with Input & Validation Inside ===

def bubble_sort_names():
    student_names = input("Enter student names separated by space: ").split()
    
    print("Original names:", student_names)

    n = len(student_names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_names[j] > student_names[j + 1]:
                student_names[j], student_names[j + 1] = student_names[j + 1], student_names[j]

    print("Performing Bubble Sort...")
    print("Sorted names:", student_names)


def insertion_sort_scores():
    while True:
        try:
            scores = list(map(float, input("Enter test scores separated by space: ").split()))
            break
        except ValueError:
            print("Error: Only numbers are allowed. Please try again.")
    
    print("Original scores:", scores)


    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        while j >= 0 and scores[j] > key:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key

    print("\nPerforming Insertion Sort...")
    print("Sorted scores:", scores)

    #Top 5
    top5 = scores[-5:][::-1]#from back(top) take 5; [-5] and slice and reverse it [:: -1]
    print("\nTop 5 Scores:")
    for idx, score in enumerate(top5, 1):
        print(f"{idx}. {score}")


def quick_sort_prices():
    while True:
        try:
            prices = list(map(float, input("Enter book prices separated by space: ").split()))
            break
        except ValueError:
            print("Error: Only numbers are allowed. Please try again.")

    print("Original prices:", prices)


    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)

    sorted_prices = quick_sort(prices)
    print("Performing Quick Sort...")
    print("Sorted prices:", sorted_prices)

    top5 = sorted_prices[-5:][::-1]
    print("\nTop 5 Prices:")
    for i, price in enumerate(top5, 1):
        print(f"{i}. {price}")


def sorting_menu():
    while True:
        print("\n Sorting Algorithms Menu")
        print("Select a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            bubble_sort_names()
        elif choice == "2":
            insertion_sort_scores()
        elif choice == "3":
            quick_sort_prices()
        elif choice == "4":
            print("Thank you for using the sorting program!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")
            continue

        again = input("\nWould you like to perform another sort? (y/n): ").lower()

        if again != 'y':
            print("Thank you for using the sorting program!")
            break


#runn
if __name__ == "__main__":
    sorting_menu()
