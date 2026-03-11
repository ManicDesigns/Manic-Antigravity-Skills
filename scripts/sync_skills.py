import os
import subprocess
import shutil
import argparse
from pathlib import Path

# Configuration
SKILLS_ROOT = Path(__file__).parent.parent.absolute()
EXTERNAL_ROOT = SKILLS_ROOT / "external"
REPOS = {
    "anthropics-skills": {"path": EXTERNAL_ROOT / "anthropics-skills", "url": None},
    "obra-superpowers": {"path": EXTERNAL_ROOT / "obra-superpowers", "url": None},
    "awesome-agent-skills": {"path": EXTERNAL_ROOT / "awesome-agent-skills", "url": "https://github.com/VoltAgent/awesome-agent-skills.git"},
    "expo-skills": {"path": EXTERNAL_ROOT / "expo-skills", "url": "https://github.com/expo/skills.git"},
    "agent-scan": {"path": EXTERNAL_ROOT / "agent-scan", "url": "https://github.com/snyk/agent-scan.git"}
}

# Mapping of external skills to local names (Source Path relative to Repo Root -> Local Name)
# If mapping is not here, it won't be auto-synced unless we add a generic rule.
SYNC_MAP = {
    "anthropics-skills": {
        "skills/xlsx": "managing-excel-files",
        "skills/pdf": "managing-pdf-files",
        "skills/docx": "managing-word-docs",
        "skills/mcp-builder/reference": "building-mcp-servers/reference"
    },
    "obra-superpowers": {
        "skills/brainstorming": "brainstorming",
        "skills/writing-plans": "planning"
    },
    "awesome-agent-skills": {
        "": "awesome-agent-skills"
    },
    "expo-skills": {
        "plugins/expo-app-design": "expo-app-design",
        "plugins/expo-deployment": "expo-deployment",
        "plugins/upgrading-expo": "upgrading-expo"
    },
    "agent-scan": {
        "": "agent-scan"
    }
}

def run_git_cmd(cwd, args):
    try:
        result = subprocess.run(
            ["git"] + args, 
            cwd=cwd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed in {cwd}: git {' '.join(args)}\nError: {e.stderr}")
        return None

def sync_repo(repo_name, repo_info):
    repo_path = repo_info["path"]
    repo_url = repo_info["url"]
    print(f"--- Checking {repo_name} ---")
    if not repo_path.exists():
        if repo_url:
            print(f"Cloning {repo_url} into {repo_path}...")
            EXTERNAL_ROOT.mkdir(parents=True, exist_ok=True)
            run_git_cmd(EXTERNAL_ROOT, ["clone", repo_url, repo_path.name])
            return True
        else:
            print(f"Repo not found at {repo_path} and no URL provided.")
            return False
    
    # 1. Pull changes
    print("Pulling latest changes...")
    output = run_git_cmd(repo_path, ["pull"])
    if output == "Already up to date.":
        print("No changes found.")
        return False
    
    print(f"Updates received:\n{output}")
    return True

def update_local_skills(repo_name, repo_path):
    print(f"Syncing skills from {repo_name}...")
    mappings = SYNC_MAP.get(repo_name, {})
    
    for src_rel, dest_rel in mappings.items():
        src = repo_path / src_rel if src_rel else repo_path
        dest = SKILLS_ROOT / dest_rel
        
        if not src.exists():
            print(f"Warning: Source {src} does not exist.")
            continue
            
        print(f"Updating {dest.name}...")
        
        # If directory, copy recursively
        if src.is_dir():
            if dest.exists():
                for item in src.iterdir():
                    if item.name == ".git": continue
                    s = item
                    d = dest / item.name
                    if s.is_dir():
                        if d.exists(): shutil.rmtree(d)
                        shutil.copytree(s, d)
                    else:
                        shutil.copy2(s, d)
            else:
                # Copy everything but exclude .git
                shutil.copytree(src, dest, ignore=shutil.ignore_patterns('.git', '.github'))
        else:
            # Single file sync
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            
def fix_skill_names():
    # Enforce our naming conventions in SKILL.md after sync
    updates = [
        ("managing-excel-files/SKILL.md", "xlsx", "managing-excel-files"),
        ("managing-pdf-files/SKILL.md", "pdf", "managing-pdf-files"),
        ("managing-word-docs/SKILL.md", "docx", "managing-word-docs"),
        ("planning/SKILL.md", "writing-plans", "planning")
    ]
    
    for rel_path, old, new in updates:
        path = SKILLS_ROOT / rel_path
        if path.exists():
            content = path.read_text(encoding="utf-8")
            if f"name: {old}" in content:
                print(f"Restoring name for {new}...")
                path.write_text(content.replace(f"name: {old}", f"name: {new}"), encoding="utf-8")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--push", action="store_true", help="Push changes to Manic Antigravity Skills repo")
    args = parser.parse_args()
    
    changes_detected = False
    
    # 1. Update Externals
    for name, info in REPOS.items():
        if sync_repo(name, info):
            update_local_skills(name, info["path"])
            changes_detected = True
            
    # 2. Fix Metadata
    if changes_detected:
        fix_skill_names()
        
    # 3. Commit to Manic Repo
    if changes_detected:
        print("--- Committing to Manic Skills Repo ---")
        run_git_cmd(SKILLS_ROOT, ["add", "."])
        run_git_cmd(SKILLS_ROOT, ["commit", "-m", "Auto-sync: Updated external skills"])
        
        if args.push:
            print("Pushing to remote...")
            res = run_git_cmd(SKILLS_ROOT, ["push"])
            if res: print(res)
    else:
        print("No updates found.")

if __name__ == "__main__":
    main()
