import streamlit as st

from gui2.pages.video_editing.ui_tab_short_automation import ShortAutomationUI
from gui2.pages.video_editing.ui_tab_video_automation import VideoAutomationUI
from gui2.pages.video_editing.ui_tab_video_translation import \
    VideoTranslationUI
from gui2.ui_components_html import StreamlitComponentsHTML

st.set_page_config(
    page_title="Hello",
    page_icon="🎬",
    layout="wide"
)

st.write("# Video Engine 🎬")
st.write("## Welcome to the Video Engine! 🚀")
st.write("### 🏆 Content Automation 🚀")
st.write("Choose your desired automation task.")
StreamlitComponentsHTML.add_logo("assets/img/logo.png", st)

tab1, tab2, tab3 = st.tabs(["🎬 Automate the creation of shorts", "🎞️ Automate a video with stock assets", "📹 Automate video translation"])

with tab1:
    ShortAutomationUI().create_ui()
with tab2:
    st.write("## 🎞️ Automate a video with stock assets")
with tab3:
    VideoTranslationUI().create_ui()
