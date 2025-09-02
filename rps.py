import streamlit as st
import random

# 🎨 Page config
st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮", layout="centered")

# 🌟 Title & subtitle
st.markdown(
    """
    <h1 style='text-align: center; color: #FF4B4B;'>🎮 Rock ✊ Paper 📄 Scissors ✂️</h1>
    <h3 style='text-align: center; color: #58D68D;'>Can you beat the computer? 😎</h3>
    """,
    unsafe_allow_html=True
)

# 🔢 Initialize session state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

choices = ["Rock", "Paper", "Scissors"]
emoji_map = {"Rock": "✊", "Paper": "📄", "Scissors": "✂️"}

# 🎲 Game logic
def play(user_choice):
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "🤝 It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "🏆 You Win! 🎉"
        st.session_state.user_score += 1
        st.snow()  # ❄️ Fun effect instead of balloons
    else:
        result = "💻 Computer Wins! 😈"
        st.session_state.comp_score += 1

    return user_choice, comp_choice, result

# 🎮 Game UI
if not st.session_state.game_over:
    st.markdown("### ✨ Choose your move:")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("✊ Rock", use_container_width=True):
            st.session_state.last_play = play("Rock")

    with col2:
        if st.button("📄 Paper", use_container_width=True):
            st.session_state.last_play = play("Paper")

    with col3:
        if st.button("✂️ Scissors", use_container_width=True):
            st.session_state.last_play = play("Scissors")

    # 🏆 Show results
    if "last_play" in st.session_state:
        user_choice, comp_choice, result = st.session_state.last_play
        st.markdown("---")
        st.subheader(f"🧑 You: {emoji_map[user_choice]} **{user_choice}**")
        st.subheader(f"💻 Computer: {emoji_map[comp_choice]} **{comp_choice}**")

        if "Win" in result:
            st.success(result)
        elif "Tie" in result:
            st.info(result)
        else:
            st.error(result)

        # Ask if player wants to continue
        st.markdown("### 🔄 Do you want to play again?")
        col_yes, col_no = st.columns(2)

        with col_yes:
            if st.button("✅ Yes, Play Again"):
                pass  # do nothing, continue game

        with col_no:
            if st.button("❌ No, End Game"):
                st.session_state.game_over = True
                st.rerun()

else:
    # Final result
    st.markdown("## 🏁 Game Over!")
    st.write(f"🧑 Your Final Score: **{st.session_state.user_score}**")
    st.write(f"💻 Computer Final Score: **{st.session_state.comp_score}**")

    if st.session_state.user_score > st.session_state.comp_score:
        st.success("🎉 Congratulations, You Won the Match! 🏆")
    elif st.session_state.user_score < st.session_state.comp_score:
        st.error("😈 Computer Wins the Match!")
    else:
        st.info("🤝 It's a Tie Match!")

    if st.button("🔄 Restart Game"):
        st.session_state.user_score = 0
        st.session_state.comp_score = 0
        st.session_state.game_over = False
        if "last_play" in st.session_state:
            del st.session_state.last_play
        st.rerun()
