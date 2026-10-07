# Resume Screening App

A lightweight resume screening application that compares a candidate resume and a job description, extracts relevant information using OpenAI, and evaluates whether the candidate is a fit for the role.

## Overview

This project contains:

- A FastAPI backend that accepts PDF uploads and processes screening logic
- A Streamlit frontend for uploading a resume and job description
- AI-powered resume and JD parsing using prompt-based OpenAI extraction
- Candidate evaluation that checks required skills and experience fit

## How it works

1. The user uploads a PDF resume and a PDF job description in the Streamlit UI.
2. The backend reads the PDFs and extracts raw text.
3. The app uses OpenAI GPT-4 prompts to extract structured data from both documents.
4. The candidate profile is compared against the job requirements.
5. The API returns a JSON payload with:
   - candidate status (`Selected` or `Rejected`)
   - reason/explanation
   - skill match percentage
   - matched and missing skills
   - strengths and gaps

## Project structure

```text
resume-screening/
├── app/
│   ├── agents/
│   │   ├── candidate_evaluation.py
│   │   ├── jd_extractor.py
│   │   └── resume_extractor.py
│   ├── ui/
│   │   └── app.py
│   ├── main.py
│   ├── parsepdf.py
│   ├── prompts.py
│   └── __init__.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

- Python 3.10+
- A valid OpenAI API key
- Access to the internet for the OpenAI API

## Setup

From the project root, create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Run the app

Start the backend API:

```bash
uvicorn app.main:app --reload
```

In a second terminal, start the Streamlit UI:

```bash
streamlit run app/ui/app.py
```

Then open the local Streamlit URL in your browser and upload both PDFs.

## API endpoint

The backend exposes:

```text
POST /screening/
```

It accepts:

- `resume`: PDF file
- `jd`: PDF file

It returns JSON describing the screening decision.

## Notes

- The app currently relies on OpenAI GPT-4 for text extraction and evaluation.
- PDF parsing is handled with `PyPDF2`.
- The UI is built with Streamlit, while the backend is built with FastAPI.
- This project is intended for demonstration and prototype use rather than production-grade hiring automation.

## License

This project is provided as-is for educational and internal use. Add your preferred license if you plan to distribute it.
