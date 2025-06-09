import streamlit as st

# ✅ 차이 있을 때의 팁
difference_tips = {
    ("E", "I"): "🎧 조용한 분위기에서 천천히 다가가 보세요. 내향형은 에너지 충전 시간이 필요해요.",
    ("I", "E"): "🎤 활기찬 활동에 함께 참여하며 자연스럽게 친해져 보세요!",
    ("S", "N"): "🌌 추상적 이야기에도 열린 마음으로 귀 기울여 보세요. 직관형은 상상과 아이디어를 즐겨요.",
    ("N", "S"): "🧭 현실적인 대화와 구체적인 예시로 다가가면 신뢰를 얻을 수 있어요.",
    ("T", "F"): "💞 논리보단 감정에 공감해 주세요. 따뜻한 한 마디가 더 효과적일 수 있어요.",
    ("F", "T"): "🧠 비판을 개인적인 것으로 받아들이기보다, 문제 해결 의도를 이해해보세요.",
    ("P", "J"): "📅 계획을 존중하고, 약속은 가능한 한 지켜주는 게 좋아요!",
    ("J", "P"): "🧘‍♂️ 상대의 유연함을 존중하고, 일정이 바뀌어도 여유를 가져보세요."
}

# ✅ 같을 때의 공감 멘트
same_tips = {
    "E": "⚡️ 둘 다 외향형이라서 에너지 넘치는 활동을 함께 즐기기 좋아요!",
    "I": "🌙 둘 다 내향형이라 조용한 시간도 서로 편하게 느껴요.",
    "S": "📦 둘 다 현실적이라 공감대 형성이 쉬워요. 안정감 있는 대화가 잘 통해요!",
    "N": "🌠 둘 다 상상력과 아이디어가 풍부해서 대화가 끊기지 않아요!",
    "T": "🧩 둘 다 이성적으로 사고해서, 감정 대신 문제 해결 중심의 대화가 잘 맞아요.",
    "F": "💖 둘 다 감정에 민감해서 서로 잘 이해하고 배려할 수 있어요.",
    "P": "🌊 둘 다 즉흥적인 성향이라 유연하고 자유로운 일정이 잘 맞아요!",
    "J": "📋 둘 다 계획형이라 체계적이고 정돈된 관계를 유지하기 좋아요!"
}

# ✅ MBTI 기능 추출 함수
def extract_mbti_functions(mbti):
    return {
        "EI": mbti[0],
        "SN": mbti[1],
        "TF": mbti[2],
        "PJ": mbti[3]
    }

# ✅ 스트림릿 앱 시작
st.set_page_config(page_title="MBTI 궁합 팁 💕", page_icon="🤝")
st.title("🤝 나와 친구의 MBTI로 알아보는 친해지는 방법 ✨")
st.markdown("당신과 친구의 MBTI를 선택하면, 서로 **다른 점은 이해**, **같은 점은 칭찬**해드릴게요! 💬")

# ✅ MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

my_mbti = st.selectbox("🧍 내 MBTI를 선택해주세요", [""] + mbti_list)
friend_mbti = st.selectbox("👤 친구의 MBTI를 선택해주세요", [""] + mbti_list)

# ✅ 결과 출력
if my_mbti and friend_mbti:
    my = extract_mbti_functions(my_mbti)
    friend = extract_mbti_functions(friend_mbti)

    st.markdown("### 💬 관계 팁 요약")

    for key in ["EI", "SN", "TF", "PJ"]:
        my_letter = my[key]
        friend_letter = friend[key]
        
        if my_letter == friend_letter:
            # 같을 때
            tip = same_tips.get(my_letter)
            if tip:
                st.success(f"✅ **{my_letter} vs {friend_letter}**: {tip}")
        else:
            # 다를 때
            pair = (my_letter, friend_letter)
            tip = difference_tips.get(pair)
            if tip:
                st.info(f"🔁 **{my_letter} vs {friend_letter}**: {tip}")

    st.balloons()

elif my_mbti or friend_mbti:
    st.warning("📌 두 사람의 MBTI를 모두 선택해주세요!")
else:
    st.info("👆 위에서 두 사람의 MBTI를 골라보세요!")
