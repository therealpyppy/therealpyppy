from datetime import datetime, timedelta

today = datetime.today().date()
target = datetime(today.year, 5, 29).date()
if today > target:
    target = datetime(today.year + 1, 5, 29).date()
days_left = (target - today).days

# Update README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

afterContent = "} days until my summer break! 🎉🎊\n</div>\n\n<div align=\"center\">\n  <img src=\"https://github-readme-stats.vercel.app/api?username=therealpyppy&theme=prussian&show_icons=true&hide_border=true&count_private=true\"/>\n</div>\n\n<div align=\"center\">\n  <img src=\"https://streak-stats.demolab.com?user=therealpyppy&theme=prussian&hide_border=true\"/>\n</div>\n\n<div align=\"center\">\n  <img src=\"https://github-readme-stats.vercel.app/api/top-langs/?username=therealpyppy&theme=prussian&show_icons=true&hide_border=true&layout=compact\"/>\n</div>"

new_content = content.replace(
    content.split("{")[1]+afterContent, str(days_left)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
