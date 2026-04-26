import streamlit as st

# 1. إعدادات الصفحة (Flutter Style)
st.set_page_config(page_title="العراق للطاقة الشمسية", layout="wide")

# 2. إدارة البيانات (عقل التطبيق - Python Logic)
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'approved_cos' not in st.session_state:
    st.session_state.approved_cos = [
        {"name": "شركة الرافدين للطاقة", "city": "بغداد", "phone": "07801112223"},
        {"name": "طاقة الجنوب المحدودة", "city": "البصرة", "phone": "07704445556"}
    ]

def navigate_to(page):
    st.session_state.current_page = page

# 3. دزاين Flutter (CSS مخصص لجعل الواجهة بيضاء ونصوصها واضحة)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل الخط العام أسود للوضوح والخلفية بيضاء */
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #ffffff; }

    /* دزاين الكروت (Flutter Cards) */
    .flutter-card {
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        border-radius: 25px;
        padding: 30px;
        color: white !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .flutter-card h1, .flutter-card h2, .flutter-card p { color: white !important; }

    /* تنسيق النصوص البيضاء داخل الأزرار */
    .stButton > button {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border-radius: 15px !important;
        height: 55px !important;
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    
    /* خانات الأرقام (المدخلات) - خلفية بيضاء ونصوص سوداء حادة */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 2px solid #1976D2 !important;
        border-radius: 15px !important;
    }
    input { color: #000000 !important; font-weight: 900 !important; font-size: 1.3rem !important; }
    label { color: #1a1a1a !important; font-weight: 800 !important; font-size: 1.1rem !important; }

    /* المخرجات والنتائج */
    .success-card {
        background-color: #e8f5e9;
        border: 2px solid #2e7d32;
        padding: 20px;
        border-radius: 20px;
        color: #1b5e20 !important;
        font-weight: 800;
    }

    /* إخفاء زوائد Streamlit */
    [data-testid="stHeader"], footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. بناء الصفحات (Logic + Design)

# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown("""
        <div class='flutter-card'>
            <h1>أهلاً بك، محمد صادق 👋</h1>
            <p>منصة طاقة العراق - دليلك المتكامل</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='text-align:center;'>🚀 الخدمات</h3>", unsafe_allow_html=True)
        st.button("📐 فتح الحاسبة", on_click=navigate_to, args=("calc",))
        st.button("🔧 طلب صيانة")
    with col2:
        st.markdown("<h3 style='text-align:center;'>🏢 الدليل</h3>", unsafe_allow_html=True)
        st.button("📋 الشركات", on_click=navigate_to, args=("cos_list",))
        st.button("📝 تسجيل شركة", on_click=navigate_to, args=("cos_reg",))

# --- صفحة الحاسبة (العقل البرمجي) ---
elif st.session_state.current_page == "calc":
    st.markdown("<div class='flutter-card'><h2>📐 الحاسبة الهندسية</h2></div>", unsafe_allow_html=True)
    
    # مدخلات واضحة جداً
    amp_day = st.number_input("الاستخدام النهاري (أمبير):", value=10)
    amp_night = st.number_input("الاستخدام الليلي (أمبير):", value=5)
    hours = st.number_input("ساعات التشغيل الليلي (اكتب الرقم):", value=6)
    
    if st.button("توليد النتائج ⚡"):
        # المنطق الرياضي (العقل)
        panels = round(((amp_day * 230) + (amp_night * 230 * 0.2)) / 450) + 2
        capacity_test = amp_night * hours
        
        if capacity_test <= 100: bat = "5 كيلو واط"
        elif capacity_test <= 200: bat = "10 كيلو واط"
        else: bat = "15 كيلو واط"
        
        st.markdown(f"""
            <div class='success-card'>
                ✅ النتائج المقترحة للمنظومة:<br>
                • الألواح المطلوبة: {panels} لوح (550 واط)<br>
                • سعة البطارية: {bat}
            </div>
        """, unsafe_allow_html=True)
    
    st.button("⬅️ عودة للرئيسية", on_click=navigate_to, args=("home",))

# --- دليل الشركات ---
elif st.session_state.current_page == "cos_list":
    st.markdown("<div class='flutter-card'><h2>🏢 الشركات المعتمدة</h2></div>", unsafe_allow_html=True)
    for co in st.session_state.approved_cos:
        st.markdown(f"""
            <div style='border:2px solid #1976D2; padding:15px; border-radius:15px; margin-bottom:10px;'>
                <b style='color:#1976D2;'>{co['name']}</b><br>
                📍 {co['city']} | 📞 {co['phone']}
            </div>
        """, unsafe_allow_html=True)
    st.button("⬅️ عودة", on_click=navigate_to, args=("home",))

# --- تسجيل الشركات ---
elif st.session_state.current_page == "cos_reg":
    st.markdown("<div class='flutter-card'><h2>📝 تسجيل شركة جديدة</h2></div>", unsafe_allow_html=True)
    with st.form("reg_form"):
        name = st.text_input("اسم الشركة")
        city = st.text_input("المحافظة")
        phone = st.text_input("الهاتف")
        code = st.text_input("كود الموافقة", type="password")
        if st.form_submit_button("تفعيل التسجيل"):
            if code == "1234":
                st.session_state.approved_cos.append({"name": name, "city": city, "phone": phone})
                st.success("تم الإضافة!")
            else: st.error("الكود خاطئ")
    st.button("⬅️ عودة", on_click=navigate_to, args=("home",))

# 5. شريط التنقل السفلي (Floating Nav Bar)
st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)
nav = st.columns(4)
with nav[0]: st.button("🏠", on_click=navigate_to, args=("home",))
with nav[1]: st.button("📊", on_click=navigate_to, args=("calc",))
with nav[2]: st.button("🏢", on_click=navigate_to, args=("cos_list",))
with nav[3]: st.button("👤")
