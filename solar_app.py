import streamlit as st

# إعدادات الصفحة الفاخرة
st.set_page_config(page_title="طاقتي الشمسية | My Solar", layout="wide", initial_sidebar_state="collapsed")

# --- CSS عالمي متطور جداً (Ultra Premium UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; }

    .stApp {
        background-color: #030712;
        color: #f8fafc;
    }

    /* هيرو سيكشن متطور */
    .hero {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(3,7,18,1)), 
                    url('https://images.unsplash.com/photo-1509391366360-fe5bb6058826?q=80&w=1500');
        background-size: cover;
        padding: 120px 20px;
        text-align: center;
        border-radius: 0 0 60px 60px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }

    /* بطاقات النتائج الزجاجية */
    .glass-card {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 35px;
        margin-bottom: 25px;
        transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glass-card:hover {
        transform: translateY(-10px);
        border-color: #fbbf24;
        background: rgba(30, 41, 59, 0.8);
    }

    /* الأزرار الذهبية */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        padding: 18px;
        background: linear-gradient(90deg, #fbbf24 0%, #f59e0b 100%);
        color: #030712;
        font-weight: 900;
        font-size: 1.1rem;
        border: none;
        box-shadow: 0 10px 20px rgba(245, 158, 11, 0.2);
    }

    /* تجميل التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        color: #94a3b8 !important;
    }
    .stTabs [aria-selected="true"] {
        background: #fbbf24 !important;
        color: #030712 !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة البيانات ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'pending_requests' not in st.session_state: st.session_state.pending_requests = []
if 'approved_companies' not in st.session_state:
    # شركات تجريبية (امسحها من لوحة الإدارة لاحقاً)
    st.session_state.approved_companies = [
        {"الاسم": "عراق سولار للتقنيات", "المدينة": "بغداد", "هاتف": "9647700000000", "الوصف": "متخصصون في ألواح N-Type وبطاريات الليثيوم."}
    ]

# --- الواجهة العلوية ---
st.markdown("""
    <div class="hero">
        <h1 style="font-size: 4.5rem; font-weight: 900; color: #fbbf24; margin-bottom:0;">طاقتي الشمسية</h1>
        <p style="font-size: 1.4rem; color: #cbd5e1; letter-spacing: 2px;">المنصة الاحترافية الأولى لتصميم حلول الطاقة في العراق</p>
    </div>
    """, unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- نظام التبويبات الجديد ---
tab_calc, tab_co, tab_admin = st.tabs(["💡 المصمم الذكي", "🏢 دليل الشركات المعتمدة", "🔐 بوابة الإدارة"])

# ---------------------------------------------------------
# 1. المصمم الذكي
# ---------------------------------------------------------
with tab_calc:
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("## 01 | استهلاك النهار")
            st.write("كم أمبير تحتاج من الشمس مباشرة؟")
            st.session_state.day_amp = st.number_input("", min_value=0.0, value=10.0)
            st.button("الخطوة التالية ➡️", on_click=lambda: st.session_state.update(step=2))

        elif st.session_state.step == 2:
            st.markdown("## 02 | استهلاك الليل")
            st.write("كم أمبير مطلوب تشغيله من البطاريات؟")
            st.session_state.night_amp = st.number_input("", min_value=0.0, value=5.0)
            c1, c2 = st.columns(2)
            c1.button("⬅️ السابق", on_click=lambda: st.session_state.update(step=1))
            c2.button("التالي ➡️", on_click=lambda: st.session_state.update(step=3))

        elif st.session_state.step == 3:
            st.markdown("## 03 | ساعات التشغيل واللوح")
            st.session_state.hours = st.select_slider("ساعات العمل الليلي", options=[2, 4, 6, 8, 12], value=4)
            st.session_state.panel_cap = st.selectbox("قدرة اللوح (Watt)", [550, 585, 615, 670], index=2)
            c1, c2 = st.columns(2)
            c1.button("⬅️ السابق", on_click=lambda: st.session_state.update(step=2))
            c2.button("توليد التقرير 🚀", on_click=lambda: st.session_state.update(step=4))

        elif st.session_state.step == 4:
            # المعادلات (كفاءة 75%)
            panels = round((st.session_state.day_amp * 230) / (st.session_state.panel_cap * 0.75))
            ah_result = (st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8)
            inv = "6kW" if st.session_state.day_amp <= 15 else "12kW"
            batt = "5kWh" if ah_result < 100 else ("10kWh" if ah_result <= 200 else "15kWh")

            st.markdown("<h2 style='text-align:center; color:#fbbf24;'>التقرير الفني</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align:center; margin-bottom:20px;">
                    <h1 style="font-size: 50px;">{panels} ألواح</h1>
                    <p style="color:#94a3b8;">إنفيرتر: {inv} | بطارية: {batt}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 إعادة الحساب"): st.session_state.step = 1; st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. دليل الشركات (المكان الذي تظهر فيه الشركات)
# ---------------------------------------------------------
with tab_co:
    st.markdown("<h2 style='text-align:center;'>الشركات المعتمدة في العراق</h2>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    if not st.session_state.approved_companies:
        st.info("سيتم إدراج الشركات قريباً.")
    else:
        # عرض الشركات في شبكة احترافية
        for co in st.session_state.approved_companies:
            st.markdown(f"""
                <div class="glass-card" style="border-right: 8px solid #fbbf24;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h3 style="margin:0; color:#fbbf24;">{co['الاسم']}</h3>
                            <p style="color:#94a3b8; font-size:0.9rem;">📍 {co['المدينة']}</p>
                        </div>
                        <div style="text-align: left;">
                            <span style="background:#fbbf24; color:black; padding:5px 15px; border-radius:50px; font-weight:bold;">شركة معتمدة</span>
                        </div>
                    </div>
                    <p style="margin-top:15px; font-size:1.1rem;">{co['الوصف']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # زر المراسلة لطلب السعر
            msg = f"مرحباً {co['الاسم']}، لقد قمت بتصميم منظومة عبر تطبيق 'طاقتي الشمسية' وأريد الحصول على عرض سعر لمواصفات (لوح {panels} عدد، إنفيرتر {inv}، بطارية {batt})."
            st.link_button(f"💬 اطلب عرض سعر من {co['الاسم']}", f"https://wa.me/{co['هاتف']}?text={msg}")

    st.write("---")
    st.markdown("### هل تمتلك شركة طاقة شمسية؟")
    with st.expander("📝 قدم طلب انضمام لشركتك هنا"):
        with st.form("join_form"):
            name = st.text_input("اسم الشركة")
            city = st.text_input("المحافظة")
            phone = st.text_input("رقم الواتساب (بالصيغة الدولية مثلاً 96477...)")
            about = st.text_area("نبذة عن خبرتكم")
            if st.form_submit_button("إرسال الطلب للمراجعة"):
                st.session_state.pending_requests.append({"الاسم": name, "المدينة": city, "هاتف": phone, "الوصف": about})
                st.success("تم إرسال طلبك. سيتم مراجعته من قبل إدارة المنصة.")

# ---------------------------------------------------------
# 3. لوحة الإدارة
# ---------------------------------------------------------
with tab_admin:
    st.markdown("## 🔐 لوحة تحكم الإدارة")
    pw = st.text_input("كلمة مرور المسؤول", type="password")
    if pw == "1234":
        st.subheader("طلبات الانضمام الجديدة")
        if not st.session_state.pending_requests:
            st.write("لا توجد طلبات جديدة حالياً.")
        for i, req in enumerate(st.session_state.pending_requests):
            with st.container():
                st.write(f"**{req['الاسم']}** ({req['المدينة']})")
                st.write(req['الوصف'])
                c1, c2 = st.columns(5)
                if c1.button("✅ قبول", key=f"acc_{i}"):
                    st.session_state.approved_companies.append(req)
                    st.session_state.pending_requests.pop(i)
                    st.rerun()
                if c2.button("❌ رفض", key=f"rej_{i}"):
                    st.session_state.pending_requests.pop(i)
                    st.rerun()
