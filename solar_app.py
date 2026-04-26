import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة طاقة العراق", layout="wide")

# 2. إدارة البيانات
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'approved_cos' not in st.session_state:
    st.session_state.approved_cos = [
        {"name": "شركة الرافدين للطاقة", "city": "بغداد", "phone": "07801112223"},
        {"name": "طاقة الجنوب المحدودة", "city": "البصرة", "phone": "07704445556"}
    ]

def navigate_to(page): st.session_state.current_page = page

# 3. CSS التصميم (نصوص بيضاء ووضوح عالي)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #ffffff; }

    /* تحويل كل النصوص الأساسية في الأزرار والبطاقات إلى الأبيض */
    button p, .stButton button { 
        color: white !important; 
        font-weight: 900 !important; 
        font-size: 1.1rem !important;
    }

    /* العناوين داخل البطاقات ملونة لتبرز */
    .hero-section h1, .hero-section p { color: white !important; }
    
    /* جعل خانات الإدخال (الأرقام) واضحة جداً: خلفية بيضاء ونصوص سوداء */
    div[data-baseweb="input"] {
        background-color: white !important;
        border: 2px solid #0052D4 !important;
        border-radius: 12px !important;
    }
    input { 
        color: #000000 !important; 
        font-weight: 800 !important; 
        font-size: 1.2rem !important; 
    }

    /* البانر العلوي */
    .hero-section {
        background: linear-gradient(135deg, #0052D4 0%, #4364F7 100%);
        padding: 40px 20px;
        border-radius: 0px 0px 30px 30px;
        text-align: center;
        margin: -60px -20px 30px -20px;
    }

    /* أزرار الدليل والتسجيل - خلفية داكنة ونصوص بيضاء ناصعة */
    .stButton > button {
        background-color: #1a1a1a !important;
        border-radius: 12px !important;
        border: none !important;
        height: 50px;
    }

    /* إخفاء واجهة ستريم ليت */
    [data-testid="stHeader"], footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
if st.session_state.current_page == "home":
    st.markdown("""<div class='hero-section'><h1>أهلاً بك، محمد صادق 👋</h1>
    <p>منصة الطاقة الشمسية الأولى في العراق</p></div>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align:center;'>📐 الحاسبة</h4>", unsafe_allow_html=True)
        st.button("افتح الحاسبة 🚀", use_container_width=True, on_click=navigate_to, args=("calc",))
    with col2:
        st.markdown("<h4 style='text-align:center;'>🏢 الشركات</h4>", unsafe_allow_html=True)
        st.button("دليل الشركات 📋", use_container_width=True, on_click=navigate_to, args=("cos_list",))

elif st.session_state.current_page == "calc":
    st.markdown("<h2 style='text-align:center;'>📊 حاسبة المنظومة</h2>", unsafe_allow_html=True)
    
    # هنا حقول الأرقام ستظهر بخلفية بيضاء وخط أسود واضح جداً
    amp_day = st.number_input("الاستخدام النهاري (أمبير):", value=10)
    amp_night = st.number_input("الاستخدام الليلي (أمبير):", value=5)
    hours = st.number_input("ساعات التشغيل الليلي:", value=6)
    
    if st.button("احسب النتائج الآن ✨", use_container_width=True):
        res = amp_night * hours
        bat = "5kW" if res <= 100 else "10kW" if res <= 200 else "15kW"
        st.success(f"النتيجة: تحتاج بطارية بسعة {bat}")

    st.button("⬅️ عودة", on_click=navigate_to, args=("home",))

# صفحة الشركات والتسجيل (بنفس منطق الخط الأبيض الواضح)
elif st.session_state.current_page == "cos_list":
    st.markdown("<h3>🏢 الشركات المعتمدة</h3>", unsafe_allow_html=True)
    for co in st.session_state.approved_cos:
        st.info(f"{co['name']} - {co['city']} - {co['phone']}")
    st.button("⬅️ عودة", on_click=navigate_to, args=("home",))
