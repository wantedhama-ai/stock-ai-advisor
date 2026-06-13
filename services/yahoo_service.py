import yfinance as yf


class YahooService:

    def get_stock_data(self, ticker):

        try:

            stock = yf.Ticker(ticker)

            info = stock.info

            return {
                "ticker": ticker,
                "current_price": info.get("currentPrice"),
                "market_cap": info.get("marketCap"),
                "pe": info.get("trailingPE"),
                "pb": info.get("priceToBook"),
                "eps": info.get("trailingEps"),
                "revenue": info.get("totalRevenue"),
                "operating_margin": info.get("operatingMargins"),
                "gross_margin": info.get("grossMargins"),
                "free_cash_flow": info.get("freeCashflow"),
                "net_income": info.get("netIncomeToCommon"),
                "total_debt": info.get("totalDebt"),
                "total_equity": info.get("totalStockholderEquity"),
                "recommendation": info.get("recommendationKey")
            }

        except Exception as e:

            print(f"{ticker} 오류 발생: {e}")

            return None