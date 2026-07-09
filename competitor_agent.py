import json
import os

class CompetitorAgent:

    def research(self):
        print("Researching competitors...")

        competitors = [
            {
                "name": "TradingView",
                "website": "https://www.tradingview.com",
                "strength": "Charts and community"
            },
            {
                "name": "TrendSpider",
                "website": "https://trendspider.com",
                "strength": "AI market analysis"
            },
            {
                "name": "StockTwits",
                "website": "https://stocktwits.com",
                "strength": "Social trading discussions"
            }
        ]

        os.makedirs("data", exist_ok=True)

        with open("data/competitors.json", "w") as file:
            json.dump(competitors, file, indent=4)

        print("Competitor data saved.")

        return competitors