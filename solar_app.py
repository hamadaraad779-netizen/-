import streamlit as st
import time

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="طاقتي الشمسية | Premium Solar", layout="wide", initial_sidebar_state="collapsed")

# --- CSS سينمائي فائق التطور ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    * { font-family: 'Cairo', sans-serif; }

    /* خلفية متحركة هادئة */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #030712);
        color: #f8fafc;
    }

    /* أنيميشن الظهور التدريجي */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .hero-text {
        animation: fadeInUp 1s ease-out;
        text-align: center;
        padding: 60px 0;
    }

    /* بطاقة الحاسبة السينمائية */
    .cinema-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 40px;
        padding: 40px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        animation: fadeInUp 1.2s ease-in-out;
        transition: 0.5s;
    }
    
    .cinema-card:hover {
        border-color: #fbbf24;
        box-shadow: 0 0 40px rgba(251, 191, 36, 0.1);
    }

    /* تصميم حقول الإدخال */
    .stNumberInput input {
        background: rgba(255,255,255,0.05) !important;
        color: white !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        padding: 10px !important;
        font-size: 1.2rem !important;
    }

    /* الأزرار السينمائية بنبض خفيف */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        padding: 20px;
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: #030712;
        font-weight: 900;
        font-size: 1.2rem;
        border: none;
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: scale(1.05) translateY(-5px);
        box-shadow: 0 15px 30px rgba(245, 158, 11, 0.4);
    }

    /* تجميل التبويبات */
    .stTabs [data-baseweb="tab-list"] { gap: 15px; }
    .stTabs [data-baseweb="tab"] {
        border-radius: 30px !important;
        padding: 8px 25px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الحالة ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'approved_companies' not in st.session_state: st.session_state.approved_companies = []

# دالة الانتقال مع تأثير بصري
def go_to(step_num):
    st.session_state.step = step_num

# --- الهيدر السينمائي ---
st.markdown("""
    <div class="hero-text">
        <h1 style="font-size: 4rem; font-weight: 900; color: #fbbf24; margin-bottom:0;">طـاقتـي الشمسيـة</h1>
        <p style="font-size: 1.2rem; color: #94a3b8; letter-spacing: 3px;">DESIGN • ENERGY • FUTURE</p>
    </div>
    """, unsafe_allow_html=True)

# التبويبات
tab_calc, tab_co, tab_admin = st.tabs(["💎 المحرك الذكي", "🏢 شبكة الشركات", "🔑 الإدارة"])

# 1. المحرك الذكي (الحاسبة السينمائية)
with tab_calc:
    _, center_col, _ = st.columns([1, 2, 1])
    
    with center_col:
        st.markdown("<div class='cinema-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("<h3 style='text-align:center;'>01. كفاءة النهار</h3>", unsafe_allow_html=True)
            st.write("أدخل عدد الأمبيرات المطلوبة وقت الذروة:")
            st.session_state.day_amp = st.number_input("", min_value=0.0, value=10.0, key="d1")
            if st.button("الخطوة التالية →"): go_to(2); st.rerun()

        elif st.session_state.step == 2:
            st.markdown("<h3 style='text-align:center;'>02. احتياطي الليل</h3>", unsafe_allow_html=True)
            st.write("الأمبيرية المطلوبة للتشغيل الليلي:")
            st.session_state.night_amp = st.number_input("", min_value=0.0, value=5.0, key="n1")
            c1, c2 = st.columns(2)
            if c1.button("← عودة"): go_to(1); st.rerun()
            if c2.button("متابعة →"): go_to(3); st.rerun()

        elif st.session_state.step == 3:
            st.markdown("<h3 style='text-align:center;'>03. تخصيص العتاد</h3>", unsafe_allow_html=True)
            st.session_state.hours = st.select_slider("ساعات التغطية الليلية", options=[2,4,6,8,12], value=4)
            st.session_state.panel_cap = st.selectbox("سعة اللوح المفضل", [550, 585, 615, 670], index=2)
            c1, c2 = st.columns(2)
            if c1.button("← عودة"): go_to(2); st.rerun()
            if c2.button("تحليل البيانات ✨"): go_to(4); st.rerun()

        elif st.session_state.step == 4:
            # الحسابات (كفاءة 75%)
            panels = round((st.session_state.day_amp * 230) / (st.session_state.panel_cap * 0.75))
            ah_result = (st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8)
            inv = "6kW Smart" if st.session_state.day_amp <= 15 else "12kW Ultra"
            batt = "5kWh" if ah_result < 100 else ("10kWh" if ah_result <= 200 else "15kWh")

            st.markdown("<h2 style='text-align:center; color:#fbbf24;'>التقرير الهندسي</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
                    <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:20px; text-align:center;">
                        <p style="color:#fbbf24; margin:0;">الألواح</p><h2 style="margin:0;">{panels}</h2>
                    </div>
                    <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:20px; text-align:center;">
                        <p style="color:#fbbf24; margin:0;">الخزن</p><h2 style="margin:0;">{batt}</h2>
                    </div>
                </div>
                <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:20px; text-align:center; margin-top:20px;">
                    <p style="color:#fbbf24; margin:0;">الإنفيرتر المقترح</p><h2 style="margin:0;">{inv}</h2>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("إعادة الحساب 🔄"): go_to(1); st.rerun()
            
        st.markdown("</div>", unsafe_allow_html=True)

# 2. شبكة الشركات (التصميم العالمي)
with tab_co:
    st.markdown("<h2 style='text-align:center;'>مزودي الخدمة المعتمدين</h2>", unsafe_allow_html=True)
    if not st.session_state.approved_companies:
        st.info("نحن نقوم بمراجعة الشركات حالياً لتوفير أفضل الخيارات لك.")
    else:
        for co in st.session_state.approved_companies:
            with st.container():
                st.markdown(f"""
                <div class="cinema-card" style="padding:25px; margin-bottom:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h3 style="color:#fbbf24; margin:0;">{co['الاسم']}</h3>
                        <span style="font-size:0.8rem; color:#94a3b8;">📍 {co['المدينة']}</span>
                    </div>
                    <p style="margin: 15px 0;">{co['الوصف']}</p>
                </div>
                """, unsafe_allow_html=True)
                # نص رسالة احترافي
                res_msg = f"مرحباً، طلبي من تطبيق طاقتي: {panels} لوح، إنفيرتر {inv}، خزن {batt}."
                st.link_button(f"أرسل طلب السعر إلى {co['الاسم']}", f"https://wa.me/{co['هاتف']}?text={res_msg}")

# 3. لوحة الإدارة
with tab_admin:
    st.markdown("<div class='cinema-card'>", unsafe_allow_html=True)
    pw = st.text_input("رمز الدخول الإداري", type="password")
    if pw == "1234":
        st.success("تم تأكيد الهوية.")
        # إدارة الطلبات هنا
    st.markdown("</div>", unsafe_allow_html=True)
