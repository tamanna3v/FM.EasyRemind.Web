#!/usr/bin/env python3
"""Build index.html (GitHub Pages) from src/artifact.html (the single source, body-only artifact format).

Usage: python3 scripts/build.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
body = (root / "src" / "artifact.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="EasyRemind by EasyDo: every subscription on one page, one honest total, and a reminder before each charge. Bangla and English.">
<meta name="theme-color" content="#0f7b74">
<link rel="manifest" href="manifest.json">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
(root / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
print("built index.html from src/artifact.html")
