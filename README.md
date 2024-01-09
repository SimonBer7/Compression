
# Compressor Application

Vítejte v aplikaci Compressor! Tento Python program poskytuje funkcionalitu pro komprimaci a dekomprimaci textových souborů a zároveň umožňuje zaznamenávání operací do logu.

## Obsah

- [Popis](#popis)
- [Funkce](#funkce)
- [Struktura Souborů](#struktura-souborů)
- [Použití](#použití)
- [Konfigurace](#konfigurace)
- [Závislosti](#závislosti)

## Popis

Aplikace Compressor umožňuje komprimovat a dekomprimovat textové soubory pomocí stylu zvaný camelCase. Zahrnuje také možnost zaznamenávání operací do logu.

## Funkce

- **Komprese Souboru:** Komprimuje obsah textového souboru pomocí formátu camelCase.
- **Dekomprese Souboru:** Dekomprimuje obsah komprimovaného textového souboru zpět do původního formátu.
- **Logování:** Zaznamenává různé operace, chyby a úspěšné události do logovacího souboru.

## Struktura Souborů

- **`compressor.py`**: Obsahuje hlavní třídu `Compressor` s metodami pro kompresi, dekompresi a kontrolu souborů.
- **`logmanager.py`**: Implementuje třídu `LogManager`, která zajišťuje operace logování.
- **`configuration.py`**: Spravuje konfigurační nastavení, jako jsou názvy vstupního a výstupního souboru.
- **`main.py`**: Hlavní vstupní bod aplikace s uživatelským rozhraním a příkazovou řádkou.
- **`logs/`**: Adresář pro ukládání logovacích souborů.

## Použití

1. **Nastavení:**
    - Spusťte `main.py`.
    - Vyberte mezi výchozím nastavením a vlastním nastavením.

2. **Možnosti:**
    - **Komprese souboru:** Volba 1 v menu. Kompresuje zadaný vstupní soubor.
    - **Dekomprese souboru:** Volba 2 v menu. Dekomprimuje zadaný výstupní soubor.
    - **Vypsání logu:** Volba 3 v menu. Zobrazuje obsah logovacího souboru.
    - **Nápověda:** Volba 4 v menu. Poskytuje stručný manuál k používání aplikace.
    - **Ukončení:** Volba 5 v menu. Ukončuje aplikaci.

## Konfigurace

- Výchozí vstupní soubor: "input.txt"
- Výchozí výstupní soubor: "output.txt"

Během nastavení můžete upravit názvy vstupního a výstupního souboru.

## Závislosti

- Python 3.x

Užijte si komprimaci a dekomprimaci souborů s aplikací Kompresor! Pokud narazíte na nějaké problémy, podívejte se do logů pro více informací.

