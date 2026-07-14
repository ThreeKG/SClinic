from __future__ import annotations

from pathlib import Path
import sys

sys.path = [p for p in sys.path if '/.hermes/hermes-agent/venv/' not in p]

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfgen import canvas

BASE = Path('/Users/loay/Desktop/3kg/SClinic')
OUT = BASE / 'Docs & Planing' / 'deliverables'
OUT.mkdir(parents=True, exist_ok=True)

PDF_PATH = OUT / 'SClinic_Executive_Report.pdf'
FOOTER_URL = 'https://threekg.com'

# Palette
DARK = '#132238'
NAVY = '#1B2B49'
TEAL = '#1B8C8B'
GOLD = '#D7A643'
LIGHT = '#F5F7FA'
SLATE = '#4A5668'
MUTED = '#718096'
BORDER = '#D8DEE9'
WHITE = '#FFFFFF'
RED = '#B24A4A'
GREEN = '#2E7D5B'

M = 18 * mm
PAGE_W, PAGE_H = A4
CONTENT_W = PAGE_W - 2 * M

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10.5,
    leading=13.2,
    textColor=colors.HexColor(SLATE),
    spaceAfter=2,
    alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name='BodySmall',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.1,
    leading=11.5,
    textColor=colors.HexColor(SLATE),
    spaceAfter=1,
    alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name='DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=25,
    leading=28,
    textColor=colors.HexColor(DARK),
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='DocSection',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=21,
    textColor=colors.HexColor(NAVY),
    spaceAfter=3,
))
styles.add(ParagraphStyle(
    name='CardTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=16,
    textColor=colors.HexColor(NAVY),
))
styles.add(ParagraphStyle(
    name='CardBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10.4,
    leading=12.8,
    textColor=colors.HexColor(SLATE),
))
styles.add(ParagraphStyle(
    name='MetricLabel',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=10,
    textColor=colors.HexColor(MUTED),
    alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name='MetricValue',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=16,
    textColor=colors.HexColor(DARK),
))
styles.add(ParagraphStyle(
    name='Footer',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=9,
    textColor=colors.HexColor(MUTED),
))


def p(text: str, style: str = 'Body') -> Paragraph:
    return Paragraph(text, styles[style])


def hexcolor(value: str):
    if isinstance(value, str) and not value.startswith('#'):
        value = f'#{value}'
    return colors.HexColor(value)


def draw_paragraph(c: canvas.Canvas, text: str, x: float, y_top: float, width: float, style='Body') -> float:
    para = p(text, style)
    w, h = para.wrap(width, PAGE_H)
    para.drawOn(c, x, y_top - h)
    return h


def draw_box(c: canvas.Canvas, x: float, y: float, w: float, h: float, fill=WHITE, stroke=BORDER, radius=10, stroke_width=1):
    c.setFillColor(hexcolor(fill) if isinstance(fill, str) else fill)
    c.setStrokeColor(hexcolor(stroke) if isinstance(stroke, str) else stroke)
    c.setLineWidth(stroke_width)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def footer(c: canvas.Canvas, page_num: int, total_pages: int = 5):
    y = 10 * mm
    c.setStrokeColor(hexcolor(BORDER))
    c.setLineWidth(0.5)
    c.line(M, 14 * mm, PAGE_W - M, 14 * mm)
    c.setFont('Helvetica', 8)
    c.setFillColor(hexcolor(MUTED))
    brand = '3KG'
    tail = ' | SClinic client materials'
    x = M
    c.drawString(x, y, brand)
    c.linkURL(FOOTER_URL, (x, y - 1, x + stringWidth(brand, 'Helvetica', 8), y + 8), relative=0)
    c.drawString(x + stringWidth(brand, 'Helvetica', 8), y, tail)
    right = f'Page {page_num} of {total_pages}'
    c.drawRightString(PAGE_W - M, y, right)


def metric_card(c: canvas.Canvas, x: float, y: float, w: float, h: float, label: str, value: str, note: str, accent: str):
    draw_box(c, x, y, w, h, fill=WHITE, stroke=BORDER, radius=12)
    c.setFillColor(hexcolor(accent))
    c.roundRect(x, y + h - 6, w, 6, 12, fill=1, stroke=0)
    draw_paragraph(c, label.upper(), x + 8, y + h - 13, w - 16, 'MetricLabel')
    draw_paragraph(c, value, x + 8, y + h - 25, w - 16, 'MetricValue')
    draw_paragraph(c, note, x + 8, y + 8, w - 16, 'BodySmall')


