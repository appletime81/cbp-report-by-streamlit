import streamlit as st
import requests
import pandas as pd
import numpy as np


def intro():
    import streamlit as st

    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


def showing_billmaster_data():
    BillDatas = requests.get(
        "http://localhost:8000/api/v1/getBillMaster&BillDetail/all"
    ).json()

    for BillData in BillDatas:
        BillDetailList = BillData["BillDetail"]
        dict_data = dict([(k, []) for k, v in BillDetailList[0].items()])
        for BillDetail in BillDetailList:
            for k, v in BillDetail.items():
                dict_data[k].append(v)
        df = pd.DataFrame(dict_data)

        expander = st.expander(f"{BillData['BillMaster']['BillingNo']}")
        # set expander width
        expander.dataframe(df)


page_names_to_funcs = {
    "—": intro,
    "BillMaster": showing_billmaster_data,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
