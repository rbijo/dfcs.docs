# Home / Project Overview

Welcome to the official visual technical documentation portal for **Domain FAQ Support Chatbot Using Fine Tuned Small Language Models**.

---

## 🛡️ Project Status & Technology Badges

### Project
![Status](https://img.shields.io/badge/Status-In%20Development-blue?style=for-the-badge)
![Domain](https://img.shields.io/badge/Domain-FAQ%20Support-0052CC?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### AI & Machine Learning
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![PEFT](https://img.shields.io/badge/Fine--Tuning-PEFT%20%2F%20LoRA%20%2F%20QLoRA-8A2BE2?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-Small%20Language%20Models-orange?style=for-the-badge)

### Application & Infrastructure
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Web UI](https://img.shields.io/badge/Frontend-Responsive%20Web%20UI-20B2AA?style=for-the-badge)
![GitHub Pages](https://img.shields.io/badge/Docs-GitHub%20Pages-222222?style=for-the-badge&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

## 📌 Problem Statement

Customer support and internal domain guidance often rely on repetitive manual responses or rigid keyword-based FAQ systems that fail to understand natural language variations.

While Large Language Models (LLMs) offer strong conversational reasoning, deploying massive models for narrow domain FAQs is computationally expensive, latency-heavy, and poses privacy concerns.

**The Challenge:**
1. High operational costs associated with proprietary LLM APIs.
2. Domain domain-specific terminology misalignment in generic off-the-shelf models.
3. Need for predictable, highly accurate domain answers without hallucinating unsupported policies.

---

## 💡 High-Level Solution

This project builds a specialized, efficient **Domain FAQ Support Chatbot** leveraging **Fine-Tuned Small Language Models (SLMs)**.

By fine-tuning parameter-efficient open SLMs (such as LLaMA/Qwen/Phi variants via PEFT/LoRA/QLoRA) on curated domain FAQ paired datasets:
- **Low Latency & High Speed:** Runs efficiently on modest hardware or edge instances.
- **Precision Responses:** Tailored to strict domain knowledge bases.
- **Cost Effective:** Low inference costs compared to general-purpose cloud LLMs.

---

## 🏗️ System Architecture

The project decouples offline training from real-time online inference:

```mermaid
flowchart TD
    subgraph Offline ["Offline Fine-Tuning Pipeline"]
        A["Domain FAQ Knowledge Base"] --> B["Data Cleaning & Curation"]
        B --> C["Dataset Formatting (Instruction-Answer Pairs)"]
        C --> D["Dataset Validation"]
        D --> E["Base SLM Model Selection"]
        E --> F["PEFT / LoRA Fine-Tuning"]
        F --> G["Evaluation & Benchmarking"]
        G --> H["Optimized Fine-Tuned Weights"]
    end

    subgraph Online ["Online Inference & User System"]
        User(["End User / Customer"]) <--> UI["Web Interface"]
        UI <--> API["Backend API (FastAPI)"]
        API <--> Engine["Inference Engine (Fine-Tuned SLM)"]
        Engine <--> H
    end
```

---

## 🔬 Core Focus Areas

- **Dataset Construction:** Scraped, cleaned, and formatted domain-specific FAQ pairs with strict validation.
- **Fine-Tuning Methodology:** Quantized parameter-efficient fine-tuning (QLoRA) maximizing domain accuracy while keeping resource overhead minimal.
- **Evaluation Framework:** Multi-metric evaluation checking exact factual recall, response relevance, and hallucination bounds.
- **Deployment & Web Integration:** Modular FastAPI backend serving a lightweight, modern web frontend.

---

## 👥 Team Overview

The project is developed by a dedicated 3-member engineering team:

| Team Member | Primary Focus Areas |
| :--- | :--- |
| **Member 1** | Data Pipeline, Data Cleaning & FAQ Formatting |
| **Member 2** | SLM Selection, PEFT/LoRA Fine-Tuning & Model Evaluation |
| **Member 3** | Backend API, System Architecture & Web UI Integration |

---

## 🚀 Navigation Quick Links

- Explore ongoing technical documentation in the **[Development Workspace](development/index.md)**.
- Read website contributor guides in **[For the Devs](for-the-devs/getting-started.md)**.
- View website updates in the **[Documentation Changelog](for-the-devs/changelog.md)**.
- Inspect the source code on **[GitHub Repository](https://github.com/rbijo/dfcs.docs)**.
