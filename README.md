# ResumeRoleMatcherAPI
The Resume Role Matcher API uses Natural Language Processing (via spaCy) to extract skills from resumes and match them against predefined role profiles. It returns the most relevant roles based on skill overlap and category-weighted scoring.

# Resume Role Matcher API

This project provides a resume analysis API that extracts and evaluates role-based skills from resumes. It uses natural language processing (NLP) to lemmatize and match resume content with predefined job role profiles, assigning relevance scores based on skill overlap and weighted categories.

## Features

- Extracts and preprocesses resume text using spaCy
- Matches resume content against role-specific skill categories
- Scores skill matches with category-weighted normalization (out of 100)
- Returns a structured JSON response with role-wise matches and skill breakdowns
- Exposes the functionality as a FastAPI endpoint

## Project Structure
JobRecommendation/
│
│  main.py # FastAPI app with /match_roles endpoint
│
├── utils/
│ ├── parser.py # Utility to extract text from PDF resumes
│ ├── skills_extractor.py # Core logic for skill extraction and scoring
│ └── role_profile.py # Dictionary of job roles and associated skills
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation


