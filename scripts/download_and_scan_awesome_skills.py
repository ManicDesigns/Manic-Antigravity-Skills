import os
import re
import shutil
import subprocess
import time
import argparse
from pathlib import Path
from urllib.parse import urlparse

# Configuration
SKILLS_ROOT = Path(__file__).parent.parent.absolute()
AWESOME_README = SKILLS_ROOT / "external" / "awesome-agent-skills" / "README.md"
TEMP_CLONES_DIR = SKILLS_ROOT / "external" / "temp_clones"
APPROVED_SKILLS_DIR = SKILLS_ROOT / "external" / "awesome-imported-skills"
AGENT_SCAN_DIR = SKILLS_ROOT / "external" / "agent-scan"

def run_cmd(args, cwd=None, capture=True):
    try:
        result = subprocess.run(
            args,
            cwd=cwd or SKILLS_ROOT,
            capture_output=capture,
            text=True,
            check=True
        )
        out = result.stdout.strip() if result.stdout else ""
        return result.returncode == 0, out
    except subprocess.CalledProcessError as e:
        err = e.stderr or e.stdout or str(e)
        return False, err

def parse_awesome_readme():
    """Extracts all github links from the awesome-agent-skills README."""
    if not AWESOME_README.exists():
        print(f"Error: Could not find {AWESOME_README}")
        return []
    
    content = AWESOME_README.read_text(encoding="utf-8")
    # Matches: - **[name](url)**
    pattern = re.compile(r'- \*\*\[([^\]]+)\]\((https://github\.com/[^\)]+)\)\*\*')
    matches = pattern.findall(content)
    
    skills = []
    for name, url in matches:
        # Avoid linking to non-skill repos if possible, but the list is curated.
        repo_url = url
        subpath = ""
        
        if "/tree/" in url:
            parts = url.split("/tree/", 1)
            repo_url = parts[0] + ".git"
            branch_and_path = parts[1]
            b_parts = branch_and_path.split("/", 1)
            if len(b_parts) == 2:
                subpath = b_parts[1]
        elif "/blob/" in url:
            parts = url.split("/blob/", 1)
            repo_url = parts[0] + ".git"
            branch_and_path = parts[1]
            b_parts = branch_and_path.split("/", 1)
            if len(b_parts) == 2:
                subpath = b_parts[1]
        else:
            if not repo_url.endswith(".git"):
                repo_url += ".git"
                
        # Parse github org and repo for folder structure
        parsed = urlparse(repo_url)
        path_parts = parsed.path.strip("/").replace(".git", "").split("/")
        if len(path_parts) >= 2:
            org = path_parts[0]
            repo = path_parts[1]
        else:
            continue
            
        skills.append({
            "name": name.replace("/", "_").replace("\\", "_"),
            "url": url,
            "repo_url": repo_url,
            "org": org,
            "repo": repo,
            "subpath": subpath
        })
        
    return skills

def clone_repo(org, repo, repo_url):
    """Clones a repo into the temp directory if it doesn't exist."""
    org_dir = TEMP_CLONES_DIR / org
    org_dir.mkdir(parents=True, exist_ok=True)
    repo_dir = org_dir / repo
    
    if not repo_dir.exists():
        print(f"  Cloning {repo_url} into {repo_dir}...")
        success, _ = run_cmd(["git", "clone", repo_url, str(repo_dir)], capture=False)
        return success, repo_dir
    else:
        return True, repo_dir

def scan_skill(skill_path):
    """Runs snyk-agent-scan against the target directory."""
    print(f"  Scanning {skill_path}...")
    # Using the python module directly since it was installed in editable mode
    success, output = run_cmd(
        ["python", "-m", "src.agent_scan.cli", "scan", str(skill_path)],
        cwd=AGENT_SCAN_DIR,
        capture=True
    )
    if not success:
        # Check if the failure is just "no skills found" or an actual security error
        if "No agent configuration found" in output or "No items found to scan" in output:
            print(f"  Scan Warning: No recognizable configurations found (Safe, but empty).")
            return True, output
        print(f"  SCAN FAILED OR VULNERABILITY FOUND: {output[:200]}...")
        return False, output
    return True, output

def process_skills(max_skills=None):
    skills = parse_awesome_readme()
    print(f"Found {len(skills)} skills in the README.")
    
    if max_skills:
        skills = skills[:max_skills]
        print(f"Limiting to first {max_skills} skills for testing.")
        
    TEMP_CLONES_DIR.mkdir(parents=True, exist_ok=True)
    APPROVED_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    fail_count = 0
    
    for idx, skill in enumerate(skills, 1):
        print(f"\n[{idx}/{len(skills)}] Processing {skill['name']}...")
        print(f"  URL: {skill['repo_url']}")
        
        # 1. Clone
        clone_success, repo_dir = clone_repo(skill['org'], skill['repo'], skill['repo_url'])
        if not clone_success:
            print(f"  Failed to clone {skill['repo_url']}. Skipping.")
            fail_count += 1
            continue
            
        # 2. Locate Skill Path
        skill_target_path = repo_dir / skill['subpath'] if skill['subpath'] else repo_dir
        
        if not skill_target_path.exists():
            print(f"  Skill path {skill_target_path} does not exist in repo. Skipping.")
            fail_count += 1
            continue
            
        # 3. Scan
        dest_dir = APPROVED_SKILLS_DIR / skill['name']
        if dest_dir.exists():
            print(f"  Skill {skill['name']} already exists in approved directory. Skipping scan.")
            success_count += 1
            continue

        scan_success, _ = scan_skill(skill_target_path)
        
        if scan_success:
            # 4. Copy to Approved
            print(f"  Scan passed. Moving to {dest_dir.name}...")
            try:
                # If it's a file (like a single Markdown file), handle it differently
                if skill_target_path.is_file():
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(skill_target_path, dest_dir / skill_target_path.name)
                else:
                    shutil.copytree(skill_target_path, dest_dir, ignore=shutil.ignore_patterns('.git', '.github'))
                success_count += 1
            except Exception as e:
                print(f"  Failed to copy: {e}")
                fail_count += 1
        else:
            fail_count += 1
            
    print(f"\n--- Batch Process Complete ---")
    print(f"Successfully Vetted & Copied: {success_count}")
    print(f"Failed / Vulnerable / Errors: {fail_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, help="Limit the number of skills to process for testing.")
    args = parser.parse_args()
    
    if not os.environ.get("SNYK_TOKEN"):
        print("WARNING: SNYK_TOKEN environment variable is not set. The scanner will likely fail.")
        # We don't exit immediately just in case the scanner can run offline or anonymous,
        # but the implementation plan explicitly warned about it.
        
    process_skills(args.limit)
