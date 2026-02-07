import streamlit as st
import pandas as pd
from datetime import time
import numpy as np
import altair as alt

# 예제1
st.header('st.wrtite')
st.write('Hello, *World!* :sunglasses:')

# 예제2
st.write(1234)

# 예제3
df = pd.DataFrame({
    '첫 번째 열': [1, 2, 3, 4],
    '두 번째 열': [10, 20, 30, 40]
})
st.write(df)

# 예제4
st.write('아래는 DataFrame입니다.', df, '위는 DataFrame입니다.')



# 변수 전달, 그래프 표시
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)



# Streamlit 응용 1: 입력 -> 출력
st.title("Streamlit 응용 1: 입력 -> 출력")

name = st.text_input("이름 입력")
age = st.number_input("나이", min_value=0, max_value=120, step=1)

if st.button("확인"):
    st.success(f"{name}님은 {age}세 입니다.")



# 범위 슬라이더
st.subheader('시간 범위 슬라이더')

appintment = st.slider(
    "약속을 예약하세요:",
    value=(time(11, 30), time(12, 45)))

st.write("예약된 시간:", appintment)
