import streamlit as st
import time

st.title('streamlitの基礎')
st.write('hello world')

col1, col2 = st.columns(2)


with col1:
    st.write('列1がここに表示されます')

with col2:
    st.write('列2がここに表示されます')
    
st.sidebar.write('hello world')
st.text_input("ここに文字が入力できます")

slider_text = st.slider('スライダーで数字を決定できます',0,100,50)
"スライダーの数字：",slider_text

st.button('ボタン')

x = st.empty()
bar = st.progress(0)

for i in range(100):
    time.sleep(0.001)
    x.text(i)
    bar.progress(i)
    i += 1
    
st.selectbox("選んでください", ['選択肢1', '選択肢2', '選択肢3'])

output_text = 'この文字がダウンロードされます'

st.download_button(label='記事内容 Download',
                   data= output_text,
                   file_name='out_put.text',
                   mime='text/plan',
                   )

file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください", type=["png", "jpg"])

if(file_upload != None):
    st.image(file_upload)
    

import numpy as np
import pandas as pd

def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.rand(r, c),
        columns=('col %d' %i for i in range(c)))
    return df

datafreme = rand_df(r=10, c=3)


st.dataframe(datafreme.head(n=3))

st.line_chart(datafreme)