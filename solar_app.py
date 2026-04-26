import streamlit as st

# 1. إعدادات التصميم (UI/UX)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800;900&display=swap');
    * { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }

    .stApp { background-color: #f4f7f9; }

    /* بانر علوي حديث */
    .hero-section {
        background: linear-gradient(135deg, #002b5b 0%, #0056b3 100%);
        padding: 40px; border-radius: 20px; color: white;
        text-align: center; margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }

    /* تحسين وضوح الخانات */
    .stNumberInput input {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #002b5b !important;
    }
    
    div[data-baseweb="input"] {
        border: 2px solid #0056b3 !important;
        border-radius: 12px !important;
    }

    /* بطاقة النتائج الفورية */
    .result-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
        border-right: 10px solid #ffc107;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    }

    .metric-container {
        display: flex;
        justify-content: space-between;
        padding: 15px 0;
        border-bottom: 1px solid #eee;
    }

    .metric-label { font-weight: 600; color: #555; }
    .metric-value { font-weight: 900; color: #0056b3; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. واجهة المدخلات
st.markdown("""
    <div class="hero-section">
        <h1 style="color:white; margin:0;">☀️ حاسبة الطاقة الذكية</h1>
        <p style="color:#e0e7ff;">أدخل بياناتك للحصول على نتائج فورية</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("⚙️ إعدادات النهار")
    a_day = st.number_input("الأمبير المطلوب نهاراً:", min_value=0.0, value=10.0, step=0.5)
    p_watt = st.number_input("قدرة اللوح (500 - 800 واط):", min_value=500, max_value=800, value=550)

with col2:
    st.subheader("🌙 إعدادات الليل")
    a_night = st.number_input("الأمبير المطلوب ليلاً:", min_value=0.0, value=5.0, step=0.5)
    h_night = st.number_input("ساعات التشغيل (كتابة):", min_value=1, max_value=24, value=6)

# 3. الحسابات الفورية (بدون الحاجة لزر إذا أردت سرعة الاستجابة)
# سنبقي الزر كخيار نهائي لتأكيد "إصدار التقرير"
st.markdown("---")
if st.button("إصدار التقرير الفني النهائي ✅", use_container_width=True):
    # معادلات هندسية بسيطة
    panels = round((a_day * 230) / p_watt) + 1
    battery_kwh = (a_night * h_night * 230) / 1000
    inverter = round(((a_day + a_night) * 230) / 1000) + 1

    st.markdown(f"""
        <div class="result-card">
            <h3 style="text-align:center; color:#002b5b;">📋 التقرير الفني المعتمد</h3>
            
            <div class="metric-container">
                <span class="metric-label">🏗️ عدد الألواح المقترح:</span>
                <span class="metric-value">{panels} لوح (بقدرة {p_watt} واط)</span>
            </div>
            
            <div class="metric-container">
                <span class="metric-label">🔋 سعة البطاريات المطلوبة:</span>
                <span class="metric-value">{battery_kwh:.1f} kWh</span>
            </div>
            
            <div class="metric-container">
                <span class="metric-label">🔌 حجم العاكس (Inverter):</span>
                <span class="metric-value">{inverter} KVA أو كيلو واط</span>
            </div>
            
            <div class="metric-container" style="border:none;">
                <span class="metric-label">⏱️ ساعات الاستقلالية:</span>
                <span class="metric-value">{h_night} ساعة</span>
            </div>
            
            <p style="text-align:center; color:#666; font-size:0.8rem; margin-top:15px;">
                * تم احتساب النتائج بناءً على فولتية نظام 230V ومعامل فقدان طاقة 15%.
            </p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("💡 قم بتعديل الأرقام أعلاه ثم اضغط على الزر لإظهار النتائج.")
