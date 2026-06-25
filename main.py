from etf import get_etf
from kakao import send_kakao

etfs = {
    "TIGER 미국S&P500": "360750.KS",
    "KODEX 미국나스닥100": "379800.KS",
    "TIGER 미국필라델피아반도체": "381180.KS",
    "ACE KRX금현물": "411060.KS",
    "TIGER 미국배당다우존스": "458730.KS",
    "ACE 미국배당퀄리티": "441640.KS"
}

def build_message():
    msg = "📊 [연금저축 ETF 데일리 리포트]\n\n"
    msg += "🕙 기준: 자동 업데이트\n\n"
    msg += "━━━━━━━━━━━━━━\n\n"
    msg += "🔥 MARKET SNAPSHOT\n\n"

    for name, ticker in etfs.items():
        price, change, pct = get_etf(ticker)

        if price is None:
            continue

        emoji = "📉" if pct < 0 else "📈"
        hot = "🔥" if pct < -2 else ""

        msg += f"{name} {hot}\n"
        msg += f"💰 현재가: {price}\n"
        msg += f"{emoji} 변동: {pct:+.2f}% ({change:+.2f})\n\n"

    msg += "━━━━━━━━━━━━━━\n\n"
    msg += "🧠 투자 전략\n\n"
    msg += "✔ 나스닥 조정 구간 → 분할매수 고려\n"
    msg += "✔ 반도체 과매도 구간\n"
    msg += "✔ 금: 방어 자산 유지\n\n"

    msg += "━━━━━━━━━━━━━━\n\n"
    msg += "💡 추천 매수\n\n"
    msg += "- 나스닥100 : 20만원\n"
    msg += "- 반도체 : 30만원\n\n"

    msg += "━━━━━━━━━━━━━━\n"
    msg += "📌 자동 알림 시스템"

    return msg

def run():
    message = build_message()
    send_kakao(message)


if __name__ == "__main__":
    run()
