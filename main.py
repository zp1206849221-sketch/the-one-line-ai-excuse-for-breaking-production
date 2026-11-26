import os

LINE = "Good news: it still works on my machine. Bad news: after that Friday deploy, production is my machine — and I just paged you to fix it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
