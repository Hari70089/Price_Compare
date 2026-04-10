import serpapi
import streamlit as st
import pandas as pd
import matplotlib.pylab as plt

def compare(med_name):  
    params = {
        "engine": "google_shopping",
        "q": med_name,
        "api_key": "0be8218c3c29f22cc5644d81dfe820bfd5a4d6d73c03594e4535427b7ece7ff9",
        "gl": "in",
    }
    search = serpapi.GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["shopping_results"]
    return shopping_results


c1, c2 = st.columns(2)
c1.image("e_pharm_logo.png", width=200)
c2.header("E pherma Price Comparison Tool")


#--------------------------------------------------#
st.sidebar.title("Enter the product name")
med_name = st.sidebar.text_input("Product Name:-")
number = st.sidebar.text_input("Enter Quantity:-")
medecine_comp=[]
med_price=[]

if med_name is not None:
    if st.sidebar.button("Compare"):
        shooping_results = compare(med_name)

        lowest_price = float(shooping_results[0].get("price")[1:])
        print(lowest_price)
        lowest_price_index = 0
        st.sidebar.image(shooping_results[1].get("thumbnail"))

        for i in range(int(number)):
            current_price  = float(shooping_results[i].get("price")[1:])
            medecine_comp.append(shooping_results[i].get("source"))
            med_price.append( float(shooping_results[i].get("price")[1:]))
#-----------------------------------------------------------------------------------------#
            st.title(f"Option {i+1}") 

            c1, c2 = st.columns(2)
            c1.write("Company Name:-")
            c2.write(shooping_results[i].get("source"))

            c1.write("Title:-")
            c2.write(shooping_results[i].get("title"))

            c1.write("Price:-")
            c2.write(shooping_results[i].get("price"))

            url = shooping_results[i].get("product_link")
            c1.write("Buy Link:-")
            c2.write("[Link](%s)" % url)

            if current_price<lowest_price:
                lowest_price = current_price
                lowest_price_index = i

        # This is best Option
        st.title("Best Option") 
    
        c1, c2 = st.columns(2)
        c1.write("Company Name:-")
        c2.write(shooping_results[lowest_price_index].get("source"))

        c1.write("Title:-")
        c2.write(shooping_results[lowest_price_index].get("title"))

        c1.write("Price:-")
        c2.write(shooping_results[lowest_price_index].get("price"))

        url = shooping_results[lowest_price_index].get("product_link")
        c1.write("Buy Link:-")
        c2.write("[Link](%s)" % url)

        #---------------------------
        #graph comparision

        df=pd.DataFrame(med_price,medecine_comp)
        st.title("Chart Comaprison:-")
        st.bar_chart(df)

        fig,ax=plt.subplots()
        ax.pie(med_price,labels=medecine_comp,shadow=True)
        ax.axis("equal")
        st.pyplot(fig)
