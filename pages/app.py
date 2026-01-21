import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="말랑말랑 숫자 두뇌 트레이닝", page_icon="🧩")

# --- 게임 로직 함수 ---
def generate_sudoku():
    """4x4 간단한 스도쿠 생성 (어린이용)"""
    # 기본 행렬 (1~4 숫자 조합)
    base = [1, 2, 3, 4]
    random.shuffle(base)
    
    # 간단한 규칙으로 4x4 완성 (복잡한 알고리즘 대신 셔플 활용)
    grid = [
        base,
        base[2:] + base[:2],
        [base[1], base[0], base[3], base[2]],
        [base[3], base[2], base[1], base[0]]
    ]
    
    # 정답 보관
    solution = [row[:] for row in grid]
    
    # 힌트 남기기 (빈칸 만들기 - 난이도 조절)
    for r in range(4):
        for c in range(4):
            if random.random() > 0.5:  # 50% 확률로 빈칸
                grid[r][c] = 0
                
    return grid, solution

# --- 세션 상태 초기화 (오류 방지 핵심) ---
if 'board' not in st.session_state:
    grid, sol = generate_sudoku()
    st.session_state.board = grid
    st.session_state.solution = sol
    st.session_state.game_over = False

# --- UI 레이아웃 ---
st.title("🧩 말랑말랑 숫자 트레이닝")
st.subheader("빈칸에 알맞은 숫자를 채워보세요!")

# 이모지 매핑 (아이들의 흥미 유발)
num_to_emoji = {0: "❓", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣"}

# 게임판 그리기
cols = st.columns(4)
user_answers = []

for r in range(4):
    row_answers = []
    cols = st.columns(4)
    for c in range(4):
        val = st.session_state.board[r][c]
        with cols[c]:
            if val == 0:
                # 빈칸일 경우 숫자 선택 (Key값을 다르게 주어 오류 방지)
                choice = st.selectbox(f"R{r}C{c}", [0, 1, 2, 3, 4], 
                                      key=f"cell_{r}_{c}", 
                                      label_visibility="collapsed")
                row_answers.append(choice)
            else:
                # 고정된 숫자는 텍스트로 표시
                st.info(num_to_emoji[val])
                row_answers.append(val)
    user_answers.append(row_answers)

st.divider()

# --- 결과 확인 및 게임 제어 ---
c1, c2 = st.columns(2)

with c1:
    if st.button("정답 확인! ✨", use_container_width=True):
        if user_answers == st.session_state.solution:
            st.balloons()
            st.success("대단해요! 두뇌 트레이닝 성공! 🎉")
            st.session_state.game_over = True
        else:
            st.error("조금 더 생각해보세요! 할 수 있어요! 💪")

with c2:
    if st.button("새 게임 시작 🔄", use_container_width=True):
        # 세션 초기화 후 재실행
        del st.session_state.board
        st.rerun()

# --- 도움말 ---
with st.expander("💡 게임 방법"):
    st.write("1. 가로 줄에 1부터 4까지 숫자가 하나씩 들어가야 해요.")
    st.write("2. 세로 줄에도 1부터 4까지 숫자가 하나씩 들어가야 해요.")
    st.write("3. ❓ 표시가 된 곳을 클릭해서 숫자를 골라주세요!")
