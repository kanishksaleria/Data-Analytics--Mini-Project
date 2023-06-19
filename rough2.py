import csv
import os.path

def enter_report():
    student_id = input("Enter your User ID: ")
    week = int(input("Enter week number: "))
    report = input("Enter report: ")

    csv_file_path = "Data/Students_report.csv"

    # Check if the file exists, if not, write the column headers
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["User ID", "Week", "Report"])

    # Append the report to the CSV file
    with open(csv_file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, week, report])

    print("Report entered successfully!")


print("Welcome to the Weekly Report System")

while True:
    print("\nMenu:")
    print("1. Enter Report")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        enter_report()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Weekly Report System!")
