# 🤖 AI Recruiter Agency

## Overview
The **AI Recruiter Agency** is an intelligent recruitment automation system that streamlines candidate screening, resume parsing, and job-role matching using AI-driven agents.  
Built with **LangChain**, **ChromaDB**, and **Streamlit**, it leverages natural language processing and semantic search to extract candidate details, evaluate skill-job alignment, and recommend top matches for open roles.  

---

## Key Features
- 🧠 **AI Resume Parsing:** Extracts candidate details, experience, and skills from uploaded resumes using NLP.  
- ⚙️ **Skill-Based Job Matching:** Uses vector embeddings to match candidate skills with job descriptions for accurate recommendations.  
- 🤝 **Recommender Agent:** Suggests the most relevant roles or candidates based on semantic similarity scores.  
- 📊 **Profile Enhancement:** Fills missing details and enriches profiles using contextual AI reasoning.  
- 📄 **Streamlit UI:** Provides an intuitive web interface for resume uploads and recruiter insights.  

---

## Architecture Overview
The system follows a **modular agent-based architecture**, ensuring scalability and flexibility.  
Each agent is responsible for a specific stage of the pipeline — extraction, analysis, matching, or recommendation.

### Core Modules
| Module | Description |
|---------|-------------|
| **agents/** | Contains specialized AI agents for analysis, extraction, matching, and recommendation. |
| **data/** | Handles job dataset logic and connections to the job database. |
| **db/** | SQLite-based backend with schema and seed data for job listings. |
| **utils/** | Includes logging and exception management utilities. |
| **resumes/** | Contains sample resumes for demo and testing. |

### Workflow
Candidate Resume Upload
→ Extractor Agent parses and cleans text
→ Analyzer Agent extracts and normalizes skills
→ Matcher Agent compares skills with job descriptions
→ Recommender Agent ranks best-fit roles
→ Streamlit displays interactive results


---

## Tech Stack
`Python` • `Streamlit` • `LangChain` • `ChromaDB` • `Pandas` • `OpenAI API`

---

## Setup & Run
Follow these steps to set up and launch the application locally:

```bash
# 1. Clone the repository
git clone https://github.com/Akashj-data/akash-j-portfolio.git
cd AI-Recruiter-Agency

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py
Once started, open the URL shown in your terminal (usually http://localhost:8501
) to interact with the recruiter interface.

Example Output

When a resume is uploaded:

The system extracts and displays structured data: name, experience, education, and skills.

It performs a similarity-based match against available job roles.

Displays ranked recommendations such as:

Top Match: Data Analyst – 89% similarity  
Next Match: Machine Learning Engineer – 82% similarity  


Provides reasoning context explaining why each role fits.

Future Enhancements

🔗 API Integration: Connect with LinkedIn and Indeed APIs for real-time job updates.

🗣️ Conversational Interface: Enable AI-driven interviews and candidate Q&A.

📈 Recruiter Dashboard: Add analytics on candidate pool, job matches, and hiring trends.

🔒 Data Privacy: Implement anonymized resume processing for secure data handling.

Outcome

The AI Recruiter Agency demonstrates the power of AI in transforming the recruitment lifecycle — automating resume analysis, skill extraction, and intelligent job matching.
It highlights strong proficiency in LangChain, ChromaDB, and Streamlit, showcasing practical AI deployment for real-world business workflows.
