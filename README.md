# 🎓 AI & Computer Engineering Tuition Dashboard (Thailand)

A data-driven dashboard project that collects tuition fee data from **MyTCAS** and presents insightful visualizations for students interested in **Computer Engineering**, **Artificial Intelligence**, and other related fields.

This dashboard is designed specifically for **high school students planning to attend university next year** — helping them make informed decisions based on tuition fees and program offerings across top Thai universities.

---

## 📌 Objectives

- 🔍 **Collect data** from MyTCAS website on tuition fees for relevant programs (AI / CE / Robotics).
- 📊 **Analyze and visualize** tuition costs across universities and programs.
- 🎯 **Build an interactive dashboard** (with Streamlit) aimed at students seeking higher education guidance.

---

## 🗂️ Project Structure

```bash
.
├── data/
│   └── engineering_ai_programs_full.xlsx   # Collected tuition fee data
├── ai_programs_dashboard.py                # Streamlit dashboard source code
├── collect_tcas_data.py                    # (To be implemented) Web scraper for MyTCAS
├── requirements.txt                        # Python dependencies
└── README.md                               # Project overview
```

---

## 🧪 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-tuition-dashboard.git
cd ai-tuition-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit dashboard

```bash
streamlit run ai_programs_dashboard.py
```

---

## 🛠️ Features

- ✅ **Filter by university**
- ✅ **Compare tuition by program and school**
- ✅ **Interactive charts** (Bar, Pie, Line)
- ✅ **Executive summary**: number of programs, average fees
- ✅ **Tailored for high school students** (easy to read, interactive)

---

## 💾 Data Collection

We aim to scrape and clean tuition fee data from the official **MyTCAS** portal:

```python
# (collect_tcas_data.py - under development)
# The script will target programs such as:
# - วิศวกรรมคอมพิวเตอร์ (Computer Engineering)
# - วิศวกรรมปัญญาประดิษฐ์ (AI Engineering)
# - วิศวกรรมหุ่นยนต์ (Robotics and Automation)
```

---

## 📈 Executive Summary Dashboard Preview

![Dashboard Preview](./preview.png)

---

## 🔁 Git Workflow: Commit Early, Commit Often

This repository follows the **commit early, commit often** philosophy. Each update, whether small or large, is committed to ensure full transparency, collaboration, and version traceability.

---

## 👩‍🎓 Target Audience

This dashboard is created with **Grade 12 students** in mind — those preparing for university admission in Thailand. The insights will help them:

- Compare tuition fees across top universities
- Understand the financial impact of choosing certain programs
- Filter information based on their interests in AI and computer-related fields

---

## 📋 License

This project is open source and free to use for academic or non-commercial purposes.

---

## 🙏 Acknowledgements

- ข้อมูลจากเว็บไซต์ [MyTCAS](https://www.mytcas.com/)
- ข้อมูลเพิ่มเติมจากมหาวิทยาลัยต่างๆ และเว็บไซต์ประกาศหลักสูตร
