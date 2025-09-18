

import streamlit as st
from collections import Counter
import math

# --- 핵심 기능: 소인수분해 함수 ---
def prime_factorize(n):
    """
    주어진 자연수 n을 소인수분해하여 소인수들의 리스트를 반환하는 함수.
    최적화를 위해 제곱근까지만 검사합니다.
    """
    factors = []
    # 2로 나누어 떨어지는 동안 계속 2를 추가
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # 이제 n은 홀수이므로, 3부터 시작하여 홀수만 검사
    # n의 제곱근까지만 검사하면 충분
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
            
    # 위 루프가 끝난 후 n이 1보다 크면, 남은 n 자체가 소수
    if n > 1:
        factors.append(n)
        
    return factors

# --- 결과 포맷팅 함수 ---
def format_factors_with_exponents(factors):
    """
    소인수 리스트를 지수 형태로 보기 좋게 변환합니다.
    예: [2, 2, 3] -> "2^2 \\times 3" (Streamlit LaTeX 형식)
    """
    if not factors:
        return ""
        
    # Counter를 사용하여 각 소인수의 개수를 셈
    counts = Counter(factors)
    
    # LaTeX 문자열로 변환
    parts = []
    for factor, exponent in sorted(counts.items()):
        if exponent > 1:
            parts.append(f"{factor}^{{{exponent}}}")
        else:
            parts.append(str(factor))
            
    return " \\times ".join(parts)

# --- Streamlit 앱 UI 구성 ---

st.set_page_config(page_title="소인수분해 계산기", page_icon="🔢")

st.title("🔢 소인수분해 계산기")
st.markdown("자연수를 입력하면 소인수분해 결과를 보여주는 웹 앱입니다.")
st.markdown("---")

# 사용자로부터 숫자 입력받기
# min_value=2: 소인수분해는 2 이상의 자연수에 대해 의미가 있음
# step=1: 정수만 입력받도록 설정
number_to_factorize = st.number_input(
    "소인수분해 할 자연수를 입력하세요 (2 이상)", 
    min_value=2, 
    step=1,
    value=120  # 기본 예시 값
)

# '계산하기' 버튼을 누르면 소인수분해 실행
if st.button("결과 확인하기"):
    if number_to_factorize:
        # 소인수분해 함수 호출
        factors = prime_factorize(number_to_factorize)
        
        st.success(f"**{number_to_factorize}**의 소인수분해 결과입니다.")
        
        # 1. 기본 곱셈 형태로 결과 표시
        st.subheader("곱셈 형태")
        result_string = " x ".join(map(str, factors))
        st.markdown(f"### `{result_string}`")

        # 2. 지수 형태로 결과 표시 (LaTeX 사용)
        st.subheader("지수 형태")
        latex_result = format_factors_with_exponents(factors)
        st.latex(f"{number_to_factorize} = {latex_result}")
    else:
        st.warning("숫자를 입력해주세요.")

st.markdown("---")
st.info("만든이: Gemini")