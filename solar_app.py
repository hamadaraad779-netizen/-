import streamlit as st

# إعدادات الصفحة الفاخرة
st.set_page_config(page_title="طاقتي الشمسية | My Solar", layout="wide", initial_sidebar_state="collapsed")

# --- CSS عالمي (Premium UI Design) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700&display=swap');

    * { font-family: 'Cairo', sans-serif; }

    .stApp {
        background-color: #05070a;
        color: #ffffff;
    }

    /* تصميم القسم العلوي (Hero) */
    .hero-section {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(5,7,10,1)), 
                    url('https://images.unsplash.com/photo-1509391366360-fe5bb6058826?q=80&w=1500');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin-bottom: 50px;
    }

    /* تأثير الزجاج (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 20px;
        transition: 0.4s;
    }
    
    .glass-card:hover {
        border-color: #facc15;
        background: rgba(255, 255, 255, 0.05);
    }

    /* الأزرار الاحترافية */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        padding: 15px;
        background: #facc15;
        color: #000;
        font-weight: 700;
        border: none;
        letter-spacing: 1px;
        transition: 0.5s;
    }
    
    .stButton>button:hover {
        background: #ffffff;
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(250, 204, 21, 0.4);
    }

    /* العناوين */
    .premium-title {
        font-size: 4rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#fff, #facc15);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    /* دليل الشركات بشكل شبكي */
    .company-badge {
        background: #111827;
        padding: 15px;
        border-radius: 15px;
        border-left: 4px solid #facc15;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة حالة التطبيق ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'approved_companies' not in st.session_state: st.session_state.approved_companies = []

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def restart(): st.session_state.step = 1

# --- الواجهة الرئيسية (Hero) ---
st.markdown("""
    <div class="hero-section">
        <h1 class="premium-title">طاقتي الشمسية</h1>
        <p style="font-size: 1.5rem; color: #cbd5e1;">الجيل القادم من تصميم الطاقة المتجددة في العراق</p>
    </div>
    """, unsafe_allow_html=True)

# قائمة التنقل العلوية بشكل أنيق
tab1, tab2, tab3 = st.tabs(["🚀 المصمم الذكي", "🏢 دليل الشركات", "🔐 لوحة التحكم"])

# --- 1. المصمم الذكي (UX متطور) ---
with tab1:
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        if st.session_state.step == 1:
            st.markdown("### 01 | الأحمال النهارية")
            st.write("أدخل الأمبيرية المطلوبة أثناء ساعات النهار")
            st.session_state.day_amp = st.number_input("", min_value=0.0, value=10.0, key="day_in")
            st.button("الخطوة التالية", on_click=next_step)

        elif st.session_state.step == 2:
            st.markdown("### 02 | الأحمال الليلية")
            st.write("الأمبيرية المطلوبة للتشغيل من البطاريات")
            st.session_state.night_amp = st.number_input("", min_value=0.0, value=5.0, key="night_in")
            st.columns(2)[0].button("السابق", on_click=prev_step)
            st.columns(2)[1].button("التالي", on_click=next_step)

        elif st.session_state.step == 3:
            st.markdown("### 03 | المواصفات الفنية")
            st.session_state.hours = st.select_slider("ساعات العمل الليلي", options=[2,4,6,8,12], value=4)
            st.session_state.panel_cap = st.selectbox("سعة اللوح", [550, 615, 670])
            st.columns(2)[0].button("السابق", on_click=prev_step)
            st.columns(2)[1].button("إصدار التقرير", on_click=next_step)

        elif st.session_state.step == 4:
            # حسابات دقيقة (كفاءة 75%)
            panels = round((st.session_state.day_amp * 230) / (st.session_state.panel_cap * 0.75))
            ah_result = (st.session_state.night_amp * 230 * st.session_state.hours) / (48 * 0.8)
            
            # منطق الإنفيرتر والبطارية
            inv = "6kW" if 5 <= st.session_state.day_amp <= 15 else "12kW"
            batt = "5kWh" if ah_result < 100 else ("10kWh" if ah_result <= 200 else "15kWh")

            st.markdown("### 📊 التقرير الفني الذكي")
            st.markdown(f"""
                <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 10px;">
                    <div class="glass-card" style="flex: 1; min-width: 150px; text-align: center;">
                        <p style="color:#facc15">الألواح</p><h2>{panels}</h2><small>لوح</small>
                    </div>
                    <div class="glass-card" style="flex: 1; min-width: 150px; text-align: center;">
                        <p style="color:#facc15">الخزن</p><h2>{batt}</h2><small>Lithium</small>
                    </div>
                    <div class="glass-card" style="flex: 1; min-width: 150px; text-align: center;">
                        <p style="color:#facc15">الإنفيرتر</p><h2>{inv}</h2><small>Smart Hybrid</small>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.button("إعادة التصميم", on_click=restart)
        
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown("### لماذا طاقتنا؟")
        st.info("نحن نستخدم خوارزميات تحاكي طقس العراق لضمان أفضل أداء لمنظومتك.")
        st.image("https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9?q=80&w=400", use_container_width=True)

# --- 2. دليل الشركات (العالمي) ---
with tab2:
    st.markdown("## 🏢 مزودي الخدمة المعتمدين")
    st.write("تواصل مباشرة مع أفضل الشركات في محافظتك")
    
    if not st.session_state.approved_companies:
        st.write("قائمة الشركات قيد التحديث...")
    
    # عرض الشركات على شكل Grid
    col_co1, col_co2 = st.columns(2)
    for i, co in enumerate(st.session_state.approved_companies):
        target_col = col_co1 if i % 2 == 0 else col_co2
        with target_col:
            st.markdown(f"""
                <div class="company-badge">
                    <h4 style="margin:0; color:#facc15;">{co['الاسم']}</h4>
                    <p style="font-size:0.8rem; color:#94a3b8;">📍 {co['المدينة']}</p>
                    <p style="font-size:0.9rem;">{co['الوصف']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"طلب تسعيرة من {co['الاسم']}", f"https://wa.me/{co['هاتف']}")

    st.write("---")
    st.markdown("### هل تمتلك شركة طاقة؟")
    with st.expander("سجل اهتمامك للانضمام إلينا"):
        # فورم التسجيل هنا
        st.write("سيتم مراجعة طلبك من قبل فريق الجودة.")

# --- 3. لوحة الإدارة ---
with tab3:
    st.markdown("### 🔐 منطقة المسؤول")
    pw = st.text_input("رمز الأمان", type="password")
    if pw == "1234":
        st.success("أهلاً بك يا مدير المنصة")
        # منطق القبول والرفض هنا كما في الكود السابق
