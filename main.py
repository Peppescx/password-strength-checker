from src.checker import analyze_password, calculate_entropy, validate_email


def main():
    """Menu principale dell'applicazione (Solo Analisi)."""
    print("=== Security Tool v2.0 ===")
    print("1. Analizza una password")
    print("2. Esci")

    scelta = input("\nScegli un'opzione (1/2): ")

    if scelta == "1":
        pwd = input("Inserisci la password da analizzare: ")

        # Calcolo entropia e analisi
        entropia = calculate_entropy(pwd)
        livello, criticita = analyze_password(pwd)

        print("\n--- Analisi Sicurezza ---")
        print(f"Livello: {livello}")
        print(f"Entropia: {entropia} bit")

        if criticita:
            print("Criticità riscontrate:")
            for nota in criticita:
                print(f" [!] {nota}")
        else:
            print(" [+] Nessuna criticità rilevata.")

        # Richiesta email per il report con validazione
        email = input("\nInserisci la tua email per il report: ")
        if validate_email(email):
            # report da fare
            print("salvare dati..")
        else:
            print("Email non valida. Il report non verrà salvato.")

    elif scelta == "2":
        print("Chiusura del programma. Stay safe!")
    else:
        print("Opzione non valida.")


if __name__ == "__main__":
    main()
