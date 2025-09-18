# 소인수 분해 함수
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

st.header("소인수 분해 앱")
num = st.number_input("소인수 분해할 자연수를 입력하세요", min_value=2, step=1)
if num:
    factors = prime_factors(int(num))
    st.write(f"{int(num)}의 소인수 분해 결과: {factors}")
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Streamlit의 다양한 UI 요소 예시 페이지입니다. 아래에서 여러 컴포넌트를 확인해보세요."
)

# 텍스트 입력
name = st.text_input("이름을 입력하세요")
if name:
    st.success(f"안녕하세요, {name}님!")

# 숫자 슬라이더
age = st.slider("나이", 0, 100, 25)
st.write(f"선택한 나이: {age}")

# 체크박스
agree = st.checkbox("약관에 동의합니다")
if agree:
    st.info("동의해주셔서 감사합니다.")

# 라디오 버튼
color = st.radio("좋아하는 색상은?", ["빨강", "파랑", "초록"])
st.write(f"선택한 색상: {color}")

# 선택 박스
fruit = st.selectbox("좋아하는 과일은?", ["사과", "바나나", "오렌지"])
st.write(f"선택한 과일: {fruit}")

# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file:
    st.success(f"{uploaded_file.name} 파일이 업로드되었습니다.")

# 이미지 표시 (예시)
st.image(
    "https://static.streamlit.io/examples/dog.jpg",
    caption="Streamlit 샘플 이미지",
    use_column_width=True
)
