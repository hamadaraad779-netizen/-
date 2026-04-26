import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية", layout="wide")

# 2. مخزن البيانات (Database Simulation)
if 'user_data' not in st.session_state: st.session_state.user_data = None
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
# قاعدة بيانات الشركات (يمكنك الإضافة إليها من لوحة الإدارة)
if 'companies_list' not in st.session_state:
    st.session_state.companies_list = [
        {"name": "شركة شمس الرافدين", "city": "بغداد", "phone": "07801234567", "info": "مجهز معتمد لألواح Jinko"},
        {"name": "شركة طاقة المستقبل", "city": "البصرة", "phone": "07709876543", "info": "متخصصون ببطاريات الليثيوم"}
    ]

def navigate_to(page): st.session_state.current_page = page

# 3. CSS التصميم الفاخر (إصلاح القوائم والألوان)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #ffffff; }
    
    /* البانر العلوي */
    .hero {
        background: linear-gradient(135deg, #007bff 0%, #00d4ff 100%);
        padding: 30px; border-radius: 20px; color: white; text-align: center; margin-bottom: 20px;
    }

    /* البطاقات المربعة (الرئيسية) */
    .card {
        background: #f8f9fa; border: 1px solid #eee; border-radius: 15px;
        padding: 20px; text-align: center; margin-bottom: 10px; min-height: 150px;
    }
    .card h4 { color: #333 !important; font-weight: 900; }

    /* شريط التنقل السفلي الثابت بصف واحد */
    .nav-bar {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; border-top: 1px solid #ddd;
        padding: 10px 0; z-index: 1000;
    }

    /* إصلاح مدخلات البيانات */
    div[data-baseweb="input"] { border: 2px solid #007bff !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. شاشة التسجيل
if st.session_state.user_data is None:
    st.markdown("<div class='hero'><h1>أهلاً بك ☀️</h1><p>الرجاء تسجيل الدخول أولاً</p></div>", unsafe_allow_html=True)
    n = st.text_input("الأسم الكامل")
    p = st.text_input("رقم الهاتف")
    c = st.selectbox("المحافظة", ["بغداد", "البصرة", "أربيل", "الموصل", "أخرى"])
    if st.button("دخول للمنصة", use_container_width=True):
        if n and p:
            st.session_state.user_data = {"name": n, "phone": p, "city": c}
            st.rerun()
    st.stop()

# 5. محتوى الصفحات
# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown(f"<div class='hero'><h1>أهلاً {st.session_state.user_data['name']}</h1></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h4>🚀 الحاسبة الهندسية</h4></div>', unsafe_allow_html=True)
        st.button("احسب الآن", key="go_calc", on_click=navigate_to, args=("calc",), use_container_width=True)
        st.markdown('<div class="card"><h4>🛠️ طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز فني", key="go_fix", use_container_width=True)
    with col2:
        st.markdown('<div class="card"><h4>🏢 دليل الشركات</h4></div>', unsafe_allow_html=True)
        st.button("تصفح المجهزين", key="go_cos", on_click=navigate_to, args=("cos",), use_container_width=True)
        st.markdown('<div class="card"><h4>⚙️ لوحة الإدارة</h4></div>', unsafe_allow_html=True)
        st.button("إضافة شركة", key="go_admin", on_click=navigate_to, args=("admin",), use_container_width=True)

# --- صفحة الحاسبة (تعمل الآن) ---
elif st.session_state.current_page == "calc":
    st.markdown("### 📊 حاسبة المنظومة")
    amp = st.number_input("الأمبير المطلوب:", value=10)
    hrs = st.slider("ساعات التشغيل ليلاً:", 2, 12, 4)
    if st.button("توليد النتائج"):
        st.success(f"النتيجة: تحتاج {round(amp*1.5)} لوح، وبطارية سعة {amp*hrs*0.5} kWh")

# --- صفحة دليل الشركات (تعرض البيانات الحقيقية) ---
elif st.session_state.current_page == "cos":
    st.markdown("### 🏢 الشركات المسجلة")
    for co in st.session_state.companies_list:
        with st.expander(f"{co['name']} - {co['city']}"):
            st.write(f"📞 هاتف: {co['phone']}")
            st.write(f"📝 نبذة: {co['info']}")
            st.button(f"اتصال بـ {co['name']}", key=co['name'])

# --- لوحة الإدارة (لإضافة بيانات جديدة) ---
elif st.session_state.current_page == "admin":
    st.markdown("### ⚙️ إضافة شركة جديدة للدليل")
    with st.form("add_co"):
        new_n = st.text_input("اسم الشركة")
        new_c = st.selectbox("المحافظة", ["بغداد", "البصرة", "أربيل", "أخرى"])
        new_p = st.text_input("رقم التواصل")
        new_i = st.text_area("وصف الخدمة")
        if st.form_submit_button("حفظ الشركة"):
            st.session_state.companies_list.append({"name": new_n, "city": new_c, "phone": new_p, "info": new_i})
            st.success("تمت الإضافة بنجاح!")

# 6. شريط التنقل السفلي الموحد (بصف واحد)
st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)
nav_cols = st.columns(4)
with nav_cols[0]: st.button("🏠", on_click=navigate_to, args=("home",), use_container_width=True)
with nav_cols[1]: st.button("🏢", on_click=navigate_to, args=("cos",), use_container_width=True)
with nav_cols[2]: st.button("⚙️", on_click=navigate_to, args=("admin",), use_container_width=True)
with nav_cols[3]: st.button("👤", on_click=navigate_to, args=("profile",), use_container_width=True)
