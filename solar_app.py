import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظومتي الشمسية", layout="wide")

# 2. إدارة قاعدة البيانات والحالة
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'companies' not in st.session_state:
    st.session_state.companies = [
        {"name": "شركة الرافدين للطاقة", "city": "بغداد", "phone": "07801112223"},
        {"name": "نور المستقبل", "city": "البصرة", "phone": "07704445556"}
    ]

def navigate_to(page): st.session_state.current_page = page

# 3. CSS "التباين العالي" - أزرق غامق جداً للنصوص وإطارات واضحة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #ffffff; }

    /* نصوص العناوين والفقرات - أزرق غامق جداً لضمان القراءة */
    h1, h2, h3, h4, p, label, .stMarkdown {
        color: #000b1a !important; font-weight: 900 !important;
    }

    /* مدخلات البيانات: خلفية بيضاء، إطار أسود عريض، نص أسود */
    div[data-baseweb="input"], .stNumberInput input {
        background-color: #ffffff !important;
        border: 3px solid #000b1a !important;
        border-radius: 10px !important;
        color: #000000 !important;
        font-size: 1.2rem !important;
    }

    /* المخرجات (النتائج): تمييزها بلون أخضر غامق واضح */
    .result-box {
        background-color: #e6fffa;
        border: 2px solid #28a745;
        padding: 15px; border-radius: 15px;
        color: #155724 !important; font-size: 1.1rem; margin-top: 10px;
    }

    /* شريط التنقل السفلي الاحترافي */
    .nav-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: #f8f9fa; border-top: 2px solid #000b1a; padding: 10px 0; z-index: 1000; }
    
    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-bottom: 100px; }
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown("<div style='background:#0056b3; padding:25px; border-radius:20px; text-align:center;'><h1 style='color:white !important;'>☀️ تطبيق طاقة العراق</h1></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='text-align:center; padding:20px; border:2px solid #eee; border-radius:15px;'><h4>📐 حاسبة المنظومة</h4></div>", unsafe_allow_html=True)
        st.button("دخول للحاسبة", key="b1", use_container_width=True, on_click=navigate_to, args=("calc",))
    with col2:
        st.markdown("<div style='text-align:center; padding:20px; border:2px solid #eee; border-radius:15px;'><h4>🏢 دليل الشركات</h4></div>", unsafe_allow_html=True)
        st.button("عرض الشركات", key="b2", use_container_width=True, on_click=navigate_to, args=("cos",))

# --- صفحة الحاسبة (تعديلك المطلوب) ---
elif st.session_state.current_page == "calc":
    st.markdown("### 📊 حساب الأحمال والألواح")
    
    c1, c2 = st.columns(2)
    with c1:
        amp_day = st.number_input("الاستخدام النهاري (أمبير):", min_value=0, value=10, step=1)
    with c2:
        amp_night = st.number_input("الاستخدام الليلي (أمبير):", min_value=0, value=5, step=1)
    
    # عدد الساعات كتابة (Number Input بدلاً من Slider)
    hours = st.number_input("عدد ساعات التشغيل الليلي (اكتب الرقم هنا):", min_value=1, max_value=24, value=6)

    if st.button("احسب النتائج الآن ⚡", use_container_width=True):
        total_panels = round(((amp_day * 230) + (amp_night * 230 * 0.2)) / 450) + 2
        st.markdown(f"""
            <div class='result-box'>
                ✅ <b>عدد الألواح المقترح:</b> {total_panels} ألواح (بقدرة 550 واط)<br>
                ✅ <b>نظام البطاريات:</b> تحتاج سعة تخزين تضمن لك تشغيل {amp_night} أمبير لمدة {hours} ساعات.
            </div>
        """, unsafe_allow_html=True)
    st.button("🏠 عودة", on_click=navigate_to, args=("home",))

# --- صفحة دليل الشركات وتسجيل شركة جديدة ---
elif st.session_state.current_page == "cos":
    st.markdown("### 🏢 الشركات المعتمدة")
    for co in st.session_state.companies:
        st.markdown(f"""<div style='border:2px solid #000b1a; padding:10px; border-radius:10px; margin-bottom:10px;'>
        <b>{co['name']}</b> | 📍 {co['city']} | 📞 {co['phone']}</div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ➕ طلب تسجيل شركة جديدة")
    with st.form("reg_form"):
        new_n = st.text_input("اسم الشركة")
        new_c = st.text_input("المحافظة")
        new_p = st.text_input("رقم الهاتف")
        admin_code = st.text_input("كود الموافقة (خاص بصاحب التطبيق)", type="password")
        
        if st.form_submit_button("إرسال الطلب للتسجيل"):
            if admin_code == "1234": # يمكنك تغيير هذا الكود السري
                st.session_state.companies.append({"name": new_n, "city": new_c, "phone": new_p})
                st.success("تمت الموافقة وإضافة الشركة بنجاح!")
                st.rerun()
            else:
                st.error("عذراً، كود الموافقة خاطئ. لا يمكن التسجيل بدون موافقة الإدارة.")
    
    st.button("🏠 عودة", on_click=navigate_to, args=("home",))

# 5. شريط التنقل السفلي (أزرار واضحة)
st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)
nav = st.columns(4)
with nav[0]: st.button("🏠 الرئيسية", on_click=navigate_to, args=("home",), use_container_width=True)
with nav[1]: st.button("📊 الحاسبة", on_click=navigate_to, args=("calc",), use_container_width=True)
with nav[2]: st.button("🏢 الشركات", on_click=navigate_to, args=("cos",), use_container_width=True)
with nav[3]: st.button("👤 حسابي", use_container_width=True)
