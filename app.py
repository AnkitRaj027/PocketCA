import streamlit as st

from rag.services.query_service import QueryService

st.set_page_config(
    page_title="PocketCA",
    page_icon="💰",
    layout="wide",
)

st.title("💰 PocketCA")
st.caption("AI-powered Indian Tax Assistant")

if "query_service" not in st.session_state:
    st.session_state.query_service = QueryService()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        fallback_message = "I couldn't find this information in the official knowledge base."
        if message.get("sources") and fallback_message not in message["content"]:
            st.divider()
            st.markdown("**Sources**")
            for source in message["sources"]:
                filename = getattr(source, "filename", source.get("filename") if isinstance(source, dict) else "Unknown")
                page = getattr(source, "page", source.get("page") if isinstance(source, dict) else 1)
                st.write(f"📄 {filename} (Page {page})")

question = st.chat_input("Ask your tax question...")

if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        stream, response_container = st.session_state.query_service.ask_stream(question)
        response_text = st.write_stream(stream)

        
        sources = response_container.get('sources') or []
        
        
        if sources:
            st.divider()
            st.markdown("**Sources**")
            for source in sources:
                st.write(
                    f"📄 {source.filename} (Page {source.page})"
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response_text,
            "sources": sources,
        }
    )
