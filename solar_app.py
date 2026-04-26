import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="طاقتي الشمسية | My Solar", layout="wide")

# 2. تصميم CSS سينمائي (احترافي جداً)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .stApp { background-color: #05070a; color: #ffffff; }
    
    /* بطاقة التصميم الزجاجية */
    .premium-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }

    .gold-text { color: #fbbf24; font-weight: 900; }
    
    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        background: linear-gradient(90deg, #fbbf24 0%, #f59e0b 100%);
        color: #000;
        font-weight: bold;
        border: none;
        padding: 12px;
    }
    
    /* إخفاء القوائم الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة بيانات النظام (الحالة)
if 'step' not in st.session_state: st.session_state.step = 1
if 'pending_requests' not in st.session_state: st.session_state.pending_requests = []
if 'approved_companies' not in st.session_state: st.session_state.approved_companies = []

# 4. الهيدر الرئيسي للموقع
st.markdown("<h1 style='text-align: center;' class='gold-text'>☀️ طاقتي الشمسية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>نظام التصميم الهندسي الذكي - العراق</p>", unsafe_allow_html=True)
st.write("---")

# 5. توزيع الأقسام (Tabs) - لضمان عدم اختفاء أي شيء
tab1, tab2, tab3 = st.tabs(["🚀 الحاسبة الذكية", "🏢 دليل الشركات", "🔐 لوحة الإدارة"])

# ---------------------------------------------------------
# القسم الأول: الحاسبة الذكية (المحرك)
# ---------------------------------------------------------
with tab1:
    col_img, col_calc = st.columns([1, 1.5], gap="large")
    
    with col_img:
        # صور احترافية تتغير حسب الخطوات
        if st.session_state.step == 1:
            st.image("https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?q=80&w=500", caption="توليد الطاقة النظيفة")
        else:
            st.image("https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?q=80&w=500", caption="أنظمة الخزن المتطورة")

    with col_calc:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("<h3 class='gold-text'>المرحلة 1: تحديد الأحمال</h3>", unsafe_allow_html=True)
            st.session_state.day_amp = st.number_input("الأمبير المطلوب بالنهار:", min_value=1.0, value=10.0)
            st.session_state.night_amp = st.number_input("الأمبير المطلوب بالليل:", min_value=0.0, value=5.0)
            st.session_state.hours = st.selectbox("ساعات تشغيل البطارية ليلاً:", [2, 4, 6, 8, 10, 12, 16], index=1)
            st.session_state.panel_cap = st.selectbox("قدرة اللوح المستخدم (واط):", [400, 450, 550, 585, 615, 670], index=3)
            
            if st.button("تحليل البيانات وإصدار التقرير 🚀"):
                st.session_state.step = 2
                st.rerun()

        elif st.session_state.step == 2:
            st.markdown("<h3 class='gold-text'>المرحلة 2: التقرير الفني</h3>", unsafe_allow_html=True)
            
            # الحسابات الهندسية (كفاءة 75%)
            effective_p = st.session_state.panel_cap * 0.75
            panels = round((st.session_state.day_amp * 230) / effective_p)
            ah_calc = (st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8)
            
            # منطق الإنفيرتر والبطارية كما طلبت
            inv = "6kW" if 5 <= st.session_state.day_amp <= 15 else ("12kW" if 18 <= st.session_state.day_amp <= 35 else "حسب الطلب")
            batt = "5kWh" if ah_calc < 100 else ("10kWh" if ah_calc <= 200 else "15kWh")

            st.markdown(f"""
                <div style="background: rgba(251, 191, 36, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #fbbf24;">
                    <p>📦 عدد الألواح: <b>{max(1, panels)} لوح</b> (سعة {st.session_state.panel_cap}W)</p>
                    <p>🔌 حجم الإنفيرتر: <b>{inv}</b></p>
                    <p>🔋 نظام البطاريات: <b>{batt}</b></p>
                    <p>⏱️ ساعات التغطية: <b>{st.session_state.hours} ساعة</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 حساب جديد"):
                st.session_state.step = 1
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# القسم الثاني: دليل الشركات والمراسلة
# ---------------------------------------------------------
with tab2:
    st.markdown("<h2 class='gold-text'>🏢 الشركات المعتمدة</h2>", unsafe_allow_html=True)
    
    if not st.session_state.approved_companies:
        st.info("لا توجد شركات مدرجة حالياً. سيقوم المسؤول بإضافتها قريباً.")
    else:
        for co in st.session_state.approved_companies:
            st.markdown(f"""
                <div class='premium-card'>
                    <h3 style='color:#fbbf24; margin:0;'>{co['الاسم']}</h3>
                    <p style='color:#94a3b8;'>📍 {co['المدينة']}</p>
                    <p>{co['الوصف']}</p>
                </div>
            """, unsafe_allow_html=True)
            # زر المراسلة
            st.link_button(f"💬 اطلب عرض سعر من {co['الاسم']}", f"https://wa.me/{co['هاتف']}")

    st.write("---")
    with st.expander("📝 انضم كشركة (تقديم طلب)"):
        with st.form("company_reg"):
            n = st.text_input("اسم الشركة")
            c = st.text_input("المحافظة")
            p = st.text_input("رقم الواتساب (مثال: 964770...)")
            d = st.text_area("نبذة عن الأعمال")
            if st.form_submit_button("إرسال الطلب للمراجعة"):
                st.session_state.pending_requests.append({"الاسم": n, "المدينة": c, "هاتف": p, "الوصف": d})
                st.success("تم الإرسال!")

# ---------------------------------------------------------
# القسم الثالث: لوحة الإدارة (المخفية بكلمة سر)
# ---------------------------------------------------------
with tab3:
    st.markdown("<h2 class='gold-text'>🔐 إدارة المنصة</h2>", unsafe_allow_html=True)
    password = st.text_input("كلمة مرور المسؤول:", type="password")
    
    if password == "1234":
        st.success("أهلاً بك يا مدير الموقع")
        if not st.session_state.pending_requests:
            st.write("لا توجد طلبات انضمام جديدة.")
        for i, req in enumerate(st.session_state.pending_requests):
            st.markdown(f"**طلب من: {req['الاسم']}**")
            col1, col2 = st.columns(5)
            if col1.button("قبول ✅", key=f"a_{i}"):
                st.session_state.approved_companies.append(req)
                st.session_state.pending_requests.pop(i)
                st.rerun()
            if col2.button("رفض ❌", key=f"r_{i}"):
                st.session_state.pending_requests.pop(i)
                st.rerun()
