import streamlit as st

# 1. إعدادات الصفحة والأيقونة
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. إدارة البيانات (Session State)
if 'user_data' not in st.session_state: st.session_state.user_data = None
if 'current_page' not in st.session_state: st.session_state.current_page = "home"

def navigate_to(page): st.session_state.current_page = page

# 3. CSS الفائق (تصميم الموبايل الحديث - نصوص واضحة جداً)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #f0f2f5; color: #1c1e21; }
    
    /* لافتة علوية فخمة */
    .main-banner {
        background: linear-gradient(135deg, #0062ff 0%, #0041ab 100%);
        padding: 40px 20px;
        border-radius: 25px;
        color: white !important;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 12px 24px rgba(0,98,255,0.2);
    }
    .main-banner h1 { font-weight: 900 !important; color: white !important; font-size: 2.5rem; margin:0; }

    /* شبكة الأزرار المربعة (Grid) */
    .menu-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
    
    .card-item {
        background: white;
        border-radius: 25px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 6px 15px rgba(0,0,0,0.04);
        border: 1.5px solid #ffffff;
        transition: 0.3s ease-in-out;
        cursor: pointer;
    }
    .card-item:hover { transform: translateY(-10px); border-color: #fbbf24; }
    .card-item img { width: 65px; height: 65px; margin-bottom: 15px; }
    .card-item h4 { 
        color: #050505 !important; 
        font-weight: 900 !important; 
        font-size: 1.2rem !important; 
        margin: 0; 
    }

    /* شريط التنقل السفلي */
    .nav-bar {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; border-top: 1px solid #e4e6eb;
        display: flex; justify-content: space-around; padding: 15px 0;
        z-index: 1000;
    }
    
    /* تحسين شكل الأزرار الأصلية */
    .stButton>button {
        width: 100%; border-radius: 15px !important;
        background: #ffffff !important; color: #0062ff !important;
        border: 2px solid #0062ff !important; font-weight: 700 !important;
    }
    .stButton>button:hover { background: #0062ff !important; color: white !important; }

    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 10rem; }
    </style>
    """, unsafe_allow_html=True)

# 4. نظام التسجيل الإجباري (أول مرة فقط)
if st.session_state.user_data is None:
    st.markdown("<div class='main-banner'><h1>أهلاً بك في طاقتي</h1><p>سجل معلوماتك للبدء</p></div>", unsafe_allow_html=True)
    with st.form("reg"):
        n = st.text_input("الأسم الكامل")
        p = st.text_input("رقم الهاتف")
        c = st.selectbox("المحافظة", ["بغداد", "البصرة", "أربيل", "الموصل", "النجف", "كربلاء", "أخرى"])
        if st.form_submit_button("دخول للمنصة"):
            if n and p:
                st.session_state.user_data = {"name": n, "phone": p, "city": c}
                st.rerun()
    st.stop()

# 5. محتوى الصفحات
# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown("<div class='main-banner'><h1>مرحباً، " + st.session_state.user_data['name'] + "</h1><p>ماذا تريد أن تفعل اليوم؟</p></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card-item"><img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png"><h4>حساب المنظومة</h4></div>', unsafe_allow_html=True)
        st.button("فتح الحاسبة", key="btn_c", on_click=lambda: navigate_to("calc"))
        
        st.markdown('<div class="card-item"><img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png"><h4>طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز فني", key="btn_f")

    with col2:
        st.markdown('<div class="card-item"><img src="https://cdn-icons-png.flaticon.com/512/995/995260.png"><h4>دليل الشركات</h4></div>', unsafe_allow_html=True)
        st.button("تصفح المجهزين", key="btn_co")

        st.markdown('<div class="card-item"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><h4>الإدارة</h4></div>', unsafe_allow_html=True)
        st.button("دخول المسؤول", key="btn_a")

# --- صفحة حسابي (تعديل البيانات) ---
elif st.session_state.current_page == "profile":
    st.markdown("<h2>👤 معلومات حسابي</h2>", unsafe_allow_html=True)
    with st.container():
        st.session_state.user_data['name'] = st.text_input("الأسم", st.session_state.user_data['name'])
        st.session_state.user_data['phone'] = st.text_input("الهاتف", st.session_state.user_data['phone'])
        st.session_state.user_data['city'] = st.selectbox("المحافظة", ["بغداد", "البصرة", "أربيل", "أخرى"], index=0)
        if st.button("حفظ التعديلات"): st.success("تم الحفظ بنجاح!")

# --- صفحة الحاسبة الهندسية (المعادلات الدقيقة) ---
elif st.session_state.current_page == "calc":
    st.markdown("<h2>🚀 الحاسبة الهندسية المطورة</h2>", unsafe_allow_html=True)
    with st.expander("أدخل بيانات الاستهلاك", expanded=True):
        d_amp = st.number_input("الأمبير المطلوب نهاراً:", value=10.0)
        n_amp = st.number_input("الأمبير المطلوب ليلاً:", value=5.0)
        hrs = st.select_slider("ساعات تشغيل البطارية:", options=[2,4,6,8,10,12], value=4)
        p_watt = st.selectbox("قدرة اللوح:", [400, 550, 585, 670], index=1)
        
        if st.button("احسب النتائج"):
            panels = round((d_amp * 230) / (p_watt * 0.75))
            st.success(f"تحتاج إلى {max(1, panels)} لوح شمسي.")

# --- صفحة تسجيل الشركات ---
elif st.session_state.current_page == "reg_co":
    st.markdown("<h2>🏢 سجل شركتك الآن</h2>", unsafe_allow_html=True)
    st.text_input("اسم الشركة")
    st.text_area("وصف الخدمات")
    st.button("إرسال الطلب")

# 6. ناف بار سفلي (ثابت وواضح)
st.markdown("<div class='nav-bar'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("🏠 الرئيسية", on_click=lambda: navigate_to("home"))
with c2: st.button("🏢 سجل شركتك", on_click=lambda: navigate_to("reg_co"))
with c3: st.button("🎁 خصومات")
with c4: st.button("👤 حسابي", on_click=lambda: navigate_to("profile"))
