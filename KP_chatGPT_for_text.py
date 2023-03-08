#----------------------------------- import labrary
import easyocr
import PIL
from PIL import ImageDraw
import requests
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
#--------------------------------for side bar section 

#st.set_page_config(page_title="EXTRACT TEXT FROM IMAGE GPT (KP MODEL)", page_icon=":sunglasses:", layout="centered", initial_sidebar_state="expanded")
st.title("""EXTRACT TEXT FROM IMAGE GPT \n (KP MODEL)""")
reader= pickle.load(open("text_extract.pkl", "rb"))

#--------------------------------------------

st.markdown("""  
<style>
.css-1rs6os.edgvbvh3
{
    visibility: hidden;
}
</style>""",unsafe_allow_html=True)
#following code is used to remove "made with streamlit" 
st.markdown("""
<style>
.css-1lsmgbg.egzxvld0
{
    visibility: hidden;
 } 
</style>""", unsafe_allow_html=True)
#--------------------------------
def lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lote_1 = lottie("https://assets4.lottiefiles.com/packages/lf20_4kmUDEKo63.json")
#st.markdown(f"<h5 style='text-align: center;'>Please Upload Your File Below</h5>",unsafe_allow_html=True)
st_lottie(lote_1)
st.sidebar.markdown(f"<h3 style='text-align: center;'>KP CHAT GPT</h3>",unsafe_allow_html=True)
st.sidebar.markdown("This is KP CHAT GPT you can use for Extract Text From Images. It will Automatically Extract Text from your images")
st.sidebar.markdown(f"<h3 style='text-align: center;'>Instructions</h3>",unsafe_allow_html=True)
st.sidebar.markdown("1. Please make sure your file must be in jpg, png format")
from io import StringIO
data = st.file_uploader("Upload Image",type=["png","jpg"])
#print(data.name)
if data:
    print(data.name)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h3 style='text-align: center;'>You Want To See Your Image</h3>",unsafe_allow_html=True)
        bu= st.checkbox("See The Image", key="disabled")
        but_1 = st.button("Submit", key="kund")
        if bu and but_1:
            im = PIL.Image.open(data)
            st.image(im)
    with col2:
        st.markdown(f"<h3 style='text-align: center;'>You Want To See Your Image Text</h3>",unsafe_allow_html=True)
        bu_3= st.checkbox("See Your Text")
        but_4 = st.button("Submit")
        if bu_3 and but_4:
            text = reader.readtext(data.name, contrast_ths=0.05, adjust_contrast=0.7, add_margin=0.45, width_ths=0.7, decoder='beamsearch')
            for i in text:
                st.write(i[1])
