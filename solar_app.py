import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية | My Solar", layout="wide")

# 2. تصميم CSS سينمائي لضمان ظهور العناصر بوضوح
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .stApp { background-color: #05070a; color: #ffffff; }
    
    .premium-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    .gold-text { color: #fbbf24; font-weight: 900; }
    
    /* جعل حقول الإدخال واضحة جداً */
    .stNumberInput, .stSelectbox {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 15px !important;
        margin-bottom: 15px;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        background: linear-gradient(90deg, #fbbf24 0%, #f59e0b 100%);
        color: #000;
        font-weight: bold;
        height: 3.5em;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. تهيئة البيانات
if 'pending_requests' not in st.session_state: st.session_state.pending_requests = []
if 'approved_companies' not in st.session_state: st.session_state.approved_companies = []

# 4. واجهة الموقع
st.markdown("<h1 style='text-align: center;' class='gold-text'>☀️ طاقتي الشمسية</h1>", unsafe_allow_html=True)
st.write("---")

tab1, tab2, tab3 = st.tabs(["🚀 الحاسبة الهندسية", "🏢 دليل الشركات", "🔐 لوحة الإدارة"])

# ---------------------------------------------------------
# القسم الأول: الحاسبة (كل الحقول هنا)
# ---------------------------------------------------------
with tab1:
    col_img, col_calc = st.columns([1, 1.5], gap="large")
    
    with col_img:
        st.image("https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?q=80&w=600", caption="تصميم منظومات الطاقة باحترافية")
        st.info("💡 ملاحظة: الحسابات تعتمد كفاءة 75% للألواح لضمان استقرار التشغيل في العراق.")

    with col_calc:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='gold-text'>أدخل بيانات الاستهلاك</h3>", unsafe_allow_html=True)
        
        # حقول الإدخال (كلها في مكان واحد لتجنب الاختفاء)
        day_amp = st.number_input("الأمبير المطلوب وقت النهار (الذروة):", min_value=1.0, value=10.0)
        night_amp = st.number_input("الأمبير المطلوب وقت الليل (من البطاريات):", min_value=0.0, value=5.0)
        hours = st.selectbox("عدد ساعات تشغيل البطارية المطلوبة:", [2, 4, 6, 8, 10, 12, 16], index=1)
        panel_cap = st.selectbox("قدرة اللوح المستخدم (واط):", [400, 450, 550, 585, 615, 670, 700], index=3)
        
        if st.button("إصدار التقرير الفني النهائي ✨"):
            st.write("---")
            # الحسابات
            effective_p = panel_cap * 0.75
            panels = round((day_amp * 230) / effective_p)
            ah_calc = (night_amp * 230 * hours) / (48 * 0.8)
            
            # منطق الإنفيرتر والبطارية
            inv = "6kW" if 5 <= day_amp <= 15 else ("12kW" if 18 <= day_amp <= 35 else "نظام مخصص")
            batt = "5kWh" if ah_calc < 100 else ("10kWh" if ah_calc <= 200 else "15kWh")

            # عرض النتائج بشكل احترافي
            st.markdown(f"""
                <div style="background: rgba(251, 191, 36, 0.1); padding: 25px; border-radius: 20px; border: 2px solid #fbbf24;">
                    <h4 style="color:#fbbf24; text-align:center;">النتائج المقترحة للمنظومة</h4>
                    <p style="font-size:1.2rem;">📦 عدد الألواح: <b>{max(1, panels)} لوح</b></p>
                    <p style="font-size:1.2rem;">🔌 حجم الإنفيرتر: <b>{inv}</b></p>
                    <p style="font-size:1.2rem;">🔋 نظام البطارية: <b>{batt}</b></p>
                    <hr>
                    <small>تم الحساب بناءً على لوح سعة {panel_cap} واط وتغطية {hours} ساعات ليلاً.</small>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# القسم الثاني: دليل الشركات
# ---------------------------------------------------------
with tab2:
    st.markdown("<h2 class='gold-text'>🏢 الشركات المعتمدة</h2>", unsafe_allow_html=True)
    if not st.session_state.approved_companies:
        st.warning("لا توجد شركات معتمدة حالياً.")
    else:
        for co in st.session_state.approved_companies:
            with st.container():
                st.markdown(f"""
                    <div class='premium-card'>
                        <h3 style='color:#fbbf24;'>{co['الاسم']}</h3>
                        <p><b>المحافظة:</b> {co['المدينة']}</p>
                        <p>{co['الوصف']}</p>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"💬 مراسلة {co['الاسم']} عبر واتساب", f"https://wa.me/{co['هاتف']}")

# ---------------------------------------------------------
# القسم الثالث: لوحة الإدارة
# ---------------------------------------------------------
with tab3:
    st.markdown("<h2 class='gold-text'>🔐 لوحة التحكم</h2>", unsafe_allow_html=True)
    password = st.text_input("رمز الدخول:", type="password")
    if password == "1234":
        st.success("أهلاً بك يا مدير")
        for i, req in enumerate(st.session_state.pending_requests):
            st.write(f"طلب من: **{req['الاسم']}**")
            if st.button("قبول ✅", key=f"acc_{i}"):
                st.session_state.approved_companies.append(req)
                st.session_state.pending_requests.pop(i)
                st.rerun()
