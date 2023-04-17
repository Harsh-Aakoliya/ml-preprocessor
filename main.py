from datainput import DataInput

class Preprocessor:

    impute = None
    standardization = None
    normalization = None
    categorical = None
    data = 0

    def __init__(self, filepath):
        self.data = DataInput().inputFunction(filepath)

    def printData(self):
        print(self.data)

    def main(self):
        while(1):
            print("Welcome to ML Pre-Processor")
            print("---------TASKS---------------")
            print('1. Data Description')
            print('2. Handling NULL Values')
            print('3. Encoding Categorical Data')
            print('4. Feature Scaling of the Dataset')

            try:
                choice = int(input("Enter the choice of operation: "))
            except ValueError:
                print("Invalid Input! Please enter an integer")
                continue
            break

        if choice == -1:
            print("Thank you for using the app!")
            exit()
        elif choice == 1:
            print()
        elif choice == 2:
            print()
        elif choice == 3:
            print()
        elif choice == 4:
            print()
        elif choice == 5:
            print()
        else:
            print("Try Again! No such operation exists")

obj = Preprocessor()
obj.main()
        