import streamlit as st

st.set_page_config(page_title="منصة طاقة العراق", layout="wide")

# الحالة
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

if 'approved_cos' not in st.session_state:
    st.session_state.approved_cos = [
        {"name": "شركة الرافدين للطاقة", "city": "بغداد", "phone": "07801112223"},
        {"name": "طاقة الجنوب المحدودة", "city": "البصرة", "phone": "07704445556"}
    ]

def navigate_to(page):
    st.session_state.current_page = page

# 🎨 CSS محدث
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

* {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
}

/* خلفية */
.stApp {
    background-color: #F8FAFC;
}

/* نصوص عامة بالازرق */
h1, h2, h3, h4, p, label {
    color: #1D4ED8 !important;
}

/* بانر */
.hero {
    background: linear-gradient(135deg, #1D4ED8, #3B82F6);
    padding: 40px;
    border-radius: 0 0 30px 30px;
    text-align: center;
    color: white !important;
}

/* كروت */
.card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 15px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
}

/* الشركات بالاسود */
.company-card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 15px;
    color: black !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
}

/* أزرار */
.stButton > button {
    background: linear-gradient(135deg, #1D4ED8, #2563EB);
    color: white;
    border-radius: 10px;
    height: 45px;
    font-weight: bold;
}

/* مدخلات */
div[data-baseweb="input"] {
    background-color: white;
    border: 2px solid #3B82F6;
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
        <p>احسب منظومتك بسهولة</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'><h3>📐 الحاسبة</h3></div>", unsafe_allow_html=True)
        st.button("افتح الحاسبة", use_container_width=True, on_click=navigate_to, args=("calc",))

    with col2:
        st.markdown("<div class='card'><h3>🏢 الشركات</h3></div>", unsafe_allow_html=True)
        st.button("دليل الشركات", use_container_width=True, on_click=navigate_to, args=("cos_list",))


# ---------------- CALCULATOR ----------------
elif st.session_state.current_page == "calc":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2>📊 الحاسبة</h2>", unsafe_allow_html=True)

    amp_day = st.number_input("الاستخدام النهاري", value=10)
    amp_night = st.number_input("الاستخدام الليلي", value=5)
    hours = st.number_input("الساعات", value=6)

    if st.button("احسب 🚀"):
        res = amp_night * hours
        bat = "5kW" if res <= 100 else "10kW" if res <= 200 else "15kW"
        st.success(f"🔋 البطارية المطلوبة: {bat}")

    st.markdown("</div>", unsafe_allow_html=True)

    st.button("⬅️ رجوع", on_click=navigate_to, args=("home",))


# ---------------- COMPANIES ----------------
elif st.session_state.current_page == "cos_list":

    st.markdown("<h2 style='color:black;'>🏢 دليل الشركات</h2>", unsafe_allow_html=True)

    # عرض الشركات
    for co in st.session_state.approved_cos:
        st.markdown(f"""
        <div class='company-card'>
            <h4>{co['name']}</h4>
            <p>📍 {co['city']}</p>
            <p>📞 {co['phone']}</p>
        </div>
        """, unsafe_allow_html=True)

    # ➕ إضافة شركة جديدة
    st.markdown("### ➕ إضافة شركة جديدة")

    name = st.text_input("اسم الشركة")
    city = st.text_input("المدينة")
    phone = st.text_input("رقم الهاتف")

    if st.button("إضافة الشركة"):
        if name and city and phone:
            st.session_state.approved_cos.append({
                "name": name,
                "city": city,
                "phone": phone
            })
            st.success("تمت إضافة الشركة بنجاح ✅")
        else:
            st.error("يرجى ملء جميع الحقول")

    st.button("⬅️ رجوع", on_click=navigate_to, args=("home",))
