# AI Resume Analyzer

A Python + Streamlit project that analyzes a resume against ATS-style criteria and an optional job description.

## Features

- PDF, DOCX and TXT resume upload
- PDF text extraction with PyMuPDF
- DOCX extraction with python-docx
- Resume section detection
- Skills detection
- ATS-style score
- Job-description keyword overlap
- TF-IDF/cosine job similarity
- Missing skill detection
- Strengths and improvement suggestions
- Optional OpenAI-powered feedback
- JSON export
- Streamlit Community Cloud deployment

## 1. Create environment

Python 3.12 is a good deployment target for Streamlit Community Cloud.

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run

```bash
streamlit run app.py
```

Open the local URL shown by Streamlit, normally:

```text
http://localhost:8501
```

## 3. Optional OpenAI setup

Create:

```text
.streamlit/secrets.toml
```

with:

```toml
OPENAI_API_KEY = "your-key"
```

Do not commit that file.

The app will still work without the key; only the AI-feedback tab needs it.

## 4. GitHub

```bash
git init
git add .
git commit -m "Initial AI resume analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
git push -u origin main
```

## 5. Streamlit Community Cloud

1. Sign in to Streamlit Community Cloud.
2. Create app.
3. Select your GitHub repository.
4. Branch: `main`
5. Main file: `app.py`
6. In Advanced settings, choose Python 3.12.
7. In Secrets, paste:

```toml
OPENAI_API_KEY = "your-key"
```

8. Deploy.

Your app gets a `streamlit.app` URL.

## Project flow

```text
Resume PDF/DOCX/TXT
        |
        v
Text Extraction
        |
        v
Text Cleaning
        |
        +--> Section Detection
        |
        +--> Skill Detection
        |
        +--> ATS Checks
        |
        +--> Job Description
                |
                +--> Keyword Coverage
                |
                +--> TF-IDF Similarity
        |
        v
Overall Score
        |
        +--> Missing Skills
        +--> Issues
        +--> Strengths
        +--> Optional LLM Feedback
```

## How the score works

Without a job description:

```text
Overall = ATS score
```

With a job description:

```text
Job Match = 60% keyword coverage + 40% TF-IDF similarity

Overall = 55% ATS + 45% Job Match
```

This is an educational ATS-style score, not a prediction of a real company's hiring decision.

## Important limitation

Scanned/image-only PDFs may have no machine-readable text. Add OCR later if you need scanned resumes.

## Good extensions for a final-year project

- OCR for scanned resumes
- Named Entity Recognition for education/company names
- Better skill taxonomy from a JSON database
- Resume section classification
- Sentence embeddings
- Resume rewrite suggestions
- Job-to-resume ranking for multiple jobs
- Authentication
- Database/history
- Admin dashboard
- Unit tests and CI/CD

# AI-resume-analyzer
>>>>>>> 6a427ff04b38dcabd0a44d27e1e227d46d6d5380
