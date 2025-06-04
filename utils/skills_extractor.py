import spacy
from collections import Counter
from utils.role_profile import ROLE_SKILLS

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

# You can customize category weights here
CATEGORY_WEIGHTS = {
    "clinical_skills": 0.35,
    "technical_skills": 0.35,
    "soft_skills": 0.1,
    "certifications": 0.2
}

def preprocess_text(text: str) -> list[str]:
    """Lemmatize and clean text into token list."""
    doc = nlp(text.lower())
    return [
        token.lemma_.strip().lower()
        for token in doc
        if not token.is_stop and not token.is_punct and token.lemma_.strip()
    ]

def skill_token_overlap(skill_tokens: set[str], resume_tokens: set[str], threshold: float = 0.3) -> bool:
    """Return True if overlap ratio >= threshold."""
    return bool(skill_tokens) and len(skill_tokens & resume_tokens) / len(skill_tokens) >= threshold

def extract_skills_from_text(resume_text: str, debug: bool = False) -> dict:
    """
    Extract matched skills from resume and return role-wise breakdown with normalized weighted scores.
    """
    # Preprocess resume
    token_list = preprocess_text(resume_text)
    token_counter = Counter(token_list)
    token_set = set(token_list)

    matched_roles = {}

    for role, skill_categories in ROLE_SKILLS.items():
        weighted_score = 0
        role_matches = {}

        for category, skills in skill_categories.items():
            matched_skills = []

            for skill in skills:
                skill_tokens = set(preprocess_text(skill))
                if skill_token_overlap(skill_tokens, token_set):
                    count = sum(token_counter[token] for token in skill_tokens)
                    if count > 0:
                        matched_skills.append((skill, count))

                        if debug:
                            print(f"[DEBUG] Role: {role}")
                            print(f"[DEBUG] Category: {category}")
                            print(f"[DEBUG] Skill: {skill}")
                            print(f"[DEBUG] Overlap: {skill_tokens & token_set}")
                            print(f"[DEBUG] Count: {count}")

            if matched_skills:
                role_matches[category] = matched_skills

            # Calculate normalized category score
            match_ratio = len(matched_skills) / len(skills) if skills else 0
            category_weight = CATEGORY_WEIGHTS.get(category, 0)
            weighted_score += match_ratio * category_weight * 100  # Scale to 100

        if role_matches:
            matched_roles[role] = {
                "score": round(weighted_score, 2),
                "skills": role_matches
            }

    if debug:
        print(f"[DEBUG] Final Token Set: {token_set}")

    return matched_roles
