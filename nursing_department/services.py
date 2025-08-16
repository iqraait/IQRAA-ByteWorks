from .models import Form1_assement

def build_results_table(staff):
    """Return a dict of {criteria: {evaluation_period: score}} for a staff."""
    assessments = Form1_assement.objects.filter(staff=staff)

    results_table = {}
    for assessment in assessments:
        for section, items in assessment.data.items():
            for criteria, score in items.items():
                if criteria not in results_table:
                    results_table[criteria] = {}
                results_table[criteria][assessment.evaluation_period] = score
    return results_table
