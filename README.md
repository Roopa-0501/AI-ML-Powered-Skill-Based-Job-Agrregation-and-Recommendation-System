# 🚀 SkillWeave – AI-Powered Job Aggregation & Recommendation System

## 📌 Project Overview
SkillWeave is an AI-driven job recommendation platform that analyzes a job seeker’s resume and intelligently recommends the most relevant job opportunities across multiple job portals. The system uses Natural Language Processing (NLP) and Machine Learning (ML) to understand resume content, predict suitable job roles, and rank jobs based on semantic skill relevance.

---

## ❓ Problem Statement
Job seekers often spend excessive time manually searching across different job portals. Traditional job platforms rely on keyword-based filtering, which fails to capture true skill relevance and results in inefficient and inaccurate job matching.

---

## 💡 Proposed Solution
SkillWeave automates the job discovery process by:
- Parsing resumes to extract skills and personal details using NLP
- Predicting professional category and suitable job role using ML models
- Aggregating jobs from multiple platforms via APIs
- Matching resumes with job descriptions using TF-IDF and cosine similarity
- Ranking jobs based on relevance with explainable match scores

---

## 🛠 Tech Stack
**Frontend**
- HTML5
- CSS3
- React (planned)

**Backend**
- Python
- Flask (REST API)

**AI / ML**
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- NLP Parsing

**Job Aggregation APIs**
- Adzuna
- The Muse
- USAJobs
- Jooble

**Data Processing**
- JSON
- PyPDF2

**Tools**
- GitHub
- VS Code

---

## 🏗 System Architecture
1. User uploads resume (PDF/TXT)
2. Resume text is extracted and cleaned
3. Skills and details are identified
4. ML model predicts job category and role
5. Jobs are fetched from multiple APIs
6. TF-IDF vectorization is applied
7. Cosine similarity computes relevance
8. Ranked job recommendations are displayed

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|------|----------|-------------|
| GET  | `/`      | Home page (resume upload) |
| POST | `/pred`  | Resume processing & job recommendation |

---

## 📊 Sample Output
- Predicted job category and role
- Extracted resume details (skills, education, contact info)
- Ranked job recommendations with match percentage
- Redirect link to original employer platform

---

## 🔮 Future Improvements
- Skill gap analysis with learning recommendations
- User authentication and job history storage
- React-based interactive UI
- Advanced filters (location, experience, salary)
- AI-based resume improvement suggestions

---

## ▶️ How to Run
```bash
git clone https://github.com/your-username/SkillWeave.git
cd SkillWeave
pip install -r requirements.txt
python app.py
