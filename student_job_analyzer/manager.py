from analyzers import MatchScoreCalculator, MissingSkillDetector

class Manager:
    def __init__(self, student, job):
        self._student = student
        self._job = job
        self._analyzers = [
            MatchScoreCalculator(),
            MissingSkillDetector(),
        ]

    def run_analysis(self):

        match_result = None
        missing_skills = None

        for analyzer in self._analyzers:
            result = analyzer.analyze(self._student, self._job)

            if isinstance(result, dict):
                match_result = result
            else:
                missing_skills = result

        self._display_report(match_result, missing_skills)

    def _display_report(self, match_result, missing_skills):

        print("=" * 50)
        print("STUDENT–JOB SKILL ANALYSIS REPORT")
        print("=" * 50)
        print()
        print("Student Name:", self._student.get_name())
        print()
        print("Job Title:", self._job.get_title())
        print()
        print("Required Skills:", match_result["total_required"])
        print()

        print("Matching Skills:")
        if len(match_result["matching_skills"]) == 0:
            print("- None")
        else:
            for skill in match_result["matching_skills"]:
                print("-", skill)
        print()

        print("Missing Skills:")
        if len(missing_skills) == 0:
            print("- None")
        else:
            for skill in missing_skills:
                print("-", skill)
        print()

        percentage = match_result["percentage"]
        if percentage == int(percentage):
            print("Match Score: {}%".format(int(percentage)))
        else:
            print("Match Score: {:.1f}%".format(percentage))
        print()

        print("Explanation:")
        print(
            "The student matches {} out of {} unique required skills. "
            "Therefore, the skill match percentage is {}%.".format(
                match_result["match_count"],
                match_result["total_required"],
                int(percentage) if percentage == int(percentage) else round(percentage, 1),
            )
        )
        print()