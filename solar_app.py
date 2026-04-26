import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. CSS متقدم لمحاكاة تصميم التطبيقات (مثل الصورة المرفقة)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    .stApp { background-color: #f8f9fa; color: #333; }
    
    /* تصميم اللافتات (Banners) */
    .banner {
        width: 100%;
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* حاوية المربعات (Grid) */
    .main-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        margin-bottom: 20px;
    }

    /* تصميم البطاقة المربعة */
    .menu-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #eee;
        transition: 0.3s;
        cursor: pointer;
    }
    .menu-card:hover { transform: translateY(-5px); border-color: #007bff; }
    .menu-card img { width: 60px; height: 60px; margin-bottom: 10px; }
    .menu-card h4 { margin: 0; color: #333; font-size: 1.1rem; }

    /* إخفاء عناصر ستريم ليت الافتراضية */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. محاكاة الهيدر (اللافتة العلوية)
st.markdown("""
    <div style="background: linear-gradient(90deg, #0052D4, #4364F7, #6FB1FC); padding: 40px; border-radius: 20px; color: white; text-align: center; margin-bottom: 20px;">
        <h1 style="margin:0;">خصم 20%</h1>
        <p>على أول منظومة تشتريها عبر التطبيق</p>
        <div style="background: white; color: #0052D4; display: inline-block; padding: 5px 20px; border-radius: 50px; font-weight: bold;">
            كود الخصم: SOLAR2026
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. شبكة الخيارات (Grid Menu) مثل الصورة
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="menu-card">
            <img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png">
            <h4>الحاسبة الذكية</h4>
        </div>
    """, unsafe_allow_html=True)
    if st.button("افتح الحاسبة", key="btn_calc"):
        st.session_state.page = "calc"

with col2:
    st.markdown("""
        <div class="menu-card">
            <img src="https://cdn-icons-png.flaticon.com/512/995/995260.png">
            <h4>دليل الشركات</h4>
        </div>
    """, unsafe_allow_html=True)
    if st.button("تصفح الشركات", key="btn_co"):
        st.session_state.page = "companies"

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
        <div class="menu-card">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png">
            <h4>لوحة الإدارة</h4>
        </div>
    """, unsafe_allow_html=True)
    if st.button("دخول المدير", key="btn_admin"):
        st.session_state.page = "admin"

with col4:
    st.markdown("""
        <div class="menu-card">
            <img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png">
            <h4>طلب صيانة</h4>
        </div>
    """, unsafe_allow_html=True)
    st.button("احجز موعد", key="btn_fix")

# 5. عرض المحتوى بناءً على الاختيار
st.write("---")

if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "calc":
    st.markdown("<h2 class='gold-text'>🚀 الحاسبة الهندسية</h2>", unsafe_allow_html=True)
    with st.expander("أدخل بيانات منظومتك", expanded=True):
        day_amp = st.number_input("الأمبير النهاري:", value=10)
        night_amp = st.number_input("الأمبير الليلي:", value=5)
        if st.button("احسب الآن"):
            st.success(f"تحتاج إلى {round((day_amp*230)/(550*0.75))} ألواح تقريباً.")

elif st.session_state.page == "companies":
    st.markdown("<h2>🏢 الشركات المعتمدة</h2>", unsafe_allow_html=True)
    st.info("قائمة الشركات ستظهر هنا..")

# 6. شريط التنقل السفلي (Bottom Navigation) لمحاكاة الموبايل
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: white; border-top: 1px solid #eee; display: flex; justify-content: space-around; padding: 10px; z-index: 1000;">
        <div style="text-align: center; color: #007bff;">🏠<br><small>الرئيسية</small></div>
        <div style="text-align: center; color: #888;">📋<br><small>طلباتي</small></div>
        <div style="text-align: center; color: #888;">🎁<br><small>خصومات</small></div>
        <div style="text-align: center; color: #888;">👤<br><small>حسابي</small></div>
    </div>
    <div style="height: 80px;"></div>
    """, unsafe_allow_html=True)
