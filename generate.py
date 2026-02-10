import os
import glob
import markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# 設定
PROJECTS_DIR = "projects"
TEMPLATE_DIR = "templates"
OUTPUT_FILE = "index.html"

# ステータスの定義
STATUS_COLORS = {
    "planning": "bg-yellow-100 text-yellow-800",
    "poc": "bg-green-100 text-green-800",
    "done": "bg-blue-100 text-blue-800",
    "withdrawn": "bg-gray-100 text-gray-800"
}

STATUS_LABELS = {
    "planning": "🟡 計画中",
    "poc": "🟢 検証中",
    "done": "🔵 完了",
    "withdrawn": "⚪️ 撤退"
}

def load_projects():
    projects = []
    # Markdownファイルを取得
    files = glob.glob(os.path.join(PROJECTS_DIR, "*.md"))
    
    for file_path in files:
        post = frontmatter.load(file_path)
        content_html = markdown.markdown(post.content)
        
        project = {
            "file_name": os.path.basename(file_path),
            "title": post.get("title", "No Title"),
            "status": post.get("status", "planning"),
            "status_class": STATUS_COLORS.get(post.get("status", "planning"), "bg-gray-100"),
            "status_label": STATUS_LABELS.get(post.get("status", "planning"), "Unknown"),
            "progress": post.get("progress", 0),
            "updated_at": post.get("updated_at", ""),
            "summary": post.get("summary", ""),
            "content": content_html
        }
        projects.append(project)
        
    # 更新日順にソート
    return sorted(projects, key=lambda x: x["updated_at"], reverse=True)

def generate_html(projects):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("dashboard.html")
    
    # ステータス集計
    summary = {
        "total": len(projects),
        "planning": sum(1 for p in projects if p["status"] == "planning"),
        "poc": sum(1 for p in projects if p["status"] == "poc"),
        "done": sum(1 for p in projects if p["status"] == "done"),
    }
    
    html_output = template.render(
        projects=projects, 
        summary=summary,
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_output)
    
    print(f"Successfully generated {OUTPUT_FILE}")

def main():
    if not os.path.exists(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR)
        print(f"Created {PROJECTS_DIR}")
        
    if not os.path.exists(TEMPLATE_DIR):
        os.makedirs(TEMPLATE_DIR)
        print(f"Created {TEMPLATE_DIR}")
        
    projects = load_projects()
    generate_html(projects)

if __name__ == "__main__":
    main()
