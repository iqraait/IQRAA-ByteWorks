from .models import Form1_assement
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.http import HttpResponse

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





def generate_assessment_pdf(assessment):
    """Generate PDF for a Form1_assement instance."""

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="assessment_{assessment.staff.staff_name}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)

    # Header Info
    p.drawString(100, 800, f"Assessment Report - {assessment.staff.staff_name}")
    p.drawString(100, 770, f"Evaluator: {assessment.evaluator_name}")
    p.drawString(100, 740, f"Period: {assessment.get_evaluation_period_display()}")
    p.drawString(100, 710, f"Total Score: {assessment.total_score}")
    p.drawString(100, 680, f"Percentage: {assessment.percentage}%")

    # Dynamic JSON Data
    y = 650
    for section, items in assessment.data.items():
        p.drawString(80, y, f"Section: {section}")
        y -= 20
        for item, score in items.items():
            p.drawString(120, y, f"{item}: {score}")
            y -= 15

    p.showPage()
    p.save()
    return response
