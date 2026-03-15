"""Unit test per il modulo src.checker."""

import os

import pytest

from src.checker import (
    analyze_password,
    calculate_entropy,
    generate_secure_password,
    get_password_criteria,
    get_strength_bar,
    is_commonly_used,
    save_report,
    validate_email,
)


@pytest.mark.parametrize(
    "password,expected_level",
    [
        # 1. Livello: Pessima (Password cortissima o molto comune)
        ("123456", "Pessima"),
        # 2. Livello: Debole (Corta e senza varietà)
        ("sololeggere", "Debole"),
        # 3. Livello: Media (Lunghezza ok, ma manca qualche criterio)
        # Ad esempio: solo lettere e numeri, senza caratteri speciali
        ("Progetto2024", "Media"),
        # 4. Livello: Forte (Lunga, maiuscole, numeri e caratteri speciali)
        ("P@ssw0rdSicura2025!!", "Forte"),
    ],
)
def test_analyze_password(password, expected_level):
    """Testa tutti i livelli di giudizio sulla robustezza."""
    livello, _ = analyze_password(password)
    assert livello == expected_level


def test_password_criteria():
    """
    Verifica che la funzione get_password_criteria identifichi
    correttamente tutti i criteri di sicurezza soddisfatti da
    una password complessa.
    """
    criteria = get_password_criteria("Password1!")
    assert criteria["length"][0] is True
    assert criteria["lowercase"][0] is True
    assert criteria["uppercase"][0] is True
    assert criteria["numbers"][0] is True
    assert criteria["special"][0] is True


@pytest.mark.parametrize(
    "password,condition",
    [
        # Password vuota
        ("", lambda x: x == 0.0),
        # Pool = 0 (solo spazi)
        ("   ", lambda x: x == 0.0),
        # Password corta solo minuscole = entropia bassa
        ("abc", lambda x: x < 20),
        # Password complessa = entropia alta
        ("A1!b2C3#d4E5", lambda x: x > 50),
    ],
)
def test_calculate_entropy(password, condition):
    """Testa il calcolo dell'entropia."""
    assert condition(calculate_entropy(password))


@pytest.mark.parametrize(
    "email,expected",
    [
        ("test@unict.it", True),
        ("email_errata.it", False),
        ("TEST@MAIL.COM", True),
    ],
)
def test_validate_email(email, expected):
    """Testa la validazione delle email."""
    assert validate_email(email) is expected


@pytest.mark.parametrize(
    "password,expected",
    [
        # Questo funzionerà se hai creato data/common_passwords.txt
        ("123456", True),
        ("UnaPasswordMoltoRara2026!", False),
    ],
)
def test_is_commonly_used(password, expected):
    """Testa il rilevamento di password comuni."""
    assert is_commonly_used(password) is expected


def test_is_commonly_used_missing_file(monkeypatch):
    """
    Simula il caso in cui il file contenente le password comuni
    non sia presente nel filesystem.
    """
    monkeypatch.setattr("os.path.exists", lambda x: False)
    assert is_commonly_used("123456") is False


def test_is_commonly_used_io_error(monkeypatch):
    """
    Verifica la gestione di errori di I/O durante la lettura del file
    delle password comuni.
    """

    def mock_open(*args, **kwargs):
        raise OSError

    monkeypatch.setattr("builtins.open", mock_open)
    assert is_commonly_used("password") is False


def test_generate_password_variants():
    """Testa la generazione con e senza caratteri speciali."""
    pwd1 = generate_secure_password(length=16, use_special=True)
    assert len(pwd1) == 16
    pwd2 = generate_secure_password(length=8, use_special=False)
    assert len(pwd2) == 8


def test_generate_password_contains_special():
    """
    Verifica che la funzione generate_secure_password produca
    effettivamente password contenenti caratteri speciali quando
    l'opzione use_special è attiva.

    Il test controlla che almeno uno dei caratteri speciali previsti
    sia presente nella password generata.
    """
    pwd = generate_secure_password(length=20, use_special=True)
    assert any(c in '!@#$%^&*(),.?":{}|<>' for c in pwd)


def test_save_report_execution():
    """Testa il salvataggio fisico del file JSON."""
    test_file = "test_result.json"
    result = save_report("TestPassword123!", filename=test_file)
    assert result is True
    assert os.path.exists(test_file)
    # Pulizia dopo il test
    if os.path.exists(test_file):
        os.remove(test_file)


def test_save_report_io_error(monkeypatch):
    """
    Testa il comportamento della funzione save_report quando si verifica
    un errore di scrittura sul filesystem.
    """

    def mock_open(*args, **kwargs):
        raise IOError

    monkeypatch.setattr("builtins.open", mock_open)
    assert save_report("Password123!") is False


@pytest.mark.parametrize(
    "password,expected_symbol",
    [
        # Verifica che una password debole produca una barra con blocchi vuoti
        ("abc", "░"),
        # Verifica che una password forte produca una barra con blocchi pieni
        ("Complessa_!@_99_Z", "█"),
    ],
)
def test_strength_bar_symbols(password, expected_symbol):
    strength_bar = get_strength_bar(password)
    assert expected_symbol in strength_bar


def test_strength_bar_format():
    """Verifica che l'output contenga una percentuale"""
    strength_bar = get_strength_bar("Password123!")
    assert "%" in strength_bar
