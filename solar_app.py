<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>حاسبة الطاقة الشمسية الاحترافية</title>
    <style>
        :root {
            --primary-blue: #0061f2;
            --bg-color: #f0f2f5;
            --card-radius: 20px;
            --text-dark: #1c1e21;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background-color: var(--bg-color);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .app-wrapper {
            width: 100%;
            max-width: 480px;
            background: white;
            border-radius: var(--card-radius);
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            padding: 25px;
        }

        .header-section {
            text-align: center;
            margin-bottom: 30px;
        }

        .header-section h2 {
            color: var(--primary-blue);
            margin: 0;
            font-size: 24px;
        }

        .info-tag {
            display: inline-block;
            background: #e7f3ff;
            color: var(--primary-blue);
            padding: 5px 15px;
            border-radius: 50px;
            font-size: 12px;
            margin-top: 10px;
            font-weight: bold;
        }

        .input-box {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 15px;
            border: 1px solid #eee;
        }

        .input-box label {
            display: block;
            font-size: 13px;
            color: #65676b;
            margin-bottom: 8px;
        }

        .input-box input {
            width: 100%;
            border: none;
            background: transparent;
            font-size: 18px;
            font-weight: bold;
            outline: none;
            color: var(--text-dark);
        }

        .calc-button {
            width: 100%;
            background: var(--primary-blue);
            color: white;
            border: none;
            padding: 18px;
            border-radius: 15px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .calc-button:active {
            transform: scale(0.98);
        }

        .results-container {
            margin-top: 25px;
            display: none;
        }

        .result-card {
            background: #ffffff;
            border: 2px solid #eef0f2;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
        }

        .icon-box {
            width: 45px;
            height: 45px;
            background: #f0f2f5;
            border-radius: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-left: 15px;
            font-size: 20px;
        }

        .res-text span {
            display: block;
            font-size: 12px;
            color: #65676b;
        }

        .res-text strong {
            font-size: 17px;
            color: var(--text-dark);
        }
    </style>
</head>
<body>

<div class="app-wrapper">
    <div class="header-section">
        <h2>حاسبة الطاقة الذكية</h2>
        <div class="info-tag">نظام 48V | لوح 630W</div>
    </div>

    <div class="input-box">
        <label>مجموع سحب الأجهزة (أمبير AC):</label>
        <input type="number" id="amps" placeholder="0.0">
    </div>

    <div class="input-box">
        <label>ساعات التشغيل المطلوبة:</label>
        <input type="number" id="hours" placeholder="مثلاً: 12">
    </div>

    <button class="calc-button" onclick="calculate()">احسب الآن</button>

    <div class="results-container" id="results">
        <div class="result-card">
            <div class="icon-box">☀️</div>
            <div class="res-text">
                <span>عدد الألواح (630 واط)</span>
                <strong id="panelCount">0 لوح</strong>
            </div>
        </div>

        <div class="result-card">
            <div class="icon-box">🔋</div>
            <div class="res-text">
                <span>سعة البطارية (الليثيوم)</span>
                <strong id="batCapacity">0 Ah @ 48V</strong>
            </div>
        </div>

        <div class="result-card">
            <div class="icon-box">⚡</div>
            <div class="res-text">
                <span>إجمالي الطاقة اليومية</span>
                <strong id="totalKwh">0 kWh</strong>
            </div>
        </div>
    </div>
</div>

<script>
    function calculate() {
        const amps = parseFloat(document.getElementById('amps').value);
        const hours = parseFloat(document.getElementById('hours').value);
        const panelWatt = 630;
        const voltageSystem = 48;
        const sunPeakHours = 5; // معدل ساعات الذروة

        if (amps > 0 && hours > 0) {
            // تحويل الأمبير إلى واط (بافتراض كهرباء البيت 220 فولت)
            const watts = amps * 220;
            const dailyConsumptionWh = watts * hours;
            const dailyKwh = dailyConsumptionWh / 1000;

            // حساب عدد الألواح (مع تعويض فاقد 15% للإنفرتر والأسلاك)
            const requiredPanelPower = (dailyConsumptionWh / sunPeakHours) * 1.15;
            const numberOfPanels = Math.ceil(requiredPanelPower / panelWatt);

            // حساب سعة بطارية الليثيوم 48 فولت (مع مراعاة عمق التفريغ 80%)
            const requiredAh = (dailyConsumptionWh / voltageSystem) / 0.8;

            // تحديث الواجهة
            document.getElementById('panelCount').innerText = numberOfPanels + " ألواح";
            document.getElementById('batCapacity').innerText = requiredAh.toFixed(1) + " أمبير (48V)";
            document.getElementById('totalKwh').innerText = dailyKwh.toFixed(2) + " كيلو واط/ساعة";
            
            document.getElementById('results').style.display = 'block';
        } else {
            alert("يرجى إدخال قيم صحيحة");
        }
    }
</script>

</body>
</html>
