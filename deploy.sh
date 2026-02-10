#!/bin/bash

# 生成実行
python3 generate.py

# Git操作
git add .
git commit -m "Update dashboard: $(date)"
git push origin main

echo "Deployed to GitHub!"
