import os
import streamlit as st

# Check for Mistral API key (needed before importing modules that load BaseSettings)
mistral_key = os.environ.get("MISTRAL_API_KEY")
try:
    if not mistral_key and "MISTRAL_API_KEY" in st.secrets:
        mistral_key = st.secrets["MISTRAL_API_KEY"]
        os.environ["MISTRAL_API_KEY"] = mistral_key
except Exception:
    pass

st.set_page_config(
    page_title="PocketCA",
    page_icon="💰",
    layout="wide",
)

st.title("💰 PocketCA")
st.caption("AI-powered Indian Tax Assistant")

if not mistral_key:
    st.error("🔑 **Mistral API Key Missing**")
    st.info("""
        Please configure your Mistral API Key to run the app.
        
        **How to configure on Streamlit Cloud:**
        1. Go to your Streamlit Cloud Workspace.
        2. Click on the app's options (three dots) and select **Settings**.
        3. Go to the **Secrets** section.
        4. Paste your API key in TOML format:
        ```toml
        MISTRAL_API_KEY = "your_actual_api_key_here"
        ```
        5. Click **Save**. The app will automatically reboot and start working.
    """)
    st.stop()

# Import core query service now that environment variables are set
from rag.services.query_service import QueryService

if "query_service" not in st.session_state:
    st.session_state.query_service = QueryService()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Helper to render source references cleanly
def render_source(source):
    if isinstance(source, dict):
        filename = source.get("filename", "Unknown")
        page = source.get("page", 1)
    else:
        filename = getattr(source, "filename", "Unknown")
        page = getattr(source, "page", 1)
    st.write(f"📄 {filename} (Page {page})")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        fallback_message = "I couldn't find this information in the official knowledge base."
        if message.get("sources") and fallback_message not in message["content"]:
            st.divider()
            st.markdown("**Sources**")
            for source in message["sources"]:
                render_source(source)

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
                render_source(source)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response_text,
            "sources": sources,
        }
    )
