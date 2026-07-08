import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

st.title("My ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "is_ai_responding" not in st.session_state:
    st.session_state.is_ai_responding = False


def lock_chat_input():
    """사용자가 메시지를 제출하는 즉시 추가 입력을 막습니다."""
    st.session_state.is_ai_responding = True


# 이전 대화는 매번 다시 그려 페이지가 갱신되어도 유지되게 합니다.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input(
    "무엇이든 물어보세요.",
    disabled=st.session_state.is_ai_responding,
    on_submit=lock_chat_input,
)

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        client = OpenAI()

        with st.chat_message("assistant"):
            with st.spinner("AI가 답변을 생각하고 있어요..."):
                response = client.responses.create(
                    model="gpt-5.5",
                    input=prompt,
                )
                answer = response.output_text

            st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
    except Exception as error:
        error_message = f"답변을 생성하지 못했습니다: {error}"
        st.session_state.messages.append(
            {"role": "assistant", "content": error_message}
        )
        with st.chat_message("assistant"):
            st.error(error_message)
    finally:
        # 성공/실패 여부와 관계없이 다시 입력할 수 있게 잠금을 해제합니다.
        st.session_state.is_ai_responding = False

    st.rerun()
