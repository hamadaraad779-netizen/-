import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية | Premium", layout="wide")

# --- CSS سينمائي فائق الوضوح ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; }
    .stApp { background-color: #05070a; color: #ffffff; }
    
    /* بطاقة الحاسبة المتطورة */
    .premium-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        margin-bottom: 30px;
    }

    /* تحسين العناوين */
    .gold-title {
        color: #fbbf24;
        font-weight: 900;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 10px;
    }

    /* تصميم الصور الاحترافي */
    .img-fluid {
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        transition: 0.5s;
    }
    .img-fluid:hover { transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الحالة ---
if 'step' not in st.session_state: st.session_state.step = 1

# --- الهيدر الرئيسي ---
st.markdown("<h1 class='gold-title'>طاقتي الشمسية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:1.2rem;'>نظام التصميم الهندسي المتكامل للمنظومات الشمسية</p>", unsafe_allow_html=True)

# تبويبات الموقع
tab_calc, tab_co = st.tabs(["🚀 الحاسبة المتطورة", "🏢 دليل الشركات المعتمدة"])

with tab_calc:
    col_img, col_form = st.columns([1, 1.2], gap="large")
    
    with col_img:
        # إضافة صور احترافية تتغير حسب الخطوة
        if st.session_state.step == 1:
            st.image("https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?q=80&w=600", caption="توليد الطاقة من الشمس مباشرة", use_container_width=True)
        elif st.session_state.step == 2:
            st.image("https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?q=80&w=600", caption="أنظمة التخزين والبطاريات الذكية", use_container_width=True)
        else:
            st.image("https://images.unsplash.com/photo-1548337138-e87d889cc369?q=80&w=600", caption="منظومتك المتكاملة أصبحت جاهزة", use_container_width=True)

    with col_form:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("### ⚡ خطوة 1: تحديد الأحمال")
            st.session_state.day_amp = st.number_input("الأمبير المطلوب بالنهار (AC):", min_value=1.0, value=10.0)
            st.session_state.night_amp = st.number_input("الأمبير المطلوب بالليل (AC):", min_value=0.0, value=5.0)
            if st.button("الخطوة التالية ➡️"): 
                st.session_state.step = 2
                st.rerun()

        elif st.session_state.step == 2:
            st.markdown("### 🛠️ خطوة 2: تخصيص العتاد (المطلوب)")
            
            # حقل ساعات العمل الذي طلبته
            st.session_state.hours = st.selectbox("كم ساعة تريد تشغيل البطارية بالليل؟", [2, 4, 6, 8, 10, 12, 16, 24], index=1)
            
            # حقل سعة اللوح الذي طلبته (قابل للتغيير)
            st.session_state.panel_cap = st.selectbox("اختر قدرة اللوح المستخدم (Watt):", [400, 450, 550, 585, 615, 670], index=3)
            
            c1, c2 = st.columns(2)
            if c1.button("⬅️ عودة"): 
                st.session_state.step = 1
                st.rerun()
            if c2.button("إصدار التقرير النهائي 🚀"): 
                st.session_state.step = 3
                st.rerun()

        elif st.session_state.step == 3:
            # الحسابات الفنية (كفاءة 75%)
            effective_p = st.session_state.panel_cap * 0.75
            panels = round((st.session_state.day_amp * 230) / effective_p)
            ah_calc = (st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8)
            
            # منطق الإنفيرتر والبطارية (كما طلبت بدقة)
            inv = "6kW" if 5 <= st.session_state.day_amp <= 15 else ("12kW" if 18 <= st.session_state.day_amp <= 35 else "حسب الطلب")
            batt = "5kWh" if ah_calc < 100 else ("10kWh" if ah_calc <= 200 else "15kWh")

            st.markdown("### 📊 التقرير الهندسي النهائي")
            st.success(f"تم الحساب بناءً على كفاءة {st.session_state.panel_cap} واط بنسبة 75%")
            
            st.markdown(f"""
                <div style="background:rgba(251,191,36,0.1); padding:20px; border-radius:15px; border:1px solid #fbbf24;">
                    <p style="margin:0;">📦 الألواح: <b>{max(1, panels)} لوح</b></p>
                    <p style="margin:0;">🔌 الإنفيرتر: <b>{inv}</b></p>
                    <p style="margin:0;">🔋 البطارية: <b>{batt}</b></p>
                    <p style="margin:0;">⏱️ ساعات التشغيل: <b>{st.session_state.hours} ساعة</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 إعادة الحساب"): 
                st.session_state.step = 1
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

with tab_co:
    st.markdown("<h2 style='text-align:center;'>دليل الشركات المعتمدة</h2>", unsafe_allow_html=True)
    st.info("هنا تظهر الشركات التي وافقت عليها الإدارة. يمكنك المراسلة لطلب السعر مباشرة.")
    # (هنا يوضع كود عرض الشركات والمراسلة الذي برمجناه سابقاً)
