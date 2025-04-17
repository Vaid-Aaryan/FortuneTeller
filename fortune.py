import random

def main():
    print("🔮 Welcome to Vaid Aaryan's Fortune Teller (21JE01019) 🔮")
    
    mood = input("How are you feeling today? (happy/sad/neutral/excited/stressed/confused): ").lower()
    
    happy_fortunes = [
        "✨ Your fortune: Great things await you, Vaid Aaryan! Keep smiling. ✨",
        "✨ Your fortune: Your positive energy will lead to wonderful opportunities today! ✨",
        "✨ Your fortune: The sun shines brighter because of your happiness! ✨"
    ]
    
    sad_fortunes = [
        "✨ Your fortune: Better days are coming. Tomorrow will bring you joy. ✨",
        "✨ Your fortune: Even in darkness, Vaid Aaryan, you'll find your inner light. ✨",
        "✨ Your fortune: This feeling is temporary. Happiness awaits around the corner. ✨"
    ]
    
    neutral_fortunes = [
        "✨ Your fortune: Balance in all things will lead you to success. ✨", 
        "✨ Your fortune: Vaid Aaryan, your calm demeanor will help solve a mystery today. ✨",
        "✨ Your fortune: Neither too high nor too low - you're on the perfect path. ✨"
    ]

    excited_fortunes = [
        "✨ Your fortune: Channel your excitement into creating something amazing today! ✨",
        "✨ Your fortune: Vaid Aaryan's enthusiasm will inspire others around you! ✨",
        "✨ Your fortune: Your excited energy will attract wonderful opportunities! ✨"
    ]
    
    stressed_fortunes = [
        "✨ Your fortune: Take a deep breath. The challenges you face will soon pass. ✨",
        "✨ Your fortune: Vaid Aaryan, remember that difficult times build strength. ✨",
        "✨ Your fortune: Today's stress is preparing you for tomorrow's success. ✨"
    ]
    
    confused_fortunes = [
        "✨ Your fortune: Clarity will come when you least expect it. ✨",
        "✨ Your fortune: Vaid Aaryan, trust your intuition to guide you through uncertainty. ✨",
        "✨ Your fortune: The fog will lift soon, revealing your true path. ✨"
    ]
    
    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))
    elif mood == "excited":
        print(random.choice(excited_fortunes))
    elif mood == "stressed":
        print(random.choice(stressed_fortunes))
    elif mood == "confused":
        print(random.choice(confused_fortunes))    
    else:
        print("✨ Your fortune: I cannot read your mood, but Vaid Aaryan's destiny is still bright! ✨")

if __name__ == "__main__":
    main()