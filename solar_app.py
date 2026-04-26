import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="العراق للطاقة الشمسية", layout="wide")

# 2. إدارة البيانات والحالة
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'user_data' not in st.session_state: st.session_state.user_data = {"name": "محمد صادق", "city": "بغداد"}

def navigate_to(page): st.session_state.current_page = page

# 3. CSS "الاحترافي" لضمان الوضوح والجمال
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* خلفية بيضاء ناصعة للتطبيق */
    .stApp { background-color: #ffffff; }

    /* إجبار النصوص على اللون الأزرق الغامق جداً */
    h1, h2, h3, h4, p, span, label {
        color: #001a33 !important;
        font-weight: 900 !important;
    }

    /* تصميم البطاقات المربعة (مثل بلي) */
    .menu-card {
        background-color: #f0f7ff;
        border: 2px solid #0056b3;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-bottom: 10px;
        min-height: 140px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .menu-card img { width: 50px; margin-bottom: 10px; }

    /* تصميم الخانات (المستطيلات الواضحة) */
    div[data-baseweb="input"], .stNumberInput, .stSelectbox, .stSlider {
        background-color: #ffffff !important;
        border: 2px solid #001a33 !important;
        border-radius: 12px !important;
    }
    input { color: #000000 !important; font-weight: 700 !important; }

    /* البانر العلوي */
    .top-banner {
        background: linear-gradient(135deg, #0056b3 0%, #00aaff 100%);
        padding: 30px; border-radius: 20px; color: white !important;
        text-align: center; margin-bottom: 20px;
    }
    .top-banner h1, .top-banner p { color: white !important; }

    /* إخفاء زوائد ستريم ليت */
    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-top: 1rem; padding-bottom: 6rem; }
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown(f"""<div class='top-banner'><h1>أهلاً بك، {st.session_state.user_data['name']}</h1>
    <p>محافظة {st.session_state.user_data['city']}</p></div>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png"><h4>حساب المنظومة</h4></div>', unsafe_allow_html=True)
        st.button("افتح الحاسبة", key="c1", use_container_width=True, on_click=navigate_to, args=("calc",))
        
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png"><h4>طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز موعد", key="c2", use_container_width=True)

    with col2:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/995/995260.png"><h4>دليل الشركات</h4></div>', unsafe_allow_html=True)
        st.button("تصفح الشركات", key="c3", use_container_width=True, on_click=navigate_to, args=("cos",))

        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><h4>إعدادات حسابي</h4></div>', unsafe_allow_html=True)
        st.button("تعديل البيانات", key="c4", use_container_width=True)

# --- صفحة الحاسبة (كاملة وواضحة) ---
elif st.session_state.current_page == "calc":
    st.markdown("<h2 style='text-align:center;'>📊 حاسبة الطاقة الشمسية</h2>", unsafe_allow_html=True)
    
    with st.container():
        a_day = st.number_input("الأمبير المطلوب نهاراً:", value=10)
        a_night = st.number_input("الأمبير المطلوب ليلاً (بطارية):", value=5)
        h_night = st.slider("عدد ساعات عمل البطارية:", 2, 12, 6)
        
        if st.button("احسب النتائج الآن ✨", use_container_width=True):
            st.markdown("---")
            panels = round((a_day * 230) / 400)
            batt = (a_night * h_night * 230) / 1000
            
            res_css = "background:#f0f7ff; padding:15px; border-radius:15px; border:2px solid #0056b3; margin-bottom:10px;"
            st.markdown(f"<div style='{res_css}'>✅ تحتاج إلى <b>{panels} ألواح</b> قدرة 550 واط.</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='{res_css}'>✅ سعة البطارية المطلوبة: <b>{batt:.1f} kWh</b>.</div>", unsafe_allow_html=True)

    st.button("⬅️ عودة للرئيسية", on_click=navigate_to, args=("home",))

# --- صفحة دليل الشركات ---
elif st.session_state.current_page == "cos":
    st.markdown("<h2>🏢 الشركات المعتمدة</h2>", unsafe_allow_html=True)
    companies = [{"n": "شمس الرافدين", "l": "بغداد"}, {"n": "طاقة المستقبل", "l": "البصرة"}]
    for c in companies:
        st.markdown(f"""<div style='background:white; padding:15px; border-radius:15px; border:2px solid #001a33; margin-bottom:10px;'>
        <h4>{c['n']}</h4><p>📍 الموقع: {c['l']}</p></div>""", unsafe_allow_html=True)
    st.button("⬅️ عودة للرئيسية", on_click=navigate_to, args=("home",))

# 5. شريط التنقل السفلي (بصف واحد منظم)
st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)
nav_cols = st.columns(4)
with nav_cols[0]: st.button("🏠 الرئيسية", key="nav1", on_click=navigate_to, args=("home",), use_container_width=True)
with nav_cols[1]: st.button("🏢 الشركات", key="nav2", on_click=navigate_to, args=("cos",), use_container_width=True)
with nav_cols[2]: st.button("🎁 هدايا", key="nav3", use_container_width=True)
with nav_cols[3]: st.button("👤 حسابي", key="nav4", use_container_width=True)
