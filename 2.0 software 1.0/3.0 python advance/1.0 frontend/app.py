import streamlit as st
# # st.title("Welcome to my Gen Ai")
# # print("run")
# # pressed=st.button("click me")
# # print(pressed)


# # from profile import markdown_code
# # st.image("bg-card-front.png", caption="Roberta's profile", use_container_width=True) 
# # uploaded_image=st.file_uploader("upload  your profile picture", type=["png","jpg","jpeg"])
# # if uploaded_image:
# #     st.image(uploaded_image, caption="uploaded image", use_container_width=False)

# # st.title("My GenAi frontend journey")
# # st.header("I specialized pre training")
# # st.subheader("happy to get started")
# # st.markdown(markdown_code)

# #forms
# import streamlit as st
# st.write("please fill out the form below")

# #creating the form container
# with st.form(key="registration_form"):
#     st.sidebar.subheader("personal information")
#     user_name=st.sidebar.text_input(label="Enter your username")
#     email=st.sidebar.text_input(label="Enter Email")
#     password=st.text_input(label="Enter pasword", type="password")
#     st.subheader("preferences")
#     fav_color=st.selectbox("what is your favorite color?",["red", "green", "orange"])
#     agree_to_terms=st.checkbox("i agree to terms and conditions")
#     submitted=st.form_submit_button(label="Submit")
#     temperature=st.sidebar.select_slider("select temp range",[20, 2, 80])
#     if submitted:
#         if not user_name:
#             st.error("username required")
#         elif not email:
#             st.error("email required")
#         elif not agree_to_terms:
#             st.error("Agree to terms and conditions") 
#         else:
#             st.success("registration successful")   
#             st.write("Here are your details")
#             st.write(f"**user name:**{user_name}")  
#             st.write(f"** email:** {email}") 
#             st.write(f"**favourite:**{fav_color}") 
#             st.balloons()


import time
progress = st.progress(0)

for i in range(100):
    time.sleep(0.02) #simulate computation
    progress.progress(i +1)
   
st.success("Generation complete")  
#creating tabs (st.tabs)
# seperate content into modules without navigating.
tab1, tab2 =st.tabs(["prompt","output"])
with tab1:
    st.text_area("enter your prompt")
with tab2:
    st.write("Generated results appear here")  

    #creating columns(st.columns)
#placing elements side by side
col1, col2 = st.columns(2)
with col1:
    st.text_input("enter prompt")
with col2:
    st.write("Ai results goes here")
#containers(st.container)
# Group related elements and allow for dynamic updates inside the group
container=st.container()
container.write("Generated Text here")
btn=container.button("submit text")
#___________________________________________________________________________ 
# 5. expander(st.expander)
# #hide/show details on demand  - useful for advanced settings or explanations
with st.expander("Advanced options"):
    st.slider("Max Tokens Options")
    st.checkbox("Stream Output")
    #_____________________________________
    # Empty(st.empty)
    #reserve space a space fot content that updates later (e.g, dynamic result areas)
placeholder=st.empty()

if st.button("Generated"):
    placeholder.write("Generating....")
    #simulate generation
    placeholder.write("Done! Here's the result")
    #________________________________________
    #combine layouts for GenAI App
st.title("GenAi prompt generator")
#side bar settings
st.sidebar.title("settings")
temp=st.sidebar.slider("Creativity (temperature)",0.0, 1.0, 0.7) 
##tabs
tab1, tab2 = st.tabs(["prompt","output"]) 
with tab1:
    prompt=st.text_area("Enter your prompt")
#with tab2:
    st.write("**AI Output:**")
    if st.button("Generate"):
        st.success(f"Response from model (temp={temp}) for : {prompt}")

 




                                           
