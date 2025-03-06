MODERN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        :root {
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --background: #f8fafc;
            --card-bg: #ffffff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        }

        body {
            background: linear-gradient(135deg, var(--background) 0%, #e2e8f0 100%);
            min-height: 100vh;
            padding: 2rem;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 2rem;
        }

        .title {
            font-size: 2.5rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        .stats {
            display: flex;
            gap: 1.5rem;
            justify-content: center;
            color: #64748b;
            margin-bottom: 1.5rem;
        }

        .card {
            background: var(--card-bg);
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-2px);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .event-name {
            font-size: 1.3rem;
            color: #1e293b;
            font-weight: 600;
        }

        .event-status {
            font-size: 0.9rem;
            padding: 0.3rem 0.7rem;
            border-radius: 999px;
            background: #e2e8f0;
            color: #475569;
        }

        .event-time {
            color: #64748b;
            margin-bottom: 0.8rem;
            font-size: 0.95rem;
        }

        .event-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--primary);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            background: rgba(99, 102, 241, 0.1);
            transition: all 0.2s;
        }

        .event-link:hover {
            background: rgba(99, 102, 241, 0.2);
        }

        .footer {
            text-align: center;
            color: #64748b;
            margin-top: 2rem;
            padding: 1rem;
            border-top: 1px solid #e2e8f0;
        }

        @media (max-width: 640px) {
            body {
                padding: 1rem;
            }
            
            .title {
                font-size: 2rem;
            }
            
            .stats {
                flex-direction: column;
                gap: 0.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="title">CTF赛事日历</h1>
            <div class="stats">
                <span>总赛事: {{ total }}</span>
                <span>当前显示: {{ competitions|length }}</span>
            </div>
        </div>

        {% for comp in competitions %}
        <div class="card">
            <div class="card-header">
                <span class="event-name">{{ comp.name }}</span>
                <span class="event-status">{{ comp.status }}</span>
            </div>
            <div class="event-time">
                {{ comp.start_time }} 至 {{ comp.end_time }}
            </div>
            <a href="{{ comp.link }}" target="_blank" class="event-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M4.715 6.542 3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 8.586 5.5L8 6.086a1 1 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4 4 0 0 1-.128-1.287z"/>
                    <path d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 1 1 2.83 2.83l-.793.792c.112.42.155.855.128 1.287l1.372-1.372a3 3 0 1 0-4.243-4.243z"/>
                </svg>
                赛事链接
            </a>
        </div>
        {% endfor %}

        <div class="footer">
            Data from HelloCTF • Updated at {{ updated_at }}
        </div>
    </div>
</body>
</html>
'''