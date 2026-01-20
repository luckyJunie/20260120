import streamlit as st

# 페이지 설정
st.set_page_config(page_title="꿈을 찾는 MBTI 여행", page_icon="🌈", layout="centered")

# --- 화려한 스타일 설정 ---
st.markdown("""
    <style>
    /* 전체 배경색 및 폰트 */
    .main {
        background: linear-gradient(to bottom, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    /* 카드 스타일 */
    .job-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        text-align: center;
        border: 3px solid #ff4b4b;
    }
    /* 제목 스타일 */
    .title-text {
        font-size: 50px;
        font-weight: bold;
        color: #FF4B4B;
        text-shadow: 2px 2px #ffccd5;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 헤더 섹션 ---
st.markdown('<p class="title-text">🌈 MBTI 진로 탐색기 🌈</p>', unsafe_allow_html=True)
st.write("### 여러분의 MBTI를 선택하면 멋진 직업을 추천해드려요! ✨")
st.markdown("---")

# --- MBTI 데이터 ---
mbti_info = {
    "ISTJ": {"job": "🎯 공무원, 회계사, 데이터 분석가", "desc": "신중하고 철저한 당신은 정확성이 필요한 일이 딱이야!"},
    "ISFJ": {"job": "🏥 간호사, 선생님, 사회복지사", "desc": "친절하고 책임감 있는 당신은 남을 돕는 일에서 빛이 나!"},
    "INFJ": {"job": "✍️ 작가, 상담 심리사, 예술가", "desc": "통찰력 있고 이상적인 당신은 사람들의 마음을 치유해!"},
    "INTJ": {"job": "🧠 과학자, 전략 기획자, 개발자", "desc": "논리적이고 독립적인 당신은 문제를 해결하는 천재!"},
    "ISTP": {"job": "🛠️ 엔지니어, 파일럿, 프로게이머", "desc": "도구를 잘 다루는 당신은 실용적인 기술 전문가!"},
    "ISFP": {"job": "🎨 화가, 요리사, 디자이너", "desc": "예술적 감각이 뛰어난 당신은 세상을 아름답게 만들어!"},
    "INFP": {"job": "📚 소설가, 작곡가, 유튜버", "desc": "상상력이 풍부한 당신은 나만의 감성을 표현하는 예술가!"},
    "INTP": {"job": "🧪 물리학자, 철학자, 보안 전문가", "desc": "호기심 많은 당신은 깊이 있는 연구와 분석에 최고!"},
    "ESTP": {"job": "🏃 사업가, 경찰관, 운동선수", "desc": "적응력이 뛰어나고 에너지가 넘치는 당신은 현장의 리더!"},
    "ESFP": {"job": "🎤 연예인, 승무원, 이벤트 플래너", "desc": "사교적이고 즐거운 당신은 어디서나 분위기 메이커!"},
    "ENFP": {"job": "🌟 광고 기획자, 파티 플래너, 작가", "desc": "열정적이고 창의적인 당신은 새로운 도전을 즐기는 탐험가!"},
    "ENTP": {"job": "💡 발명가, 변호사, 마케팅 전문가", "desc": "아이디어가 넘치는 당신은 세상을 바꾸는 혁신가!"},
    "ESTJ": {"job": "📊 경영자, 프로젝트 매니저, 군인", "desc": "조직적이고 체계적인 당신은 목표를 이끄는 지휘관!"},
    "ESFJ": {"job": "🤝 홍보 전문가, 호텔리어, 초등교사", "desc": "배려심 깊고 협력적인 당신은 사람들과 함께할 때 행복해!"},
    "ENFJ": {"job": "📢 정치인, 연설가, 사회운동가", "desc": "카리스마 있는 리더인 당신은 사람들에게 영감을 줘!"},
    "ENTJ": {"job": "👑 CEO, 경영 컨설턴트, 판사", "desc": "결단력 있고 통솔력이 강한 당신은 미래를 이끄는 리더!"}
}

# --- 사용자 입력 ---
selected_mbti = st.selectbox("나의 MBTI 유형은 무엇인가요? 👇", list(mbti_info.keys()))

# --- 결과 출력 버튼 ---
if st.button("💖 나의 추천 직업 확인하기 💖"):
    # 축하 효과
    st.balloons()
    
    # 결과 정보 가져오기
    res = mbti_info[selected_mbti]
    
    # 카드 형식으로 출력
    st.markdown(f"""
        <div class="job-card">
            <h1 style='font-size: 60px;'>{selected_mbti}</h1>
            <p style='font-size: 20px; color: #666;'>{res['desc']}</p>
            <hr>
            <h2 style='color: #FF4B4B;'>💎 추천 직업 💎</h2>
            <p style='font-size: 28px; font-weight: bold;'>{res['job']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info(f"항상 {selected_mbti}인 여러분의 꿈을 응원해요! 화이팅! 🔥")

# --- 푸터 ---
st.markdown("<br><br><p style='text-align: center; color: #888;'>© 2026 Dream MBTI Project ✨</p>", unsafe_allow_html=True)
