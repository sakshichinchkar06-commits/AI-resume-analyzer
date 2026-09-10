from io import BytesIO
from resume_analyzer import detect_sections, detect_skills, keyword_coverage


def test_sections():
    text = """
    Professional Summary
    Education
    Skills
    Experience
    Projects
    """
    result = detect_sections(text)
    assert result["Education"] is True
    assert result["Skills"] is True
    assert result["Experience"] is True


def test_skills():
    text = "Python, SQL, FastAPI, Docker and machine learning"
    skills = detect_skills(text)
    assert "python" in skills
    assert "sql" in skills
    assert "docker" in skills
    assert "machine learning" in skills


def test_keyword_coverage():
    resume = "Python SQL FastAPI Docker"
    jd = "Python SQL FastAPI AWS"
    score, matched, missing = keyword_coverage(resume, jd)
    assert score == 75
    assert "aws" in missing
    assert "python" in matched
