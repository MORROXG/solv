import time
import sys

# ANSI escape codes for text colors
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Funkce pro pomalé psaní textu, aby to vypadalo realisticky
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Zobrazení banneru (červená barva)
slow_print(RED + "XSOLVER BY ALFI KEITA\n" + RESET, delay=0.1)

# Žádost o zadání IP adresy (modrá barva)
ip_address = input(BLUE + "Enter IP address: " + RESET)

# Simulace průběhu zpráv (zelená barva)
slow_print(GREEN + f"[!] IP address found: {ip_address}\n" + RESET, delay=0.05)

# Iterace pro zobrazení zpráv simulujících nalezení exploitu a jeho řešení
for i in range(28):
    slow_print(GREEN + "[+] Network DDoS found exploit. Resolving..." + RESET, delay=0.05)
    time.sleep(0.2)  # Krátká prodleva mezi zprávami

# Poslední dvě zprávy (zelená barva)
slow_print(GREEN + "[!] Resolved. Rebooting..." + RESET, delay=0.05)
slow_print(GREEN + "Reboot your software.\n" + RESET, delay=0.05)