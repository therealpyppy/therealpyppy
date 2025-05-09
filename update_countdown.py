from datetime import datetime, timedelta

today = datetime.today().date()
target = datetime(today.year, 5, 29).date()
if today > target:
    target = datetime(today.year + 1, 5, 29).date()
days_left = (target - today).days

# Update README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace(
    "{{COUNTDOWN}}", str(days_left)
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
