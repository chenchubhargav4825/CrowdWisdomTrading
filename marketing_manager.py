from agents.competitor_agent import CompetitorAgent

class MarketingManager:

    def __init__(self):
        self.competitor_agent = CompetitorAgent()

    def run(self):
        print("================================")
        print("CrowdWisdom Marketing Manager")
        print("================================")

        competitors = self.competitor_agent.research()

        print()
        print("Competitors Found:")

        for competitor in competitors:
            print("-", competitor["name"])

        print()
        print("Workflow Completed")