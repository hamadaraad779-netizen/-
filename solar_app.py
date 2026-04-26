import streamlit as st
import pandas as pd

st.set_page_config(page_title="مصمم المنظومات الذكي", layout="centered")

# --- إدارة حالة التطبيق (الخطوات والبيانات) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'approved_companies' not in st.session_state:
    st.session_state.approved_companies = [
        {"الاسم": "شركة الرافدين للطاقة", "المدينة": "بغداد", "واتساب": "+964000000000"},
        {"الاسم": "نور الشمس للمقاولات", "المدينة": "أربيل", "واتساب": "+964000000000"}
    ]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def restart(): st.session_state.step = 1

# --- واجهة التطبيق ---
st.title("☀️ مصمم المنظومات الشمسية الاحترافي")

# --- الخطوة 1: أمبير النهار ---
if st.session_state.step == 1:
    st.subheader("الخطوة 1: استهلاك النهار")
    st.write("كم أمبير تحتاج لتشغيل الأجهزة أثناء وجود الشمس؟")
    st.session_state.day_amp = st.number_input("أمبير النهار (AC):", min_value=0.0, value=10.0, step=1.0)
    st.button("التالي ➡️", on_click=next_step)

# --- الخطوة 2: أمبير الليل ---
elif st.session_state.step == 2:
    st.subheader("الخطوة 2: استهلاك الليل")
    st.write("كم أمبير تحتاج لتشغيله من البطاريات بعد غياب الشمس؟")
    st.session_state.night_amp = st.number_input("أمبير الليل (AC):", min_value=0.0, value=5.0, step=1.0)
    st.columns(2)[0].button("⬅️ السابق", on_click=prev_step)
    st.columns(2)[1].button("التالي ➡️", on_click=next_step)

# --- الخطوة 3: ساعات البطارية وسعة اللوح ---
elif st.session_state.step == 3:
    st.subheader("الخطوة 3: تفاصيل التشغيل والعتاد")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.hours = st.number_input("كم ساعة تشغيل بالليل؟", min_value=1, value=4)
        st.session_state.panel_cap = st.number_input("سعة اللوح (وات):", value=615)
    with col2:
        st.session_state.sys_volt = st.selectbox("جهد النظام (فولت):", [12, 24, 48], index=2)
    
    st.columns(2)[0].button("⬅️ السابق", on_click=prev_step)
    st.columns(2)[1].button("تصميم المنظومة الآن 🚀", on_click=next_step)

# --- الخطوة 4: النتيجة النهائية والشركات ---
elif st.session_state.step == 4:
    st.header("📋 تقرير تصميم المنظومة")
    
    # الحسابات الدقيقة
    V_AC = 230
    SUN_HOURS = 5 # متوسط ساعات الذروة
    
    # حساب الألواح (مع كفاءة 80% للوح)
    total_watt_day = st.session_state.day_amp * V_AC
    effective_panel_power = st.session_state.panel_cap * 0.8
    needed_panels = round(total_watt_day / (effective_panel_power * (SUN_HOURS/5)))
    
    # حساب البطاريات (مع تفريغ 80% لليثيوم)
    total_watt_night = st.session_state.night_amp * V_AC * st.session_state.hours
    needed_battery_ah = round(total_watt_night / (st.session_state.sys_volt * 0.8))

    # عرض النتائج
    c1, c2 = st.columns(2)
    with c1:
        st.metric("عدد الألواح", f"{max(1, needed_panels)} لوح")
    with c2:
        st.metric("سعة البطاريات", f"{needed_battery_ah} Ah")
    
    st.info(f"ملاحظة: تم الحساب بناءً على كفاءة لوح 80% وتفريغ بطارية 80% لضمان ديمومة المنظومة.")

    st.divider()
    st.subheader("🏢 شركات مقترحة للتنفيذ")
    st.write("يمكنك مراسلة الشركات التالية للحصول على عرض سعر لهذه المنظومة:")
    
    for co in st.session_state.approved_companies:
        with st.expander(f"📍 {co['الاسم']} - {co['المدينة']}"):
            st.write(f"شركة معتمدة لتركيب منظومات {st.session_state.sys_volt} فولت.")
            # زر المراسلة (واتساب)
            msg = f"مرحباً {co['الاسم']}، أريد عرض سعر لمنظومة: {needed_panels} لوح {st.session_state.panel_cap} وات، مع بطارية {needed_battery_ah} أمبير."
            whatsapp_url = f"https://wa.me/{co['واتساب']}?text={msg}"
            st.link_button("💬 مراسلة الشركة عبر واتساب", whatsapp_url)

    st.button("🔄 إعادة حساب جديدة", on_click=restart)
