#!/usr/bin/env python3
"""Refresh cases, sitemap and AI knowledge in order; no publishing or dependencies."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
for script in ('build-cases.py','build-ai-search.py','check-ai-search.py'):
    subprocess.run([sys.executable,str(root/'scripts'/script)],cwd=root,check=True)
