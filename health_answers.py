
def get_health_answer(question):
    question = question.lower().strip()

    if any(word in question for word in ["water", "hydration", "drink"]):
        return (
            "Drinking enough water helps maintain normal body functions. "
            "Drink water regularly throughout the day."
        )

    elif any(word in question for word in ["sleep", "insomnia", "sleeping"]):
        return (
            "Maintain a regular sleep schedule, reduce screen use before "
            "bedtime, and keep your bedroom comfortable."
        )

    elif any(word in question for word in ["digestion", "digestive", "constipation"]):
        return (
            "Eat fiber-rich foods, drink enough water, and stay physically "
            "active to support digestive health."
        )

    elif any(word in question for word in ["stress", "anxiety", "relax"]):
        return (
            "Try slow breathing, regular exercise, adequate sleep, and "
            "talking with someone you trust."
        )

    elif any(word in question for word in ["fever", "temperature"]):
        return (
            "Rest, drink fluids if you can, and monitor your symptoms. "
            "Seek medical advice if symptoms persist or worsen."
        )

    elif any(word in question for word in ["headache", "head pain"]):
        return (
            "Rest, drink water, and take a break from screens if helpful. "
            "Seek urgent help for a sudden, extremely severe headache."
        )

    elif any(word in question for word in ["cold", "cough", "sneeze"]):
        return (
            "For mild cold symptoms, rest and drink fluids. "
            "Seek medical advice if symptoms worsen or breathing becomes difficult."
        )

    elif any(word in question for word in ["healthy food", "healthy eating", "nutrition", "diet"]):
        return (
            "Aim for a balanced diet containing vegetables, fruits, "
            "whole grains, and suitable protein sources."
        )

    elif any(word in question for word in ["infection", "hygiene", "germs"]):
        return (
            "Wash your hands regularly, cover coughs and sneezes, "
            "and keep vaccinations up to date."
        )

    else:
        return (
            "I do not have a predefined answer for this question yet. "
            "Please consult a reliable health resource or healthcare professional."
        )
