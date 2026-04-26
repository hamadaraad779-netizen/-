import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="منظومتي الشمسية", layout="centered")

# --- إدارة البيانات (سري للمسؤول فقط) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'pending_requests' not in st.session_state:
    st.session_state.pending_requests = []
if 'approved_companies' not in st.session_state:
    # شركات افتراضية (يمكنك مسحها وإضافة شركاتك يدوياً)
    st.session_state.approved_companies = []

# دالة التنقل
def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def restart(): st.session_state.step = 1

# --- القائمة الجانبية (مخفية وبسيطة) ---
st.sidebar.title("القائمة")
app_mode = st.sidebar.radio("انتقل إلى:", ["حاسبة المنظومة", "طلب انضمام شركة", "إدارة المنصة (سري)"])

# ---------------------------------------------------------
# 1. واجهة الحاسبة (نظام الخطوات)
# ---------------------------------------------------------
if app_mode == "حاسبة المنظومة":
    st.title("☀️ صمم منظومتك الآن")
    
    if st.session_state.step == 1:
        st.subheader("كم أمبير تحتاج لتشغيل الأجهزة (بالنهار)؟")
        st.session_state.day_amp = st.number_input("أمبير النهار:", min_value=0.0, value=10.0)
        st.button("التالي ➡️", on_click=next_step)

    elif st.session_state.step == 2:
        st.subheader("كم أمبير تحتاج لتشغيل الأجهزة (بالليل)؟")
        st.session_state.night_amp = st.number_input("أمبير الليل:", min_value=0.0, value=5.0)
        col_a, col_b = st.columns(2)
        col_a.button("⬅️ السابق", on_click=prev_step)
        col_b.button("التالي ➡️", on_click=next_step)

    elif st.session_state.step == 3:
        st.subheader("ساعات التشغيل وسعة الألواح")
        st.session_state.hours = st.number_input("عدد ساعات تشغيل البطارية بالليل:", min_value=1, value=4)
        st.session_state.panel_cap = st.number_input("سعة اللوح (وات) - افتراضي 615:", value=615)
        col_a, col_b = st.columns(2)
        col_a.button("⬅️ السابق", on_click=prev_step)
        col_b.button("إظهار النتيجة النهائية 🚀", on_click=next_step)

    elif st.session_state.step == 4:
        st.header("📋 التقرير النهائي لمنظومتك")
        
        # المعادلات (الحسابات سرية في الكود لا تظهر للمستخدم كمعادلة)
        # كفاءة اللوح 80% وتفريغ البطارية 80%
        watt_day = st.session_state.day_amp * 230
        effective_panel = st.session_state.panel_cap * 0.8
        needed_panels = round(watt_day / (effective_panel * 1.0)) # فرضية 5 ساعات شمس ذروة
        
        watt_night = st.session_state.night_amp * 230 * st.session_state.hours
        needed_battery = round(watt_night / (48 * 0.8)) # حساب على نظام 48 فولت كمثال

        col1, col2 = st.columns(2)
        col1.success(f"✅ تحتاج: {max(1, needed_panels)} ألواح")
        col2.success(f"✅ تحتاج بطارية سعة: {needed_battery} Ah")
        
        st.write("---")
        st.subheader("🏢 شركات معتمدة لتنفيذ هذه المنظومة")
        if not st.session_state.approved_companies:
            st.warning("سيتم إضافة الشركات المعتمدة قريباً.")
        for co in st.session_state.approved_companies:
            with st.expander(f"📍 {co['الاسم']} - {co['المدينة']}"):
                st.write(f"وصف: {co['الوصف']}")
                st.link_button("💬 طلب عرض سعر من الشركة", f"https://wa.me/{co['هاتف']}")

        st.button("🔄 حساب جديد", on_click=restart)

# ---------------------------------------------------------
# 2. طلب إضافة شركة (متاح للجميع)
# ---------------------------------------------------------
elif app_mode == "طلب انضمام شركة":
    st.header("📝 تقديم طلب انضمام للمنصة")
    st.write("أدخل معلومات شركتك وسيتم مراجعتها من قبل الإدارة.")
    with st.form("company_form"):
        name = st.text_input("اسم الشركة:")
        city = st.text_input("المدينة:")
        phone = st.text_input("رقم الواتساب (مع رمز الدولة):")
        desc = st.text_area("وصف الخدمات:")
        if st.form_submit_button("إرسال الطلب"):
            st.session_state.pending_requests.append({"الاسم": name, "المدينة": city, "هاتف": phone, "الوصف": desc})
            st.success("تم إرسال طلبك بنجاح. سيتم التواصل معك بعد المراجعة.")

# ---------------------------------------------------------
# 3. لوحة الإدارة (سري - أنت فقط من يضيف)
# ---------------------------------------------------------
elif app_mode == "إدارة المنصة (سري)":
    st.header("🔐 لوحة تحكم المسؤول")
    password = st.text_input("أدخل كلمة المرور للدخول:", type="password")
    
    if password == "1234": # يمكنك تغيير كلمة المرور هنا
        st.subheader("الطلبات الواردة")
        if not st.session_state.pending_requests:
            st.write("لا توجد طلبات جديدة.")
        for i, req in enumerate(st.session_state.pending_requests):
            st.write(f"**{req['الاسم']}** - {req['المدينة']}")
            if st.button(f"موافقة على {req['الاسم']}", key=f"ok_{i}"):
                st.session_state.approved_companies.append(req)
                st.session_state.pending_requests.pop(i)
                st.rerun()
    elif password != "":
        st.error("كلمة المرور غير صحيحة!")
