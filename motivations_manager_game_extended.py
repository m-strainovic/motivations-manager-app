
def motivations_manager():
    print("🎯 Willkommen bei 'Motivations-Manager – Was bringt Zufriedenheit?'\n")
    print("Du bist Führungskraft und triffst Entscheidungen, um deine Mitarbeitenden zufriedenzustellen.\n")

    zufriedenheit = 0

    mitarbeiter = [
        ("Lisa", "sicherheitsorientiert, zuverlässig und risikoscheu", "1) Fixes Gehalt und Altersvorsorge", "2) Akkordlohn und Erfolgsprämie", "1", "Maslow: Sicherheitsbedürfnis", "Herzberg: Hygienefaktor (Gehalt)"),
        ("Max", "leistungsorientiert und liebt Herausforderungen", "1) Regelmäßige Gehaltserhöhungen", "2) Leistungsprämien und Zielvereinbarungen", "2", "Herzberg: Motivator (Leistung)", ""),
        ("Ali", "neu im Unternehmen, sucht Anschluss und Entwicklung", "1) Einführungsseminare und Teambuilding", "2) Dienstwagen und Einzelbüro", "1", "Maslow: soziale Bedürfnisse", "SDT: Eingebundenheit"),
        ("Sarah", "möchte Verantwortung übernehmen und wachsen", "1) Weiterbildung und Führungsprogramme", "2) Homeoffice mit fixer Routine", "1", "Herzberg: Motivator (Wachstum)", ""),
        ("Jonas", "wünscht sich ein stabiles, faires Umfeld", "1) Transparente Kommunikation und Gleichbehandlung", "2) Bonus nur für Top-Performer", "1", "SDT: Fairness & Autonomie", ""),
        ("Elena", "möchte Familie und Arbeit gut vereinbaren", "1) Flexible Arbeitszeiten & Kinderbetreuung", "2) Projektarbeit mit langen Deadlines", "1", "Maslow: Sicherheit & Familie", ""),
        ("David", "strebt nach Anerkennung für seine Leistung", "1) Rückmeldungsgespräche & Lob", "2) Mehr Gehalt ohne Feedback", "1", "Herzberg: Motivator (Anerkennung)", ""),
        ("Nina", "braucht klare Ziele und Feedback zur Weiterentwicklung", "1) Mentoring und Karriereplanung", "2) Freiraum ohne Führung", "1", "Herzberg: Motivator (Karriere)", ""),
        ("Tobias", "ist introvertiert, schätzt klare Strukturen", "1) Klare Aufgaben und Prozesssicherheit", "2) Kreativteam mit wechselnden Rollen", "1", "Maslow: Struktur/Sicherheit", ""),
        ("Amira", "möchte sich selbst verwirklichen und ihre Ideen einbringen", "1) Innovationsprojekte mit Eigenverantwortung", "2) Routinetätigkeit mit wenig Abwechslung", "1", "Maslow: Selbstverwirklichung", "SDT: Autonomie")
    ]

    for name, beschreibung, option1, option2, richtige_antwort, theorie1, theorie2 in mitarbeiter:
        print(f"👤 Mitarbeiter/in: {name}")
        print(f"{name} ist {beschreibung}.")
        print("Was bietest du an?")
        print(f"1) {option1}")
        print(f"2) {option2}")
        wahl = input("Deine Wahl (1 oder 2): ")

        if wahl == richtige_antwort:
            print(f"\n✅ Gute Entscheidung! {theorie1}", end="")
            if theorie2:
                print(f" und {theorie2}.")
            else:
                print(".")
            zufriedenheit += 1
        else:
            print("\n❌ Diese Entscheidung entspricht nicht den Bedürfnissen.")
            zufriedenheit -= 1
        print()

    print("\n🎯 Spielende – Auswertung deiner Führungskompetenz:")
    print(f"Gesamtpunkte: {zufriedenheit}/10")
    if zufriedenheit == 10:
        print("🏆 Exzellent! Du hast alle Bedürfnisse optimal erkannt und erfüllt.")
    elif zufriedenheit >= 7:
        print("🎉 Sehr gut! Du hast ein gutes Gespür für Motivation.")
    elif zufriedenheit >= 4:
        print("🙂 In Ordnung, aber es ist noch Luft nach oben.")
    else:
        print("❌ Deine Entscheidungen haben wenig Zufriedenheit erzeugt. Analysiere die Bedürfnisse genauer!")

motivations_manager()
