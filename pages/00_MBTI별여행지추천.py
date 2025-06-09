import streamlit as st

# 🎬 MBTI별 과학 명작 영화 추천 데이터
mbti_movies = {
    "INTJ": ("인터스텔라 🌌", "전략적인 사고와 깊이 있는 이야기 선호"),
    "INTP": ("인셉션 🧠", "복잡한 개념과 이론을 즐김"),
    "ENTJ": ("마션 🚀", "리더십과 문제 해결 중심 이야기 선호"),
    "ENTP": ("아이언맨 🤖", "혁신적이고 도전적인 스토리 선호"),
    "INFJ": ("컨택트 👽", "깊은 의미와 철학적 메시지에 끌림"),
    "INFP": ("월-E 🧡", "감성적이고 메시지 있는 영화 선호"),
    "ENFJ": ("매트릭스 🕶️", "이상과 현실의 조화를 추구"),
    "ENFP": ("백 투 더 퓨처 ⏰", "모험과 상상력이 넘치는 이야기"),
    "ISTJ": ("그래비티 🌍", "현실적이고 구조적인 이야기 선호"),
    "ISFJ": ("히든 피겨스 🧮", "사명감과 인간애가 돋보이는 이야기"),
    "ESTJ": ("아폴로 13 🛰️", "책임감과 위기 관리 중심 스토리"),
    "ESFJ": ("오펜하이머 ☢️", "사명과 갈등 속 인간미 있는 서사"),
    "ISTP": ("엣지 오브 투모로우 ⚔️", "액션과 논리적 전개 선호"),
    "ISFP": ("가타카 🧬", "섬세하면서도 깊이 있는 스토리"),
    "ESTP": ("쥬라기 월드 🦖", "긴장감 넘치는 모험과 액션"),
    "ESFP": ("가디언즈 오브 갤럭시 🎧", "유쾌하고 신나는 우주 대모험")
}

# 🎨 Streamlit 설정
st.set_page_config(page_title="MBTI 과학 영화 추천", page_icon="🎥")

# 🎉 타이틀과 설명
st.title("🎥 MBTI 과학 명작 영화 추천기 🚀")
st.markdown("당신의 MBTI를 입력하면, **성격에 딱 맞는 과학 영화**를 추천해드릴게요! 💡")

# 🎯 사용자 입력
user_mbti = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP)", max_chars=4).upper()

if user_mbti:
    if user_mbti in mbti_movies:
        movie, reason = mbti_movies[user_mbti]
        st.success(f"🎬 추천 영화: **{movie}**")
        st.info(f"💡 이유: {reason}")
        st.balloons()  # 🎈 풍선 효과!
    else:
        st.error("❌ 올바른 MBTI를 입력해주세요. 예: ENFP, ISTJ 등")
else:
    st.warning("👉 MBTI를 입력해보세요! 예: INTP, ENFJ 등")
