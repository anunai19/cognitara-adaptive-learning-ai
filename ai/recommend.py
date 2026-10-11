
def recommend_intervention(percentage):
    if percentage < 40:
        return (
            "Start with a visual explanation of recursion, "
            "learn how the base case works, and solve simple examples."
        )

    elif percentage < 70:
        return (
            "Review step-by-step recursive function examples "
            "and practise tracing function calls."
        )

    else:
        return (
            "You have a good starting understanding. "
            "Try advanced recursion problems and coding challenges."
        )
      
