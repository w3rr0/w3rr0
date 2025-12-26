import re

BADGES = [
    ("C++", "#00599C", "../assets/cpp.svg"),
    ("Python", "#3776AB", "../assets/python.svg"),
    ("Java", "#ED8B00", "../assets/java.svg")
]

TEMPLATE = "../assets/template.svg"

def extract_svg_content(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
            if match:
                return match.group(1)
            else:
                return content
    except FileNotFoundError:
        print(f"BŁĄD: Nie znaleziono pliku logo: {filepath}")
        return None
    
def create_badge(label, color, icon_path):
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        svg = f.read()

    icon_content = extract_svg_content(icon_path)
    if not icon_content:
        return

    svg = svg.replace("{{LABEL}}", label)
    svg = svg.replace("{{COLOR}}", color)
    svg = svg.replace("{{LOGO}}", icon_content)

    output_filename = f"badge_{label.lower().replace('++', 'pp')}.svg"
    with open(f"../output/{output_filename}", "w", encoding="utf-8") as f:
        f.write(svg)
    
    print(f"Sukces! Utworzono: {output_filename}")


if __name__ == "__main__":
    print("--- Rozpoczynam generowanie odznak ---")
    for label, color, path in BADGES:
        create_badge(label, color, path)
    print("--- Gotowe! ---")