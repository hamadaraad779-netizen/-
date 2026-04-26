import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="سولار إيراك | منصة الطاقة الذكية", layout="centered")

# --- تحسين التصميم باستخدام CSS المتقدم ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
    }
    
    .stApp {
        background: linear-gradient(180deg, #f0f4f8 0%, #ffffff 100%);
    }

    /* تصميم البطاقات الاحترافي */
    .main-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border-top: 6px solid #1e40af;
        margin-bottom: 25px;
    }

    .stat-box {
        background: #f8fafc;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
    }

    /* تحسين الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        transform: scale(1.02);
    }

    /* تحسين النصوص */
    .big-title {
        color: #1e3a8a;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 0px;
    }
    
    .subtitle {
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 30px;
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

# --- الهيدر الرئيسي مع صورة ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="مستقبل الطاقة بين يديك")
st.markdown("<h1 class='big-title'>سولار إيراك</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>المساعد الذكي لتصميم منظومات الطاقة الشمسية في العراق</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# القائمة الجانبية
app_mode = st.sidebar.selectbox("القائمة الرئيسية", ["الحاسبة الذكية", "انضمام الشركات", "إدارة المنصة"])

# --- 1. الحاسبة الذكية ---
if app_mode == "الحاسبة الذكية":
    st.progress((st.session_state.step - 1) / 3)
    
    with st.container():
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("### ⚡ أحمال النهار")
            st.write("أدخل مجموع الأمبيرات التي تعمل وقت ذروة الشمس:")
            st.session_state.day_amp = st.number_input("أمبير النهار (AC)", min_value=0.0, value=10.0)
            st.button("الانتقال للخطوة التالية", on_click=next_step)

        elif st.session_state.step == 2:
            st.markdown("### 🌙 أحمال الليل")
            st.write("أدخل مجموع الأمبيرات المطلوبة من البطاريات:")
            st.session_state.night_amp = st.number_input("أمبير الليل (AC)", min_value=0.0, value=5.0)
            col1, col2 = st.columns(2)
            col1.button("السابق", on_click=prev_step)
            col2.button("التالي", on_click=next_step)

        elif st.session_state.step == 3:
            st.markdown("### ⚙️ إعدادات النظام")
            st.session_state.hours = st.select_slider("ساعات تشغيل البطارية", options=[2, 4, 6, 8, 12], value=4)
            st.session_state.panel_cap = st.selectbox("قدرة اللوح (وات)", [550, 585, 615, 670], index=2)
            col1, col2 = st.columns(2)
            col1.button("السابق", on_click=prev_step)
            col2.button("تحليل النتائج", on_click=next_step)

        elif st.session_state.step == 4:
            st.markdown("### 📊 نتائج التصميم الفني")
            
            # حسابات دقيقة (كفاءة 80%)
            panels = round((st.session_state.day_amp * 230) / (st.session_state.panel_cap * 0.8))
            batteries = round((st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8))

            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"<div class='stat-box'><h4>الألواح المطلوبة</h4><h2>{max(1, panels)}</h2><p>لوح سعة {st.session_state.panel_cap}W</p></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='stat-box'><h4>خزن البطاريات</h4><h2>{batteries} Ah</h2><p>نظام ليثيوم 48V</p></div>", unsafe_allow_html=True)
            
            st.write("---")
            st.markdown("### 🏢 الشركات المقترحة للتنفيذ")
            if not st.session_state.approved_companies:
                st.info("سيتم إدراج الشركات المعتمدة هنا قريباً.")
            for co in st.session_state.approved_companies:
                with st.expander(f"📍 {co['الاسم']} - {co['المدينة']}"):
                    st.write(co['الوصف'])
                    st.link_button("اطلب تسعيرة الآن", f"https://wa.me/{co['هاتف']}")

            st.button("إجراء حساب جديد", on_click=restart)
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- 2. انضمام الشركات ---
elif app_mode == "انضمام الشركات":
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown("### سجل شركتك في المنصة")
    with st.form("co_form"):
        name = st.text_input("اسم الشركة الرسمي")
        city = st.text_input("المحافظة")
        phone = st.text_input("رقم الواتساب (بالصيغة الدولية)")
        desc = st.text_area("نبذة مختصرة عن مشاريعكم")
        if st.form_submit_button("إرسال طلب الانضمام"):
            st.session_state.pending_requests.append({"الاسم": name, "المدينة": city, "هاتف": phone, "الوصف": desc})
            st.success("تم استلام الطلب بنجاح.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 3. الإدارة ---
elif app_mode == "إدارة المنصة":
    pw = st.text_input("رمز الدخول الإداري", type="password")
    if pw == "1234":
        st.write("طلبات الشركات بانتظار الموافقة:")
        for i, r in enumerate(st.session_state.pending_requests):
            st.write(f"**{r['الاسم']}**")
            if st.button("قبول", key=f"a_{i}"):
                st.session_state.approved_companies.append(r)
                st.session_state.pending_requests.pop(i)
                st.rerun()
