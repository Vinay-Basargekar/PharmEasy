import streamlit as st
import pandas as pd
from PIL import Image
#from drug_db import *
import random

## SQL DATABASE CODE
import sqlite3
import pdfkit

conn = sqlite3.connect("drug_data.db",check_same_thread=False)
c = conn.cursor()

def cust_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Customers(
                    C_Name VARCHAR(50) NOT NULL,
                    C_Password VARCHAR(50) NOT NULL,
                    C_Email VARCHAR(50) PRIMARY KEY NOT NULL, 
                    C_State VARCHAR(50) NOT NULL,
                    C_Number VARCHAR(50) NOT NULL 
                    )''')
    print('Customer Table create Successfully')

def customer_add_data(Cname,Cpass, Cemail, Cstate,Cnumber):
    c.execute('''INSERT INTO Customers (C_Name,C_Password,C_Email, C_State, C_Number) VALUES(?,?,?,?,?)''', (Cname,Cpass,  Cemail, Cstate,Cnumber))
    conn.commit()

def customer_view_all_data():
    c.execute('SELECT * FROM Customers')
    customer_data = c.fetchall()
    return customer_data
def customer_update(Cemail,Cnumber):
    c.execute(''' UPDATE Customers SET C_Number = ? WHERE C_Email = ?''', (Cnumber,Cemail,))
    conn.commit()
    print("Updating")
def customer_delete(Cemail):
    c.execute(''' DELETE FROM Customers WHERE C_Email = ?''', (Cemail,))
    conn.commit()

def drug_update(Duse, Did):
    c.execute(''' UPDATE Drugs SET D_Use = ? WHERE D_id = ?''', (Duse,Did))
    conn.commit()
def drug_delete(Did):
    c.execute(''' DELETE FROM Drugs WHERE D_id = ?''', (Did,))
    conn.commit()

def drug_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Drugs(
                D_Name VARCHAR(50) NOT NULL,
                D_ExpDate DATE NOT NULL, 
                D_Use VARCHAR(50) NOT NULL,
                D_Qty INT NOT NULL, 
                D_id INT PRIMARY KEY NOT NULL)
                ''')
    print('DRUG Table create Successfully')

def drug_add_data(Dname, Dexpdate, Duse, Dqty, Did):
    c.execute('''INSERT INTO Drugs (D_Name, D_Expdate, D_Use, D_Qty, D_id) VALUES(?,?,?,?,?)''', (Dname, Dexpdate, Duse, Dqty, Did))
    conn.commit()

def drug_view_all_data():
    c.execute('SELECT * FROM Drugs')
    drug_data = c.fetchall()
    return drug_data

