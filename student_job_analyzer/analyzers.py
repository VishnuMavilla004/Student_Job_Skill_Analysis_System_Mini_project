# SkillAnalyzer
from abc import ABC, abstractmethod

class SkillAnalyzer(ABC):

    @abstractmethod
    def analyze(self, student, job):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self, student, job):
        student_skills = student.get_skills()
        job_skills = job.get_required_skills()
        original_job_skills = job.get_original_skills()

        matched_skills = []

        index = 0
        while index < len(job_skills):
            required = job_skills[index]
            original_name = original_job_skills[index]

            is_match = False
            for student_skill in student_skills:
                if student_skill == required:
                    is_match = True
                    break

            if is_match:
                already_counted = False
                for matched in matched_skills:
                    if matched.lower() == required:
                        already_counted = True
                        break

                if not already_counted:
                    matched_skills.append(original_name)

            index = index + 1

        total_required = len(job_skills)

        if total_required == 0:
            percentage = 0
        else:
            percentage = (len(matched_skills) / total_required) * 100

        return {
            "matching_skills": matched_skills,
            "match_count": len(matched_skills),
            "total_required": total_required,
            "percentage": percentage,
        }

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self, student, job):
        student_skills = student.get_skills()
        job_skills = job.get_required_skills()
        original_job_skills = job.get_original_skills()

        missing_skills = []

        index = 0
        while index < len(job_skills):
            required = job_skills[index]
            original_name = original_job_skills[index]

            has_skill = False
            for student_skill in student_skills:
                if student_skill == required:
                    has_skill = True
                    break

            if not has_skill:
                # Avoid listing the same missing skill more than once
                already_listed = False
                for missing in missing_skills:
                    if missing.lower() == required:
                        already_listed = True
                        break

                if not already_listed:
                    missing_skills.append(original_name)

            index = index + 1

        return missing_skills