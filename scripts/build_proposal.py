"""Render the project's simple Markdown proposal as a portable PDF.

Requires the optional requirements-docs.txt dependency. Supported Markdown:
# and ## headings, paragraphs, - bullets, **bold**, and pagebreak comments.
"""

from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "development-proposal.md"
OUTPUT = ROOT / "docs" / "development-proposal.pdf"


def inline(text):
    """Escape content before introducing the supported bold markup."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escape(text))


def footer(pdf, document):
    pdf.saveState()
    pdf.setFont("Helvetica", 9)
    pdf.setFillColor(colors.HexColor("#555555"))
    pdf.drawString(48, 28, "Daikibo Machine Health Dashboard Proposal")
    pdf.drawRightString(A4[0] - 48, 28, str(document.page))
    pdf.restoreState()


def build():
    styles = {
        "title": ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=21,
                                leading=26, spaceAfter=18, textColor=colors.black),
        "heading": ParagraphStyle("Heading", fontName="Helvetica-Bold", fontSize=14,
                                  leading=18, spaceBefore=12, spaceAfter=9,
                                  keepWithNext=True, textColor=colors.black),
        "body": ParagraphStyle("Body", fontName="Helvetica", fontSize=10.8,
                               leading=15, spaceAfter=10, alignment=TA_LEFT),
        "bullet": ParagraphStyle("Bullet", fontName="Helvetica", fontSize=10.8,
                                 leading=15, leftIndent=12, firstLineIndent=-8,
                                 spaceAfter=8),
    }
    story = []
    for block in SOURCE.read_text(encoding="utf-8").strip().split("\n\n"):
        if block.strip() == "<!-- pagebreak -->":
            story.append(PageBreak())
        elif block.startswith("# "):
            story.append(Paragraph(inline(block[2:]), styles["title"]))
        elif block.startswith("## "):
            story.append(Paragraph(inline(block[3:]), styles["heading"]))
        elif block.startswith("- "):
            for line in block.splitlines():
                story.append(Paragraph("- " + inline(line[2:]), styles["bullet"]))
        else:
            story.append(Paragraph(inline(" ".join(block.splitlines())), styles["body"]))
    document = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=48,
                                rightMargin=48, topMargin=42, bottomMargin=48,
                                title="Daikibo Machine Health Dashboard Proposal",
                                author="", subject="Software development planning")
    document.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    build()
