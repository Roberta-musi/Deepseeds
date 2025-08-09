import streamlit as st
# # if "count" not in st.session_state:
# #     st.session_state.count=0
# # #count=0
# # if st.button("increment"):
# #     st.session_state.count +=1 # each time we increment streamlit reruns the code, it doesn't keep record of the state and session
# # st.write(f"count:{st.session_state.count}") 
# if "step" not in st.session_state:
#     st.session_state.step=1
# if "info" not in st.session_state:
#     st.session_state.info={}
# def move_to_next(name,email, more_info):
#     st.session_state.step=2
#     st.session_state.info["name"]=name
#     st.session_state.info["email"]=email
#     st.session_state.info["more_info"]=more_info
# def move_to_prev():
#       st.session_state.step=1


# if st.session_state.step==1:
#     st.header("Please Enter your info")
#     st.write("trying to be nice")
#     name=st.text_input("Enter your user_name",value=st.session_state.info.get("name", ""))   
#     email=st.text_input("Enter your email", value=st.session_state.info.get("email", ""))
#     more_info=st.text_area("Tell us more about yourself", value=st.session_state.info.get("more_info", ""))
#     st.button("Next page", on_click=move_to_next, args=(name, email, more_info))
#     # if next:
#     #     st.session_state.step=2
#     #     st.session_state.info["name"]=name
#     #     st.session_state.info["email"]=email
#     #     st.session_state.info["more_info"]=more_info
# elif st.session_state.step==2:
#      st.title("Confirm your information")
#      st.write(f"Your information is:{st.session_state.info["name"]}")
#      st.write(f"Your email is:{st.session_state.info["email"]}")
#      st.write(f"your more info is:{st.session_state.info["more_info"]}")
#      check_box=st.checkbox("Confirm info")
#      if check_box:
#          st.balloons()
     
#      st.button("prev",on_click=move_to_prev)
#         #  if prev:
#         #      st.session_state.step=1
import time
def expensive_search():
    query=st.session_state.query
    time.sleep(2)#simulate  heavy work
    st.session_state.results=f"Results for'{query}'" 
st.text_input("Search for something",key="query")
st.button("Run search", on_click=expensive_search)
if "results" in st.session_state:
    st.write(st.session_state.results)

             

