# 🚀 CodeSage – Smarter Pull Request Reviews with AI

> **CodeSage** speeds up code reviews with deep insights, duplicate detection, dependency checks, PR title validation, and AI-powered suggestions.

---

## 💡 Features

- 🔍 **Dependency & Duplicate Code Detection**  
  Understand hidden dependencies and detect duplicate logic across your codebase.

- ✨ **AI-Powered Code Suggestions**  
  Context-aware improvements and code enhancements — ready to commit.

- 🧠 **Pull Request Title Validation**  
  Enforces naming conventions and review rules automatically.

- 📝 **PR Summaries**  
  Converts complex diffs into clear summaries to explain what changed and why.

- 🧩 **Inline Code Insights**  
  File-by-file and line-by-line suggestions, powered by AI, to improve clarity, performance, and quality.

- 🌐 **Supports All Languages**  
  PullSense is language-agnostic — works with Python, JavaScript, Go, Rust, and more.

- 🔐 **Data Privacy**  
  LLM queries are ephemeral. Your code is not stored or reused. [Privacy Policy](#)

---

## 📸 Screenshots

### 🔍 PR Summary
![PR Summary](images/summary.png)

### 🧠 PR Title Validation
![Title Check](images/title-check.png)

### 💬 Inline Suggestions
![Inline Feedback](images/inline.png)

---

## 🛠️ How It Works

1. Install CodeSage on your GitHub repositories.
2. When a **Pull Request** is opened:
   - Analyzes code diffs.
   - Detects **duplicates** and **dependencies**.
   - Validates PR title formatting.
   - Posts **summaries** and **inline AI feedback** as comments.

---

## 🔧 Installation

👉 [**Install PullSense from GitHub Marketplace**](https://github.com/marketplace)  
Or go directly to install:  
`https://github.com/apps/pullsense/installations/new`

---

## ⚙️ Example PR Title Rule

```yaml
# Optional: .pullsense.yml
title:
  pattern: "^(feat|fix|refactor|docs): .+$"
  error: "Title must follow Conventional Commit style (e.g., feat: add search bar)."
