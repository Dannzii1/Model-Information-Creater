def calculate_company_gpa(minimum_gpa, student_gpa, gpa_weight):
    half_minimum_gpa = minimum_gpa * 0.5
    if student_gpa <= half_minimum_gpa:
        return 0
    else:
        get_student_gpa = student_gpa - half_minimum_gpa
        student_score = get_student_gpa / half_minimum_gpa * gpa_weight

        return student_score


def calculate_skills_score(student_skills, company_skill_weighting):
    calculate_skills = 0
    student_skills = [s_skill.lower() for s_skill in student_skills]
    for company_skill in company_skill_weighting.keys():
        if company_skill.lower() in student_skills:
            calculate_skills += company_skill_weighting[company_skill]

    return calculate_skills


def check_employment_availability_score(employment_type, company_employment_needed):
    if employment_type.lower() in company_employment_needed.keys():
        return company_employment_needed.get(employment_type)
    else:
        return 0


def check_qualifications_score(student_qual, company_qual_weighting):
    if student_qual in company_qual_weighting.keys():
        return company_qual_weighting.get(student_qual)
    else:
        return 0


def sum_all_values(gpa_score, skill_score, availability_score, qual_score):
    total_score = gpa_score + skill_score + availability_score + qual_score

    return total_score