def order_create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS Orders(
                O_Name VARCHAR(100) NOT NULL,
                O_Items VARCHAR(100) NOT NULL,
                O_Qty VARCHAR(100) NOT NULL,
                O_id VARCHAR(100) PRIMARY KEY NOT NULL)
    ''')

def order_delete(Oid):
    c.execute(''' DELETE FROM Orders WHERE O_id = ?''', (Oid,))

def order_add_data(O_Name,O_Items,O_Qty,O_id):
    c.execute('''INSERT INTO Orders (O_Name, O_Items,O_Qty, O_id) VALUES(?,?,?,?)''',
               (O_Name,O_Items,O_Qty,O_id))
    conn.commit()


def order_view_data(customername):
    c.execute('SELECT * FROM ORDERS Where O_Name == ?',(customername,))
    order_data = c.fetchall()
    return order_data

def order_view_all_data():
    c.execute('SELECT * FROM ORDERS')
    order_all_data = c.fetchall()
    return order_all_data






#__________________________________________________________________________________



def admin():


    st.title("Pharmacy Database Dashboard")
    menu = ["Drugs", "Customers", "Orders", "About"]
    choice = st.sidebar.selectbox("Menu", menu)



    ## DRUGS
    if choice == "Drugs":

        st.subheader("Manage Drugs")
        menu = ["Add", "View", "Update", "Delete"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":

            st.subheader("Add Drugs")

            col1, col2 = st.columns(2)

            with col1:
                drug_name = st.text_area("Enter the Drug Name")
                drug_expiry = st.date_input("Expiry Date of Drug (YYYY-MM-DD)")
                drug_mainuse = st.text_area("When to Use")
            with col2:
                drug_quantity = st.text_area("Enter the quantity")
                drug_id = st.text_area("Enter the Drug id (example:#D1)")

            if st.button("Add Drug"):
                drug_add_data(drug_name,drug_expiry,drug_mainuse,drug_quantity,drug_id)
                st.success("Successfully Added Data")
        if choice == "View":
            st.subheader("Drug Details")
            drug_result = drug_view_all_data()
            #st.write(drug_result)
            with st.expander("View All Drug Data"):
                drug_clean_df = pd.DataFrame(drug_result, columns=["Name", "Expiry Date", "Use", "Quantity", "ID"])
                st.dataframe(drug_clean_df)
            with st.expander("View Drug Quantity"):
                drug_name_quantity_df = drug_clean_df[['Name','Quantity']]
                #drug_name_quantity_df = drug_name_quantity_df.reset_index()
                st.dataframe(drug_name_quantity_df)
        if choice == 'Update':
            st.subheader("Update Drug Details")
            d_id = st.text_area("Drug ID")
            d_use = st.text_area("Drug Use")
            if st.button(label='Update'):
                drug_update(d_use,d_id)

        if choice == 'Delete':
            st.subheader("Delete Drugs")
            did = st.text_area("Drug ID")
            if st.button(label="Delete"):
                drug_delete(did)



    ## CUSTOMERS
    elif choice == "Customers":

        menu = ["View", "Update", "Delete"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "View":
            st.subheader("Customer Details")
            cust_result = customer_view_all_data()
            #st.write(cust_result)
            with st.expander("View All Customer Data"):
                cust_clean_df = pd.DataFrame(cust_result, columns=["Name", "Password","Email-ID" ,"Area", "Number"])
                st.dataframe(cust_clean_df)

        if choice == 'Update':
            st.subheader("Update Customer Details")
            cust_email = st.text_area("Email")
            cust_number = st.text_area("Phone Number")
            if st.button(label='Update'):
                customer_update(cust_email,cust_number)

        if choice == 'Delete':
            st.subheader("Delete Customer")
            cust_email = st.text_area("Email")
            if st.button(label="Delete"):
                customer_delete(cust_email)

    elif choice == "Orders":
        menu = ["View"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "View":
            st.subheader("Order Details")
            order_result = order_view_all_data()

            with st.expander("View All Order Data", expanded=True):
                order_clean_df = pd.DataFrame(order_result, columns=["Name", "Items", "Qty", "ID"])
                st.dataframe(order_clean_df.style.set_properties(**{'font-size': '16px'}))  # Larger font size inside the expander

        # Display order details outside the expander as well
        st.subheader("Order Details (Expanded)")
        st.dataframe(order_clean_df.style.set_properties(**{'font-size': '16px'}))  # Larger font size

    elif choice == "About":
        st.subheader("Final Year Project")


def getauthenicate(username, password):
    #print("Auth")
    c.execute('SELECT C_Password FROM Customers WHERE C_Name = ?', (username,))
    cust_password = c.fetchall()
    #print(cust_password[0][0], "Outside password")
    #print(password, "Parameter password")
    if cust_password[0][0] == password:
        #print("Inside password")
        return True
    else:
        return False


###################################################################

def customer(username, password):
    if getauthenicate(username, password):
        
        # Add custom CSS for the customer dashboard
        st.markdown("""
            <style>
            .drug-card {
                background-color: #f9f9f9;
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                transition: transform 0.3s;
            }
            .drug-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }
            .drug-title {
                color: #2E7D32;
                font-size: 24px;
                margin-bottom: 10px;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 5px;
            }
            .drug-price {
                background-color: #4CAF50;
                color: white;
                padding: 5px 10px;
                border-radius: 20px;
                font-weight: bold;
                display: inline-block;
                margin: 10px 0;
            }
            .usage-info {
                background-color: #E3F2FD;
                padding: 10px;
                border-left: 4px solid #2196F3;
                border-radius: 5px;
                margin: 10px 0;
            }
            .welcome-header {
                background-color: #A594F9;
                color: white;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
                text-align: center;
            }
            .order-header {
                background-color: #A594F9;
                color: white;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
            }
            .buy-button {
                background-color: #FF5722;
                color: white;
                padding: 10px 15px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                width: 100%;
            }
            </style>
        """, unsafe_allow_html=True)
        
        # Welcome header with user information
        st.markdown(f"""
            <div class="welcome-header">
                <h1>Welcome to PharmEasy, {username}!</h1>
                <p>Your trusted online pharmacy for all medical needs</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Order details section with improved styling
        st.markdown("""
            <div class="order-header">
                <h2>Your Order History</h2>
                <p>View and download your previous orders</p>
            </div>
        """, unsafe_allow_html=True)
        
        order_result = order_view_data(username)
        
        if order_result:
            with st.expander("View All Order Data", expanded=False):
                order_clean_df = pd.DataFrame(order_result, columns=["Name", "Items", "Qty", "ID"])
                st.dataframe(order_clean_df.style.set_properties(**{'background-color': '#E3F2FD', 'color': 'black', 'border': '1px solid #B3E5FC'}))
                
                # Convert DataFrame to HTML
                order_html = order_clean_df.to_html()
                
                # Convert HTML to PDF and save it
                try:
                    pdfkit.from_string(order_html, 'order.pdf')
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.download_button(
                            label="📄 Download Order History (PDF)", 
                            data=open('order.pdf', 'rb').read(), 
                            file_name=f'{username}_orders.pdf', 
                            mime='application/pdf',
                            key="download_pdf"
                        )
                except Exception as e:
                    st.warning(f"PDF generation issue: {e}")
        else:
            st.info("You haven't placed any orders yet. Browse our products below!")
        
        # Drug catalog section
        st.markdown("""
            <div class="order-header" style="background-color: #FF5722;">
                <h2>Our Products</h2>
                <p>Browse our selection of pharmaceutical products</p>
            </div>
        """, unsafe_allow_html=True)
        
        drug_result = drug_view_all_data()
        
        # Create a variable to track items in cart
        cart_items = 0
        cart_total = 0
        
        # Create three columns for the three drugs
        col1, col2, col3 = st.columns(3)
        
        # First drug card
        with col1:
            st.markdown(f"""
                <div class="drug-card">
                    <h3 class="drug-title">{drug_result[0][0]}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            img = Image.open('images/dolo650.jpg')
            st.image(img, use_column_width=True)
            
            st.markdown('<p class="drug-price">Rs. 15/-</p>', unsafe_allow_html=True)
            
            dolo650 = st.slider(label="Quantity", min_value=0, max_value=5, key=1)
            if dolo650 > 0:
                cart_items += dolo650
                cart_total += dolo650 * 15
                
            st.markdown(f"""
                <div class="usage-info">
                    <strong>When to USE:</strong> {str(drug_result[0][2])}
                </div>
            """, unsafe_allow_html=True)
        
        # Second drug card
        with col2:
            st.markdown(f"""
                <div class="drug-card">
                    <h3 class="drug-title">{drug_result[1][0]}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            img = Image.open('images/strepsils.JPG')
            st.image(img, use_column_width=True)
            
            st.markdown('<p class="drug-price">Rs. 10/-</p>', unsafe_allow_html=True)
            
            strepsils = st.slider(label="Quantity", min_value=0, max_value=5, key=2)
            if strepsils > 0:
                cart_items += strepsils
                cart_total += strepsils * 10
                
            st.markdown(f"""
                <div class="usage-info">
                    <strong>When to USE:</strong> {str(drug_result[1][2])}
                </div>
            """, unsafe_allow_html=True)
        
        # Third drug card
        with col3:
            st.markdown(f"""
                <div class="drug-card">
                    <h3 class="drug-title">{drug_result[2][0]}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            img = Image.open('images/vicks.JPG')
            st.image(img, use_column_width=True)
            
            st.markdown('<p class="drug-price">Rs. 65/-</p>', unsafe_allow_html=True)
            
            vicks = st.slider(label="Quantity", min_value=0, max_value=5, key=3)
            if vicks > 0:
                cart_items += vicks
                cart_total += vicks * 65
                
            st.markdown(f"""
                <div class="usage-info">
                    <strong>When to USE:</strong> {str(drug_result[2][2])}
                </div>
            """, unsafe_allow_html=True)
        
        # Cart summary
        st.markdown("""
            <div style="background-color: #F5F5F5; padding: 15px; border-radius: 10px; margin: 20px 0; text-align: center;">
                <h3>Shopping Cart Summary</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Items in Cart", f"{cart_items}")
        with col2:
            st.metric("Total Amount", f"₹{cart_total}")
        with col3:
            delivery_time = "24-48 hours"
            st.metric("Estimated Delivery", delivery_time)
        
        # Buy now button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            buy_button = st.button("🛒 Complete Purchase", key="buy_button", use_container_width=True)
        
        if buy_button:
            O_items = ""
            
            if int(dolo650) > 0:
                O_items += "Dolo-650,"
            if int(strepsils) > 0:
                O_items += "Strepsils,"
            if int(vicks) > 0:
                O_items += "Vicks"
                
            O_Qty = str(dolo650)+str(',') + str(strepsils) + str(",") + str(vicks)
            
            O_id = username + "#O" + str(random.randint(0,1000000))
            order_add_data(username, O_items, O_Qty, O_id)
            
            # Show success message and confetti
            st.success("Your order has been placed successfully!")
            st.balloons()
            st.info("You can track your order in the 'Your Order History' section.")
    else:
        st.error("Authentication failed. Please check your username and password.")

if __name__ == '__main__':
    drug_create_table()
    cust_create_table()
    order_create_table()
    
    st.set_page_config(
        page_title="PharmEasy - Your Online Pharmacy",
        page_icon="💊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    menu = ["Login", "SignUp","Admin"]
    choice = st.sidebar.selectbox("Menu", menu)   
    if choice == "Login":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox(label="Login"):
            customer(username, password)
    
    elif choice == "SignUp":
        st.subheader("Create New Account")
        cust_name = st.text_input("Name")
        cust_password = st.text_input("Password", type='password', key=1000)
        cust_password1 = st.text_input("Confirm Password", type='password', key=1001)
        col1, col2, col3 = st.columns(3)

        with col1:
            cust_email = st.text_area("Email ID", placeholder="Enter your email")
        with col2:
            cust_area = st.text_area("State", placeholder="Enter your state")
        with col3:
            cust_number = st.text_area("Phone Number", placeholder="Enter your phone number")

        if st.button("Signup"):
            if (cust_password == cust_password1):
                customer_add_data(cust_name,cust_password,cust_email, cust_area, cust_number,)
                st.success("Account Created Successfully!")
                st.info("Go to the Login Menu to log in")
            else:
                st.warning('Passwords do not match. Please try again.')
    elif choice == "Admin":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        # if st.sidebar.button("Login"):
        if username == 'admin' and password == 'admin':
            admin()