def callout_card(c: canvas.Canvas, x: float, y: float, w: float, h: float, title: str, body: str, accent: str = TEAL, dark: bool = False):
    fill = DARK if dark else WHITE
    title_color = WHITE if dark else NAVY
    body_color = '#E6EEF8' if dark else SLATE
    draw_box(c, x, y, w, h, fill=fill, stroke=BORDER if not dark else fill, radius=12)
    c.setFillColor(hexcolor(accent))
    c.roundRect(x, y + h - 6, w, 6, 12, fill=1, stroke=0)
    c.setFillColor(hexcolor(title_color))
    c.setFont('Helvetica-Bold', 14)
    c.drawString(x + 10, y + h - 22, title)
    c.setFillColor(hexcolor(body_color))
    text = c.beginText(x + 10, y + h - 38)
    text.setFont('Helvetica', 10.4)
    text.setLeading(13)
    for line in simpleSplit(body, 'Helvetica', 10.4, w - 20):
        text.textLine(line)
    c.drawText(text)


def bullet_list(c: canvas.Canvas, items: list[str], x: float, y_top: float, width: float, font_size: float = 10.5) -> float:
    current_y = y_top
    for item in items:
        h = draw_paragraph(c, f'• {item}', x, current_y, width, 'Body')
        current_y -= h + 1.5 * mm
    return y_top - current_y


def title(c: canvas.Canvas, text: str, subtitle: str | None = None, dark_bg: bool = False):
    c.setFont('Helvetica-Bold', 25)
    c.setFillColor(hexcolor(WHITE if dark_bg else DARK))
    c.drawString(M, PAGE_H - 24 * mm, text)
    if subtitle:
        c.setFont('Helvetica', 12)
        c.setFillColor(hexcolor('#DCE6F3' if dark_bg else SLATE))
        c.drawString(M, PAGE_H - 31 * mm, subtitle)


def page1(c: canvas.Canvas):
    c.setFillColor(hexcolor(DARK))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(hexcolor(GOLD))
    c.rect(0, PAGE_H - 34 * mm, PAGE_W, 6, fill=1, stroke=0)
    title(c, 'SClinic Technical Audit', 'Executive report for sclinic.com.tr and sclinic.ae', dark_bg=True)
    draw_paragraph(c, 'Evidence-based assessment of performance, security, SEO, and UX.', M, PAGE_H - 44 * mm, CONTENT_W * 0.65, 'Body')
    draw_paragraph(c, 'Prepared for client presentation and rebuild decision-making.', M, PAGE_H - 50 * mm, CONTENT_W * 0.65, 'Body')
    card_w = (CONTENT_W - 16 * mm) / 3
    y = 55 * mm
    metric_card(c, M, y, card_w, 36 * mm, 'Performance', '0.71 / 0.65', 'Lighthouse scores', TEAL)
    metric_card(c, M + card_w + 8 * mm, y, card_w, 36 * mm, 'Security', 'No hardening baseline', 'Legacy stack and weak public posture', RED)
    metric_card(c, M + (card_w + 8 * mm) * 2, y, card_w, 36 * mm, 'Recommendation', 'Rebuild', 'The current stack is costly to patch', GOLD)
    footer(c, 1)


def page2(c: canvas.Canvas):
    c.setFillColor(hexcolor(WHITE))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    title(c, 'Executive summary')
    left_w = 112 * mm
    right_x = M + left_w + 10 * mm
    right_w = PAGE_W - M - right_x
    summary = (
        'Both sites are functional, but the evidence points to the same pattern: a legacy PHP/Plesk stack, '
        'heavy client-side dependencies, repeated homepage content, and avoidable performance and accessibility debt. '
        'The sites are operating, but they are not yet at the standard expected for a premium healthcare brand.'
    )
    draw_box(c, M, 210 * mm, left_w, 42 * mm, fill=LIGHT, stroke=BORDER, radius=12)
    draw_paragraph(c, summary, M + 8, PAGE_H - 52 * mm, left_w - 16, 'Body')
    bullet_list(c, [
        'Legacy stack: nginx + PHP/7.4.33 + PleskLin',
        'Same JavaScript exception on both homepages',
        'The .ae sitemap still contains Turkish legacy URLs',
        'Lighthouse reports layout shifts, unused JS, and cache waste',
    ], M + 2, PAGE_H - 84 * mm, left_w - 8)

    callout_card(c, right_x, 207 * mm, right_w, 48 * mm, 'Decision', 'Proceed with a rebuild rather than layering more fixes onto the current stack.', accent=GOLD)
    callout_card(c, right_x, 154 * mm, right_w, 48 * mm, 'Commercial implication', 'A cleaner rebuild gives the team a better platform for conversions, localization, and SEO growth.', accent=TEAL)

    draw_paragraph(c, 'Evidence table', M, 110 * mm, CONTENT_W, 'DocSection')
    table_data = [
        ['Site', 'Perf', 'A11y', 'Best Practices', 'SEO'],
        ['sclinic.com.tr', '0.71', '0.61', '0.54', '0.83'],
        ['sclinic.ae', '0.65', '0.81', '0.54', '0.83'],
    ]
    t = Table(table_data, colWidths=[45 * mm, 20 * mm, 20 * mm, 34 * mm, 20 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), hexcolor(NAVY)),
        ('TEXTCOLOR', (0, 0), (-1, 0), hexcolor(WHITE)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.4, hexcolor(BORDER)),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [hexcolor('FFFFFF'), hexcolor('F7FAFC')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ]))
    w, h = t.wrap(CONTENT_W, PAGE_H)
    t.drawOn(c, M, 104 * mm - h)
    footer(c, 2)


