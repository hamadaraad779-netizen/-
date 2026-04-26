import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="منصة طاقة العراق", layout="wide", initial_sidebar_state="collapsed")

# 2. إدارة البيانات والحالة
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'approved_cos' not in st.session_state:
    st.session_state.approved_cos = [
        {"name": "شركة الرافدين للطاقة", "city": "بغداد", "phone": "07801112223"},
        {"name": "طاقة الجنوب المحدودة", "city": "البصرة", "phone": "07704445556"}
    ]

def navigate_to(page):
    st.session_state.current_page = page

# 3. CSS "التصميم الجمالي والوضوح المطلق"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* الأساسيات */
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #ffffff; }

    /* النصوص - أسود ملكي غامق جداً للوضوح */
    h1, h2, h3, h4, p, label, span {
        color: #1a1a1a !important;
        font-weight: 900 !important;
    }

    /* بانر الترحيب العلوي - تصميم منحني */
    .hero-section {
        background: linear-gradient(135deg, #0052D4 0%, #4364F7 50%, #6FB1FC 100%);
        padding: 40px 20px;
        border-radius: 0px 0px 40px 40px;
        color: white !important;
        text-align: center;
        margin: -60px -20px 30px -20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .hero-section h1 { color: white !important; margin-bottom: 5px; font-size: 1.8rem; }
    .hero-section p { color: #e0e0e0 !important; font-weight: 400 !important; }

    /* البطاقات المربعة (مثل بلي) */
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        padding: 10px;
    }
    .option-card {
        background: #f8faff;
        border: 2px solid #e0e7ff;
        border-radius: 24px;
        padding: 20px;
        text-align: center;
        transition: 0.3s;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 160px;
    }
    .option-card img { width: 55px; height: 55px; margin-bottom: 12px; }
    .option-card h4 { font-size: 1rem; margin: 0; color: #003366 !important; }

    /* خانات الإدخال - حدود واضحة جداً */
    div[data-baseweb="input"] {
        border: 2.5px solid #003366 !important;
        border-radius: 16px !important;
        background: white !important;
    }
    input { color: black !important; font-size: 1.1rem !important; }

    /* صندوق النتائج - أخضر مشبع */
    .result-box {
        background: #f0fff4;
        border: 3px solid #22c55e;
        border-radius: 20px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(34, 197, 94, 0.15);
    }

    /* شريط التنقل السفلي الاحترافي */
    .bottom-nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; border-top: 1px solid #eee;
        display: flex; justify-content: space-around;
        padding: 10px 0; z-index: 1000;
        box-shadow: 0 -5px 15px rgba(0,0,0,0.05);
    }

    /* إخفاء واجهة ستريم ليت */
    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-top: 0rem; padding-bottom: 7rem; }
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown("""
        <div class='hero-section'>
            <h1>أهلاً بك، محمد صادق 👋</h1>
            <p>منصة الطاقة الشمسية الأولى في العراق</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="option-card"><img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png"><h4>حساب المنظومة</h4></div>', unsafe_allow_html=True)
        st.button("افتح الحاسبة", key="btn_calc", use_container_width=True, on_click=navigate_to, args=("calc",))
        
        st.markdown('<div class="option-card"><img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png"><h4>طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز فني", key="btn_fix", use_container_width=True)

    with col2:
        st.markdown('<div class="option-card"><img src="https://cdn-icons-png.flaticon.com/512/995/995260.png"><h4>دليل الشركات</h4></div>', unsafe_allow_html=True)
        st.button("تصفح المجهزين", key="btn_cos", use_container_width=True, on_click=navigate_to, args=("cos_list",))

        st.markdown('<div class="option-card"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><h4>تسجيل شركة</h4></div>', unsafe_allow_html=True)
        st.button("أضف شركتك", key="btn_reg", use_container_width=True, on_click=navigate_to, args=("cos_reg",))

# --- صفحة الحاسبة (بالمعادلات الدقيقة والوضوح) ---
elif st.session_state.current_page == "calc":
    st.markdown("<h2 style='text-align:center; color:#003366;'>📊 حاسبة الأحمال والألواح</h2>", unsafe_allow_html=True)
    
    with st.container():
        amp_day = st.number_input("الاستخدام النهاري (أمبير):", value=10, step=1)
        amp_night = st.number_input("الاستخدام الليلي (أمبير):", value=5, step=1)
        hours_night = st.number_input("عدد ساعات التشغيل الليلي (اكتب الرقم):", value=6, step=1)
        
        if st.button("احسب النتائج الآن ✨", use_container_width=True):
            # معادلة الألواح
            total_panels = round(((amp_day * 230) + (amp_night * 230 * 0.2)) / 450) + 2
            
            # معادلة البطارية الذكية
            cap_check = amp_night * hours_night
            if cap_check <= 100: bat_cap = "5 كيلو واط (5 kWh)"
            elif cap_check <= 200: bat_cap = "10 كيلو واط (10 kWh)"
            else: bat_cap = "15 كيلو واط (15 kWh)"
            
            st.markdown(f"""
                <div class='result-box'>
                    <h3 style='color:#16a34a;'>✅ التقرير الفني:</h3>
                    <p style='font-size:1.2rem;'>• عدد الألواح: <span style='color:#003366;'>{total_panels} ألواح (550W)</span></p>
                    <p style='font-size:1.2rem;'>• سعة البطارية: <span style='color:#003366;'>{bat_cap}</span></p>
                </div>
            """, unsafe_allow_html=True)
            
    st.button("⬅️ العودة للرئيسية", on_click=navigate_to, args=("home",), use_container_width=True)

# --- صفحة دليل الشركات ---
elif st.session_state.current_page == "cos_list":
    st.markdown("<h2 style='text-align:center;'>🏢 الشركات المعتمدة</h2>", unsafe_allow_html=True)
    for co in st.session_state.approved_cos:
        st.markdown(f"""
            <div style='background:#f8faff; border:2px solid #003366; padding:15px; border-radius:15px; margin-bottom:12px;'>
                <h4 style='margin:0; color:#003366;'>{co['name']}</h4>
                <p style='margin:5px 0;'>📍 {co['city']} | 📞 {co['phone']}</p>
            </div>
        """, unsafe_allow_html=True)
    st.button("⬅️ عودة", on_click=navigate_to, args=("home",), use_container_width=True)

# --- صفحة تسجيل الشركات (بالموافقة) ---
elif st.session_state.current_page == "cos_reg":
    st.markdown("<h2 style='text-align:center;'>📝 تسجيل طلب انضمام</h2>", unsafe_allow_html=True)
    with st.form("reg_form"):
        name = st.text_input("اسم الشركة")
        city = st.text_input("المحافظة")
        phone = st.text_input("رقم الهاتف")
        code = st.text_input("كود الموافقة الإداري", type="password")
        if st.form_submit_button("تفعيل التسجيل"):
            if code == "1234":
                st.session_state.approved_cos.append({"name": name, "city": city, "phone": phone})
                st.success("تم التفعيل بنجاح!")
            else:
                st.error("الكود غير صحيح، يرجى مراجعة الإدارة.")
    st.button("⬅️ عودة", on_click=navigate_to, args=("home",), use_container_width=True)

# 5. شريط التنقل السفلي (أزرار واضحة بصف واحد)
st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)
nav_cols = st.columns(4)
with nav_cols[0]: st.button("🏠 الرئيسية", on_click=navigate_to, args=("home",), use_container_width=True)
with nav_cols[1]: st.button("🏢 الشركات", on_click=navigate_to, args=("cos_list",), use_container_width=True)
with nav_cols[2]: st.button("📝 التسجيل", on_click=navigate_to, args=("cos_reg",), use_container_width=True)
with nav_cols[3]: st.button("👤 حسابي", use_container_width=True)
