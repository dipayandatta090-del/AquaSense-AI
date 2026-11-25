from io import BytesIO
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def make_pdf(inputs, prediction, probabilities):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42)
    styles = getSampleStyleSheet()
    heading = ParagraphStyle("AquaTitle", parent=styles["Title"], textColor=colors.HexColor("#12304A"), alignment=TA_CENTER)
    story = [
        Paragraph("AquaSense AI", heading),
        Paragraph("Water Quality Prediction Report", ParagraphStyle("Sub", parent=styles["Normal"], alignment=TA_CENTER)),
        Spacer(1, 12),
        Paragraph("Generated: " + datetime.now().strftime("%d %B %Y, %I:%M %p"), styles["Normal"]),
        Spacer(1, 12),
        Paragraph("<b>Predicted class:</b> " + str(prediction), styles["Heading2"]),
        Paragraph("Input measurements", styles["Heading2"])
    ]
    rows = [["Parameter", "Value"]] + [[str(k), f"{float(v):,.4f}"] for k, v in inputs.items()]
    table = Table(rows, colWidths=[270, 180], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#12304A")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), .4, colors.HexColor("#D9E4EC")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F1F7FA")]),
        ("PADDING", (0,0), (-1,-1), 7)
    ]))
    story += [table, Spacer(1, 12), Paragraph("Class probabilities", styles["Heading2"])]
    prows = [["Class", "Probability"]] + [[str(k), f"{v:.2%}"] for k, v in probabilities.items()]
    pt = Table(prows, colWidths=[270, 180])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#12304A")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), .4, colors.HexColor("#D9E4EC")),
        ("PADDING", (0,0), (-1,-1), 7)
    ]))
    story += [pt, Spacer(1, 14), Paragraph("Important limitation", styles["Heading2"]),
        Paragraph("This is an educational machine-learning estimate, not a laboratory certificate. Do not use it alone to decide whether water is safe to drink. Appropriate laboratory testing and applicable drinking-water standards are required.", styles["BodyText"])]
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
