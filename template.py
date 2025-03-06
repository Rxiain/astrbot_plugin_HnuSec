CTF_MATCH_TMPL = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
:root {
    --live: #ff4757;
    --upcoming: #2ed573;
    --ended: #57606f;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', system-ui, sans-serif;
}

.container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1rem;
}

.match-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
    position: relative;
    border: 1px solid rgba(0, 0, 0, 0.08);
}

.match-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1.2rem;
}

.match-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #2d3436;
    margin-right: 1rem;
}

.match-status {
    font-size: 0.9rem;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-weight: 600;
}

.status-ended {
    background: var(--ended);
    color: white;
}

.match-meta {
    display: flex;
    gap: 1rem;
    color: #636e72;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.time-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin: 1rem 0;
}

.time-card {
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
    position: relative;
}

.time-card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 4px;
    background: #70a1ff;
    border-radius: 4px;
}

.time-label {
    font-size: 0.85rem;
    color: #636e72;
    margin-bottom: 0.3rem;
}

.time-value {
    font-weight: 600;
    color: #2d3436;
}

.detail-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0.5rem 0;
    font-size: 0.95rem;
}

.detail-item i {
    width: 1.2rem;
    color: #636e72;
}

.qq-group {
    background: #f1f2f6;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.qq-group::before {
    content: "👥";
    font-size: 0.9rem;
}

.readmore {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    font-size: 0.9rem;
    line-height: 1.6;
    color: #636e72;
}

.reg-btn {
    display: inline-block;
    background: #70a1ff;
    color: white !important;
    padding: 0.6rem 1.5rem;
    border-radius: 6px;
    text-decoration: none;
    margin-top: 1rem;
    transition: transform 0.2s;
}

.reg-btn:hover {
    transform: translateY(-2px);
}
</style>
</head>
<body>
<div class="container">
    <h1 style="text-align: center; margin-bottom: 2rem; color: #2d3436; font-size: 2rem;">🏆 CTF 赛事列表 (共{{ data.total }}场)</h1>
    
    {% for match in data.result %}
    <div class="match-card">
        <div class="match-header">
            <div>
                <div class="match-title">{{ match.name }}</div>
                <div class="match-meta">
                    <span>📌 {{ match.type }}</span>
                    <span>🏷️ {{ match.tag if match.tag else '常规赛' }}</span>
                    <span>🏛️ {{ match.organizer }}</span>
                </div>
            </div>
            <div class="match-status status-ended">{{ match.status }}</div>
        </div>

        <div class="time-grid">
            <div class="time-card">
                <div class="time-label">⏳ 注册时间</div>
                <div class="time-value">{{ match.reg_time_start }}<br>至 {{ match.reg_time_end }}</div>
            </div>
            <div class="time-card">
                <div class="time-label">🏁 比赛时间</div>
                <div class="time-value">{{ match.comp_time_start }}<br>至 {{ match.comp_time_end }}</div>
            </div>
        </div>

        <div class="detail-item">
            <i>📞</i>
            <div class="qq-group">
                {% for platform, contact in match.contac.items() %}
                {{ platform }}: {{ contact }}
                {% endfor %}
            </div>
        </div>

        <div class="detail-item">
            <i>🌐</i>
            <a href="{{ match.link }}" target="_blank">{{ match.link }}</a>
        </div>

        <div class="readmore">
            {{ match.readmore }}
        </div>

        {% if match.is_reg %}
        <a href="{{ match.link }}" class="reg-btn" target="_blank">立即报名</a>
        {% endif %}
    </div>
    {% endfor %}
</div>
</body>
</html>
'''