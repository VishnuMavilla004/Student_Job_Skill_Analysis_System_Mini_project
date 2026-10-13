# Student Profile
class StudentProfile:
    def __init__(self, student_name, student_skills):
        self._student_name = student_name
        self._original_skills = []
        self._student_skills = self._normalize_skills(student_skills)

    def _normalize_skills(self, skills):
        normalized = []

        if skills is None:
            return normalized

        for skill in skills:
            cleaned = skill.strip()
            if cleaned == "":
                continue

            lower_skill = cleaned.lower()

            already_added = False
            for existing in normalized:
                if existing == lower_skill:
                    already_added = True
                    break

            if not already_added:
                normalized.append(lower_skill)
                self._original_skills.append(cleaned)

        return normalized

    def get_name(self):
        return self._student_name

    def get_skills(self):
        return self._student_skills

    def get_original_skills(self):
        return self._original_skills

    
# Job Description

class JobDescription:

    def __init__(self, job_title, required_skills):
        self._job_title = job_title
        self._original_skills = []
        self._required_skills = self._normalize_skills(required_skills)

    def _normalize_skills(self, skills):
        normalized = []

        if skills is None or len(skills) == 0:
            return normalized

        for skill in skills:
            cleaned = skill.strip()
            if cleaned == "":
                continue

            lower_skill = cleaned.lower()

            already_added = False
            for existing in normalized:
                if existing == lower_skill:
                    already_added = True
                    break

            if not already_added:
                normalized.append(lower_skill)
                self._original_skills.append(cleaned)

        return normalized

    def get_title(self):
        return self._job_title

    def get_required_skills(self):
        return self._required_skills

    def get_original_skills(self):
        return self._original_skills

    def get_skill_count(self):
        return len(self._required_skills)

