import streamlit as st

# --- محرك الحسابات الهندسي ---
def build_solar_calculator():
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 25px; border-radius: 20px; color: white; margin-bottom: 20px; border-right: 5px solid #fbbf24;">
            <h2 style="color: #fbbf24; margin:0;">🚀 المحرك الهندسي الذكي</h2>
            <p style="color: #cbd5e1;">ادخل بيانات الاستهلاك للحصول على أدق النتائج لمنظومتك</p>
        </div>
    """, unsafe_allow_html=True)

    # حاوية الإدخال (تصميم نظيف واحترافي)
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ☀️ أحمال النهار")
            day_amp = st.number_input("الأمبير المطلوب (تشغيل مباشر):", min_value=1.0, value=10.0, step=1.0, help="كم أمبير تحتاج لتشغيل أجهزتك وقت ذروة الشمس؟")
            
            st.markdown("### 🔋 سعة العتاد")
            panel_cap = st.selectbox("قدرة اللوح المستخدم (واط):", [400, 450, 550, 585, 615, 670, 700], index=2)

        with col2:
            st.markdown("### 🌙 أحمال الليل")
            night_amp = st.number_input("الأمبير المطلوب (من البطارية):", min_value=0.0, value=5.0, step=1.0)
            hours = st.select_slider("ساعات تشغيل البطارية المطلوبة:", options=[2, 4, 6, 8, 10, 12], value=4)

    st.write("---")

    # زر الحساب السينمائي
    if st.button("توليد التقرير الهندسي النهائي ✨", use_container_width=True):
        
        # 1. حساب الألواح (معادلة الكفاءة 75%)
        # القدرة الفعلية للوح = القدرة الاسمية * 0.75
        effective_panel_power = panel_cap * 0.75
        total_watt_needed = day_amp * 230 # تحويل الأمبير إلى واط (على فولتية 230)
        panels_count = round(total_watt_needed / effective_panel_power)
        if panels_count < 1: panels_count = 1

        # 2. حساب البطاريات (AH) 
        # (أمبير الليل * 230 فولت * الساعات) / (فولتية النظام 48 * عمق التفريغ 0.8)
        required_ah = (night_amp * 230 * hours) / (48 * 0.8)
        
        # 3. تحديد حجم الإنفيرتر (Inverter)
        if day_amp <= 15:
            inv_size = "6.2 kW Hybrid"
        elif day_amp <= 30:
            inv_size = "10.2 kW Hybrid"
        else:
            inv_size = "12 kW Ultra (Parallel)"

        # 4. تحديد سعة الخزن (kWh)
        if required_ah < 100:
            storage_type = "5.12 kWh (Lithium)"
        elif required_ah <= 200:
            storage_type = "10.24 kWh (Lithium)"
        else:
            storage_type = "15 kWh + (High Capacity)"

        # --- عرض النتائج بتصميم البطاقات الفخمة ---
        st.markdown("### 📋 التقرير الفني المقترح")
        
        res1, res2, res3 = st.columns(3)
        
        with res1:
            st.markdown(f"""
                <div style="background: white; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #eee; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <h1 style="margin:0; color: #007bff;">{panels_count}</h1>
                    <p style="color: #666; font-weight: bold;">عدد الألواح</p>
                    <small>سعة {panel_cap} واط</small>
                </div>
            """, unsafe_allow_html=True)

        with res2:
            st.markdown(f"""
                <div style="background: white; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #eee; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <h2 style="margin:0; color: #fbbf24; font-size: 1.5rem;">{inv_size}</h2>
                    <p style="color: #666; font-weight: bold;">حجم العاكس</p>
                    <small>نظام Smart Hybrid</small>
                </div>
            """, unsafe_allow_html=True)

        with res3:
            st.markdown(f"""
                <div style="background: white; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #eee; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <h2 style="margin:0; color: #10b981; font-size: 1.5rem;">{storage_type}</h2>
                    <p style="color: #666; font-weight: bold;">خزن البطاريات</p>
                    <small>تغطية لـ {hours} ساعات</small>
                </div>
            """, unsafe_allow_html=True)
            
        st.info(f"💡 نصيحة هندسية: تم احتساب {panels_count} لوح لضمان تشغيل {day_amp} أمبير نهاراً مع تعويض الفقد الحراري في العراق.")

# استدعاء الدالة لتعمل داخل التطبيق
build_solar_calculator()
