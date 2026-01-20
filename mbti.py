import streamlit as st
import time
import random

# 1. 페이지 설정
st.set_page_config(page_title="나의 꿈 판타지 MBTI", page_icon="🔮", layout="centered")

# 2. 화려한 네온 스타일 CSS (성적 결과 레이아웃 추가)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #e60073; }
        to { text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6; }
    }
    .main-title {
        font-size: 50px; font-weight: bold; text-align: center;
        animation: glow 1s ease-in-out infinite alternate;
        margin-bottom: 20px;
    }
    .result-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 30px; border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center; margin-top: 20px;
    }
    .roulette-box {
        background: #ff00cc; padding: 10px; border-radius: 50%;
        width: 100px; height: 100px; margin: 0 auto;
        display: flex; align-items: center; justify-content: center;
        font-size: 40px; animation: spin 0.5s linear infinite;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🔮 MBTI 진로 & 성적 돌림판 🔮</h1>', unsafe_allow_html=True)

# 3. 데이터 설정
mbti_db = {
    "ENFP": {"job": "🎨 유튜버, 여행 작가", "desc": "영감이 샘솟는 활동가!", "emoji": "🧚"},
    "INTJ": {"job": "🧠 인공지능 전문가, 전략가", "desc": "미래를 설계하는 지휘관!", "emoji": "🔭"},
    "ENTP": {"job": "💡 스타트업 창업가, 변호사", "desc": "천재적인 아이디어 뱅크!", "emoji": "🚀"},
    "INFJ": {"job": "📜 상담사, 심리학자", "desc": "영혼을 울리는 통찰가!", "emoji": "🌊"},
    "INFP": {"job": "✍️ 예술 심리 치료사, 작가", "desc": "꿈꾸는 감성 중재자!", "emoji": "🍀"},
    "ISTP": {"job": "🔧 엔지니어, 파일럿", "desc": "냉철한 기술 전문가!", "emoji": "🏍️"},
    # (공간상 생략, 실제 실행시에는 위 코드의 16개를 모두 넣으시면 됩니다!)
}

# 성적 성취도 키워드 리스트
performance_levels = [
    "🔝 전교 1등급 성취!", "⭐ 기대 이상의 고득점", "📈 꾸준한 우상향", 
    "🔥 열정적인 학구파", "💎 잠재력 폭발 직전", "🎯 목표 달성 성공"
]

# 4. 사용자 입력
selected = st.selectbox("✨ 당신의 MBTI를 선택해 보세요:", list(mbti_db.keys()))

col1, col2 = st.columns(2)

# --- 왼쪽: 직업 추천 ---
with col1:
    if st.button("🚀 직업 문 열기"):
        st.balloons()
        res = mbti_db.get(selected, {"job": "준비중", "desc": "탐색중", "emoji": "✨"})
        st.markdown(f"""
            <div class="result-card">
                <h1>{res['emoji']}</h1>
                <h3>{selected} 추천 직업</h3>
                <p style='font-weight:bold; color:#00ffcc;'>{res['job']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- 오른쪽: 성적 돌림판 ---
with col2:
    if st.button("🎡 성적 성취도 돌리기"):
        # 돌림판 돌아가는 시각적 효과
        placeholder = st.empty()
        for _ in range(10):  # 1초 동안 빠르게 변함
            temp_result = random.choice(performance_levels)
            placeholder.markdown(f"""
                <div class="result-card">
                    <div class="roulette-box">🎡</div>
                    <p style='margin-top:10px;'>분석 중: {temp_result}</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(0.1)
        
        # 최종 결과
        final_score = random.choice(performance_levels)
        placeholder.markdown(f"""
            <div class="result-card" style="border: 2px solid #ffde59;">
                <h2 style='color:#ffde59;'>🎉 결과 확정!</h2>
                <hr>
                <h3 style='font-size:24px;'>{final_score}</h3>
                <p>당신의 노력이 빛을 발할 거예요!</p>
            </div>
        """, unsafe_allow_html=True)
        st.snow()

# 5. 하단 안내
st.markdown("---")
st.write("<p style='text-align: center; opacity: 0.6;'>※ 본 결과는 교육용 재미로 보는 분석입니다. 당신의 미래를 응원해요! ✨</p>", unsafe_allow_html=True)
