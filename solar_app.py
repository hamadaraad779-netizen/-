import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="منصة طاقة العراق", layout="wide")

# إدارة الحالة
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

if 'approved_cos' not in st.session_state:
    st.session_state.approved_cos = [
        {"name": "شركة الرافدين للطاقة", "city": "بغداد", "phone": "07801112223"},
        {"name": "طاقة الجنوب المحدودة", "city": "البصرة", "phone": "07704445556"}
    ]

def navigate_to(page):
    st.session_state.current_page = page

# 🎨 نظام ألوان احترافي
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

* {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
}

/* الخلفية */
.stApp {
    background-color: #F8FAFC;
}

/* بانر علوي */
.hero {
    background: linear-gradient(135deg, #f59e0b, #fbbf24);
    padding: 40px;
    border-radius: 0 0 30px 30px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

/* كروت */
.card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* أزرار */
.stButton > button {
    background: linear-gradient(135deg, #f59e0b, #f97316);
    color: white;
    border: none;
    border-radius: 12px;
    height: 50px;
    font-weight: bold;
}

/* مدخلات */
div[data-baseweb="input"] {
    background-color: white;
    border: 2px solid #e5e7eb;
    border-radius: 10px;
}

input {
    color: black !important;
    font-weight: bold;
}

/* إخفاء */
[data-testid="stHeader"], footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------
if st.session_state.current_page == "home":
    st.markdown("""
    <div class='hero'>
        <h1>☀️ منصة الطاقة الشمسية</h1>
        <p>احسب منظومتك بسهولة وتواصل مع أفضل الشركات</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'><h3>📐 الحاسبة</h3><p>احسب احتياجك من الطاقة بسهولة</p></div>", unsafe_allow_html=True)
        st.button("افتح الحاسبة", use_container_width=True, on_click=navigate_to, args=("calc",))

    with col2:
        st.markdown("<div class='card'><h3>🏢 الشركات</h3><p>تصفح أفضل الشركات المعتمدة</p></div>", unsafe_allow_html=True)
        st.button("دليل الشركات", use_container_width=True, on_click=navigate_to, args=("cos_list",))


# ---------------- CALCULATOR ----------------
elif st.session_state.current_page == "calc":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<h2>📊 حاسبة الطاقة</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        amp_day = st.number_input("الاستخدام النهاري (أمبير)", value=10)

    with col2:
        amp_night = st.number_input("الاستخدام الليلي (أمبير)", value=5)

    hours = st.number_input("ساعات التشغيل الليلي", value=6)

    if st.button("احسب الآن 🚀", use_container_width=True):
        res = amp_night * hours
        bat = "5kW" if res <= 100 else "10kW" if res <= 200 else "15kW"

        st.success(f"🔋 تحتاج بطارية بسعة: {bat}")

    st.markdown("</div>", unsafe_allow_html=True)

    st.button("⬅️ رجوع", on_click=navigate_to, args=("home",))


# ---------------- COMPANIES ----------------
elif st.session_state.current_page == "cos_list":

    st.markdown("<h2>🏢 الشركات المعتمدة</h2>", unsafe_allow_html=True)

    for co in st.session_state.approved_cos:
        st.markdown(f"""
        <div class='card'>
            <h4>{co['name']}</h4>
            <p>📍 {co['city']}</p>
            <p>📞 {co['phone']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.button("⬅️ رجوع", on_click=navigate_to, args=("home",))
