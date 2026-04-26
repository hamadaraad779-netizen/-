import streamlit as st

# 1. إعدادات الصفحة والأيقونة
st.set_page_config(page_title="طاقتي الشمسية", page_icon="☀️", layout="wide")

# 2. CSS المتطور لمحاكاة "بلي" (تصميم الموبايل)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #f8f9fa; color: #333; }
    
    /* تصميم البطاقة المربعة (Grid) */
    .menu-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #eee;
        margin-bottom: 10px;
    }
    .menu-card img { width: 50px; height: 50px; margin-bottom: 12px; }
    .menu-card h4 { margin: 0; color: #333; font-size: 1rem; font-weight: 700; }

    /* شريط التنقل السفلي */
    .bottom-nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; border-top: 1px solid #eee;
        display: flex; justify-content: space-around; padding: 12px 0;
        z-index: 1000; box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }
    .nav-item { text-align: center; cursor: pointer; color: #888; font-size: 0.8rem; }
    .nav-item.active { color: #007bff; font-weight: bold; }

    /* إخفاء الهوامش الافتراضية */
    [data-testid="stHeader"], footer {visibility: hidden;}
    .main .block-container { padding-top: 20px; padding-bottom: 100px; }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة البيانات (المستخدم والصفحات)
if 'user_data' not in st.session_state: st.session_state.user_data = None
if 'current_page' not in st.session_state: st.session_state.current_page = "home"

# --- دالة لتغيير الصفحة ---
def navigate_to(page):
    st.session_state.current_page = page

# 4. شاشة التسجيل (تظهر إذا لم يكن المستخدم مسجلاً)
if st.session_state.user_data is None:
    st.markdown("<h2 style='text-align:center;'>مرحباً بك في طاقتي ☀️</h2>", unsafe_allow_html=True)
    st.write("يرجى ملء معلوماتك للبدء باستخدام التطبيق:")
    with st.form("registration"):
        name = st.text_input("الاسم الكامل")
        phone = st.text_input("رقم الهاتف")
        city = st.selectbox("المحافظة", ["بغداد", "البصرة", "الموصل", "أربيل", "النجف", "كربلاء", "أخرى"])
        if st.form_submit_button("دخول"):
            if name and phone:
                st.session_state.user_data = {"name": name, "phone": phone, "city": city}
                st.rerun()
            else:
                st.error("يرجى ملء جميع الحقول")
    st.stop()

# 5. محتوى الصفحات
# ------------------ صفحة الرئيسية ------------------
if st.session_state.current_page == "home":
    st.markdown("""
        <div style="background: #007bff; padding: 30px; border-radius: 20px; color: white; margin-bottom: 25px;">
            <h3>منظومتك الشمسية تبدأ من هنا</h3>
            <p>صمم، قارن، واطلب بضغطة زر واحدة</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3106/3106856.png"><h4>حساب المنظومة</h4></div>', unsafe_allow_html=True)
        if st.button("ابدأ الحساب", key="go_calc"): navigate_to("calc")
        
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/1067/1067555.png"><h4>طلب صيانة</h4></div>', unsafe_allow_html=True)
        st.button("احجز فني", key="go_fix")

    with col2:
        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/995/995260.png"><h4>دليل الشركات</h4></div>', unsafe_allow_html=True)
        if st.button("تصفح المجهزين", key="go_co"): navigate_to("companies")

        st.markdown('<div class="menu-card"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><h4>الإدارة</h4></div>', unsafe_allow_html=True)
        st.button("دخول المسؤول", key="go_admin")

# ------------------ صفحة حسابي (عرض وتعديل) ------------------
elif st.session_state.current_page == "profile":
    st.markdown("<h2>👤 ملفي الشخصي</h2>", unsafe_allow_html=True)
    with st.container():
        st.write("يمكنك تعديل معلوماتك الشخصية أدناه:")
        new_name = st.text_input("الاسم", value=st.session_state.user_data['name'])
        new_phone = st.text_input("الهاتف", value=st.session_state.user_data['phone'])
        new_city = st.selectbox("المحافظة", ["بغداد", "البصرة", "الموصل", "أربيل", "النجف", "كربلاء", "أخرى"], index=0)
        
        if st.button("حفظ التغييرات"):
            st.session_state.user_data = {"name": new_name, "phone": new_phone, "city": new_city}
            st.success("تم تحديث البيانات!")

# ------------------ صفحة الحاسبة ------------------
elif st.session_state.current_page == "calc":
    st.button("⬅️ عودة للرئيسية", on_click=lambda: navigate_to("home"))
    st.markdown("<h3>🚀 الحاسبة الهندسية</h3>", unsafe_allow_html=True)
    # كود الحاسبة الذي صممناه سابقاً يوضع هنا
    st.number_input("الأمبير المطلوب نهاراً:")
    st.button("احسب")

# ------------------ صفحة تسجيل الشركات ------------------
elif st.session_state.current_page == "register_co":
    st.button("⬅️ عودة", on_click=lambda: navigate_to("home"))
    st.markdown("<h3>🏢 تسجيل شركة جديدة</h3>", unsafe_allow_html=True)
    st.text_input("اسم الشركة")
    st.button("إرسال الطلب")

# 6. شريط التنقل السفلي (المفعّل)
st.markdown("---") # فاصل بسيط قبل الناف بار
c_nav1, c_nav2, c_nav3, c_nav4 = st.columns(4)

with c_nav1:
    if st.button("🏠 الرئيسية", key="nav_h"): navigate_to("home")
with c_nav2:
    if st.button("🏢 سجل شركتك", key="nav_r"): navigate_to("register_co")
with c_nav3:
    st.button("🎁 خصومات")
with c_nav4:
    if st.button("👤 حسابي", key="nav_p"): navigate_to("profile")
