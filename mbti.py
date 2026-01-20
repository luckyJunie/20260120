import streamlit as st

# 1. 페이지 설정 (아이콘과 레이아웃)
st.set_page_config(page_title="나의 꿈 판타지 MBTI", page_icon="🔮", layout="centered")

# 2. 화려한 네온 스타일 CSS
st.markdown("""
    <style>
    /* 전체 배경 그라데이션 */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* 제목 애니메이션 효과 */
    @keyframes glow {
        from { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #e60073; }
        to { text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6; }
    }
    
    .main-title {
        font-size: 55px;
        font-weight: bold;
        text-align: center;
        color: white;
        animation: glow 1s ease-in-out infinite alternate;
        margin-bottom: 30px;
    }

    /* 결과 카드 디자인 */
    .result-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 30px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        text-align: center;
    }

    /* 드롭다운 박스 스타일 */
    .stSelectbox div[data-baseweb="select"] {
        background-color: white !important;
        border-radius: 15px !important;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background: linear-gradient(45deg, #ff00cc, #3333ff);
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 50px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 0, 204, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 메인 화면 구성
st.markdown('<h1 class="main-title">🔮 미래 직업 포탈 🔮</h1>', unsafe_allow_html=True)
st.write("<h3 style='text-align: center;'>신비로운 기운이 당신의 천직을 안내합니다... ✨</h3>", unsafe_allow_html=True)
st.write("")

# 4. MBTI 데이터 (16가지 모두 수록)
mbti_db = {
    "ENFP": {"job": "🎨 크리에이티브 디렉터, 유튜버, 여행 작가", "desc": "무궁무진한 영감의 소유자!", "emoji": "🧚"},
    "ENTP": {"job": "💡 스타트업 창업가, 변호사, 평론가", "desc": "지치지 않는 아이디어 뱅크!", "emoji": "🚀"},
    "INTJ": {"job": "🧠 인공지능 전문가, 전략가, 과학자", "desc": "미래를 내다보는 체스 플레이어!", "emoji": "🔭"},
    "INFJ": {"job": "📜 상담사, 심리학자, 소설가", "desc": "사람의 영혼을 울리는 통찰가!", "emoji": "🌊"},
    "ISTP": {"job": "🔧 카레이서, 보안 전문가, 엔지니어", "desc": "차분하게 문제를 해결하는 기술자!", "emoji": "🏍️"},
    "ISFP": {"job": "🎨 예술가, 뷰티 디렉터, 작곡가", "desc": "현재를 즐기는 감각적인 예술가!", "emoji": "🎨"},
    "INFP": {"job": "✍️ 시인, 정신건강 상담사, 일러스트레이터", "desc": "세상을 아름답게 보는 중재자!", "emoji": "🍀"},
    "INTP": {"job": "💻 소프트웨어 아키텍트, 철학자, 연구원", "desc": "논리로 세상을 분석하는 천재!", "emoji": "🧬"},
    "ESTP": {"job": "🏎️ 사업가, 경찰관, 마케팅 실무자", "desc": "몸으로 부딪히는 실전파 에너자이저!", "emoji": "🔥"},
    "ESFP": {"job": "🎤 연예인, 승무원, 파티 플래너", "desc": "모두를 행복하게 만드는 축제 주인공!", "emoji": "✨"},
    "ENFJ": {"job": "📢 사회운동가, 교육자, PR 전문가", "desc": "사람들을 이끄는 따뜻한 리더!", "emoji": "☀️"},
    "ENTJ": {"job": "👑 CEO, 정치인, 경영 컨설턴트", "desc": "목표를 향해 거침없이 나가는 지휘관!", "emoji": "🏆"},
    "ESTJ": {"job": "📊 프로젝트 매니저, 판사, 감사관", "desc": "체계와 질서를 세우는 현실 관리자!", "emoji": "📐"},
    "ESFJ": {"job": "🤝 호텔리어, 간호사, 커뮤니티 매니저", "desc": "타인을 챙기는 다정한 협동가!", "emoji": "🎁"},
    "ISTJ": {"job": "📝 회계사, 공무원, 사서", "desc": "세상의 질서를 유지하는 원칙주의자!", "emoji": "📜"},
    "ISFJ": {"job": "🏥 초등교사, 사서, 사회복지사", "desc": "묵묵히 자리를 지키는 수호천사!", "emoji": "🛡️"}
}

# 5. 선택창
selected = st.selectbox("✨ 당신의 MBTI를 선택해 보세요:", list(mbti_db.keys()))

st.write("") # 간격 조절

# 6. 결과 확인 버튼
if st.button("🌟 직업의 문 열기 🌟"):
    st.balloons() # 축하 풍선
    
    res = mbti_db[selected]
    
    # 결과 표시 레이아웃
    st.markdown(f"""
        <div class="result-card">
            <h1 style='font-size: 80px; margin: 0;'>{res['emoji']}</h1>
            <h2 style='color: #ffde59; margin-top: 10px;'>{selected}</h2>
            <p style='font-size: 22px; font-style: italic;'>"{res['desc']}"</p>
            <hr style='border: 1px solid rgba(255,255,255,0.2);'>
            <h3 style='color: white;'>💎 추천 드리는 길 💎</h3>
            <p style='font-size: 28px; font-weight: bold; color: #00ffcc;'>{res['job']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.warning(f"💡 {selected} 유형의 당신은 정말 특별해요! 이 직업들이 당신의 잠재력을 깨워줄 거예요.")

# 7. 푸터
st.markdown("<br><br><p style='text-align: center; font-size: 14px; opacity: 0.7;'>Designed for Future Leaders 🌠</p>", unsafe_allow_html=True)
