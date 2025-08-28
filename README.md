# password-check-devops
Praktische CI/CD Einheit in der Lerneinheit Testmanagement (LF10)

# 🔐 DevOps-Übung: Passwort-Checker mit GitHub Actions & Unit-Tests

## 🎯 Ziel

In dieser Aufgabe wirst du:

- eine bestehende Python-Funktion zur Passwortprüfung testen,
- **Black-Box- und White-Box-Tests** schreiben,
- automatisierte Tests mit **GitHub Actions (CI)** einrichten,
- einen Fehler im Quellcode durch Tests erkennen (je nach Version).

---

## 🧱 Voraussetzungen

Bitte stelle sicher, dass du folgendes beherrschst oder bereit bist zu lernen:

- Python-Grundlagen
- `pytest`
- Arbeiten mit GitHub (Fork, Commit, Push)
- Grundverständnis für **CI/CD** und **GitHub Actions**
- Basiswissen in **YAML**

---

## 🗂️ Projektstruktur

```plaintext
password-check-devops/
├── password_checker.py          # Passwortprüfung
├── test_password_checker.py     # Hier schreibst du deine Tests
├── README.md                    # Diese Datei
└── .github/
    └── workflows/
        └── python-tests.yml     # CI/CD Workflow für GitHub Actions
