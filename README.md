# Resume Role Matcher API

This project provides a resume analysis API that extracts and evaluates role-based skills from resumes. It uses natural language processing (NLP) to lemmatize and match resume content with predefined job role profiles, assigning relevance scores based on skill overlap and weighted categories.

## Features

- Extracts and preprocesses resume text using spaCy
- Matches resume content against role-specific skill categories
- Scores skill matches with category-weighted normalization (out of 100)
- Returns a structured JSON response with role-wise matches and skill breakdowns
- Exposes the functionality as a FastAPI endpoint