def page3(c: canvas.Canvas):
    c.setFillColor(hexcolor(WHITE))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    title(c, 'Evidence snapshot')
    metric_card(c, M, 215 * mm, 55 * mm, 30 * mm, 'Runtime bug', '2x', 'Same JS exception in aliaygir.js', RED)
    metric_card(c, M + 60 * mm, 215 * mm, 55 * mm, 30 * mm, 'Hidden waste', '1.9–2.2 MiB', 'Cache savings reported by Lighthouse', GOLD)
    metric_card(c, M + 120 * mm, 215 * mm, 55 * mm, 30 * mm, 'Layout shifts', '15', 'Both homepages trigger instability', TEAL)

    draw_paragraph(c, 'Technical profile', M, 182 * mm, 82 * mm, 'DocSection')
    bullet_list(c, [
        'nginx + PHP/7.4.33 + PleskLin',
        'Legacy jQuery-era assets and plugin stack',
        'Google Tag Manager, Google Ads, Facebook Pixel',
        'No major hardening headers in the captured response',
    ], M, 174 * mm, 82 * mm)

    draw_paragraph(c, 'SEO and crawlability', 108 * mm, 182 * mm, 82 * mm, 'DocSection')
    bullet_list(c, [
        'robots.txt allows crawling and lists a sitemap.',
        '.com.tr sitemap: 60 unique URLs.',
        '.ae sitemap: 62 unique URLs, with Turkish legacy routes still present.',
    ], 110 * mm, 174 * mm, 82 * mm)

    draw_paragraph(c, 'Priority metrics', M, 118 * mm, CONTENT_W, 'DocSection')
    table_data = [
        ['Metric', 'sclinic.com.tr', 'sclinic.ae'],
        ['Performance', '0.71', '0.65'],
        ['LCP', '2.2s', '3.5s'],
        ['CLS', '0.434', '0.344'],
        ['Unused JS', '311 KiB', '429 KiB'],
        ['Cache savings', '2,172 KiB', '1,936 KiB'],
    ]
    t = Table(table_data, colWidths=[52 * mm, 47 * mm, 47 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), hexcolor(TEAL)),
        ('TEXTCOLOR', (0, 0), (-1, 0), hexcolor(WHITE)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.4, hexcolor(BORDER)),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [hexcolor('FFFFFF'), hexcolor('F7FAFC')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ]))
    w, h = t.wrap(CONTENT_W, PAGE_H)
    t.drawOn(c, M, 112 * mm - h)
    footer(c, 3)


