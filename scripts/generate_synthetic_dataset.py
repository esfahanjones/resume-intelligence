# scripts/generate_synthetic_dataset.py
import json
import random
import uuid
from datetime import datetime
from pathlib import Path

from faker import Faker
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer

fake = Faker("en_US")

TECH_STACKS = [
    ["Python", "FastAPI", "SQL", "PostgreSQL", "Docker", "AWS"],
    ["JavaScript", "TypeScript", "React", "Node.js", "Express", "MongoDB"],
    ["Python", "PyTorch", "TensorFlow", "scikit-learn", "Pandas", "MLflow"],
    ["Java", "Spring Boot", "Kubernetes", "Terraform", "GCP", "Microservices"],
    ["C#", ".NET", "Azure", "SQL Server", "Entity Framework", "CI/CD"],
    ["Go", "gRPC", "Kubernetes", "Redis", "Kafka", "Prometheus"],
    ["Rust", "Actix", "Postgres", "Linux", "Data Engineering", "Docker"],
]

JOB_TITLES = [
    "Software Engineer",
    "Senior Software Engineer",
    "ML Engineer",
    "Data Engineer",
    "Backend Engineer",
    "Full Stack Engineer",
    "Product Engineer",
    "Platform Engineer",
    "DevOps Engineer",
    "Data Scientist",
]

COMPANIES = [
    "Northstar Labs",
    "OpenSignal AI",
    "Apex Systems",
    "HelioWorks",
    "BluePeak Analytics",
    "Horizon Grid",
    "NovaStack",
    "Signal Harbor",
    "CloudForm Labs",
    "Quantum Foundry",
    "Summit Systems",
    "ByteForge",
    "LatticeWorks",
    "Fjord Dynamics",
    "Cinderworks",
]

DEGREES = [
    "B.S. in Computer Science",
    "M.S. in Data Science",
    "B.E. in Software Engineering",
    "B.A. in Economics",
    "B.S. in Information Systems",
    "M.S. in Computer Science",
    "B.S. in Mathematics",
]

UNIVERSITIES = [
    "University of Michigan",
    "Georgia Tech",
    "University of Texas at Austin",
    "Carnegie Mellon University",
    "University of Washington",
    "University of Illinois Urbana-Champaign",
    "Northeastern University",
    "University of California, Berkeley",
]

CERTIFICATES = [
    "AWS Certified Developer",
    "Google Associate Cloud Engineer",
    "Azure Fundamentals",
    "Certified Kubernetes Administrator",
    "Databricks Certified Associate Developer",
    "Oracle Certified Java Programmer",
    "TensorFlow Developer Certificate",
    "Professional Scrum Master",
    "HashiCorp Terraform Associate",
]

CITIES = [
    "San Francisco, CA",
    "New York, NY",
    "Seattle, WA",
    "Austin, TX",
    "Boston, MA",
    "Chicago, IL",
    "Denver, CO",
    "Atlanta, GA",
    "Miami, FL",
    "Remote",
]


def generate_work_experience():
    work_experience = []
    start_year = random.randint(2015, 2021)
    jobs = random.randint(1, 4)

    for _ in range(jobs):
        job_title = random.choice(JOB_TITLES)
        company = random.choice(COMPANIES)
        end_year = start_year + random.randint(1, 4)
        start_date = f"{start_year}-0{random.randint(1, 9)}-01"
        end_date = f"{end_year}-0{random.randint(1, 9)}-01"
        years = round(random.uniform(1.0, 5.0), 1)

        bullets = [
            f"Built and maintained {random.choice(['backend services', 'API integrations', 'data pipelines', 'deployment automation'])} using {random.choice(['Python', 'TypeScript', 'Go', 'Java'])}.",
            f"Improved system reliability and performance by optimizing {random.choice(['database queries', 'service latency', 'job throughput', 'query efficiency'])}.",
            f"Collaborated with cross-functional teams to deliver {random.choice(['production features', 'platform tooling', 'data products', 'customer-facing workflows'])}.",
            f"Worked with {random.choice(['AWS', 'GCP', 'Azure', 'Kubernetes', 'Docker', 'PostgreSQL'])} to support scalable services.",
        ]

        work_experience.append(
            {
                "title": job_title,
                "company": company,
                "start_date": start_date,
                "end_date": end_date,
                "years": years,
                "bullet_points": bullets[:3],
            }
        )
        start_year += random.randint(1, 3)

    return work_experience


