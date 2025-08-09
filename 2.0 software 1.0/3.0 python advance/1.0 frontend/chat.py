import streamlit as st
st.set_page_config(page_title="Chat with DEEPSEED", layout="wide")
st.markdown("""
            <style>
              .message_box {
                  padding:15px;
                  margin: 10px;
                  font_size: 16px:
              }
            """, unsafe_allow_html=True)
with st.sidebar:
    st.title("DEEPSEED")
    st.caption("One seed at the time")
    st.write("___________________________________")
    st.markdown("### session stats")
    col1, col2=st.columns(2)
    with col1:

     st.write("Messages: 2")
    with col2:
      st.write("Total: 2")
    st.write("___________________________________")
    st.markdown("### Quick actions")
    st.button("Tell me a Joke")
    st.button("Explain AI")
    st.button("Help Brainstorm")
    st.button("Writing Tips")
    st.button("Book recommendations")
#main area
st.markdown("## Chat with DEEPSEED")
#chat areaa
chat_box=st.container(border=True, height=500)
with chat_box:
 st.markdown("""
        <div class="message_box">
            <span> Welcome to the world of deepseed </span></div>  
        <div class="message_box">
                <span> Based on your message , i can provide some insights on this.</span> </div>
                """, unsafe_allow_html=True)
with st.form(key="chat_form",clear_on_submit=True): 
      user_input=st.text_input("Message DEEPSEED:",label_visibility="collapsed", placeholder="Type your message here...")
      submit_button=st.form_submit_button("Send") 
if submit_button and user_input: 
     st.markdown(f"""
                 <div class="message_box">
                 <strong>You:</strong> {user_input}</div>
                 """, unsafe_allow_html=True)        