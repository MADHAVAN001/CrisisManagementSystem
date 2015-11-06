__author__ = 'Ankur Bansal'

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from DontCrysis.models import Crisis

width, height = A4
styles = getSampleStyleSheet()
styleBH = styles["Normal"]
styleN = styles["BodyText"]
styleBH.alignment = TA_CENTER
styleN.alignment = TA_LEFT

def coord(x, y, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

def generate():
    # Headers
    h_sno = Paragraph('''<b>S No</b>''', styleBH)
    h_title = Paragraph('''<b>Crisis Title</b>''', styleBH)
    h_description = Paragraph('''<b>Description</b>''', styleBH)
    h_postal_code = Paragraph('''<b>Postal Code</b>''', styleBH)
    h_type = Paragraph('''<b>Type</b>''', styleBH)
    h_severity = Paragraph('''<b>Severity</b>''', styleBH)
    h_date = Paragraph('''<b>Date</b>''', styleBH)
    h_time= Paragraph('''<b>Time</b>''', styleBH)
    h_person_name= Paragraph('''<b>Person Name</b>''', styleBH)
    h_person_phone= Paragraph('''<b>Person Phone No.</b>''', styleBH)
    h_is_active= Paragraph('''<b>Active</b>''', styleBH)
    # Texts
    data= [[h_sno, h_title, h_postal_code, h_type, h_severity, h_date, h_time, h_is_active]]
    crisis_object=Crisis.objects.all()
    for item in crisis_object:
        crisis_data=[]
        crisis_data.append(item.id)
        crisis_data.append(item.title)
        crisis_data.append(item.postalcode)
        crisis_data.append(item.type)
        crisis_data.append(item.severity)
        crisis_data.append(item.date)
        crisis_data.append(item.time)
        crisis_data.append(item.isActive)
        data.append(crisis_data)
    table = Table(data, colWidths=[1.5* cm, 3 * cm, 2* cm, 2 * cm, 2* cm, 3 * cm, 2* cm, 1.5 * cm ])
    table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.15, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.15, colors.black),
                       ]))
    c = canvas.Canvas("crisis_report.pdf", pagesize=A4)
    table.wrapOn(c, width, height)
    table.drawOn(c, *coord(1.5, 3.5, cm))
    c.save()
generate()