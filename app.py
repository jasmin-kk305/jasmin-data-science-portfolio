import random
from datetime import datetime
import streamlit as st


# ==============================
# MOBILE RECHARGE CLASS
# ==============================

class MobileRecharge:

    def __init__(self, customer_name, mobile_number):

        self.customer_name = customer_name
        self.mobile_number = mobile_number

        self.plans = {
            1: {
                "name": "Basic Plan",
                "price": 199,
                "data": "1.5 GB/day",
                "validity": "28 days"
            },

            2: {
                "name": "Standard Plan",
                "price": 299,
                "data": "2 GB/day",
                "validity": "28 days"
            },

            3: {
                "name": "Premium Plan",
                "price": 499,
                "data": "3 GB/day",
                "validity": "56 days"
            }
        }

        self.history = []


    # ==============================
    # MOBILE NUMBER VALIDATION
    # ==============================

    def validate_number(self):

        return (
            len(self.mobile_number) == 10
            and self.mobile_number.isdigit()
            and self.mobile_number[0] in "6789"
        )


    # ==============================
    # DISPLAY RECHARGE PLANS
    # ==============================

    def display_plans(self):

        return self.plans


    # ==============================
    # PAYMENT METHOD
    # ==============================

    def payment_method(self, payment_choice):

        payment_methods = {
            "UPI": "UPI",
            "Debit Card": "Debit Card",
            "Credit Card": "Credit Card",
            "Net Banking": "Net Banking"
        }

        return payment_methods.get(payment_choice)


    # ==============================
    # GENERATE TRANSACTION ID
    # ==============================

    def generate_transaction_id(self):

        return "TXN" + str(random.randint(100000, 999999))


    # ==============================
    # RECHARGE
    # ==============================

    def recharge(self, choice, payment):

        if choice not in self.plans:
            return None

        plan = self.plans[choice]

        payment_method = self.payment_method(payment)

        if payment_method is None:
            return None

        transaction_id = self.generate_transaction_id()

        date_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        recharge_details = {

            "Transaction ID": transaction_id,

            "Customer": self.customer_name,

            "Mobile Number": self.mobile_number,

            "Plan": plan["name"],

            "Amount": plan["price"],

            "Data": plan["data"],

            "Validity": plan["validity"],

            "Payment": payment_method,

            "Date & Time": date_time,

            "Status": "Successful"
        }

        self.history.append(recharge_details)

        return recharge_details


    # ==============================
    # RECHARGE HISTORY
    # ==============================

    def recharge_history(self):

        return self.history


# ==================================================
# STREAMLIT APPLICATION
# ==================================================

st.set_page_config(
    page_title="Mobile Recharge System",
    page_icon="📱",
    layout="wide"
)


# ==============================
# TITLE
# ==============================

st.title("📱 Mobile Recharge System")

st.write(
    "A Python OOP based Mobile Recharge System"
)


# ==================================================
# SESSION STATE
# ==================================================

if "recharge" not in st.session_state:
    st.session_state.recharge = None


if "history" not in st.session_state:
    st.session_state.history = []


# ==================================================
# CUSTOMER DETAILS
# ==================================================

st.sidebar.header("👤 Customer Details")

customer_name = st.sidebar.text_input(
    "Enter Customer Name"
)

mobile_number = st.sidebar.text_input(
    "Enter Mobile Number",
    max_chars=10
)


# ==================================================
# CREATE OBJECT
# ==================================================

if customer_name and mobile_number:

    recharge_object = MobileRecharge(
        customer_name,
        mobile_number
    )

    st.session_state.recharge = recharge_object


# ==================================================
# CHECK MOBILE NUMBER
# ==================================================

if st.session_state.recharge:

    recharge = st.session_state.recharge

    if recharge.validate_number():

        st.sidebar.success(
            "✓ Valid Mobile Number"
        )

    else:

        st.sidebar.error(
            "Invalid Mobile Number"
        )

        st.info(
            "Please enter a valid 10-digit mobile number starting with 6, 7, 8 or 9."
        )

        st.stop()


# ==================================================
# MAIN MENU
# ==================================================

