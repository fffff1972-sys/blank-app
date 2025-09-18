import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Matplotlib 한글 폰트 설정 (Mac, Windows, Linux 환경에 맞게) ---
# 대다수 환경에서 깨끗한 나눔고딕을 사용하도록 설정
try:
    plt.rc('font', family='NanumGothic') 
except:
    # 나눔고딕이 없을 경우 기본 폰트 사용
    pass

plt.rcParams['axes.unicode_minus'] = False # 마이너스 부호 깨짐 방지


# --- Streamlit 앱 UI 구성 ---

st.set_page_config(page_title="일차함수 그래프 생성기", page_icon="📈")

st.title("📈 일차함수 그래프 생성기")
st.write("슬라이더를 조절하여 y = mx + b 그래프를 그려보세요.")

st.markdown("---")

# --- 사용자 입력 컨트롤 (사이드바) ---
st.sidebar.header("함수 계수 조절")

# st.sidebar.slider를 사용하여 슬라이더 생성
slope_m = st.sidebar.slider("기울기 (m)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
intercept_b = st.sidebar.slider("y절편 (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# --- 그래프 데이터 생성 ---
# -50부터 50까지 500개의 점을 x축 데이터로 생성하여 부드러운 직선을 표현
x = np.linspace(-50, 50, 500)
y = slope_m * x + intercept_b

# --- 현재 함수식을 LaTeX으로 예쁘게 표시 ---
# y절편이 음수일 때 부호를 자연스럽게 처리
sign = "-" if intercept_b < 0 else "+"
equation = f"y = {slope_m:.1f}x {sign} {abs(intercept_b):.1f}"
st.latex(equation)

# --- Matplotlib으로 그래프 그리기 ---
fig, ax = plt.subplots(figsize=(10, 6)) # 그래프 크기 조절

# 1. 함수 그래프 그리기
ax.plot(x, y, label=equation, color='royalblue', linewidth=3)

# 2. x축, y축 그리기 (중심선)
ax.axhline(0, color='gray', linewidth=1.5, linestyle='--')
ax.axvline(0, color='gray', linewidth=1.5, linestyle='--')

# 3. 그래프 꾸미기
ax.set_title("일차함수 그래프", fontsize=18)
ax.set_xlabel("x축", fontsize=12)
ax.set_ylabel("y축", fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, which='both', linestyle=':', linewidth=0.5)

# 4. 축의 범위 고정 (슬라이더 조작 시 그래프가 흔들리지 않도록)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# 5. 축 눈금 설정
ax.set_xticks(np.arange(-10, 11, 2))
ax.set_yticks(np.arange(-10, 11, 2))


# --- Streamlit에 그래프 표시 ---
st.pyplot(fig)

st.markdown("---")
st.info("사이드바의 슬라이더를 움직여 기울기와 y절편을 바꿔보세요!")
