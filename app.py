import streamlit as st
import matplotlib.pyplot as plt

st.title("💸 Money Expenses Tracker")

months = []
expenses = []

st.subheader("📆 Enter Monthly Expense Data")

num_months = st.number_input("Number of months to track:", min_value=1, max_value=12, step=1)

for i in range(num_months):
    col1, col2 = st.columns(2)
    with col1:
        month = st.text_input(f"Month {i+1}", key=f"month_{i}")
    with col2:
        expense = st.number_input(f"Expense for {month or f'Month {i+1}'}", key=f"expense_{i}")
    if month and expense >= 0:
        months.append(month)
        expenses.append(expense)

if st.button("Analyze & Plot") and months and expenses:
    total = sum(expenses)
    avg = total / len(expenses)
    max_expense = max(expenses)
    min_expense = min(expenses)
    max_month = months[expenses.index(max_expense)]
    min_month = months[expenses.index(min_expense)]

    st.subheader("📊 Analysis")
    st.write(f"**Total Expense:** ₹{total}")
    st.write(f"**Average Expense:** ₹{avg:.2f}")
    st.write(f"**Highest Expense:** ₹{max_expense} in {max_month}")
    st.write(f"**Lowest Expense:** ₹{min_expense} in {min_month}")

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(months, expenses, marker='o', linestyle='-', color='blue')
    ax.set_title("Monthly Expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Expense (₹)")
    ax.grid(True)
    st.pyplot(fig)
