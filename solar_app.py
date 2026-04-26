import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. إدارة الحالة
if 'user_data' not in st.session_state: st.session_state.user_data = None
if 'current_page' not in st.session_state: st.session_state.current_page = "home"

def navigate_to(page): st.session_state.current_page = page

# 3. CSS التصميم الاحترافي (وضوح فائق للنصوص والخانات)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #ffffff; }

    /* لافتة الترحيب الملونة */
    .hero-banner {
        background: linear-gradient(135deg, #007bff 0%, #00d4ff 100%);
        padding: 35px; border-radius: 25px; color: white !important;
        text-align: center; margin-bottom: 30px; box-shadow: 0 10px 20px rgba(0,123,255,0.2);
    }
    .hero-banner h1 { color: white !important; font-weight: 900; margin: 0; }

    /* جعل خانات الإدخال بيضاء وواضحة جداً لمنع اللون الأسود */
    div[data-baseweb="input"], div[data-baseweb="select"], .stSelectbox {
        background-color: #ffffff !important;
        border: 2px solid #007bff !important;
        border-radius: 12px !important;
    }
    
    input { 
        color: #000000 !important; 
        font-weight: 700 !important; 
        font-size: 1.1rem !important;
    }

    /* عناوين الحقول (الاسم، الرقم، الخ) بجعلها سوداء وعريضة */
    label { 
        color: #000000 !important; 
        font-weight: 900 !important; 
        font-size: 1rem !important; 
        margin-bottom: 8px !important;
    }

    /* أزرار التنقل السفلي */
    .stButton>button {
        border-radius: 12px !important;
        font-weight: 700 !important;
    }

    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-bottom: 120px; }
    </style>
    """, unsafe_allow_html=True)

# 4. شاشة إدخال البيانات (التي طلبت تعديلها)
if st.session_state.user_data is None:
    st.markdown("<div class='hero-banner'><h1>مرحباً بك ☀️</h1><p>أدخل بياناتك الشخصية أدناه:</p></div>", unsafe_allow_html=True)
    
    with st.container():
        # الحقل الأول: الاسم
        u_name = st.text_input("الحقل الأول: الاسم الكامل", placeholder="اكتب اسمك هنا...")
        
        # الحقل الثاني: الرقم
        u_phone = st.text_input("الحقل الثاني: رقم الموبايل", placeholder="مثال: 0780XXXXXXXX")
        
        # الحقل الثالث: المحافظة
        u_city = st.selectbox("الحقل الثالث: اختر المحافظة", ["بغداد", "البصرة", "أربيل", "الموصل", "النجف", "كربلاء", "ديالى", "ذي قار", "أخرى"])
        
        st.write(" ") # مساحة صغيرة
        if st.button("دخول للمنصة الآن 🚀", use_container_width=True):
            if u_name and u_phone:
                st.session_state.user_data = {"name": u_name, "phone": u_phone, "city": u_city}
                st.rerun()
            else:
                st.error("عذراً، يرجى ملء الاسم والرقم للاستمرار")
    st.stop()

# 5. الصفحة الرئيسية (تظهر بعد إدخال البيانات)
if st.session_state.current_page == "home":
    st.markdown(f"<div class='hero-banner'><h1>أهلاً بك، {st.session_state.user_data['name']}</h1><p>من محافظة {st.session_state.user_data['city']}</p></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🚀 الحاسبة الهندسية", use_container_width=True, on_click=navigate_to, args=("calc",))
    with col2:
        st.button("🏢 دليل الشركات", use_container_width=True, on_click=navigate_to, args=("companies",))

# 6. شريط التنقل السفلي (مرتب بصف واحد)
st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)
nav_cols = st.columns(4)
with nav_cols[0]: st.button("🏠 الرئيسية", key="n1", on_click=navigate_to, args=("home",))
with nav_cols[1]: st.button("🏢 الشركات", key="n2")
with nav_cols[2]: st.button("🎁 خصومات", key="n3")
with nav_cols[3]: st.button("👤 حسابي", key="n4")
