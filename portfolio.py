import streamlit as st

st.title("Welcome to my portfolio")
st.header("About Me")
st.write("""
     Hello! I am Sharini S, a first year ECE student at KGisl institute of technology.\n
     I am eager to learn about both hardware and software application.\n
     I have a passion to work as assistant engineer.
     """)
v1 = st.radio("Colours",["r","g","b"],index=1)
v2 = st.selectbox("Colours",["r","g","b"],index=1)     

st.header("Education")
st.write("""
       *KGisl institue of technology*,Bachelor of engineering in Electronics and communication engineering
       """) 

st.header("Skills")
st.write("""
       Programming languages known:Python\n
       Web development:HTML,CSS\n
       Others:VS code""")   

st.header("contact") 
st.write("for any further details contact me through email")
st.write("Email: sha.123@gmail.com")        



import streamlit as st
import time

st.title("Hello Streamlit")
st.header("Header")
st.subheader("Sub Header")
st.text("Like this!")
st.markdown(""" 
# h1 tag             
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:
** bold **
_ italic _
""", unsafe_allow_html=True)
st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^(n-1) = ''')


a = [1,2,3,4,5,6]
dictionary = {
    "name":["hari","siva"],
    "age":[21,32],
    "city":["Coimbatore","Trichy"]
}
st.dataframe(dictionary, width=500, height=500)
st.table(dictionary)
st.json(dictionary)
st.write(dictionary)

 
if 'content' not in st.session_state:
    st.session_state['content'] = 0
def show_stuff1():
    st.session_state['content']=1

def show_stuff2():
    st.session_state['content']=2
    
def show_stuff3():
    st.session_state['content']=3

name = st.text_input(label="Enter your name")
if name:
    st.write(f"Hello {name}")
st.button(label="show stuff 1",on_click=show_stuff1)
st.button(label="show stuff 2",on_click=show_stuff2)
st.button(label="show stuff 3",on_click=show_stuff3)

if st.session_state['content']==1:
    st.write(1)
elif st.session_state['content'] == 2:
    st.write(2)
elif st.session_state['content'] == 3:
    st.write(3)

x=st.slider('x')
st.write(x)


@st.cache_data
def ret(a):
    time.sleep(3)
    return time.time()


if st.checkbox("1"):
    st.write(ret(1))
if st.checkbox("2"):
    st.write(ret(2))


st.line_chart(dictionary)
st.area_chart(dictionary)
st.bar_chart(dictionary)

city = {
    'awesome cities':['Chicago','Minneapolis','Louisville'],
    'lat':[41.868171,44.979840,38.257972],
    'lon':[-57.667458,-93.272474,-95.702548]
}
st.map(city)


if st.button("Click this"):
    st.write("Done you clicked")
name = st.text_input("You name")
st.write(name)
address = st.text_area("Your address")
st.write(address)
st.date_input("Date:")
st.time_input("Time:")
if st.checkbox("You like this class?"): 
    st.write("Thankyou")
if st.checkbox("You like this college?",value=True): 
    st.write("Good")



v1 = st.radio("Colours",["r","g","b"],index=1)
v2 = st.selectbox("Colours",["r","g","b"],index=1)
st.write(v1,v2)
v3 = st.multiselect("Colours",["r","g","b"])
st.write(v3)
st.slider("Age", min_value=18, max_value=25, step=2)
st.number_input("Numbers")
st.number_input("Numbers", min_value=1, max_value=10, value=5, step=2)
filee = st.file_uploader("Upload a file!")
#st.image(filee)

st.session_state['selection']=st.sidebar.selectbox(label="pick one",options=["first","second","third"])
if 'selection' in st.session_state:
    st.write(st.session_state['selection'])
read = st.sidebar.radio("Navigation",["Home","About us"])
if read == "About us":
    st.write("Hellooo im mitun!")
if read == "Home":
    st.write("5pm")

if 'counter' not in st.session_state:
    st.session_state.counter = 0
def inc():
    st.session_state.counter += 1
st.button("Inc", on_click=inc)
st.write("Counter",st.session_state.counter)

with st.form("my_forms"):
    first,last = st.columns(2)
    first.text_input("First name")
    last.text_input("Last name")
    email, mob = st.columns([3, 2])
    email.text_input("Email:")
    mob.text_input("Number:")

    user, pw, pw2 = st.columns(3)
    user.text_input("User name")
    pw.text_input("Password", type="password")
    pw2.text_input("Retype pass", type="password")

    ch, bl, sub = st.columns(3)
    ch.checkbox("I agree")

    submitted = sub.form_submit_button("Submit")

if submitted:
    st.write("Form submitted!")