if st.session_state.recharge:

    recharge = st.session_state.recharge

    menu = st.sidebar.radio(
        "Select Option",
        [
            "🏠 Home",
            "📋 Recharge Plans",
            "💳 Recharge",
            "📜 Recharge History"
        ]
    )


    # ==================================================
    # HOME
    # ==================================================

    if menu == "🏠 Home":

        st.header(
            f"Welcome, {recharge.customer_name}! 👋"
        )

        st.write(
            f"Mobile Number: **{recharge.mobile_number}**"
        )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Recharge Plans",
                len(recharge.plans)
            )

        with col2:

            st.metric(
                "Payment Methods",
                4
            )

        with col3:

            st.metric(
                "Total Recharges",
                len(st.session_state.history)
            )


    # ==================================================
    # RECHARGE PLANS
    # ==================================================

    elif menu == "📋 Recharge Plans":

        st.header("📋 Available Recharge Plans")

        plans = recharge.display_plans()

        col1, col2, col3 = st.columns(3)

        for column, (key, plan) in zip(
            [col1, col2, col3],
            plans.items()
        ):

            with column:

                st.subheader(
                    plan["name"]
                )

                st.write(
                    f"### ₹{plan['price']}"
                )

                st.write(
                    f"📶 Data: {plan['data']}"
                )

                st.write(
                    f"📅 Validity: {plan['validity']}"
                )


    # ==================================================
    # RECHARGE
    # ==================================================

    elif menu == "💳 Recharge":

        st.header("💳 Mobile Recharge")

        plans = recharge.display_plans()

        plan_names = [
            plan["name"]
            for plan in plans.values()
        ]

        selected_plan = st.selectbox(
            "Select Recharge Plan",
            plan_names
        )

        selected_plan_id = None

        for key, plan in plans.items():

            if plan["name"] == selected_plan:

                selected_plan_id = key
                selected_plan_details = plan


        st.info(
            f"Price: ₹{selected_plan_details['price']} | "
            f"Data: {selected_plan_details['data']} | "
            f"Validity: {selected_plan_details['validity']}"
        )


        # Payment Method

        payment = st.selectbox(
            "Select Payment Method",
            [
                "UPI",
                "Debit Card",
                "Credit Card",
                "Net Banking"
            ]
        )


        # Recharge button

        if st.button(
            "🔄 Recharge Now",
            use_container_width=True
        ):

            transaction = recharge.recharge(
                selected_plan_id,
                payment
            )

            if transaction:

                # Store history in session
                st.session_state.history.append(
                    transaction
                )

                st.success(
                    "🎉 Recharge Successful!"
                )

                st.divider()

                st.subheader(
                    "📄 Recharge Details"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Customer Name:** "
                        f"{transaction['Customer']}"
                    )

                    st.write(
                        f"**Mobile Number:** "
                        f"{transaction['Mobile Number']}"
                    )

                    st.write(
                        f"**Plan:** "
                        f"{transaction['Plan']}"
                    )

                    st.write(
                        f"**Amount:** "
                        f"₹{transaction['Amount']}"
                    )

                    st.write(
                        f"**Data:** "
                        f"{transaction['Data']}"
                    )

                with col2:

                    st.write(
                        f"**Validity:** "
                        f"{transaction['Validity']}"
                    )

                    st.write(
                        f"**Payment:** "
                        f"{transaction['Payment']}"
                    )

                    st.write(
                        f"**Transaction ID:** "
                        f"{transaction['Transaction ID']}"
                    )

                    st.write(
                        f"**Date & Time:** "
                        f"{transaction['Date & Time']}"
                    )

                    st.write(
                        f"**Status:** "
                        f"{transaction['Status']}"
                    )


    # ==================================================
    # RECHARGE HISTORY
    # ==================================================

    elif menu == "📜 Recharge History":

        st.header("📜 Recharge History")

        history = st.session_state.history

        if not history:

            st.info(
                "No recharge history available."
            )

        else:

            st.write(
                f"Total Recharges: **{len(history)}**"
            )

            st.divider()

            for index, transaction in enumerate(
                history,
                start=1
            ):

                with st.expander(
                    f"Recharge {index} - "
                    f"{transaction['Transaction ID']}"
                ):

                    col1, col2 = st.columns(2)

                    with col1:

                        st.write(
                            f"**Customer:** "
                            f"{transaction['Customer']}"
                        )

                        st.write(
                            f"**Mobile:** "
                            f"{transaction['Mobile Number']}"
                        )

                        st.write(
                            f"**Plan:** "
                            f"{transaction['Plan']}"
                        )

                        st.write(
                            f"**Amount:** "
                            f"₹{transaction['Amount']}"
                        )

                        st.write(
                            f"**Data:** "
                            f"{transaction['Data']}"
                        )

                    with col2:

                        st.write(
                            f"**Validity:** "
                            f"{transaction['Validity']}"
                        )

                        st.write(
                            f"**Payment:** "
                            f"{transaction['Payment']}"
                        )

                        st.write(
                            f"**Transaction ID:** "
                            f"{transaction['Transaction ID']}"
                        )

                        st.write(
                            f"**Date & Time:** "
                            f"{transaction['Date & Time']}"
                        )

                        st.success(
                            transaction["Status"]
                        )


# ==================================================
# NO CUSTOMER DETAILS
# ==================================================

else:

    st.info(
        "👈 Enter customer name and mobile number "
        "from the sidebar to start."
    )