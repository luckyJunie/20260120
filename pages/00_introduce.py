import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="My Minimal Portfolio", page_icon="✨", layout="centered")

# 2. 미니멀리스트 커스텀 CSS (흑백 + 파랑 + 노랑)
st.markdown("""
    <style>
    /* 전체 배경 및 텍스트 색상 */
    .main {
        background-color: #ffffff;
        color: #1a1a1a;
    }
    
    /* 헤더 스타일링 */
    h1 {
        color: #1a1a1a;
        border-bottom: 3px solid #0056b3; /* 파란색 포인트 */
        padding-bottom: 10px;
    }
    
    h2 {
        color: #333333;
    }

    /* 하이라이트 텍스트 */
    .highlight {
        background-color: #fff3cd; /* 노란색 포인트 */
        padding: 2px 5px;
        border-radius: 3px;
        font-weight: bold;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: #0056b3;
        color: white;
        border-radius: 5px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 레이아웃 구성
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # 프로필 이미지 (URL이나 로컬 경로 사용 가능)
    # 직접 사진을 넣으시려면 'profile.jpg' 등으로 파일명을 바꾸어 주세요.
    st.image("https://via.placeholder.com/200/000000/FFFFFF?text=PROFILE", width=180)

with col2:
    st.title("안녕하세요, 홍길동입니다.")
    st.write("""
    ### "단순함이 궁극의 정교함이다."
    저는 복잡한 문제를 <span class="highlight">심플한 코드</span>로 해결하는 것을 즐기는 개발자입니다.
    데이터와 사용자 경험 사이의 접점을 찾는 일을 하고 있습니다.
    """, unsafe_allow_html=True)

st.divider()

# 4. 상세 섹션
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🟦 What I Do")
    st.markdown("""
    * **Frontend:** React, Streamlit
    * **Backend:** Python, FastAPI
    * **Design:** Minimalist UI/UX
    """)

with col_right:
    st.subheader("🟨 Experience")
    st.info("**2024 - 현재** | 프리랜서 개발자")
    st.info("**2022 - 2023** | OO 테크 스타트업 근무")

# 5. 하단 컨택트 섹션
st.divider()
st.write("📫 **Contact me:** email@example.com")

if st.button("응원 메시지 보내기"):
    st.balloons()
    st.success("응원해주셔서 감사합니다!")
