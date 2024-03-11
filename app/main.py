import streamlit as st
import requests
import json


def getstate():
    try:
        code_input = st.text_input('code to state')
        if code_input:
            url = "http://data-service-clusterip.default.svc.cluster.local/codes"
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                result = data.get(code_input.upper())
                if result is not None:
                    st.success(result)
                else:
                    st.error("State not found")
            else:
                st.error(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


def getcode():
    try:
        state_input = st.text_input('state to code')
        if state_input:
            url = "http://data-service-clusterip.default.svc.cluster.local/states"
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                result = data.get(state_input.lower())
                if result is not None:
                    st.success(result)
                else:
                    st.error("code not found")
            else:
                st.error(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


def main():
    st.title("Simple Front")
    getstate()
    getcode()


if __name__ == '__main__':
    main()