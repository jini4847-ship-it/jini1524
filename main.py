from etf import get_etf
from kakao import send_kakao

etfs = {
    "TIGER 미국S&P500": "SPY",
    "KODEX 미국나스닥100": "QQQ",
    "TIGER 미국필라델피아반도체": "SOXX",
    "ACE KRX금현물": "GLD",
    "TIGER 미국배당다우존스": "SCHD",
    "ACE 미국배당퀄리티": "DGRO"
}

def build_message():
    msg = "[연금저축 ETF 알림]\n\n"

    for name, ticker in etfs.items():
        price, change, pct = get_etf(ticker)

        arrow = "🔥" if pct < -2 else ""

        msg += f"{name}\n현재가: {price:.2f}\n변동: {pct:+.2f}% ({change:+.2f}) {arrow}\n\n"

    msg += "추천\n- 나스닥 20만원\n- 반도체 30만원"

    return msg


def run():
    message = build_message()
    send_kakao(message)


if __name__ == "__main__":
    run()
