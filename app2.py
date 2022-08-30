import streamlit as st
import sqlite3
import pandas as pd

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pwd):
    cur.executesda(f"SELECT * FROM users WHERE id='{id}' and pw='{pwd}'")
    return cur.fetchone()



menu = st.sidebar.selectbox('Menu',options=['회원가입','로그인','회원목록','정보수정'])

if menu =='회원가입':
    # 회원가입 아이디, 비밀번호, 비밀번호 확인, 나이, 성별, 전화번호
    with st.form('my_form', clear_on_submit=True):
        id = st.text_input('아이디')
        pw = st.text_input('비밀번호')
        pw_ck = st.text_input('비밀번호 확인')




        name = st.text_input('이름')

        col1,col2,col3 = st.columns(3)
        with col1:
            age = st.text_input('나이')
        with col2:
            gender = st.radio('성별을 선택해주세요.', ['남','녀'] , horizontal=True)
        number = st.text_input('전화번호')
        register = st.form_submit_button('회원가입.')

        if register:
            if pw == pw_ck:
             cur.execute(f"INSERT INTO users(id, pw, name, age, gender, number)"
                         f"VALUES("
                         f"'{id}', '{pw}', '{name}', {age}, '{gender}', '{number}')")
             con.commit()
             st.success('회원가입이 완료되었습니다')
            else:
                st.warning('비밀번호를 확인해주세요')




if menu =='로그인':
    log_id =st.sidebar.text_input('아이디')
    log_pw = st.sidebar.text_input('비밀번호', type='password')
    log_btn = st.sidebar.button('로그인')
    if log_btn:
        user_info = login_user(log_id, log_pw)

        if user_info:
            st.subheader(user_info[2]+ '님 환영합니다')
            st.sidebar.image('./img/'+user_info[0]+'.jpeg')
        else:
            st.subheader('다시 로그인하세요')

if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql("SELECT name, age, gender FROM users", con)
    st.dataframe(df, 400, 400)


if menu == '정보수정':
    st.subheader('정보수정')