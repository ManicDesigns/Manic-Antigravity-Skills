import os
import sys
import argparse
import shutil
from pathlib import Path

def get_valid_skills(source_dir):
    """
    Scans source_dir for directories containing a SKILL.md file.
    """
    skills = []
    source = Path(source_dir)
    if not source.exists():
        print(f"Error: Source directory {source} does not exist.")
        return []

    for item in source.iterdir():
        if item.is_dir():
            skill_md = item / "SKILL.md"
            if skill_md.exists():
                skills.append(item.name)
    return skills

def deploy_skills(target_dir, specific_skills=None, use_symlinks=True):
    """
    Deploys skills to target_dir/.agent/skills/
    """
    source_root = Path(__file__).parent.absolute()
    target_root = Path(target_dir) / ".agent" / "skills"
    
    if not target_root.exists():
        print(f"Creating target directory: {target_root}")
        target_root.mkdir(parents=True, exist_ok=True)

    available_skills = get_valid_skills(source_root)
    
    if not available_skills:
        print("No valid skills found in central repository.")
        return

    skills_to_deploy = specific_skills if specific_skills else available_skills

    print(f"Deploying {len(skills_to_deploy)} skills to {target_root}...")

    for skill_name in skills_to_deploy:
        if skill_name not in available_skills:
            print(f"Warning: Skill '{skill_name}' not found locally. Skipping.")
            continue

        src_skill_path = source_root / skill_name
        dest_skill_path = target_root / skill_name

        # Clean existing
        if dest_skill_path.exists():
            if dest_skill_path.is_symlink() or dest_skill_path.is_file():
                dest_skill_path.unlink()
            else:
                shutil.rmtree(dest_skill_path)
            print(f"  - Removed existing '{skill_name}' in target.")

        try:
            if use_symlinks:
                # Windows requires Admin for symlinks usually, but Developer Mode allows it.
                # Fallback to copy if fails?
                try:
                    os.symlink(src_skill_path, dest_skill_path, target_is_directory=True)
                    print(f"  + Linked '{skill_name}'")
                except OSError as e:
                    print(f"  ! Symlink failed (needs Admin/DevMode). Falling back to copy. Error: {e}")
                    shutil.copytree(src_skill_path, dest_skill_path)
                    print(f"  + Copied '{skill_name}'")
            else:
                shutil.copytree(src_skill_path, dest_skill_path)
                print(f"  + Copied '{skill_name}'")
        except Exception as e:
            print(f"  X Failed to deploy '{skill_name}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Deploy Antigravity Skills to a project.")
    parser.add_argument("target", help="Target project root path")
    parser.add_argument("--skills", nargs="+", help="Specific skills to deploy (default: all)")
    parser.add_argument("--copy", action="store_true", help="Copy files instead of symlinking")
    
    args = parser.parse_args()
    
    deploy_skills(args.target, args.skills, use_symlinks=not args.copy)

if __name__ == "__main__":
    main()
