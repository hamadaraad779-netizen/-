import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="العراق للطاقة الشمسية", layout="wide")

# 2. تهيئة البيانات
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'user_data' not in st.session_state: st.session_state.user_data = {"name": "محمد صادق", "city": "بغداد"}

# 3. CSS لفرض الوضوح التام (نصوص زرقاء غامقة وسوداء)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* جعل كل النصوص في التطبيق باللون الأزرق الغامق لضمان الوضوح */
    p, span, label, h1, h2, h3, h4, .stMarkdown {
        color: #002d72 !important; 
        font-weight: 800 !important;
    }

    /* تحسين شكل خانات الإدخال - إطار أزرق غامق وخلفية بيضاء */
    div[data-baseweb="input"], .stNumberInput, .stSelectbox, .stSlider {
        background-color: #ffffff !important;
        border: 3px solid #002d72 !important;
        border-radius: 15px !important;
    }
    
    input { color: #000000 !important; font-size: 1.2rem !important; }

    /* بانر علوي واضح */
    .hero-box {
        background: #007bff;
        padding: 30px; border-radius: 20px;
        text-align: center; color: white !important;
    }
    .hero-box h1, .hero-box p { color: white !important; }

    /* إخفاء القوائم الافتراضية المزعجة */
    [data-testid="stHeader"], footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
def navigate_to(page): st.session_state.current_page = page

# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown(f"""<div class='hero-box'><h1>أهلاً بك، {st.session_state.user_data['name']}</h1>
    <p>من محافظة {st.session_state.user_data['city']}</p></div>""", unsafe_allow_html=True)
    
    st.write("### اختر القسم المطلوب:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 الحاسبة الهندسية", use_container_width=True): navigate_to("calc")
    with col2:
        if st.button("🏢 دليل الشركات", use_container_width=True): navigate_to("cos")

# --- صفحة الحاسبة (تم إرجاع الخانات المطلوبة) ---
elif st.session_state.current_page == "calc":
    st.markdown("<h2 style='color:#002d72;'>📊 حاسبة استهلاك البطارية والمنظومة</h2>", unsafe_allow_html=True)
    
    # الخانات المطلوبة
    amp_day = st.number_input("الأمبير المطلوب (نهاراً):", value=10)
    amp_night = st.number_input("الأمبير المطلوب (ليلاً من البطارية):", value=5)
    hours = st.slider("عدد ساعات عمل البطارية ليلاً:", 2, 12, 6)
    
    if st.button("توليد التقرير النهائي 📊", use_container_width=True):
        st.markdown("---")
        # حسابات تقريبية هندسية
        panels = round((amp_day * 230) / 450) + 2
        battery_size = (amp_night * hours * 230) / 1000
        
        st.markdown(f"""
        <div style='background:#eef6ff; padding:20px; border-radius:15px; border:2px solid #002d72;'>
            <h4 style='margin:0;'>✅ النتيجة المقترحة:</h4>
            <p>• عدد الألواح المطلوبة: {panels} لوح (قدرة 550 واط)</p>
            <p>• سعة البطارية المطلوبة: {battery_size:.1f} kWh</p>
            <p>• توفر لك المنظومة {hours} ساعات عمل فعلية ليلاً بسحب {amp_night} أمبير.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("⬅️ عودة للرئيسية"): navigate_to("home")

# --- صفحة الشركات ---
elif st.session_state.current_page == "cos":
    st.markdown("<h2 style='color:#002d72;'>🏢 مجهزي الطاقة الشمسية</h2>", unsafe_allow_html=True)
    companies = [
        {"n": "شمس الرافدين", "l": "بغداد", "p": "07801234567"},
        {"n": "طاقة المستقبل", "l": "البصرة", "p": "07709876543"}
    ]
    for c in companies:
        st.markdown(f"""
        <div style='background:white; padding:15px; border-radius:12px; border:2px solid #002d72; margin-bottom:10px;'>
            <h4 style='margin:0;'>{c['n']} - {c['l']}</h4>
            <p style='margin:5px 0;'>📞 التواصل: {c['p']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("⬅️ عودة للرئيسية"): navigate_to("home")

# 5. شريط التنقل السفلي (أزرار واضحة بصف واحد)
st.markdown("---")
nav_cols = st.columns(4)
with nav_cols[0]: st.button("🏠 الرئيسية", on_click=navigate_to, args=("home",))
with nav_cols[1]: st.button("🏢 الشركات", on_click=navigate_to, args=("cos",))
with nav_cols[2]: st.button("⚙️ الإدارة")
with nav_cols[3]: st.button("👤 حسابي")
