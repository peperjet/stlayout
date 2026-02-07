import streamlit as st
import pandas as pd
import numpy as np
from datetime import time, datetime


# 예제1. 슬라이더
st.header('st.slider 예제') 

age = st.slider('당신의 나이는?', 0, 130, 25) # 각각 최소값, 최대값 및 기본값 
st.write("당신의 나이는 ", age, '입니다.')


# 예제2. 범위 슬라이더
st.subheader('범위 슬라이더 예제')

values = st.slider(
    '값의 범위를 선택하세요',
    0.0, 100.0, (25.0, 75.0))
st.write('값 ', values)


# 예제3. 시간 범위 슬라이더
st.subheader('시간 범위 슬라이더')

appointment = st.slider(
    "약속을 예약하세요:",
    value=(time(11, 30), time(12, 45)))
st.write("예약된 시간:", appointment)


# 예제4. 날짜 범위 슬라이더
st.subheader('날짜 범위 슬라이더')

start_time = st.slider(
    "언제 시작하시겠습니까?",
    value=datetime(2024, 1, 1, 9, 30),
    format="YYYY/MM/DD - HH:mm")
st.write("시작 시간:", start_time)



# 라인차트
st.subheader('라인차트 예제')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# 셀렉트박스
st.subheader('셀렉트박스 예제')

option = st.selectbox(
    '어떤 숫자를 좋아하세요?',
    ('파랑', '초록', '빨강'))

st.write('당신이 좋아하는 색은 ', option, '입니다.')



# 멀티셀렉트박스
st.subheader('멀티셀렉트박스 예제')
options = st.multiselect(
    '좋아하는 색을 선택하세요',
    ['파랑', '초록', '빨강', '노랑', '검정', '흰색'],
    ['파랑', '빨강'])

st.write('당신이 좋아하는 색은:', options)


# 체크박스
st.subheader('체크박스 예제')
st.write('주문하고 싶은 것이 무엇인가요?')
icecream = st.checkbox('아이스크림')
coffee = st.checkbox('커피')
cola = st.checkbox('콜라')

if icecream:
    st.write('아이스크림을 선택하셨습니다.')
if coffee:
    st.write('커피를 선택하셨습니다.')
if cola:
    st.write('콜라를 선택하셨습니다.')  


# LaTex 수식 
st.latex(r"E = mc^2")

# 분수
st.latex(r"\frac{a}{b}")
# 제곱과 아래첨자
st.latex(r"x^2 + y_1")
# 합, 적분
st.latex(r"\sum_{i=1}^{n} i^2")
st.latex(r"\int_0^1 x^2 dx")
# 여러 줄 수식
st.latex(r"""
\begin{aligned}
y &= ax + b \\
z &= x^2
\end{aligned}
""")
# 항상 r"" 사용

# 수학 방정식 표시 st.latex()
# 기본 방정식
st.latex(r"E = mc^2")

# 2차 방정식
st.latex(r"ax^2 + bx + c = 0")
# 근의 공식 (자주자주 나옴)
st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
# 합, 적분
st.latex(r"\sum_{i=1}^{n} i^2")
st.latex(r"\int_0^1 x^2 dx")


