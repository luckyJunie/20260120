import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

# 1. 페이지 설정
st.set_page_config(page_title="MBTI 꿈 찾기 탐험대 🚀", page_icon="✨", layout="wide")

# 2. Lottie 로드 함수 (오류 방지 로직 추가)
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# 애니메이션 소스 (우주 테마)
lottie_main = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# 3. 화려한 CSS 스타일링
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Jua', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .stSelectbox [data-baseweb="select"] {
        border-radius: 15px;
        border: 2px solid #FF4B4B;
    }
    
    .mbti-card {
        background-color: white;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border: 2px solid #FF4B4B;
        text-align: center;
        margin-top: 20px;
        animation: fadeIn 1.5s;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. 상단 헤더
st.title("🌈 MBTI 진로 탐색: 나의 꿈을 찾아라! ✨")
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### 안녕하세요, 미래의 주인공 여러분! 👋")
    st.write("여러분의 성격 유형을 선택하면 세상에 하나뿐인 멋진 직업을 추천해 드릴게요!")
    st.info("이 앱은 여러분의 가능성을 응원하기 위해 만들어졌습니다. 💖")

with col2:
    if lottie_main:
        st_lottie(lottie_main, height=200, key="main_ani")
    else:
        st.header("🚀")

st.divider()

# 5. MBTI 데이터베이스 (내용 보강)
mbti_db = {
    "ENFP": {"job": "🎨 크리에이티브 디렉터, 유튜버, 여행작가", "desc": "재기발랄한 활동가! 아이디어가 샘솟는 당신은 창의적인 일이 딱이에요!", "color": "#FFD700"},
    "INTJ": {"job": "🧠 인공지능 전문가, 전략 기획자, 교수", "desc": "용의주도한 전략가! 복잡한 문제를 해결하는 지적인 도전이 어울려요!", "color": "#E6E6FA"},
    "ESFJ": {"job": "🤝 호텔 경영자, 상담사, 초등교사", "desc": "사교적인 외교관! 조화로운 분위기를 만들며 남을 돕는 일에 천재적이에요!", "color": "#FFB6C1"},
    "ISTP": {"job": "🛠️ 엔지니어, 데이터 분석가, 스포츠 선수", "desc": "만능 재주꾼! 도구를 다루거나 상황을 분석하는 냉철한 능력이 대단해요!", "color": "#D3D3D3"},
    "INFP": {"job": "✍️ 작가, 예술 심리 치료사, 작곡가", "desc": "열정적인 중재자! 나만의 가치를 세상에 표현하는 감성적인 직업이 좋아요!", "color": "#E0FFE0"},
    "ENTJ": {"job": "⚖️ CEO, 정치인, 기업 경영 컨설턴트", "desc": "대담한 통솔자! 목표를 향해 나아가며 팀을 이끄는 카리스마가 넘쳐요!", "color": "#FFFACD"}
}

# 6. 사용자 입력 및 결과 출력
st.markdown("### 👇 여러분의 MBTI 유형은 무엇인가요?")
choice = st.selectbox("리스트에서 선택하세요", list(mbti_db.keys()))

if st.button("✨ 내 미래 직업 확인하기 ✨"):
    # 효과음 대신 시각 효과
    st.balloons()
    
    data = mbti_db[choice]
    
    st.markdown(f"""
        <div class="mbti-card">
            <h1 style='color: #FF4B4B;'>{choice}</h1>
            <h3>"{data['desc']}"</h3>
            <hr style='border: 0.5px solid #eee;'>
            <h2 style='color: #1E90FF;'>💎 추천 직업 💎</h2>
            <p style='font-size: 28px; font-weight: bold;'>{data['job']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.success(f"항상 여러분의 꿈을 응원합니다! {choice} 파이팅! 🔥")

# 하단 푸터
st.markdown("---")
st.caption("© 2024 진로 교육 프로젝트 | Streamlit & Github 로 제작됨 ✨")
