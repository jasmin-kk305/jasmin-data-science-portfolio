import random
from datetime import datetime


class MobileRecharge:

    def __init__(self, customer_name, mobile_number):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.recharge_history = []

    # Validate mobile number
    def validate_mobile(self):
        if (len(self.mobile_number) == 10 and
                self.mobile_number.isdigit() and
                self.mobile_number[0] in "6789"):
            return True
        return False

    # Display recharge plans
    def display_plans(self):
        print("\n========== RECHARGE PLANS ==========")
        print("1. Basic Plan")
        print("   Price    : ₹199")
        print("   Data     : 1.5 GB/day")
        print("   Validity : 28 Days")

        print("\n2. Standard Plan")
        print("   Price    : ₹299")
        print("   Data     : 2 GB/day")
        print("   Validity : 28 Days")

        print("\n3. Premium Plan")
        print("   Price    : ₹499")
        print("   Data     : 3 GB/day")
        print("   Validity : 56 Days")

    # Select recharge plan
    def select_plan(self, choice):

        plans = {
            1: {
                "name": "Basic Plan",
                "price": 199,
                "data": "1.5 GB/day",
                "validity": "28 Days"
            },
            2: {
                "name": "Standard Plan",
                "price": 299,
                "data": "2 GB/day",
                "validity": "28 Days"
            },
            3: {
                "name": "Premium Plan",
                "price": 499,
                "data": "3 GB/day",
                "validity": "56 Days"
            }
        }

        return plans.get(choice)

    # Perform recharge
    def recharge(self, plan):

        transaction_id = "TXN" + str(random.randint(10000, 99999))
        date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        transaction = {
            "transaction_id": transaction_id,
            "plan": plan["name"],
            "price": plan["price"],
            "data": plan["data"],
            "validity": plan["validity"],
            "date_time": date_time
        }

        self.recharge_history.append(transaction)

        print("\n========== RECHARGE SUCCESSFUL ==========")
        print("Customer Name :", self.customer_name)
        print("Mobile Number :", self.mobile_number)
        print("Plan          :", plan["name"])
        print("Price         : ₹", plan["price"])
        print("Data          :", plan["data"])
        print("Validity      :", plan["validity"])
        print("Transaction ID:", transaction_id)
        print("Date & Time   :", date_time)

    # Display recharge history
    def display_history(self):

        if not self.recharge_history:
            print("\nNo recharge history found.")
            return

        print("\n========== RECHARGE HISTORY ==========")

        for transaction in self.recharge_history:
            print("Transaction ID :", transaction["transaction_id"])
            print("Plan           :", transaction["plan"])
            print("Price          : ₹", transaction["price"])
            print("Data           :", transaction["data"])
            print("Validity       :", transaction["validity"])
            print("Date & Time    :", transaction["date_time"])
            print("--------------------------------------")


# ================= MAIN PROGRAM =================

print("======================================")
print("       MOBILE RECHARGE SYSTEM")
print("======================================")

customer_name = input("Enter customer name: ")
mobile_number = input("Enter mobile number: ")

customer = MobileRecharge(customer_name, mobile_number)

# Validate mobile number
if not customer.validate_mobile():
    print("\nInvalid mobile number!")
    print("Please enter a valid 10-digit mobile number.")
else:

    while True:

        print("\n========== MENU ==========")
        print("1. View Recharge Plans")
        print("2. Recharge")
        print("3. Recharge History")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.display_plans()

        elif choice == 2:

            customer.display_plans()

            plan_choice = int(input("\nSelect a plan (1-3): "))

            plan = customer.select_plan(plan_choice)

            if plan:
                customer.recharge(plan)
            else:
                print("\nInvalid plan selection!")

        elif choice == 3:
            customer.display_history()

        elif choice == 4:
            print("\nThank you for using Mobile Recharge System!")
            break

        else:
            print("\nInvalid choice! Please try again.")