def page4(c: canvas.Canvas):
    c.setFillColor(hexcolor(LIGHT))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    title(c, 'Recommendation and roadmap')
    draw_box(c, M, 194 * mm, CONTENT_W, 35 * mm, fill=WHITE, stroke=BORDER, radius=12)
    draw_paragraph(c, 'Recommended architecture', M + 8, PAGE_H - 46 * mm, CONTENT_W - 16, 'DocSection')
    draw_paragraph(c, 'Modern CMS + reusable component system + CDN-backed hosting + structured local SEO + analytics governance.', M + 8, PAGE_H - 58 * mm, CONTENT_W - 16, 'Body')

    draw_paragraph(c, 'Suggested delivery roadmap', M, 172 * mm, CONTENT_W, 'DocSection')
    gap = 4 * mm
    top_row_w = (CONTENT_W - 2 * gap) / 3
    bottom_row_w = (CONTENT_W - gap) / 2
    # top row
    roadmap_cards = [
        ('1–2 wks', 'Discovery', 'Inventory content, routes, analytics, redirects', TEAL),
        ('2–3 wks', 'Design', 'Define the visual system and page templates', TEAL),
        ('4–8 wks', 'Build', 'Implement CMS, layouts, forms, and SEO foundations', GOLD),
        ('1–2 wks', 'QA + Launch', 'Validate performance, forms, redirects, and analytics', NAVY),
        ('1–2 wks', 'Stabilize', 'Monitor errors, conversions, and search visibility', NAVY),
    ]
    y1 = 118 * mm
    for i, (dur, phase, desc, accent) in enumerate(roadmap_cards[:3]):
        x = M + i * (top_row_w + gap)
        callout_card(c, x, y1, top_row_w, 44 * mm, phase, f'{dur}\n\n{desc}', accent=accent)
    y2 = 68 * mm
    for i, (dur, phase, desc, accent) in enumerate(roadmap_cards[3:]):
        x = M + i * (bottom_row_w + gap)
        callout_card(c, x, y2, bottom_row_w, 40 * mm, phase, f'{dur}\n\n{desc}', accent=accent)

    draw_box(c, M, 24 * mm, CONTENT_W, 44 * mm, fill=WHITE, stroke=BORDER, radius=12)
    draw_paragraph(c, 'Success criteria', M + 8, 58 * mm, CONTENT_W - 16, 'DocSection')
    bullet_list(c, [
        'Faster pages and fewer layout shifts.',
        'Clearer consultation funnels.',
        'Cleaner localization and URL handling.',
        'A platform the team can maintain confidently.',
    ], M + 8, 51 * mm, CONTENT_W - 16)
    footer(c, 4)


def page5(c: canvas.Canvas):
    c.setFillColor(hexcolor(WHITE))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    title(c, 'Next steps')

    draw_box(c, M, 150 * mm, 88 * mm, 80 * mm, fill=LIGHT, stroke=BORDER, radius=12)
    draw_paragraph(c, 'Immediate actions', M + 8, PAGE_H - 45 * mm, 72 * mm, 'DocSection')
    bullet_list(c, [
        'Approve the rebuild direction and scope.',
        'Map current pages to the new content model.',
        'Prioritize URLs that must preserve search equity.',
        'Prepare design and development kickoff materials.',
    ], M + 8, PAGE_H - 54 * mm, 72 * mm)

    draw_box(c, M + 98 * mm, 150 * mm, CONTENT_W - 98 * mm, 80 * mm, fill=DARK, stroke=DARK, radius=12)
    c.setFillColor(hexcolor(GOLD))
    c.roundRect(M + 98 * mm, 150 * mm + 80 * mm - 6, CONTENT_W - 98 * mm, 6, 12, fill=1, stroke=0)
    draw_paragraph(c, '<font color="#FFFFFF"><b>Prepared by 3KG</b></font>', M + 106 * mm, 221 * mm, CONTENT_W - 114 * mm, 'CardTitle')
    draw_paragraph(c, '<font color="#E6EEF8">Client-ready, evidence-based, and concise.</font>', M + 106 * mm, 207 * mm, CONTENT_W - 114 * mm, 'CardBody')
    draw_paragraph(c, '<font color="#E6EEF8">Use this PDF for decision-making and stakeholder review.</font>', M + 106 * mm, 194 * mm, CONTENT_W - 114 * mm, 'CardBody')

    draw_box(c, M, 58 * mm, CONTENT_W, 80 * mm, fill=WHITE, stroke=BORDER, radius=12)
    draw_paragraph(c, 'Why this matters', M + 8, 133 * mm, CONTENT_W - 16, 'DocSection')
    draw_paragraph(c,
                   'The current sites still deliver the right brand promise, but the technical foundation is holding them back. A rebuild gives the team a cleaner platform, a better user journey, and a stronger base for growth in both markets.',
                   M + 8, 123 * mm, CONTENT_W - 16, 'Body')

    draw_box(c, M, 20 * mm, CONTENT_W, 28 * mm, fill=LIGHT, stroke=BORDER, radius=12)
    draw_paragraph(c, 'Evidence files included: headers, robots, sitemap captures, browser snapshots, console evidence, and Lighthouse JSON for both sites.', M + 8, 38 * mm, CONTENT_W - 16, 'BodySmall')
    footer(c, 5)


def build(path: Path = PDF_PATH):
    c = canvas.Canvas(str(path), pagesize=A4)
    page1(c); c.showPage()
    page2(c); c.showPage()
    page3(c); c.showPage()
    page4(c); c.showPage()
    page5(c); c.showPage()
    c.save()


if __name__ == '__main__':
    build()
