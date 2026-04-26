import streamlit as st

# 1. إعدادات الصفحة (أيقونة التطبيق والعنوان)
# ملاحظة: تم وضع رابط الشعار الأزرق ليكون هو الأيقونة الرسمية
st.set_page_config(
    page_title="طاقتي الشمسية",
    page_icon="https://r.jina.ai/i/0586e300645c470183f3f50875c742c3", # رابط الشعار الأزرق
    layout="wide"
)

# 2. تصميم CSS سينمائي فائق الفخامة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .stApp { background-color: #05070a; color: #ffffff; }
    
    /* بطاقة الحاسبة الزجاجية */
    .premium-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    .gold-text { color: #fbbf24; font-weight: 900; }
    
    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, #fbbf24 0%, #f59e0b 100%);
        color: #000 !important;
        font-weight: 900;
        height: 3.5em;
        font-size: 1.1rem;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(251, 191, 36, 0.4);
    }
    
    /* تحسين شكل التبويبات */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; justify-content: center; }
    .stTabs [data-baseweb="tab"] {
        border-radius: 50px !important;
        padding: 10px 25px !important;
        background-color: rgba(255,255,255,0.05) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. تهيئة البيانات
if 'pending_requests' not in st.session_state: st.session_state.pending_requests = []
if 'approved_companies' not in st.session_state: st.session_state.approved_companies = []

# 4. واجهة الموقع (الشعار الجديد)
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
with col_logo_2:
    # عرض اللوكو الأزرق في منتصف الصفحة
    st.image("https://r.jina.ai/i/0586e300645c470183f3f50875c742c3", use_container_width=True)

st.markdown("<h1 style='text-align: center; margin-top: -20px;' class='gold-text'>طاقتي الشمسية</h1>", unsafe_allow_html=True)
st.write("---")

# 5. التبويبات الرئيسية
tab_calc, tab_co, tab_admin = st.tabs(["🚀 المصمم الهندسي", "🏢 الشركات المعتمدة", "🔐 الإدارة"])

# ---------------------------------------------------------
# القسم الأول: الحاسبة الهندسية
# ---------------------------------------------------------
with tab_calc:
    c_img, c_form = st.columns([1, 1.5], gap="large")
    
    with c_img:
        st.image("https://images.unsplash.com/photo-1509391366360-fe5bb6058826?q=80&w=600", caption="مستقبل الطاقة بين يديك")
        st.success("✅ النظام مبرمج الآن على كفاءة 75% للألواح لضمان أداء مثالي في درجات الحرارة العالية.")

    with c_form:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='gold-text'>تخصيص المنظومة</h3>", unsafe_allow_html=True)
        
        # الحقول المطلوبة
        day_amp = st.number_input("الأمبير المطلوب نهاراً (أحمال مباشرة):", min_value=1.0, value=10.0)
        night_amp = st.number_input("الأمبير المطلوب ليلاً (خزن بطارية):", min_value=0.0, value=5.0)
        hours = st.selectbox("ساعات عمل البطارية المطلوبة:", [2, 4, 6, 8, 10, 12, 16], index=1)
        panel_cap = st.selectbox("قدرة اللوح الذي تفضله (واط):", [400, 450, 550, 585, 615, 670, 700], index=3)
        
        if st.button("توليد التقرير الفني 📊"):
            st.write("---")
            # المعادلات الفنية
            eff_p = panel_cap * 0.75
            panels_needed = round((day_amp * 230) / eff_p)
            ah_calc = (night_amp * 230 * hours) / (48 * 0.8)
            
            # منطق اختيار الإنفيرتر والبطارية
            inv_size = "6kW Hybrid" if 5 <= day_amp <= 15 else ("12kW Hybrid" if 18 <= day_amp <= 35 else "تحتاج دراسة خاصة")
            batt_size = "5kWh" if ah_calc < 100 else ("10kWh" if ah_calc <= 200 else "15kWh")

            st.markdown(f"""
                <div style="background: rgba(251, 191, 36, 0.1); padding: 25px; border-radius: 20px; border: 2px solid #fbbf24;">
                    <h4 style="color:#fbbf24; text-align:center; margin-bottom:15px;">المواصفات الهندسية المقترحة</h4>
                    <p style="font-size:1.1rem;">🔹 عدد الألواح: <b>{max(1, panels_needed)} لوح</b> (سعة {panel_cap}W)</p>
                    <p style="font-size:1.1rem;">🔹 العاكس (Inverter): <b>{inv_size}</b></p>
                    <p style="font-size:1.1rem;">🔹 سعة الخزن: <b>{batt_size} (Lithium)</b></p>
                    <p style="font-size:1.1rem;">🔹 مدة التغطية: <b>{hours} ساعات</b></p>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# القسم الثاني: الشركات
# ---------------------------------------------------------
with tab_co:
    st.markdown("<h2 class='gold-text' style='text-align:center;'>دليل المجهزين المعتمدين</h2>", unsafe_allow_html=True)
    if not st.session_state.approved_companies:
        st.info("سيتم إظهار الشركات هنا فور تفعيلها من قبل الإدارة.")
    else:
        for co in st.session_state.approved_companies:
            with st.container():
                st.markdown(f"""
                    <div class='premium-card' style='border-right: 5px solid #fbbf24;'>
                        <h3 style='color:#fbbf24; margin:0;'>{co['الاسم']}</h3>
                        <p style='color:#94a3b8;'>📍 {co['المدينة']}</p>
                        <p>{co['الوصف']}</p>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"💬 مراسلة {co['الاسم']} لطلب السعر", f"https://wa.me/{co['هاتف']}")

    st.write("---")
    with st.expander("📝 هل أنت صاحب شركة؟ قدم طلب انضمام"):
        with st.form("reg_form"):
            n = st.text_input("اسم الشركة/المكتب")
            c = st.text_input("المحافظة")
            p = st.text_input("رقم الواتساب (مثلاً 96477...)")
            d = st.text_area("نبذة عن خدماتكم")
            if st.form_submit_button("إرسال الطلب"):
                st.session_state.pending_requests.append({"الاسم": n, "المدينة": c, "هاتف": p, "الوصف": d})
                st.success("تم الإرسال بنجاح.")

# ---------------------------------------------------------
# القسم الثالث: الإدارة
# ---------------------------------------------------------
with tab_admin:
    st.markdown("<h2 class='gold-text'>🔐 لوحة الإشراف</h2>", unsafe_allow_html=True)
    pw = st.text_input("أدخل رمز الدخول:", type="password")
    if pw == "1234":
        for i, r in enumerate(st.session_state.pending_requests):
            st.write(f"طلب جديد من: **{r['الاسم']}**")
            if st.button("تفعيل الشركة ✅", key=f"v_{i}"):
                st.session_state.approved_companies.append(r)
                st.session_state.pending_requests.pop(i)
                st.rerun()
