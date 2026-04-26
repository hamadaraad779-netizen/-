import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="العراق للطاقة الشمسية", layout="wide")

# 2. إدارة الحالة (Navigation & Data)
if 'current_page' not in st.session_state: st.session_state.current_page = "register"
if 'user_data' not in st.session_state: st.session_state.user_data = {"name": "", "city": ""}
if 'is_registered' not in st.session_state: st.session_state.is_registered = False

def navigate_to(page): st.session_state.current_page = page

# 3. تصميم الـ CSS المتقدم (وضوح الحقول + استجابة الألوان)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* وضوح الحقول (Inputs) */
    div[data-baseweb="input"], div[data-baseweb="select"], .stNumberInput {
        background-color: #fcfcfc !important;
        border: 2px solid #0056b3 !important; /* لون أزرق واضح للحدود */
        border-radius: 10px !important;
    }
    
    /* ألوان النصوص والنتائج */
    .result-box {
        background-color: #e6f3ff;
        color: #001a33;
        padding: 20px;
        border-radius: 15px;
        border-right: 10px solid #0056b3;
        margin: 10px 0px;
        font-weight: bold;
    }
    
    .stButton>button {
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
    }

    /* البانر العلوي */
    .top-banner {
        background: linear-gradient(135deg, #0056b3 0%, #001a33 100%);
        padding: 25px; border-radius: 15px; color: white;
        text-align: center; margin-bottom: 20px;
    }
    
    /* تنسيق دليل الشركات */
    .company-card {
        background: white; border: 1px solid #ddd;
        padding: 15px; border-radius: 10px; margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 4. منطق الصفحات
# --- صفحة التسجيل الأولية ---
if st.session_state.current_page == "register":
    st.markdown("<div class='top-banner'><h1>مرحباً بك في منصة طاقة العراق</h1><p>يرجى إدخال بياناتك للمتابعة</p></div>", unsafe_allow_html=True)
    with st.container():
        name = st.text_input("الاسم الكامل (المستخدم):")
        city = st.selectbox("المحافظة:", ["بغداد", "البصرة", "الموصل", "أربيل", "النجف", "كربلاء", "أخرى"])
        if st.button("دخول التطبيق 🚀", use_container_width=True):
            if name:
                st.session_state.user_data = {"name": name, "city": city}
                st.session_state.current_page = "home"
                st.rerun()

# --- الصفحة الرئيسية ---
elif st.session_state.current_page == "home":
    st.markdown(f"<div class='top-banner'><h3>أهلاً {st.session_state.user_data['name']}</h3><p>دليل وخدمات الطاقة الشمسية في {st.session_state.user_data['city']}</p></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("📊 حاسبة المنظومة", use_container_width=True, on_click=navigate_to, args=("calc",))
        st.button("🏢 دليل الشركات المعتمدة", use_container_width=True, on_click=navigate_to, args=("directory",))
    with col2:
        st.button("📝 تسجيل شركة جديدة", use_container_width=True, on_click=navigate_to, args=("reg_company",))
        st.button("👤 بيانات حسابي", use_container_width=True, on_click=navigate_to, args=("profile",))

# --- صفحة الحاسبة المحدثة ---
elif st.session_state.current_page == "calc":
    st.header("📊 حاسبة المنظومة الشمسية")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("##### الإستهلاك النهاري")
        a_day = st.number_input("الأمبير المطلوب نهاراً (A):", min_value=1, value=10)
    with col_b:
        st.markdown("##### الإستهلاك الليلي (البطاريات)")
        a_night = st.number_input("الأمبير المطلوب ليلاً (A):", min_value=1, value=5)
        h_night = st.slider("عدد ساعات التشغيل المطلوبة في الليل:", 2, 16, 6)

    if st.button("احسب احتياجك الآن ✨", use_container_width=True):
        panels = round((a_day * 230) / 400) # معادلة تقريبية للألواح
        batt_cap = (a_night * h_night * 230) / 1000 # كيلو واط ساعة
        
        st.markdown(f"""
            <div class='result-box'>
                <p>☀️ عدد الألواح المقترح (550 واط): {panels} لوح</p>
                <p>🔋 سعة البطاريات المطلوبة: {batt_cap:.1f} كيلو واط (kWh)</p>
                <p>⏱️ مدة التغطية الليلية: {h_night} ساعة مستمرة</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.button("⬅️ عودة للرئيسية", on_click=navigate_to, args=("home",))

# --- صفحة تسجيل الشركات (جديدة) ---
elif st.session_state.current_page == "reg_company":
    st.header("📝 تسجيل شركة في المنصة")
    st.info("سيتم مراجعة بيانات الشركة من قبل الإدارة والموافقة عليها.")
    with st.form("company_form"):
        c_name = st.text_input("اسم الشركة الرسمي:")
        c_location = st.text_input("عنوان المقر الرئيسي:")
        c_phone = st.text_input("رقم هاتف التواصل:")
        c_work = st.multiselect("خدمات الشركة:", ["تركيب منظومات", "بيع بطاريات", "صيانة", "ألواح شمسية"])
        if st.form_submit_button("إرسال الطلب للموافقة"):
            st.success("تم إرسال معلوماتك بنجاح! سيتم التواصل معك قريباً.")

    st.button("⬅️ عودة للرئيسية", on_click=navigate_to, args=("home",))

# --- صفحة دليل الشركات ---
elif st.session_state.current_page == "directory":
    st.header("🏢 دليل الشركات المعتمدة")
    search = st.text_input("🔍 ابحث عن شركة أو محافظة...")
    
    companies = [
        {"name": "رافدين للطاقة", "city": "بغداد", "status": "معتمدة ✅"},
        {"name": "نجمة البصرة", "city": "البصرة", "status": "معتمدة ✅"}
    ]
    
    for comp in companies:
        st.markdown(f"""
            <div class='company-card'>
                <h4>{comp['name']}</h4>
                <p>📍 الموقع: {comp['city']} | الحالة: {comp['status']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.button("⬅️ عودة للرئيسية", on_click=navigate_to, args=("home",))

# --- صفحة حسابي ---
elif st.session_state.current_page == "profile":
    st.header("👤 حسابي")
    st.write(f"**الاسم:** {st.session_state.user_data['name']}")
    st.write(f"**الموقع:** {st.session_state.user_data['city']}")
    if st.button("تعديل البيانات"):
        st.session_state.current_page = "register"
        st.rerun()
    st.button("⬅️ عودة للرئيسية", on_click=navigate_to, args=("home",))
