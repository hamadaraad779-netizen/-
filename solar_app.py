import streamlit as st

# 1. إعدادات التصميم (UI/UX) - تطوير الواجهة لتكون متطورة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800;900&display=swap');
    * { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }

    .stApp { background-color: #fcfdfe; }

    /* بانر علوي فخم */
    .hero-section {
        background: linear-gradient(135deg, #001a33 0%, #004d99 100%);
        padding: 45px; border-radius: 30px; color: white;
        text-align: center; margin-bottom: 35px;
        box-shadow: 0 15px 30px rgba(0,26,51,0.15);
    }

    /* تحسين شكل حقول الإدخال لتكون واضحة جداً */
    .stNumberInput div[data-baseweb="input"] {
        border: 2px solid #004d99 !important;
        border-radius: 12px !important;
        background-color: white !important;
        transition: 0.3s;
    }
    .stNumberInput div[data-baseweb="input"]:focus-within {
        border-color: #ffc107 !important;
        box-shadow: 0 0 10px rgba(255,193,7,0.2) !important;
    }

    /* عناوين الأقسام */
    .section-title {
        color: #001a33; border-right: 6px solid #ffc107;
        padding-right: 12px; margin-bottom: 20px; font-weight: 800;
    }

    /* بطاقة التقرير النهائي */
    .report-card {
        background: white; border-radius: 25px; padding: 35px;
        border: 1px solid #eef2f6;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        margin-top: 40px;
    }

    .stat-row {
        display: flex; justify-content: space-between;
        padding: 18px 0; border-bottom: 1px dashed #dce4ec;
    }
    .stat-label { color: #4a5568; font-weight: 600; font-size: 1.1rem; }
    .stat-value { color: #004d99; font-weight: 900; font-size: 1.4rem; }

    /* زر الحساب */
    .stButton>button {
        background: linear-gradient(90deg, #ffc107 0%, #ff9800 100%);
        color: #001a33 !important; font-weight: 900 !important;
        border: none !important; border-radius: 15px !important;
        padding: 18px !important; box-shadow: 0 8px 20px rgba(255,193,7,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيكل (Layout)
st.markdown("""
    <div class="hero-section">
        <h1 style="color:white; margin:0; font-size:2.5rem;">📊 الحاسبة الهندسية الذكية</h1>
        <p style="color:#cbd5e0; font-size:1.1rem; margin-top:10px;">أدخل المعطيات للحصول على أدق تفاصيل منظومتك</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("<div class='section-title'>☀️ مدخلات النهار والقدرة</div>", unsafe_allow_html=True)
    a_day = st.number_input("الأمبير المطلوب نهاراً (A):", min_value=0.5, value=10.0, step=0.5)
    
    # اختيار قدرة اللوح (متغير من 500 إلى 800)
    p_watt = st.number_input("قدرة اللوح الواحد (Watt):", min_value=500, max_value=800, value=550, step=10, 
                             help="اختر قدرة الألواح التي تنوي شراءها (بين 500 و 800 واط)")

with col2:
    st.markdown("<div class='section-title'>🌙 مدخلات الليل (كتابة)</div>", unsafe_allow_html=True)
    a_night = st.number_input("الأمبير المطلوب ليلاً (A):", min_value=0.0, value=5.0, step=0.5)
    
    # تحويل ساعات الليل إلى حقل كتابة بدلاً من المنزلق
    h_night = st.number_input("عدد ساعات التشغيل المطلوبة ليلاً (ساعة):", min_value=1, max_value=24, value=6, step=1)

# 3. الحسابات والنتائج
st.markdown("<br>", unsafe_allow_html=True)
if st.button("إصدار التقرير الفني الشامل ✅", use_container_width=True):
    
    # المعادلات الفنية
    efficiency_factor = 1.2 # معامل فقدان
    panels_needed = round(((a_day * 230) * efficiency_factor) / p_watt)
    battery_bank = (a_night * h_night * 230) / 1000 # كيلو واط ساعة
    
    st.markdown(f"""
        <div class="report-card">
            <h2 style="text-align:center; color:#001a33; margin-bottom:30px;">📋 ملخص المنظومة المقترحة</h2>
            
            <div class="stat-row">
                <span class="stat-label">🏗️ عدد الألواح المطلوبة</span>
                <span class="stat-value">{max(1, panels_needed)} لوح (قدرة {p_watt}W)</span>
            </div>
            
            <div class="stat-row">
                <span class="stat-label">🔋 سعة تخزين البطاريات (الليلي)</span>
                <span class="stat-value">{battery_bank:.2f} kWh</span>
            </div>
            
            <div class="stat-row">
                <span class="stat-label">🔌 حجم العاكس (Inverter) الأدنى</span>
                <span class="stat-value">{round(((a_day + a_night) * 230 / 1000) * 1.2, 1)} KVA</span>
            </div>
            
            <div class="stat-row" style="border:none;">
                <span class="stat-label">⏱️ ساعات الاستقلالية (كتابة المستخدم)</span>
                <span class="stat-value">{h_night} ساعة تشغيل</span>
            </div>
            
            <div style="background:#fff9e6; padding:15px; border-radius:12px; margin-top:20px; border:1px solid #ffeeba;">
                <p style="margin:0; font-size:0.9rem; color:#856404; text-align:center;">
                    بناءً على اختيارك لألواح <b>{p_watt} واط</b>، تم تحسين عدد الألواح لضمان كفاءة الشحن.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# العودة
st.markdown("<br>", unsafe_allow_html=True)
st.button("⬅️ الرجوع إلى لوحة التحكم", key="back_btn", use_container_width=True)
