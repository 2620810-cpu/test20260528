# 반드시 이 줄이 맨 윗줄에 있어야 합니다.
import streamlit as st

st.title("🥉 3등 찾기 프로그램")
st.write("점수를 입력하면 3등을 찾아줍니다.")

# 1. 입력 (Input)
user_input = st.text_input("점수를 쉼표(,)로 구분해서 입력하세요 (예: 95, 80, 100, 75, 85)")

if st.button("3등 찾기"):
    # 2. 조건문 (Conditional): 빈 값 검사
    if user_input.strip() == "":
        st.error("점수를 입력해주세요!")
    else:
        raw_scores = user_input.split(",")
        scores = []
        
        # 3. 반복문 (Loop): 입력된 텍스트를 숫자로 변환
        for score in raw_scores:
            # 4. 조건문 (Conditional): 숫자가 아닌 문자가 섞였을 때의 예외 처리
            try:
                scores.append(int(score.strip()))
            except ValueError:
                pass # 숫자로 바꿀 수 없는 값(문자 등)은 무시하고 넘어감
        
        # 내림차순(큰 수부터) 정렬
        scores.sort(reverse=True)
        
        # 5. 조건문 (Conditional): 제대로 된 숫자가 3개 이상인지 확인
        if len(scores) < 3:
            st.error("비교할 숫자가 3개 이상 필요합니다.")
        else:
            # 6. 출력 (Output): 결과 표시
            st.success(f"🎉 3등 점수는 **{scores[2]}점** 입니다!")
            st.write(f"🥇 1등: {scores[0]}점")
            st.write(f"🥈 2등: {scores[1]}점")
            st.write(f"🥉 3등: {scores[2]}점")