import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. إدارة البيانات والملف الشخصي (لكي يبقى الكود فعالاً)
if 'user_data' not in st.session_state: st.session_state.user_data = None
if 'current_page' not in st.session_state: st.session_state.current_page = "home"

def navigate_to(page): st.session_state.current_page = page

# 3. CSS المطور لضمان "وضوح واحترافية النصوص"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    * { 
        font-family: 'Cairo', sans-serif; 
        text-align: right; 
        direction: rtl; 
    }
    
    .stApp { background-color: #f8f9fa; color: #333; }
    
    /* لافتة ترحيبية (Banner) فائقة الوضوح */
    .hero-banner {
        background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
        padding: 40px;
        border-radius: 20px;
        color: white !important; /* ضمان اللون الأبيض للنص */
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,123,255,0.2);
    }
    .hero-banner h3 { 
        font-weight: 900 !important; 
        color: white !important; 
        font-size: 2.2rem; 
        margin-bottom: 10px; 
    }
    .hero-banner p { 
        color: rgba(255,255,255,0.9) !important; 
        font-size: 1.2rem; 
    }

    /* حاوية البطاقات (Grid Containers) لضمان التنسيق */
    [data-testid="column"] {
        display: flex;
        justify-content: center;
        padding: 10px;
    }

    /* --- تنسيق البطاقة المربعة (Grid) --- */
    .menu-card {
        background: white;
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #eee;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        width: 100%;
        max-width: 250px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .menu-card:hover {
        transform: translateY(-8px);
        border-color: #fbbf24;
        box-shadow: 0 15px 35px rgba(251,191,36,0.2);
    }
    
    .menu-card img {
        width: 70px; /* زيادة حجم الأيقونة */
        height: 70px;
        margin-bottom: 15px;
    }
    
    /* تنسيق الكلمات ليكون "فائق الوضوح" */
    .menu-card h4 {
        margin: 0;
        color: #030712 !important; /* أسود عميق للنص */
        font-size: 1.2rem !important; /* تكبير الخط */
        font-weight: 900 !important; /* تغليظ الخط */
        letter-spacing: 0.5px;
    }

    /* تنسيق الأزرار الافتراضية لتكون احترافية */
    .stButton>button {
        border-radius: 50px !important;
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%) !important;
        color: #030712 !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 10px 30px !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(251,191,36,0.3);
    }

    /* إخفاء شريط ستريم ليت للتصميم النظيف */
    [data-testid="stHeader"], footer {visibility: hidden;}
    .main .block-container { padding-top: 20px; padding-bottom: 120px; }
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
if st.session_state.current_page == "home":
    # لافتة ترحيبية مثل التطبيقات العالمية
    st.markdown("""
        <div class="hero-banner">
            <h3>طاقتي الشمسية</h3>
            <p>حلول ذكية وهندسية لمنظومتك في العراق</p>
        </div>
    """, unsafe_allow_html=True)

    # شبكة الخيارات (Grid) فائقة الوضوح
    # (الكلمات أصبحت كبيرة، غامقة، وسهلة القراءة على خلفية بيضاء)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png"><h4>حساب المنظومة</h4></div>', unsafe_allow_html=True)
        st.button("ابدأ الآن 🚀", key="go_calc", on_click=lambda: navigate_to("calc"))
        
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png"><h4>طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز موعد", key="go_fix")

    with col2:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/995/995260.png"><h4>دليل الشركات</h4></div>', unsafe_allow_html=True)
        st.button("تصفح الشركات", key="go_co")

        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><h4>دخول المدير</h4></div>', unsafe_allow_html=True)
        st.button("الإدارة", key="go_admin")

# الصفحات الفرعية (لكي تبقى فعالة كما طلبت)
elif st.session_state.current_page == "calc":
    st.button("⬅️ عودة للرئيسية", on_click=lambda: navigate_to("home"))
    st.markdown("<h2>🚀 الحاسبة الهندسية</h2>", unsafe_allow_html=True)
    day_amp = st.number_input("الأمبير المطلوب نهاراً:")
    st.button("احسب")

# شريط التنقل السفلي (المحسّن)
st.markdown("---")
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1: st.button("🏠 الرئيسية", on_click=lambda: navigate_to("home"))
with col_nav3: st.button("👤 حسابي")
