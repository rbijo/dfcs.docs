# Getting Started

Welcome to the documentation contributor guide. This guide gets you up and running to write and maintain the documentation site.

## ⚡ Quick Steps

1. **Clone Repository:**
   ```bash
   git clone https://github.com/rbijo/dfcs.docs.git
   cd dfcs.docs
   ```

2. **Install Zensical:**
   ```bash
   pip install zensical
   ```

3. **Launch Local Server:**
   ```bash
   zensical serve
   ```
   Open `http://127.0.0.1:8000` in your browser.

4. **Generate External References:**
   Before committing, run:
   ```bash
   python scripts/generate_references.py
   ```
