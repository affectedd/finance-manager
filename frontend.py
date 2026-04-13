import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Finance Manager", layout="wide")
st.title("💰 My Finance Manager")

try:
    categories = requests.get(f"{BASE_URL}/categories/").json()
    transactions = requests.get(f"{BASE_URL}/transactions/").json()
except:
    st.error("Error with connection to Backend! Make sure that FastAPI is running")
    st.stop()

col1, col2 = st.columns([1, 2])


with col1:
    st.header("📂 Categories")

    with st.form("add_category"):
        new_cat_name = st.text_input("New Category Name")
        if st.form_submit_button("Add"):
            if new_cat_name:
                response = requests.post(f"{BASE_URL}/categories/", json={"name": new_cat_name})
                st.rerun()
            else:
                st.warning("Enter the Title")

    st.subheader("Existing Categories")
    for cat in categories:
        c_cols = st.columns([3, 1])
        c_cols[0].write(f"{cat['name']} (ID: {cat['id']})")
        if c_cols[1].button("🗑️", key=f"del_cat_{cat['id']}"):
            requests.delete(f"{BASE_URL}/categories/{cat['id']}")
            st.rerun()

with col2:
    st.header("💸 Transactions")

    with st.form("add_transaction"):
        t_col1, t_col2 = st.columns(2)
        title = t_col1.text_input("Title")
        amount = t_col2.number_input("Amount", min_value=0.0)
        desc = st.text_input("Description")

        cat_options = {cat['name']: cat['id'] for cat in categories}
        selected_cat_name = st.selectbox("Category", options=list(cat_options.keys()))

        if st.form_submit_button("Save Expense"):
            data = {
                "title": title,
                "amount": amount,
                "description": desc,
                "category_id": cat_options[selected_cat_name]
            }
            requests.post(f"{BASE_URL}/transactions/", json=data)
            st.rerun()

    st.subheader("Expenses History")

    h_cols = st.columns([2, 1, 2, 2, 1])
    h_cols[0].write("**Title**")
    h_cols[1].write("**Sum**")
    h_cols[2].write("**Category**")
    h_cols[3].write("**Date**")
    h_cols[4].write("**Action**")
    st.divider()

    cat_lookup = {c['id']: c['name'] for c in categories}

    for t in transactions:
        t_cols = st.columns([2, 1, 2, 2, 1])
        t_cols[0].write(t['title'])
        t_cols[1].write(f"{t['amount']}")
        t_cols[2].write(cat_lookup.get(t['category_id'], "Unknown"))
        t_cols[3].write(t['created_at'][:10])

        if t_cols[4].button("🗑️", key=f"del_t_{t['id']}"):
            requests.delete(f"{BASE_URL}/transactions/{t['id']}")
            st.rerun()