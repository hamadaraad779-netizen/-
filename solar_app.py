import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="العراق للطاقة الشمسية", layout="wide")

# 2. تهيئة مخزن البيانات
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'pending_cos' not in st.session_state: st.session_state.pending_cos = []
if 'approved_cos' not in st.session_state:
    st.session_state.approved_cos = [
        {"name": "شركة الرافدين", "city": "بغداد", "phone": "07801112223"},
        {"name": "طاقة الجنوب", "city": "البصرة", "phone": "07704445556"}
    ]

def navigate_to(page): st.session_state.current_page = page

# 3. CSS "الوضوح الفائق" وتنسيق العناوين
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #ffffff; }

    /* جعل كلمة 'حساب' والعناوين واضحة جداً باللون الأسود */
    .super-clear-title {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 2.2rem !important;
        text-align: center;
        margin-bottom: 20px;
        border-bottom: 3px solid #0056b3;
        padding-bottom: 10px;
    }

    /* تنسيق نصوص الإدخال والمخرجات */
    label, p, span { color: #000000 !important; font-weight: 800 !important; }
    
    .result-card {
        background-color: #f0fdf4;
        border: 3px solid #16a34a;
        padding: 20px;
        border-radius: 15px;
        color: #000000 !important;
        margin-top: 15px;
    }

    /* إطارات واضحة للخانات */
    div[data-baseweb="input"] {
        border: 2px solid #000000 !important;
        border-radius: 10px !important;
    }

    /* إخفاء الزوائد */
    [data-testid="stHeader"], footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحات
# --- الصفحة الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown("<div class='super-clear-title'>☀️ منصة طاقة العراق</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("📐 حساب المنظومة", use_container_width=True, on_click=navigate_to, args=("calc",))
        st.button("🏢 دليل الشركات", use_container_width=True, on_click=navigate_to, args=("cos_list",))
    with col2:
        st.button("📝 تسجيل شركة جديدة", use_container_width=True, on_click=navigate_to, args=("cos_reg",))
        st.button("👤 حسابي", use_container_width=True)

# --- صفحة الحاسبة (بالمعادلة الجديدة) ---
elif st.session_state.current_page == "calc":
    st.markdown("<div class='super-clear-title'>📐 حساب الأحمال والألواح</div>", unsafe_allow_html=True)
    
    a_day = st.number_input("الاستخدام النهاري (أمبير):", value=10)
    a_night = st.number_input("الاستخدام الليلي (أمبير):", value=5)
    h_night = st.number_input("عدد ساعات التشغيل الليلي (كتابة):", value=6)

    if st.button("احسب النتائج الآن ✨", use_container_width=True):
        # معادلة الألواح
        panels = round(((a_day * 230) + (a_night * 230 * 0.2)) / 450) + 2
        
        # معادلة البطارية حسب طلبك: سعة (أمبير * ساعات)
        capacity_test = a_night * h_night
        
        if capacity_test <= 100:
            bat_result = "5 كيلو واط (5 kWh)"
        elif capacity_test <= 200:
            bat_result = "10 كيلو واط (10 kWh)"
        else:
            bat_result = "15 كيلو واط (15 kWh)"
            
        st.markdown(f"""
            <div class='result-card'>
                <h3>✅ النتائج النهائية:</h3>
                <p>• عدد الألواح المطلوب: <b>{panels} ألواح</b> (550 واط).</p>
                <p>• نظام البطارية المقترح: <b>{bat_result}</b>.</p>
                <p>• هذه السعة تغطي استهلاك {a_night} أمبير لمدة {h_night} ساعة ليلاً.</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.button("🏠 عودة للرئيسية", on_click=navigate_to, args=("home",))

# --- صفحة دليل الشركات (منفصلة) ---
elif st.session_state.current_page == "cos_list":
    st.markdown("<div class='super-clear-title'>🏢 دليل الشركات المعتمدة</div>", unsafe_allow_html=True)
    for co in st.session_state.approved_cos:
        st.markdown(f"""
            <div style='border:2px solid #0056b3; padding:15px; border-radius:12px; margin-bottom:10px;'>
                <h4 style='margin:0;'>{co['name']}</h4>
                <p style='margin:5px 0;'>📍 المدينة: {co['city']} | 📞 الهاتف: {co['phone']}</p>
            </div>
        """, unsafe_allow_html=True)
    st.button("🏠 عودة", on_click=navigate_to, args=("home",))

# --- صفحة تسجيل الشركات (بموافقة الإدارة) ---
elif st.session_state.current_page == "cos_reg":
    st.markdown("<div class='super-clear-title'>📝 تسجيل شركة جديدة</div>", unsafe_allow_html=True)
    with st.form("reg_form"):
        c_name = st.text_input("اسم الشركة")
        c_city = st.text_input("المحافظة")
        c_phone = st.text_input("رقم التواصل")
        admin_pass = st.text_input("كود الموافقة (خاص بالإدارة)", type="password")
        
        if st.form_submit_button("إرسال الطلب والتفعيل"):
            if admin_pass == "1234": # الكود السري الخاص بك
                st.session_state.approved_cos.append({"name": c_name, "city": c_city, "phone": c_phone})
                st.success("تم تفعيل الشركة بنجاح وظهورها في الدليل!")
            else:
                st.error("الكود خاطئ! يجب مراجعة صاحب التطبيق للموافقة.")
    st.button("🏠 عودة", on_click=navigate_to, args=("home",))

# 5. شريط التنقل السفلي
st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)
nav = st.columns(4)
with nav[0]: st.button("🏠 الرئيسية", on_click=navigate_to, args=("home",), use_container_width=True)
with nav[1]: st.button("📐 الحاسبة", on_click=navigate_to, args=("calc",), use_container_width=True)
with nav[2]: st.button("🏢 الشركات", on_click=navigate_to, args=("cos_list",), use_container_width=True)
with nav[3]: st.button("📝 التسجيل", on_click=navigate_to, args=("cos_reg",), use_container_width=True)
