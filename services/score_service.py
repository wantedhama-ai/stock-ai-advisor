class ScoreService:

    @staticmethod
    def calculate_tech_score(
            market_cap,
            gross_margin,
            operating_margin,
            recommendation):

        score = 0

        # Market Cap (25)

        if market_cap:

            if market_cap >= 100_000_000_000:
                score += 25

            elif market_cap >= 50_000_000_000:
                score += 20

            elif market_cap >= 10_000_000_000:
                score += 10

            else:
                score += 5

        # Gross Margin (25)

        if gross_margin:

            gross_margin *= 100

            if gross_margin >= 60:
                score += 25

            elif gross_margin >= 50:
                score += 20

            elif gross_margin >= 40:
                score += 10

        # Operating Margin (25)

        if operating_margin:

            operating_margin *= 100

            if operating_margin >= 20:
                score += 25

            elif operating_margin >= 15:
                score += 20

            elif operating_margin >= 10:
                score += 10

        # Analyst Recommendation (25)

        if recommendation:

            recommendation = recommendation.lower()

            if recommendation == "strong_buy":
                score += 25

            elif recommendation == "buy":
                score += 20

            elif recommendation == "hold":
                score += 10

        return score

    @staticmethod
    def calculate_buffett_score(
            market_cap,
            gross_margin,
            operating_margin,
            pe):

        score = 0

        # Market Cap

        if market_cap:

            if market_cap >= 100_000_000_000:
                score += 25

            elif market_cap >= 50_000_000_000:
                score += 20

            elif market_cap >= 10_000_000_000:
                score += 10

        # Gross Margin

        if gross_margin:

            gross_margin *= 100

            if gross_margin >= 60:
                score += 25

            elif gross_margin >= 50:
                score += 20

            elif gross_margin >= 40:
                score += 10

        # Operating Margin

        if operating_margin:

            operating_margin *= 100

            if operating_margin >= 20:
                score += 25

            elif operating_margin >= 15:
                score += 20

            elif operating_margin >= 10:
                score += 10

        # PER

        if pe:

            if 10 <= pe <= 25:
                score += 25

            elif 25 < pe <= 35:
                score += 15

        return score

    @staticmethod
    def calculate_final_score(
            buffett_score,
            tech_score):

        return round(
            (buffett_score * 0.4) +
            (tech_score * 0.6),
            1
        )

    @staticmethod
    def get_grade(score):

        if score >= 90:
            return "Excellent"

        elif score >= 80:
            return "Good"

        elif score >= 70:
            return "Fair"

        elif score >= 60:
            return "Weak"

        return "Poor"