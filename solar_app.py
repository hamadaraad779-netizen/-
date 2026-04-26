import streamlit as st
import pandas as pd

# إعدادات الصفحة والتصميم الحديث
st.set_page_config(page_title="سولار إيراك | Solar Iraq", layout="centered")

# --- CSS لتطوير الشكل العام (Modern UI) ---
st.markdown("""
    <style>
    /* تغيير الخلفية والخطوط */
    .stApp {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #1e3a8a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
    
    /* تصميم البطاقات للنتائج */
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #fbbf24;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* تحسين أزرار التنقل */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #1e3a8a;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #fbbf24;
        color: #1e3a8a;
    }
    
    /* إخفاء القائمة العلوية لزيادة الرسمية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_status=True)

# --- إدارة البيانات والحالة ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'pending_requests' not in st.session_state:
    st.session_state.pending_requests = []
if 'approved_companies' not in st.session_state:
    st.session_state.approved_companies = []

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def restart(): st.session_state.step = 1

# --- الهيدر الرئيسي ---
st.markdown("<h1>☀️ منصة سولار إيراك الذكية</h1>", unsafe_allow_status=True)
st.markdown("<p style='text-align: center; color: #64748b;'>تصميم منظومات الطاقة الشمسية بدقة واحترافية</p>", unsafe_allow_status=True)
st.write("---")

# القائمة الجانبية بشكل أنيق
st.sidebar.markdown("<h2 style='text-align: right;'>القائمة الرئيسية</h2>", unsafe_allow_status=True)
app_mode = st.sidebar.radio("", ["📱 حاسبة المنظومة", "📝 انضم كشركة", "🔐 الإدارة"], label_visibility="collapsed")

# ---------------------------------------------------------
# 1. الحاسبة المتطورة
# ---------------------------------------------------------
if app_mode == "📱 حاسبة المنظومة":
    
    # بروجرس بار (شريط تقدم)
    progress = (st.session_state.step - 1) / 3
    st.progress(progress)

    if st.session_state.step == 1:
        st.markdown("### المرحلة الأولى: أحمال النهار")
        st.info("💡 ملاحظة: أحمال النهار هي التي تعمل مباشرة من الألواح.")
        st.session_state.day_amp = st.number_input("كم أمبير تحتاج بالنهار؟", min_value=0.0, value=10.0)
        st.button("الخطوة التالية ➡️", on_click=next_step)

    elif st.session_state.step == 2:
        st.markdown("### المرحلة الثانية: أحمال الليل")
        st.info("🌙 هذه الأحمال سيتم سحبها من البطاريات التي شُحنت نهاراً.")
        st.session_state.night_amp = st.number_input("كم أمبير تحتاج بالليل؟", min_value=0.0, value=5.0)
        col_prev, col_next = st.columns(2)
        col_prev.button("⬅️ السابق", on_click=prev_step)
        col_next.button("التالي ➡️", on_click=next_step)

    elif st.session_state.step == 3:
        st.markdown("### المرحلة الثالثة: وقت التشغيل والعتاد")
        st.session_state.hours = st.select_slider("كم ساعة تشغيل ليلية مطلوبة؟", options=[2, 4, 6, 8, 10, 12], value=4)
        st.session_state.panel_cap = st.selectbox("قدرة اللوح المستخدم (وات):", [550, 580, 615, 650], index=2)
        
        col_prev, col_next = st.columns(2)
        col_prev.button("⬅️ السابق", on_click=prev_step)
        col_next.button("توليد التقرير النهائي ✨", on_click=next_step)

    elif st.session_state.step == 4:
        st.markdown("### 📊 المواصفات الفنية لمنظومتك")
        
        # الحسابات (المعادلات اللي طلبتها)
        # كفاءة لوح 80% وتفريغ بطارية 80%
        watt_day = st.session_state.day_amp * 230
        effective_panel = st.session_state.panel_cap * 0.8
        needed_panels = round(watt_day / (effective_panel * 1.0)) # افتراض ساعات ذروة
        
        watt_night = st.session_state.night_amp * 230 * st.session_state.hours
        needed_battery = round(watt_night / (48 * 0.8)) # حساب على نظام 48 فولت

        # عرض النتائج بشكل بطاقات عصرية
        st.markdown(f"""
            <div class="result-card">
                <h4 style='color: #1e3a8a;'>📦 عدد الألواح المطلوبة</h4>
                <p style='font-size: 24px; font-weight: bold;'>{max(1, needed_panels)} لوح (سعة {st.session_state.panel_cap} وات)</p>
            </div>
            <div class="result-card">
                <h4 style='color: #1e3a8a;'>🔋 سعة البطاريات (ليثيوم)</h4>
                <p style='font-size: 24px; font-weight: bold;'>{needed_battery} Ah (نظام 48 فولت)</p>
            </div>
        """, unsafe_allow_status=True)
        
        st.write("---")
        st.subheader("🏢 شركات تنفيذ معتمدة")
        if not st.session_state.approved_companies:
            st.warning("جاري تحديث قائمة الشركات المعتمدة حالياً.")
        for co in st.session_state.approved_companies:
            with st.expander(f"⭐ {co['الاسم']} - {co['المدينة']}"):
                st.write(co['الوصف'])
                st.link_button("💬 اطلب عرض سعر الآن", f"https://wa.me/{co['هاتف']}")

        st.button("🔄 ابدأ من جديد", on_click=restart)

# ---------------------------------------------------------
# 2. طلب الانضمام
# ---------------------------------------------------------
elif app_mode == "📝 انضم كشركة":
    st.markdown("### تسجيل شركة جديدة")
    with st.container():
        st.write("املأ البيانات التالية لطلب إدراج شركتك في المنصة:")
        with st.form("company_form"):
            name = st.text_input("اسم الشركة")
            city = st.text_input("المدينة / المحافظة")
            phone = st.text_input("رقم الواتساب (مثال: 9647XXXXXXXX)")
            desc = st.text_area("نبذة عن الخدمات")
            if st.form_submit_button("إرسال الطلب"):
                st.session_state.pending_requests.append({"الاسم": name, "المدينة": city, "هاتف": phone, "الوصف": desc})
                st.success("تم استلام طلبك! سيظهر للجمهور بعد موافقة الإدارة.")

# ---------------------------------------------------------
# 3. لوحة الإدارة
# ---------------------------------------------------------
elif app_mode == "🔐 الإدارة":
    st.markdown("### إدارة المحتوى")
    password = st.text_input("كلمة المرور الإدارية", type="password")
    
    if password == "1234":
        st.success("أهلاً بك أيها المدير")
        if not st.session_state.pending_requests:
            st.info("لا توجد طلبات معلقة حالياً.")
        for i, req in enumerate(st.session_state.pending_requests):
            st.markdown(f"**طلب من: {req['الاسم']}**")
            col_acc, col_rej = st.columns(2)
            if col_acc.button(f"✅ قبول", key=f"ok_{i}"):
                st.session_state.approved_companies.append(req)
                st.session_state.pending_requests.pop(i)
                st.rerun()
            if col_rej.button(f"❌ رفض", key=f"rj_{i}"):
                st.session_state.pending_requests.pop(i)
                st.rerun()
