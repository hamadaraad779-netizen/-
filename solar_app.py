import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. إدارة الصفحات والبيانات
if 'user_data' not in st.session_state: st.session_state.user_data = None
if 'current_page' not in st.session_state: st.session_state.current_page = "login"

def navigate_to(page):
    st.session_state.current_page = page

# 3. CSS "الوضوح العالي" وعودة التصميم المربع
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* خلفية التطبيق بيضاء تماماً للوضوح */
    .stApp { background-color: #ffffff; }

    /* بانر الترحيب - أزرق ناصع بنص أبيض */
    .welcome-banner {
        background: linear-gradient(135deg, #007bff 0%, #00d4ff 100%);
        padding: 40px 20px; border-radius: 25px;
        color: white !important; text-align: center;
        margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,123,255,0.2);
    }
    .welcome-banner h1 { color: white !important; font-weight: 900 !important; font-size: 2.2rem; }

    /* تصميم البطاقة المربعة (عودة الشكل المطلوب) */
    .card-box {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-bottom: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 160px;
    }
    .card-box img { width: 60px; height: 60px; margin-bottom: 15px; }
    .card-box h4 { color: #1a1a1a !important; font-weight: 900; font-size: 1.1rem; margin: 0; }

    /* تنسيق الخانات لتكون مستطيلة وواضحة (اسم، رقم، محافظة) */
    div[data-baseweb="input"], .stSelectbox {
        background-color: white !important;
        border: 2px solid #007bff !important;
        border-radius: 12px !important;
    }
    input { color: #000 !important; font-weight: 700 !important; }
    label { color: #000 !important; font-weight: 900 !important; }

    /* شريط التنقل السفلي - ترتيب أفقي ثابت */
    .footer-nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; border-top: 1px solid #eee;
        padding: 10px 0; z-index: 1000;
        display: flex; justify-content: space-around;
    }
    
    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 8rem; }
    </style>
    """, unsafe_allow_html=True)

# 4. منطق الصفحات
# --- صفحة التسجيل (الاسم، الرقم، المحافظة) ---
if st.session_state.current_page == "login" and st.session_state.user_data is None:
    st.markdown("<div class='welcome-banner'><h1>مرحباً بك ☀️</h1><p>سجل بياناتك للبدء</p></div>", unsafe_allow_html=True)
    u_name = st.text_input("الحقل الأول: الاسم الكامل")
    u_phone = st.text_input("الحقل الثاني: رقم الموبايل")
    u_city = st.selectbox("الحقل الثالث: المحافظة", ["بغداد", "البصرة", "أربيل", "الموصل", "النجف", "كربلاء", "أخرى"])
    
    if st.button("دخول للمنصة", use_container_width=True):
        if u_name and u_phone:
            st.session_state.user_data = {"name": u_name, "phone": u_phone, "city": u_city}
            navigate_to("home")
            st.rerun()

# --- الصفحة الرئيسية (البطاقات المربعة) ---
elif st.session_state.current_page == "home":
    st.markdown(f"<div class='welcome-banner'><h1>أهلاً، {st.session_state.user_data['name']}</h1><p>محافظة {st.session_state.user_data['city']}</p></div>", unsafe_allow_html=True)
    
    # توزيع البطاقات بشكل شبكة (2 في كل صف)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card-box"><img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png"><h4>حساب المنظومة</h4></div>', unsafe_allow_html=True)
        st.button("فتح الحاسبة", key="btn_calc", use_container_width=True, on_click=navigate_to, args=("calculator",))
        
        st.markdown('<div class="card-box"><img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png"><h4>طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز فني", key="btn_fix", use_container_width=True)

    with col2:
        st.markdown('<div class="card-box"><img src="https://cdn-icons-png.flaticon.com/512/995/995260.png"><h4>دليل الشركات</h4></div>', unsafe_allow_html=True)
        st.button("تصفح الشركات", key="btn_co", use_container_width=True, on_click=navigate_to, args=("companies",))

        st.markdown('<div class="card-box"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><h4>إعدادات حسابي</h4></div>', unsafe_allow_html=True)
        st.button("تعديل بياناتي", key="btn_prof", use_container_width=True, on_click=navigate_to, args=("profile",))

# --- صفحة حسابي (عرض وتعديل) ---
elif st.session_state.current_page == "profile":
    st.markdown("### 👤 ملفي الشخصي")
    st.write(f"الاسم الحالي: **{st.session_state.user_data['name']}**")
    st.write(f"رقم الهاتف: **{st.session_state.user_data['phone']}**")
    if st.button("⬅️ عودة للرئيسية"): navigate_to("home")

# 5. شريط التنقل السفلي الثابت (بصف واحد)
if st.session_state.user_data:
    st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
    with nav_col1: st.button("🏠 الرئيسية", key="n1", on_click=navigate_to, args=("home",))
    with nav_col2: st.button("🏢 الشركات", key="n2", on_click=navigate_to, args=("companies",))
    with nav_col3: st.button("🎁 خصومات", key="n3")
    with nav_col4: st.button("👤 حسابي", key="n4", on_click=navigate_to, args=("profile",))
