import json

from services.yahoo_service import YahooService
from services.score_service import ScoreService
from services.database_service import DatabaseService
from services.telegram_service import TelegramService


def main():

    yahoo = YahooService()
    db = DatabaseService()
    telegram = TelegramService()

    with open("portfolio.json", "r", encoding="utf-8") as f:
        portfolio = json.load(f)

    print("\n📈 오늘의 투자 리포트")
    print("=" * 50)

    total_portfolio_value = 0
    stock_results = []

    # -------------------------
    # 데이터 수집
    # -------------------------
    for stock in portfolio:

        ticker = stock["ticker"]
        shares = stock["shares"]

        data = yahoo.get_stock_data(ticker)

        if data is None:
            continue

        current_price = data["current_price"]

        if current_price is None:
            continue

        position_value = current_price * shares
        total_portfolio_value += position_value

        stock_results.append({
            "stock": stock,
            "data": data,
            "position_value": position_value
        })

    # -------------------------
    # 분석 + 출력 + 메시지 생성
    # -------------------------
    message = "📈 오늘의 투자 리포트\n\n"

    for item in stock_results:

        stock = item["stock"]
        data = item["data"]

        ticker = stock["ticker"]
        avg_cost = stock["avg_cost"]
        shares = stock["shares"]

        current_price = data["current_price"]

        profit_ratio = ((current_price - avg_cost) / avg_cost) * 100
        profit_amount = (current_price - avg_cost) * shares

        portfolio_weight = (item["position_value"] / total_portfolio_value) * 100

        tech_score = ScoreService.calculate_tech_score(
            data["market_cap"],
            data["gross_margin"],
            data["operating_margin"],
            data["recommendation"]
        )

        buffett_score = ScoreService.calculate_buffett_score(
            data["market_cap"],
            data["gross_margin"],
            data["operating_margin"],
            data["pe"]
        )

        final_score = ScoreService.calculate_final_score(
            buffett_score,
            tech_score
        )

        grade = ScoreService.get_grade(final_score)

        db.save(
            ticker,
            current_price,
            None,
            None,
            final_score
        )

        # 콘솔 출력
        print(f"\n{ticker}")
        print("-" * 30)
        print(f"현재가: ${current_price:.2f}")
        print(f"평단가: ${avg_cost:.2f}")
        print(f"보유수량: {shares}")
        print(f"수익률: {profit_ratio:.2f}%")
        print(f"평가손익: ${profit_amount:.2f}")
        print(f"포트폴리오 비중: {portfolio_weight:.2f}%")
        print(f"Buffett Score: {buffett_score}")
        print(f"Tech Score: {tech_score}")
        print(f"Final Score: {final_score}")
        print(f"등급: {grade}")

        # 텔레그램 메시지 추가
        message += f"{ticker}\n"
        message += f"수익률: {profit_ratio:.2f}%\n"
        message += f"Final Score: {final_score}\n"
        message += f"등급: {grade}\n\n"

    print("\n분석 완료")

    # -------------------------
    # 텔레그램 전송
    # -------------------------
    telegram.send_message(message)


if __name__ == "__main__":
    main()