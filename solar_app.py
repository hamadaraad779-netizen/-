import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="منصة الطاقة الشمسية الاحترافية", layout="wide")

# إدارة البيانات في الجلسة
if 'pending_companies' not in st.session_state:
    st.session_state.pending_companies = []
if 'approved_companies' not in st.session_state:
    st.session_state.approved_companies = [{"الاسم": "شركة الطاقة المتجددة", "المدينة": "بغداد", "التقييم": "⭐⭐⭐⭐⭐"}]

# القائمة الجانبية
st.sidebar.title("⚙️ التحكم")
page = st.sidebar.selectbox("القائمة:", ["الحاسبة بالأمبير", "دليل الشركات", "طلب انضمام شركة", "لوحة تحكم المسؤول"])

# --- 1. الحاسبة بالأمبير (المعادلة المطلوبة) ---
if page == "الحاسبة بالأمبير":
    st.header("🧮 حاسبة الأحمال بالأمبير المنزلي")
    
    col1, col2 = st.columns(2)
    with col1:
        ampere_input = st.number_input("كم أمبير تحتاج (AC)؟:", min_value=1.0, value=10.0, step=1.0)
        voltage_ac = 230  # الفولت المنزلي الثابت
        watt_total = ampere_input * voltage_ac
        
        st.info(f"💡 إجمالي الاستهلاك بالوات: **{watt_total} وات**")
        
        panel_efficiency = st.number_input("قدرة اللوح الواحد (مثلاً 615):", value=615)
        sun_hours = st.slider("ساعات الذروة الشمسية:", 3.0, 8.0, 5.0)

    with col2:
        night_hours = st.number_input("كم ساعة تريد تشغيل البطاريات بالليل؟:", min_value=1, value=4)
        battery_voltage = st.selectbox("جهد بطارية الليثيوم (فولت):", [12, 24, 48], index=2)
    
    # --- الحسابات بناءً على طلبك ---
    # 1. عدد الألواح: (الوات الكلي / قدرة اللوح) مع مراعاة ساعات الشمس
    # ملاحظة: Watt_total / panel_efficiency تعطيك العدد لو كانت الشمس موجودة دائماً، 
    # لذا نقسم على (ساعات الشمس/24) أو نستخدم المعادلة المباشرة:
    panels_needed = round((watt_total * 1.25) / (panel_efficiency * (sun_hours/5))) 
    
    # 2. حجم البطارية (ليثيوم): (الوات * عدد الساعات) / الفولت
    # قسمنا على 0.8 لأنها ليثيوم (عمق تفريغ 80%)
    battery_size_ah = round((watt_total * night_hours) / (battery_voltage * 0.8))

    if st.button("احسب المنظومة"):
        st.success(f"📊 النتائج لطلبك ({ampere_input} أمبير):")
        
        c1, c2 = st.columns(2)
        c1.metric("عدد الألواح المطلوبة", f"{max(1, panels_needed)} لوح")
        c2.metric("سعة البطارية المطلوبة", f"{battery_size_ah} Ah")
        
        st.markdown(f"""
        ---
        **تفاصيل الحساب:**
        * تم ضرب {ampere_input} أمبير في {voltage_ac} فولت = **{watt_total} وات**.
        * لتشغيل البطاريات لمدة **{night_hours} ساعات**، تحتاج مخزون طاقة يساوي **{watt_total * night_hours} وات/ساعة**.
        * تم الحساب على أساس نظام **{battery_voltage} فولت** لبطاريات الليثيوم.
        """)

# --- 2. دليل الشركات المعتمدة ---
elif page == "دليل الشركات":
    st.header("🏢 الشركات المعتمدة")
    st.table(pd.DataFrame(st.session_state.approved_companies))

# --- 3. طلب انضمام شركة ---
elif page == "طلب انضمام شركة":
    st.header("📝 تقديم طلب انضمام")
    with st.form("join_form"):
        name = st.text_input("اسم الشركة:")
        city = st.text_input("المدينة:")
        desc = st.text_area("وصف الخدمة:")
        if st.form_submit_button("إرسال الطلب"):
            if name:
                st.session_state.pending_companies.append({"الاسم": name, "المدينة": city, "الوصف": desc})
                st.success("تم الإرسال! بانتظار موافقة الإدارة.")

# --- 4. لوحة تحكم المسؤول (الموافقة اليدوية) ---
elif page == "لوحة تحكم المسؤول":
    st.header("🔐 إدارة طلبات الانضمام")
    if not st.session_state.pending_companies:
        st.write("لا توجد طلبات جديدة.")
    else:
        for i, co in enumerate(st.session_state.pending_companies):
            st.write(f"**الشركة:** {co['الاسم']} | **المدينة:** {co['المدينة']}")
            col_acc, col_rej = st.columns(2)
            if col_acc.button("✅ موافقة", key=f"a_{i}"):
                st.session_state.approved_companies.append({"الاسم": co['الاسم'], "المدينة": co['المدينة'], "التقييم": "⭐ جديد"})
                st.session_state.pending_companies.pop(i)
                st.rerun()
            if col_rej.button("❌ رفض", key=f"r_{i}"):
                st.session_state.pending_companies.pop(i)
                st.rerun()
