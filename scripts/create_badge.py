import re

BADGES = [
    ("C++", "#00599C"),
    ("Python", "#3776AB"),
    ("Java", "#ED8B00"),
    ("Go", "#00ADD8"),
    ("SQL", "#666666"),

    ("FastAPI", "#009688"),
    ("Pandas", "#150458"),
    ("Spring", "#6DB33F"),
    ("Qt", "#41CD52"),
    ("ROS", "#22314E"),
    ("PostgreSQL", "#336791"),

    ("Linux", "#FCC624"),
    ("Docker", "#2496ED"),
]

TEMPLATE = "../assets/template.svg"

create_name = lambda x: x.replace("++", "pp").lower()

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

    output_filename = f"badge_{create_name(label)}.svg"
    with open(f"../output/{output_filename}", "w", encoding="utf-8") as f:
        f.write(svg)
    
    print(f"Created: {output_filename}")


if __name__ == "__main__":
    print("--- Start generating badges ---")
    num = 0
    for label, color in BADGES:
        create_badge(label, color, f"../assets/{create_name(label)}.svg")
        num += 1
    print(f"--- Finish - {num} generated ---")