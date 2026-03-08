from app.services.extractor import extract_skills


def build_explanation(
    matched_skills: list[str],
    missing_skills: list[str],
    score: float,
) -> str:
    if score >= 75:
        strength = "strong"
    elif score >= 40:
        strength = "moderate"
    else:
        strength = "weak"

    matched_text = ", ".join(matched_skills[:5]) if matched_skills else "none"
    missing_text = ", ".join(missing_skills[:5]) if missing_skills else "none"

    return (
        f"This is a {strength} keyword match. "
        f"Matched skills: {matched_text}. "
        f"Missing skills: {missing_text}."
    )


def match_resume_to_jd(resume_text: str, jd_text: str) -> dict:
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = sorted(set(resume_skills) & set(jd_skills))
    missing_skills = sorted(set(jd_skills) - set(resume_skills))

    if jd_skills:
        overall_score = round((len(matched_skills) / len(jd_skills)) * 100, 2)
    else:
        overall_score = 0.0

    explanation = build_explanation(
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        score=overall_score,
    )

    return {
        "overall_score": overall_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_keywords": resume_skills,
        "jd_keywords": jd_skills,
        "explanation": explanation,
    }