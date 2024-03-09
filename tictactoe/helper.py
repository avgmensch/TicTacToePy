# ===========================
# User input
# ===========================

def ask_confirm(msg: str = "") -> bool:
    s: str = input(msg).strip()
    return s == "" or s[0] == "y" or s[0] == "Y"
