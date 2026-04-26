import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. إدارة البيانات
if 'user_data' not in st.session_state: st.session_state.user_data = None
if 'current_page' not in st.session_state: st.session_state.current_page = "home"
if 'calc_results' not in st.session_state: st.session_state.calc_results = None

def navigate_to(page): st.session_state.current_page = page

# 3. CSS التصميم الفاخر (Modern App Design)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #f8f9fa; }

    /* لافتة علوية ملونة */
    .hero-banner {
        background: linear-gradient(135deg, #007bff 0%, #00d4ff 100%);
        padding: 35px; border-radius: 25px; color: white;
        text-align: center; margin-bottom: 25px; box-shadow: 0 10px 20px rgba(0,123,255,0.15);
    }
    
    /* تصميم الأزرار المربعة (الشبكة) */
    .menu-card {
        background: white; border-radius: 20px; padding: 20px;
        text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #eee; margin-bottom: 10px;
    }
    .menu-card img { width: 55px; height: 55px; margin-bottom: 10px; }
    .menu-card h4 { color: #333; font-weight: 900; font-size: 1.1rem; margin: 0; }

    /* حقول الإدخال "المستطيلات الأنيقة" */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        height: 45px !important; border-radius: 12px !important;
        border: 2px solid #007bff !important; background: white !important;
    }
    input { font-weight: 700 !important; font-size: 1.1rem !important; }

    /* شريط التنقل السفلي الاحترافي */
    .bottom-nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; border-top: 1px solid #eee;
        display: flex; justify-content: space-around; padding: 10px 0;
        z-index: 1000; box-shadow: 0 -2px 15px rgba(0,0,0,0.05);
    }

    [data-testid="stHeader"], footer {visibility: hidden;}
    .block-container { padding-top: 1rem; padding-bottom: 6rem; }
    </style>
    """, unsafe_allow_html=True)

# 4. شاشة الدخول (الملف الشخصي)
if st.session_state.user_data is None:
    st.markdown("<div class='hero-banner'><h1>☀️ مرحباً بك</h1><p>أدخل بياناتك للبدء</p></div>", unsafe_allow_html=True)
    with st.form("login"):
        name = st.text_input("الأسم الكامل:")
        phone = st.text_input("رقم الموبايل:")
        city = st.selectbox("المحافظة:", ["بغداد", "البصرة", "أربيل", "الموصل", "النجف", "كربلاء"])
        if st.form_submit_button("دخول للمنصة"):
            if name and phone:
                st.session_state.user_data = {"name": name, "phone": phone, "city": city}
                st.rerun()
    st.stop()

# 5. محتوى الصفحات
# --- الرئيسية ---
if st.session_state.current_page == "home":
    st.markdown(f"<div class='hero-banner'><h1>أهلاً، {st.session_state.user_data['name']}</h1><p>صمم منظومتك الشمسية بأفضل المواصفات</p></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png"><h4>حساب المنظومة</h4></div>', unsafe_allow_html=True)
        st.button("افتح الحاسبة", key="go_c", on_click=lambda: navigate_to("calc"))
        
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png"><h4>طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز موعد", key="go_f")

    with col2:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/995/995260.png"><h4>دليل الشركات</h4></div>', unsafe_allow_html=True)
        st.button("تصفح الشركات", key="go_co", on_click=lambda: navigate_to("companies"))

        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><h4>لوحة الإدارة</h4></div>', unsafe_allow_html=True)
        st.button("دخول المسؤول", key="go_a")

# --- الحاسبة ---
elif st.session_state.current_page == "calc":
    st.markdown("### 🚀 المصمم الهندسي")
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            d_amp = st.number_input("أمبير النهار:", value=10.0)
            p_watt = st.selectbox("سعة اللوح:", [400, 550, 585, 670], index=1)
        with c2:
            n_amp = st.number_input("أمبير الليل:", value=5.0)
            hrs = st.selectbox("ساعات البطارية:", [2, 4, 6, 8, 10, 12], index=1)
        
        if st.button("احسب النتائج النهائية ✨", use_container_width=True):
            p = round((d_amp * 230) / (p_watt * 0.75))
            inv = "6.2 kW Hybrid" if d_amp <= 15 else "10.2 kW Hybrid"
            batt = (n_amp * 230 * hrs) / 1000
            st.session_state.calc_results = {"p": p, "i": inv, "b": f"{batt:.1f} kWh", "h": hrs}

    if st.session_state.calc_results:
        st.markdown("---")
        r1, r2, r3 = st.columns(3)
        res_style = "background:white; padding:15px; border-radius:15px; text-align:center; box-shadow:0 5px 15px rgba(0,0,0,0.05); border-bottom:4px solid #007bff;"
        r1.markdown(f"<div style='{res_style}'><h2 style='color:#007bff; margin:0;'>{st.session_state.calc_results['p']}</h2><small>لوح شمسي</small></div>", unsafe_allow_html=True)
        r2.markdown(f"<div style='{res_style}'><h2 style='color:#007bff; margin:0;'>{st.session_state.calc_results['i']}</h2><small>العاكس</small></div>", unsafe_allow_html=True)
        r3.markdown(f"<div style='{res_style}'><h2 style='color:#007bff; margin:0;'>{st.session_state.calc_results['b']}</h2><small>بطارية ليثيوم</small></div>", unsafe_allow_html=True)
        st.success(f"تغطية فعلية لمدة {st.session_state.calc_results['h']} ساعات.")

# --- دليل الشركات ---
elif st.session_state.current_page == "companies":
    st.markdown("### 🏢 الشركات المعتمدة")
    cos = [{"n": "شمس الرافدين", "l": "بغداد"}, {"n": "طاقة المستقبل", "l": "البصرة"}]
    for c in cos:
        st.markdown(f"<div style='background:white; padding:15px; border-radius:15px; margin-bottom:10px; border-right:5px solid #007bff;'><h4>{c['n']}</h4><p>📍 {c['l']}</p></div>", unsafe_allow_html=True)

# --- حسابي ---
elif st.session_state.current_page == "profile":
    st.markdown("### 👤 ملفي الشخصي")
    st.session_state.user_data['name'] = st.text_input("الأسم:", st.session_state.user_data['name'])
    st.session_state.user_data['phone'] = st.text_input("الهاتف:", st.session_state.user_data['phone'])
    if st.button("حفظ التعديلات"): st.success("تم الحفظ!")

# 6. شريط التنقل السفلي (أزرار ستريم ليت لتكون فعالة)
st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1: st.button("🏠 الرئيسية", key="n1", on_click=lambda: navigate_to("home"))
with nav2: st.button("🏢 الشركات", key="n2", on_click=lambda: navigate_to("companies"))
with nav3: st.button("🎁 خصومات", key="n3")
with nav4: st.button("👤 حسابي", key="n4", on_click=lambda: navigate_to("profile"))
