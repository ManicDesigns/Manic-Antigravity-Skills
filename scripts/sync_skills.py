import os
import subprocess
import shutil
import argparse
from pathlib import Path

# Configuration
SKILLS_ROOT = Path(__file__).parent.parent.absolute()
EXTERNAL_ROOT = SKILLS_ROOT / "external"
REPOS = {
    "anthropics-skills": EXTERNAL_ROOT / "anthropics-skills",
    "obra-superpowers": EXTERNAL_ROOT / "obra-superpowers"
}

# Mapping of external skills to local names (Source Path relative to Repo Root -> Local Name)
# If mapping is not here, it won't be auto-synced unless we add a generic rule.
# For now, we only sync what we've explicitly ported or want to watch.
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

def sync_repo(repo_name, repo_path):
    print(f"--- Checking {repo_name} ---")
    if not repo_path.exists():
        print(f"Repo not found at {repo_path}")
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
        src = repo_path / src_rel
        dest = SKILLS_ROOT / dest_rel
        
        if not src.exists():
            print(f"Warning: Source {src} does not exist.")
            continue
            
        print(f"Updating {dest.name}...")
        
        # If directory, copy recursively
        if src.is_dir():
            if dest.exists():
                # We carefully overwrite, maybe preserving SKILL.md header if we wanted to be fancy
                # But for now, we'll just copy over. 
                # NOTE: This might overwrite our custom SKILL.md names if source SKILL.md changed.
                # In a real "Manic" repo, we might want a merge strategy.
                # For this v1, strict overwrite is safer for "getting latest features"
                # EXCEPT we renamed the skills in the SKILL.md frontmatter.
                
                # Strategy: Copy everything, then fix SKILL.md name if needed
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
                shutil.copytree(src, dest)
        else:
            # Single file sync (unlikely for current mappings but good to support)
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
    for name, path in REPOS.items():
        if sync_repo(name, path):
            update_local_skills(name, path)
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
