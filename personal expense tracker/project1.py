import streamlit as st


st.title("💸 Personal Expense Tracker")
st.caption("Track your daily expenses — no database needed!")


if 'expenses' not in st.session_state:
    st.session_state.expenses = []


with st.form("expense_form"):
    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Amount (₹)", min_value=1, step=1)
    with col2:
        category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
    description = st.text_input("Description (optional)")
    submitted = st.form_submit_button("➕ Add Expense")
    
    if submitted:
        st.session_state.expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        st.success("Expense added!")



st.markdown("---")


st.subheader("📊 Expense Summary")
selected = st.multiselect("Filter by category", options=["Food", "Transport", "Shopping", "Bills", "Other"])


filtered = [e for e in st.session_state.expenses if not selected or e["category"] in selected]

if not filtered:
    st.warning("No expenses to show.")
else:
    
    total = sum(e["amount"] for e in filtered)
    st.metric(label="Total Spent", value=f"₹{total}")

    
    st.markdown("#### 🧁 Expense Breakdown")
    cat_totals = {}
    for e in filtered:
        cat_totals[e["category"]] = cat_totals.get(e["category"], 0) + e["amount"]

    
    for cat, amt in cat_totals.items():
        percent = int((amt / total) * 100)
        bar = "🟩" * (percent // 5)
        st.markdown(f"**{cat}: ₹{amt} ({percent}%)**  {bar}")

    
    st.markdown("---")
    st.markdown("#### 🧾 Expense Details")
    for i, e in enumerate(filtered):
        st.write(f"{i+1}. ₹{e['amount']} | {e['category']} | {e['description']}")
        

if st.button("🧹 Clear All Data"):
    st.session_state.expenses.clear()
    st.success("All expense records cleared!")

rating = st.slider("Rate this app (1-10)", 1, 10)
st.write("Your rating:", rating)
