import streamlit as st

# 1. إعدادات التصميم الاحترافي (UI/UX)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800;900&display=swap');
    
    * { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }

    /* تحسين خلفية التطبيق */
    .stApp {
        background: linear-gradient(180deg, #f8faff 0%, #ffffff 100%);
    }

    /* البانر العلوي الاحترافي */
    .hero-section {
        background: linear-gradient(90deg, #002b5b 0%, #0056b3 100%);
        padding: 40px;
        border-radius: 25px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,43,91,0.2);
    }

    /* تنسيق حقول الإدخال لتكون بارزة */
    .stNumberInput div[data-baseweb="input"], .stSlider {
        background-color: white !important;
        border: 2px solid #0056b3 !important;
        border-radius: 15px !important;
        padding: 5px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }

    /* العناوين الجانبية */
    h3 {
        color: #002b5b !important;
        border-right: 5px solid #ffc107;
        padding-right: 15px;
        font-weight: 800 !important;
    }

    /* زر الحساب الاحترافي */
    .stButton>button {
        background: linear-gradient(90deg, #ffc107 0%, #ff9800 100%);
        color: #002b5b !important;
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 15px 30px !important;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255,193,7,0.4);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255,193,7,0.6);
    }

    /* بطاقة النتائج المذهلة */
    .result-box {
        background: white;
        border-radius: 25px;
        padding: 30px;
        border: 1px solid #e0e7ff;
        box-shadow: 0 15px 35px rgba(0,86,179,0.1);
        margin-top: 30px;
    }
    
    .stat-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0;
        border-bottom: 1px border-style: solid; border-color: #f0f2f6;
    }
    
    .stat-label { color: #555; font-weight: 600; }
    .stat-value { color: #0056b3; font-weight: 900; font-size: 1.3rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. واجهة المستخدم (Layout)
st.markdown("""
    <div class="hero-section">
        <h1 style="color:white; margin:0;">📊 حاسبة المنظومة الذكية</h1>
        <p style="color:#e0e7ff; opacity:0.9;">صمم منظومتك الشمسية بدقة هندسية عالية</p>
    </div>
    """, unsafe_allow_html=True)

# إنشاء أعمدة الإدخال
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### ☀️ فترة النهار")
    a_day = st.number_input("إجمالي الأمبير المطلوب نهاراً:", min_value=1.0, value=10.0, step=0.5, help="ادخل مجموع أمبيرية الأجهزة التي تعمل وقت الذروة")
    
with col2:
    st.markdown("### 🌙 فترة الليل")
    a_night = st.number_input("الأمبير المطلوب تشغيله ليلاً:", min_value=0.0, value=5.0, step=0.5)
    st.markdown("<p style='font-size:0.9rem; color:#666;'>حدد مدة الاعتماد على البطاريات:</p>", unsafe_allow_html=True)
    h_night = st.slider("", 2, 16, 6, format="%d ساعة")

# 3. منطق الحساب والنتائج
st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)
if st.button("توليد التقرير الفني للمنظومة ✨", use_container_width=True):
    
    # حسابات فنية (تقريبية لأغراض العرض)
    panel_power = 550  # واط لكل لوح
    system_voltage = 48 # فولتية النظام
    panels_count = round((a_day * 230) / panel_power) + 1
    total_energy_night = (a_night * 230 * h_night) / 1000 # كيلو واط ساعة
    
    st.markdown(f"""
        <div class="result-box">
            <h2 style="text-align:center; color:#002b5b; margin-bottom:20px;">📋 التقرير الفني المقترح</h2>
            <div class="stat-item">
                <span class="stat-label">🏗️ عدد الألواح (قدرة {panel_power} واط)</span>
                <span class="stat-value">{panels_count} ألواح</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">🔋 سعة بنك البطاريات المطلوبة</span>
                <span class="stat-value">{total_energy_night:.1f} kWh</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">🔌 حجم العاكس (Inverter) المقترح</span>
                <span class="stat-value">{round((a_day+a_night)*230/1000)+1} KVA</span>
            </div>
            <div class="stat-item" style="border:none;">
                <span class="stat-label">⏱️ ساعات الاستقلالية الليلية</span>
                <span class="stat-value">{h_night} ساعة</span>
            </div>
            <p style="text-align:center; color:#ff9800; font-size:0.8rem; margin-top:20px;">* النتائج تقريبية وتعتمد على جودة المكونات وظروف التركيب.</p>
        </div>
    """, unsafe_allow_html=True)

# إضافة زر العودة بتنسيق بسيط
st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ العودة للقائمة الرئيسية", key="back"):
    pass # هنا تضع منطق التنقل الخاص بك
