#include <iostream>
#include <iomanip>

using namespace std;

// Function to display menu and get user choice
int displayMenu() {
    cout << "---------------------------" << endl;
    cout << "           MENU            " << endl;
    cout << "---------------------------" << endl;
    cout << "1. Cash\n2. Withdraw\n3. Deposit\n4. Exit" << endl;
    cout << "---------------------------" << endl;

    int choice;
    cout << "Enter your choice: ";
    cin >> choice;
    return choice;
}

int main() {
    int balance = 1000; // Starting balance

    // Set console background color to black
    system("color 0");

    while (true) {
        system("cls"); // Clear console screen

        int choice = displayMenu();

        switch (choice) {
            case 1: // Cash
                cout << "Your current balance: $" << balance << endl;
                break;

            case 2: // Withdraw
                int withdrawAmount;
                cout << "Enter the amount to withdraw: $";
                cin >> withdrawAmount;

                if (withdrawAmount > balance) {
                    cout << "Insufficient funds!" << endl;
                } else {
                    balance -= withdrawAmount;
                    cout << "Withdrawal successful. Your new balance: $" << balance << endl;
                }
                break;

            case 3: // Deposit
                int depositAmount;
                cout << "Enter the amount to deposit: $";
                cin >> depositAmount;

                balance += depositAmount;
                cout << "Deposit successful. Your new balance: $" << balance << endl;
                break;

            case 4: // Exit
                cout << "Exiting program. Goodbye!" << endl;
                return 0;

            default:
                cout << "Invalid choice. Please try again." << endl;
        }

        // Wait for user to press Enter before clearing the screen
        cout << "\nPress Enter to continue...";
        cin.ignore(); // Ignore previous newline character
        cin.get();    // Wait for Enter key press
    }

    return 0;
}
