import streamlit as st
from api_calling import code_debugger
from PIL import Image

st.title('AI Code Debugger App', anchor=None)
st.divider()


# sidebar section
with st.sidebar:
 
  
  # image section
  images = st.file_uploader('Upload your photo here', accept_multiple_files=True, type=('jpg', 'jpeg', 'png'))
  
  pil_images = []
  
  for i in images:
    pil_img = Image.open(i)
    pil_images.append(pil_img)
  

  if images:
    if(len(images) > 3):
      st.error("Please upload a maximum of 3 images.")
    else:
      st.subheader("Uploaded Images:")
      
      cols = st.columns(len(images))
      
      for i, img in enumerate(images):
        with cols[i]:
          st.image(img)
          
        
  
  # selection section
  options = st.selectbox('Select an option', ('Hints', 'Solution with code'), index=None)
  
  
  button = st.button('Debug Code')
  
if button:
  if not images:
    st.error('Please upload at least one image before clicking the button.')
  if not options:
    st.error('Please select an option before clicking the button.')
      
    
  if images and options:
      
    with st.container(border=True):
      st.subheader(f'Generating {options}...')
      
      with st.spinner('Processing...'):
        result = code_debugger(pil_images, options)
        st.markdown(result)