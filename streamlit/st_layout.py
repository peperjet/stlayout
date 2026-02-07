import streamlit as st
import time
st.set_page_config(layout="wide")


st.title('streamlit 앱의 와이드 레이아웃 예제')

with st.expander('이 앱에 대하여'):
    st.write('이 예제는 Streamlit 앱에서 와이드 레이아웃을 설정하는 방법을 보여줍니다.')
    st.image('data/streamlit-mark-color.png', width=200)

st.sidebar.header('입력')
user_name = st.sidebar.text_input('당신의 이름은 무엇인가요?')
user_emoji = st.sidebar.selectbox('이모티콘 선택', ['None', '😀', '🚀', '🌟', '🐍'])
user_food = st.sidebar.selectbox('좋아하는 음식은?', ['', '피자', '초밥', '햄버거', '샐러드'])  

st.header('출력')
# st 레이아웃 구성
col1, col2, col3 = st.columns(3)

with col1:
    if user_name:
       st.write(f'안녕하세요, {user_name}님!')
    else:
        st.write('이름을 입력해주세요.')

with col2:
    if user_emoji != '':
        st.write(f'{user_emoji}는 당신이 좋아하는 **이모티콘**입니다!')
    else:
        st.write('이모티콘을 선택해주세요.')

with col3:
    if user_food != '':
        st.write(f'당신이 좋아하는 음식은 **{user_food}**입니다!')
    else:
        st.write('좋아하는 음식을 선택해주세요.')


st.title('st.progress')

with st.expander('진행률 표시줄 예제- 이 앱에 대하여'):
    st.write('이 예제는 Streamlit 앱에서 진행률 표시줄을 사용하는 방법을 보여줍니다.')
progress_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    progress_bar.progress(percent_complete + 1) 
st.balloons()


st.title('st.form')

# 'with' 표기법을 사용한 예시
st.header('1. with 표기법을 사용한 예제')
st.subheader('커피 머신')

with st.form('my_form'):
    st.subheader('커피 주문하기')

    # 입력위젯
    coffee_type = st.selectbox('커피콩 선택', ['아라비카', '로부스타', '리베리카'])
    coffee_roast_val = st.selectbox('커피로스팅', ['라이트', '미디엄', '다크'])
    brewing_val = st.selectbox('추출방식', ['에스프레소', '드립', '프렌치프레스']) 
    serving_type = st.radio('서빙 방식', ['따뜻하게', '차갑게(아이스)'])
    milk_val = st.checkbox('우유정도', ['없음', '약간', '보통', '많이'])
    owncup_val = st.checkbox('개인컵 사용')

    # 제출버튼
    submit_button = st.form_submit_button(label='주문하기')

# st.title('st.form')
    if submit_button:
        st.markdown(f'''
            ☕주문하신 내용
            - 커피콩: `{coffee_type}`
            - 로스팅: `{coffee_roast_val}`
            - 추출방식: `{brewing_val}`
            - 서빙방식: `{serving_type}`
            - 우유정도: `{milk_val}`
            - 개인컵 사용: `{owncup_val}`
            ''')
    else:
        st.write('주문하세요 !')
    
# 객체 표기법을 사용한 짧은 예시
st.header('2. 객체 표기법을 사용한 짧은 예제')

form = st.form(key='my_form_2')
selected_val = form.slider('값 선택')
form.form_submit_button('제출하기')

st.write('선택된 값: ', selected_val)
