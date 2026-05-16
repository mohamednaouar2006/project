import random


questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "options": ["A. Lyon", "B. Marseille", "C. Paris", "D. Bordeaux"],
        "reponse": "C"
    },
    {
        "question": "Combien de planètes y a-t-il dans le système solaire ?",
        "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "reponse": "B"
    },
    {
        "question": "Quel est le plus grand océan du monde ?",
        "options": ["A. Atlantique", "B. Indien", "C. Arctique", "D. Pacifique"],
        "reponse": "D"
    },
    {
        "question": "En quelle année a eu lieu la Révolution française ?",
        "options": ["A. 1789", "B. 1799", "C. 1776", "D. 1815"],
        "reponse": "A"
    },
    {
        "question": "Quel langage de programmation a été créé par Guido van Rossum ?",
        "options": ["A. Java", "B. C++", "C. Python", "D. Ruby"],
        "reponse": "C"
    },
    {
        "question": "Combien de côtés a un hexagone ?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "reponse": "B"
    },
    {
        "question": "Quel est l'élément chimique dont le symbole est 'O' ?",
        "options": ["A. Or", "B. Osmium", "C. Oxygène", "D. Ozone"],
        "reponse": "C"
    },
]


def afficher_banniere():
    print("=" * 45)
    print("        🎯  BIENVENUE AU QUIZ !  🎯       ")
    print("=" * 45)
    print()


def jouer():
    afficher_banniere()

    score = 0
    questions_melangees = random.sample(questions, len(questions))

    for i, q in enumerate(questions_melangees, 1):
        print(f"Question {i}/{len(questions_melangees)} : {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        while True:
            reponse = input("Votre réponse (A/B/C/D) : ").strip().upper()
            if reponse in ["A", "B", "C", "D"]:
                break
            print("⚠️  Réponse invalide. Entrez A, B, C ou D.")

        if reponse == q["reponse"]:
            print("✅ Bonne réponse !\n")
            score += 1
        else:
            bonne = next(o for o in q["options"] if o.startswith(q["reponse"]))
            print(f"❌ Mauvaise réponse. La bonne réponse était : {bonne}\n")

    print("=" * 45)
    print(f"   🏆 Score final : {score} / {len(questions_melangees)}")
    if score == len(questions_melangees):
        print("   🎉 Parfait ! Tu es un génie !")
    elif score >= len(questions_melangees) // 2:
        print("   👍 Bien joué ! Continue comme ça !")
    else:
        print("   💪 Pas de souci, réessaie pour t'améliorer !")
    print("=" * 45)


def main():
    while True:
        jouer()
        print()
        rejouer = input("Veux-tu rejouer ? (o/n) : ").strip().lower()
        if rejouer != "o":
            print("\nMerci d'avoir joué ! À bientôt 👋")
            break
        print()


if __name__ == "__main__":
    main()