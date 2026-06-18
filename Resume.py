import PyPDF2
import re

with open("Resume.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    resume_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

clean_text = resume_text.replace(" ", "")

lines = [line.strip() for line in resume_text.split("\n") if line.strip()]

name = lines[0] if lines else "Not Found"

email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
emails = re.findall(email_pattern, clean_text)
email = emails[0] if emails else "Not Found"

phone_pattern = r'(\+91\s?\d{10}|\d{10})'
phones = re.findall(phone_pattern, resume_text)
phone = phones[0] if phones else "Not Found"

skills_keywords = [
    "Python", "Machine Learning", "Scikit-learn", "Pandas",
    "NumPy", "Prompt Engineering", "Prompt Evaluation",
    "AI Model Evaluation", "Benchmarking", "Google Colab",
    "GitHub"
]

skills = []

for skill in skills_keywords:
    if skill.lower() in resume_text.lower():
        skills.append(skill)

education = []

education_keywords = [
    "B.Tech",
    "Bachelor",
    "University",
    "Engineering",
    "College"
]

for line in lines:
    for keyword in education_keywords:
        if keyword.lower() in line.lower():
            education.append(line)
            break

experience = []

experience_keywords = [
    "Intern",
    "Developer",
    "Engineer",
    "Ambassador"
]

for line in lines:
    for keyword in experience_keywords:
        if keyword.lower() in line.lower():
            experience.append(line)
            break

print("\n========== RESUME DETAILS ==========\n")

print("Name:")
print(name)

print("\nEmail:")
print(email)

print("\nPhone:")
print(phone)

print("\nSkills:")
for skill in skills:
    print("-", skill)

print("\nEducation:")
for edu in education:
    print("-", edu)

print("\nExperience:")
for exp in experience:
        print("-", exp)