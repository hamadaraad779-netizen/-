import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية | My Solar Energy", layout="centered")

# --- تصميم احترافي متطور (Black & Gold Premium) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
    }
    
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
    }

    .main-card {
        background: #161d2f;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        border: 1px solid #1e293b;
        border-top: 5px solid #facc15;
        margin-bottom: 25px;
    }

    .result-box {
        background: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #334155;
        text-align: center;
        margin-bottom: 15px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3.8em;
        background: linear-gradient(135deg, #facc15 0%, #eab308 100%);
        color: #0b0f19;
        font-weight: bold;
        font-size: 1.1rem;
        border: none;
        transition: 0.4s;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(234, 179, 8, 0.4);
    }

    .big-title {
        color: #facc15;
        font-weight: 800;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .subtitle {
        color: #94a3b8;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة حالة التطبيق ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'pending_requests' not in st.session_state: st.session_state.pending_requests = []
if 'approved_companies' not in st.session_state: st.session_state.approved_companies = []

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def restart(): st.session_state.step = 1

# --- واجهة البداية ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# صورة احترافية جديدة
st.image("https://images.unsplash.com/photo-1509391366360-fe5bb6058826?q=80&w=1000", caption="طاقتي الشمسية.. استقلالية تامة وكفاءة عالية")
st.markdown("<h1 class='big-title'>طاقتي الشمسية</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>نصمم لك المنظومة الأنسب بناءً على استهلاكك الفعلي</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

app_mode = st.sidebar.selectbox("القائمة", ["المصمم الذكي", "طلب انضمام شركة", "لوحة الإدارة"])

# --- 1. المصمم الذكي (المحدث) ---
if app_mode == "المصمم الذكي":
    st.progress((st.session_state.step - 1) / 3)
    
    with st.container():
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("### ☀️ المرحلة الأولى: احتياج النهار")
            st.session_state.day_amp = st.number_input("إجمالي الأمبيرات المطلوبة نهاراً:", min_value=0.0, value=10.0, step=1.0)
            st.button("الخطوة التالية ➡️", on_click=next_step)

        elif st.session_state.step == 2:
            st.markdown("### 🌙 المرحلة الثانية: احتياج الليل")
            st.session_state.night_amp = st.number_input("إجمالي الأمبيرات المطلوبة ليلاً:", min_value=0.0, value=5.0, step=1.0)
            col1, col2 = st.columns(2)
            col1.button("⬅️ السابق", on_click=prev_step)
            col2.button("التالي ➡️", on_click=next_step)

        elif st.session_state.step == 3:
            st.markdown("### 🛠️ المرحلة الثالثة: خيارات العتاد")
            st.session_state.hours = st.select_slider("ساعات العمل الليلي:", options=[2, 4, 6, 8, 12], value=4)
            st.session_state.panel_cap = st.selectbox("قدرة اللوح (وات):", [550, 585, 615, 670], index=2)
            col1, col2 = st.columns(2)
            col1.button("⬅️ السابق", on_click=prev_step)
            col2.button("تحليل وتصميم المنظومة 🚀", on_click=next_step)

        elif st.session_state.step == 4:
            st.markdown("### 📋 التقرير الفني النهائي")
            
            # 1. حساب الألواح (كفاءة 75%)
            needed_watts = st.session_state.day_amp * 230
            effective_p_power = st.session_state.panel_cap * 0.75
            panels = round(needed_watts / effective_p_power)
            
            # 2. حساب الإنفيرتر (Inverter)
            total_load_amp = st.session_state.day_amp # الاعتماد على حمل النهار كأقصى حمل
            if 5 <= total_load_amp <= 15:
                inverter = "6 كيلو واط (6kW)"
            elif 18 <= total_load_amp <= 35:
                inverter = "12 كيلو واط (12kW)"
            else:
                inverter = "يتم تحديده حسب الطلب الخاص"

            # 3. حساب البطارية (Battery Ah -> kWh)
            ah_result = (st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8)
            if ah_result < 100:
                batt_kwh = "5 كيلو واط (5kWh)"
            elif 100 <= ah_result <= 200:
                batt_kwh = "10 كيلو واط (10kWh)"
            else:
                batt_kwh = "15 كيلو واط (15kWh)"

            # عرض النتائج
            st.markdown(f"""
                <div class='result-box'>
                    <p style='color:#facc15; font-size:1.1rem;'>عدد الألواح المطلوبة</p>
                    <h2 style='margin:0;'>{max(1, panels)} لوح</h2>
                    <small>بقدرة {st.session_state.panel_cap}W (بكفاءة تشغيل 75%)</small>
                </div>
                <div class='result-box'>
                    <p style='color:#facc15; font-size:1.1rem;'>سعة خزن البطارية</p>
                    <h2 style='margin:0;'>{batt_kwh}</h2>
                    <small>بطاريات ليثيوم نظام 48V</small>
                </div>
                <div class='result-box'>
                    <p style='color:#facc15; font-size:1.1rem;'>حجم الإنفيرتر المناسب</p>
                    <h2 style='margin:0;'>{inverter}</h2>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            st.markdown("### 🏢 تنفيذ المنظومة عبر شركات معتمدة")
            if not st.session_state.approved_companies:
                st.info("سيتم إضافة الشركات التي توافق عليها الإدارة هنا.")
            for co in st.session_state.approved_companies:
                with st.expander(f"🏢 {co['الاسم']} - {co['المدينة']}"):
                    st.write(co['الوصف'])
                    st.link_button("💬 اطلب عرض سعر الآن", f"https://wa.me/{co['هاتف']}")

            st.button("🔄 تصميم منظومة جديدة", on_click=restart)
        
        st.markdown("</div>", unsafe_allow_html=True)

# أقسام الإدارة والانضمام تتبع نفس التنسيق الليلي...
elif app_mode == "طلب انضمام شركة":
    st.markdown("<div class='main-card'><h3>تسجيل شركة جديدة</h3>", unsafe_allow_html=True)
    with st.form("co_form"):
        name = st.text_input("اسم الشركة")
        city = st.text_input("المحافظة")
        phone = st.text_input("رقم الواتساب")
        desc = st.text_area("نبذة عن الأعمال")
        if st.form_submit_button("إرسال الطلب"):
            st.session_state.pending_requests.append({"الاسم": name, "المدينة": city, "هاتف": phone, "الوصف": desc})
            st.success("تم استلام الطلب.")
    st.markdown("</div>", unsafe_allow_html=True)

elif app_mode == "لوحة الإدارة":
    pw = st.text_input("رمز الدخول", type="password")
    if pw == "1234":
        st.write("الطلبات الجديدة:")
        for i, r in enumerate(st.session_state.pending_requests):
            st.write(f"**{r['الاسم']}**")
            if st.button("تفعيل الشركة", key=f"a_{i}"):
                st.session_state.approved_companies.append(r)
                st.session_state.pending_requests.pop(i)
                st.rerun()
