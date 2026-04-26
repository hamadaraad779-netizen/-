import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="سولار إيراك | الوضع الليلي", layout="centered")

# --- تصميم احترافي باللون الأسود (Dark Theme) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
    }
    
    /* الخلفية السوداء */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }

    /* تصميم البطاقات في الوضع الليلي */
    .main-card {
        background: #1e293b;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid #334155;
        border-top: 5px solid #fbbf24; /* خط أصفر شمسي */
        margin-bottom: 25px;
    }

    .stat-box {
        background: #334155;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #475569;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        border-color: #fbbf24;
    }

    /* تحسين الأزرار في الوضع الليلي */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background: linear-gradient(90deg, #fbbf24 0%, #f59e0b 100%);
        color: #0f172a; /* نص غامق على زر فاتح */
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(251, 191, 36, 0.2);
    }
    
    .stButton>button:hover {
        box-shadow: 0 6px 25px rgba(251, 191, 36, 0.4);
        transform: scale(1.02);
    }

    /* تحسين النصوص والوضوح */
    .big-title {
        color: #fbbf24;
        font-weight: 700;
        font-size: 2.8rem;
        margin-bottom: 0px;
    }
    
    .subtitle {
        color: #94a3b8;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }

    h3, h4 {
        color: #f1f5f9 !important;
    }
    
    /* تعديل لون حقول الإدخال */
    input {
        background-color: #0f172a !important;
        color: white !important;
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

# --- الهيدر الرئيسي ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1509391366360-fe5bb6058826?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="الطاقة النظيفة.. استثمار المستقبل")
st.markdown("<h1 class='big-title'>سولار إيراك</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>المساعد الاحترافي لتصميم منظومات الطاقة في العراق</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# القائمة الجانبية
st.sidebar.markdown("### الإدارة")
app_mode = st.sidebar.selectbox("", ["الحاسبة الذكية", "انضمام الشركات", "إدارة المنصة"])

# --- 1. الحاسبة الذكية ---
if app_mode == "الحاسبة الذكية":
    st.progress((st.session_state.step - 1) / 3)
    
    with st.container():
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("### ⚡ أحمال النهار")
            st.write("كم أمبير تحتاج لتشغيل أجهزتك أثناء سطوع الشمس؟")
            st.session_state.day_amp = st.number_input("أمبير النهار (AC)", min_value=0.0, value=10.0, step=1.0)
            st.button("الخطوة التالية ➡️", on_click=next_step)

        elif st.session_state.step == 2:
            st.markdown("### 🌙 أحمال الليل")
            st.write("كم أمبير تحتاج لسحبه من البطاريات بعد غياب الشمس؟")
            st.session_state.night_amp = st.number_input("أمبير الليل (AC)", min_value=0.0, value=5.0, step=1.0)
            col1, col2 = st.columns(2)
            col1.button("⬅️ السابق", on_click=prev_step)
            col2.button("التالي ➡️", on_click=next_step)

        elif st.session_state.step == 3:
            st.markdown("### ⚙️ تفاصيل المنظومة")
            st.session_state.hours = st.select_slider("ساعات العمل المطلوبة من البطارية", options=[2, 4, 6, 8, 12], value=4)
            st.session_state.panel_cap = st.selectbox("قدرة اللوح المستخدم (وات)", [550, 585, 615, 670], index=2)
            col1, col2 = st.columns(2)
            col1.button("⬅️ السابق", on_click=prev_step)
            col2.button("عرض النتائج النهائية ✨", on_click=next_step)

        elif st.session_state.step == 4:
            st.markdown("### 📊 المواصفات الفنية المقترحة")
            
            # حسابات دقيقة (كفاءة 80%)
            panels = round((st.session_state.day_amp * 230) / (st.session_state.panel_cap * 0.8))
            batteries = round((st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8))

            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"<div class='stat-box'><h4 style='color:#fbbf24'>عدد الألواح</h4><h2 style='font-size: 40px;'>{max(1, panels)}</h2><p>لوح سعة {st.session_state.panel_cap}W</p></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='stat-box'><h4 style='color:#fbbf24'>سعة الخزن</h4><h2 style='font-size: 40px;'>{batteries} Ah</h2><p>نظام ليثيوم 48V</p></div>", unsafe_allow_html=True)
            
            st.write("---")
            st.markdown("### 🏢 تنفيذ المنظومة")
            if not st.session_state.approved_companies:
                st.info("سيتم عرض الشركات المعتمدة هنا قريباً.")
            for co in st.session_state.approved_companies:
                with st.expander(f"📍 {co['الاسم']} - {co['المدينة']}"):
                    st.write(co['الوصف'])
                    st.link_button("💬 مراسلة عبر واتساب", f"https://wa.me/{co['هاتف']}")

            st.button("🔄 إعادة الحساب من جديد", on_click=restart)
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- باقي الأقسام (انضمام وإدارة) تبقى كما هي مع التنسيق الجديد ---
elif app_mode == "انضمام الشركات":
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown("### تسجيل شركة جديدة")
    with st.form("co_form"):
        name = st.text_input("اسم الشركة")
        city = st.text_input("المحافظة")
        phone = st.text_input("رقم الواتساب")
        desc = st.text_area("نبذة عن الأعمال")
        if st.form_submit_button("إرسال الطلب"):
            st.session_state.pending_requests.append({"الاسم": name, "المدينة": city, "هاتف": phone, "الوصف": desc})
            st.success("تم الإرسال.")
    st.markdown("</div>", unsafe_allow_html=True)

elif app_mode == "إدارة المنصة":
    pw = st.text_input("رمز الدخول", type="password")
    if pw == "1234":
        for i, r in enumerate(st.session_state.pending_requests):
            st.write(f"**{r['الاسم']}**")
            if st.button("قبول", key=f"a_{i}"):
                st.session_state.approved_companies.append(r)
                st.session_state.pending_requests.pop(i)
                st.rerun()