def generate_education():
    university = random.choice(UNIVERSITIES)
    degree = random.choice(DEGREES)
    grad_year = random.randint(2014, 2024)

    return [
        {
            "school": university,
            "degree": degree,
            "field_of_study": "Computer Science" if "Computer Science" in degree else "Engineering",
            "start_year": grad_year - 4,
            "end_year": grad_year,
        }
    ]


def generate_certifications():
    num_certs = random.randint(0, 3)
    return random.sample(CERTIFICATES, k=num_certs)


def generate_candidate():
    full_name = fake.name()
    first_name, last_name = full_name.split()[0], full_name.split()[-1]
    email = f"{first_name.lower()}.{last_name.lower()}@{fake.free_email_domain()}"
    phone = fake.phone_number()
    location = random.choice(CITIES)
    skills = random.sample(sorted(set(skill for stack in TECH_STACKS for skill in stack)), k=random.randint(6, 12))
    work_experience = generate_work_experience()
    years_experience = round(sum(item["years"] for item in work_experience), 1)

    candidate = {
        "candidate_id": str(uuid.uuid4()),
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "location": location,
        "years_experience": years_experience,
        "linkedin_url": f"https://linkedin.com/in/{first_name.lower()}-{last_name.lower()}",
        "portfolio_url": f"https://github.com/{first_name.lower()}{last_name.lower()}",
        "summary": (
            f"{first_name} is a results-driven software professional with {years_experience} years of experience in "
            f"{random.choice(['backend engineering', 'full-stack product development', 'AI applications', 'cloud platform engineering'])}. "
            "Strong focus on system design, product delivery, and building scalable data-driven applications."
        ),
        "skills": skills,
        "work_experience": work_experience,
        "education": generate_education(),
        "certifications": generate_certifications(),
    }
    return candidate


def build_resume_pdf(output_path: Path, candidate: dict):
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=(612, 792),
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40,
    )
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(candidate["full_name"], styles["Title"]))
    story.append(Paragraph(f"{candidate['email']} | {candidate['phone']} | {candidate['location']}", styles["BodyText"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Professional Summary", styles["Heading2"]))
    story.append(Paragraph(candidate["summary"], styles["BodyText"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Skills", styles["Heading2"]))
    story.append(Paragraph(", ".join(candidate["skills"]), styles["BodyText"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Experience", styles["Heading2"]))
    for job in candidate["work_experience"]:
        story.append(Paragraph(f"<b>{job['title']}</b> | {job['company']}", styles["BodyText"]))
        story.append(Paragraph(f"{job['start_date']} - {job['end_date']}", styles["BodyText"]))
        bullet_items = [ListItem(Paragraph(b), leftIndent=18) for b in job["bullet_points"]]
        story.append(ListFlowable(bullet_items, bulletType="bullet", leftIndent=18))
        story.append(Spacer(1, 8))

    story.append(Paragraph("Education", styles["Heading2"]))
    for edu in candidate["education"]:
        story.append(Paragraph(f"<b>{edu['degree']}</b> | {edu['school']}", styles["BodyText"]))
        story.append(Paragraph(f"{edu['field_of_study']} ({edu['start_year']} - {edu['end_year']})", styles["BodyText"]))
        story.append(Spacer(1, 6))

    if candidate["certifications"]:
        story.append(Paragraph("Certifications", styles["Heading2"]))
        story.append(Paragraph(", ".join(candidate["certifications"]), styles["BodyText"]))

    doc.build(story)


def generate_dataset(num_profiles: int = 60, output_dir: str = "data/synthetic"):
    output_root = Path(output_dir)
    resumes_dir = output_root / "resumes"
    ground_truth_dir = output_root / "ground_truth"
    resumes_dir.mkdir(parents=True, exist_ok=True)
    ground_truth_dir.mkdir(parents=True, exist_ok=True)

    candidates = []
    for _ in range(num_profiles):
        candidate = generate_candidate()
        candidate_file = resumes_dir / f"{candidate['candidate_id']}.pdf"
        build_resume_pdf(candidate_file, candidate)
        candidates.append(candidate)

    ground_truth_path = ground_truth_dir / "candidates_ground_truth.json"
    with ground_truth_path.open("w", encoding="utf-8") as file:
        json.dump(
            {
                "generated_at": datetime.utcnow().isoformat(),
                "num_candidates": len(candidates),
                "candidates": candidates,
            },
            file,
            indent=2,
            ensure_ascii=False,
        )

    print(f"Generated {len(candidates)} synthetic candidates")
    print(f"Resumes saved to: {resumes_dir}")
    print(f"Ground truth saved to: {ground_truth_path}")


if __name__ == "__main__":
    generate_dataset(num_profiles=60, output_dir="data/synthetic")
