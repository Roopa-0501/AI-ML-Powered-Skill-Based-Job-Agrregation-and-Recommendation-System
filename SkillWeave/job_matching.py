

import re

def rank_jobs_by_percentage(resume_skills, jobs):
    results = []

    if not resume_skills or not jobs:
        return results

    resume_skills = set([s.lower() for s in resume_skills])

    for job in jobs:
        job_text = (
            job.get("title", "") + " " +
            job.get("description", "")
        ).lower()

        matched = [s for s in resume_skills if s in job_text]

        match_percent = round((len(matched) / len(resume_skills)) * 100, 2)

        # 🔥 keep threshold LOW for real APIs
        if match_percent >= 10:
            results.append({
                "title": job.get("title", ""),
                "company": job.get("company", ""),
                "location": job.get("location", "Not specified"),
                "match_percentage": match_percent,     # ✅ STANDARD KEY
                "matched_skills": matched,             # ✅ STANDARD KEY
                "url": job.get("url")
            })

    return sorted(results, key=lambda x: x["match_percentage"], reverse=True)[:25]
