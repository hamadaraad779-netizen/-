import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. إدارة الجلسة
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'calc_results' not in st.session_state: st.session_state.calc_results = None

def navigate_to(page): st.session_state.current_page = page

# 3. CSS التصميم "المستطيلي" الصغير والواضح
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #f8f9fa; }

    /* جعل خانات الإدخال صغيرة، نحيفة، وواضحة */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        height: 40px !important;
        border-radius: 10px !important;
        border: 2px solid #0062ff !important; /* إطار أزرق واضح */
        background-color: white !important;
    }
    
    input {
        font-size: 1rem !important;
        font-weight: 700 !important;
        color: #000 !important;
        padding: 5px 10px !important;
    }

    /* عناوين الخانات (Labels) */
    label {
        font-weight: 900 !important;
        color: #333 !important;
        font-size: 0.9rem !important;
        margin-bottom: 5px !important;
    }

    /* صناديق النتائج الفخمة */
    .result-card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    .res-val { color: #0062ff; font-size: 1.5rem; font-weight: 900; display: block; }
    .res-lbl { color: #666; font-size: 0.8rem; font-weight: 700; }

    /* إخفاء الزوائد */
    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
if st.session_state.current_page == "home":
    st.markdown("<h2 style='text-align:center; color:#0062ff;'>☀️ طاقتي الشمسية</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("🚀 الحاسبة الهندسية", on_click=lambda: navigate_to("calc"))
    with col2:
        st.button("🏢 دليل الشركات", on_click=lambda: navigate_to("companies"))

elif st.session_state.current_page == "calc":
    st.markdown("### 🛠️ صمم منظومتك")
    
    # استخدام أعمدة لجعل الخانات تظهر بجانب بعضها وتكون أصغر
    c1, c2 = st.columns(2)
    with c1:
        d_amp = st.number_input("الأمبير نهاراً:", value=10.0, step=1.0)
        p_watt = st.selectbox("قدرة اللوح:", [400, 550, 585, 670], index=1)
    with c2:
        n_amp = st.number_input("الأمبير ليلاً:", value=5.0, step=1.0)
        hrs = st.selectbox("ساعات البطارية:", [2, 4, 6, 8, 10, 12], index=1)
        
    if st.button("احسب الآن ✨", use_container_width=True):
        panels = round((d_amp * 230) / (p_watt * 0.75))
        inv = "6.2 kW Hybrid" if d_amp <= 15 else "10.2 kW Hybrid"
        battery = (n_amp * 230 * hrs) / 1000
        st.session_state.calc_results = {"p": panels, "i": inv, "b": f"{battery:.1f} kWh"}

    if st.session_state.calc_results:
        st.write("---")
        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown(f"<div class='result-card'><span class='res-val'>{st.session_state.calc_results['p']}</span><span class='res-lbl'>لوح شمسي</span></div>", unsafe_allow_html=True)
        with r2:
            st.markdown(f"<div class='result-card'><span class='res-val'>{st.session_state.calc_results['i']}</span><span class='res-lbl'>العاكس</span></div>", unsafe_allow_html=True)
        with r3:
            st.markdown(f"<div class='result-card'><span class='res-val'>{st.session_state.calc_results['b']}</span><span class='res-lbl'>البطارية</span></div>", unsafe_allow_html=True)
    
    st.button("⬅️ عودة", on_click=lambda: navigate_to("home"))

elif st.session_state.current_page == "companies":
    st.button("⬅️ عودة", on_click=lambda: navigate_to("home"))
    st.markdown("### 🏢 الشركات المعتمدة")
    st.info("سيتم عرض الشركات هنا...")

# 5. الناف بار السفلي
st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1: st.button("🏠")
with nav2: st.button("🏢")
with nav3: st.button("🎁")
with nav4: st.button("👤")
