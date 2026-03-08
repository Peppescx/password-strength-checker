"""
Modulo avanzato per la verifica della robustezza delle password.
Include analisi dettagliata dei criteri e feedback per l'utente.
"""

import math
import re


def calculate_entropy(password: str) -> float:
    """
    Calcola l'entropia della password in bit.
    Formula: E = L * log2(R) dove R è il pool di caratteri usati.
    """
    if not password:
        return 0.0

    pool = 0
    if re.search("[a-z]", password):
        pool += 26
    if re.search("[A-Z]", password):
        pool += 26
    if re.search("[0-9]", password):
        pool += 10
    if re.search('[!@#$%^&*(),.?":{}|<>]', password):
        pool += 32

    if pool == 0:
        return 0.0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)


