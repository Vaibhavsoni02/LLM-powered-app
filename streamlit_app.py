# import streamlit as st
# from langchain.llms import OpenAI

# st.title('🦜🔗 Quickstart App')

# openai_api_key = st.sidebar.text_input('OpenAI API Key')

# def generate_response(input_text):
#   llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#   st.info(llm(input_text))

# with st.form('my_form'):
#   text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
#   submitted = st.form_submit_button('Submit')
#   if not openai_api_key.startswith('sk-'):
#     st.warning('Please enter your OpenAI API key!', icon='⚠')
#   if submitted and openai_api_key.startswith('sk-'):
#     generate_response(text)


# --------------------------------------------------------------------------------------------------------------

# import streamlit as st

# # Title of the app
# st.title("Advanced Calculator App")

# # Initialize state variables
# if 'running_total' not in st.session_state:
#     st.session_state['running_total'] = 0.0
# if 'current_operation' not in st.session_state:
#     st.session_state['current_operation'] = None
# if 'new_entry' not in st.session_state:
#     st.session_state['new_entry'] = True

# # Display running total
# st.write(f"Running Total: {st.session_state['running_total']}")

# # User input
# new_number = st.number_input("Enter a number", value=0.0)
# operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide", "Reset"])

# # Perform calculation
# if st.button("Apply Operation"):
#     if st.session_state['new_entry']:
#         st.session_state['running_total'] = new_number
#         st.session_state['new_entry'] = False
#     else:
#         if st.session_state['current_operation'] == "Add":
#             st.session_state['running_total'] += new_number
#         elif st.session_state['current_operation'] == "Subtract":
#             st.session_state['running_total'] -= new_number
#         elif st.session_state['current_operation'] == "Multiply":
#             st.session_state['running_total'] *= new_number
#         elif st.session_state['current_operation'] == "Divide":
#             if new_number == 0:
#                 st.write("Cannot divide by zero")
#             else:
#                 st.session_state['running_total'] /= new_number
#         elif st.session_state['current_operation'] == "Reset":
#             st.session_state['running_total'] = 0.0
#             st.session_state['new_entry'] = True
    
#     st.session_state['current_operation'] = operation
#     st.write(f"New Running Total: {st.session_state['running_total']}")

# # Reset Calculator
# if st.button("Reset Calculator"):
#     st.session_state['running_total'] = 0.0
#     st.session_state['current_operation'] = None
#     st.session_state['new_entry'] = True
#     st.write("Calculator has been reset")


import streamlit as st

# Title of the app
st.title("Graphical Calculator App")

# Initialize or reset state variables
if 'input_string' not in st.session_state:
    st.session_state['input_string'] = ""
if 'result' not in st.session_state:
    st.session_state['result'] = None

# Display area
st.write(f"Input: {st.session_state['input_string']}")
if st.session_state['result'] is not None:
    st.write(f"Result: {st.session_state['result']}")

# Number buttons
col1, col2, col3 = st.beta_columns(3)
with col1:
    if st.button("1"):
        st.session_state['input_string'] += "1"
with col2:
    if st.button("2"):
        st.session_state['input_string'] += "2"
with col3:
    if st.button("3"):
        st.session_state['input_string'] += "3"

with col1:
    if st.button("4"):
        st.session_state['input_string'] += "4"
with col2:
    if st.button("5"):
        st.session_state['input_string'] += "5"
with col3:
    if st.button("6"):
        st.session_state['input_string'] += "6"

with col1:
    if st.button("7"):
        st.session_state['input_string'] += "7"
with col2:
    if st.button("8"):
        st.session_state['input_string'] += "8"
with col3:
    if st.button("9"):
        st.session_state['input_string'] += "9"

# Operator buttons
with col1:
    if st.button("+"):
        st.session_state['input_string'] += "+"
with col2:
    if st.button("-"):
        st.session_state['input_string'] += "-"
with col3:
    if st.button("*"):
        st.session_state['input_string'] += "*"

with col1:
    if st.button("/"):
        st.session_state['input_string'] += "/"
with col2:
    if st.button("0"):
        st.session_state['input_string'] += "0"
with col3:
    if st.button("C"):
        st.session_state['input_string'] = ""
        st.session_state['result'] = None

# Calculate and Reset buttons
if st.button("Calculate"):
    try:
        st.session_state['result'] = eval(st.session_state['input_string'])
    except ZeroDivisionError:
        st.session_state['result'] = "Cannot divide by zero"
    except Exception as e:
        st.session_state['result'] = "Invalid input"

if st.button("Reset"):
    st.session_state['input_string'] = ""
    st.session_state['result'] = None
