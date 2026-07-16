from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Avoid the local Pillow build interfering with reportlab.
sys.path = [p for p in sys.path if '/venv/' not in p]

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib.utils import simpleSplit
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfgen import canvas

BASE = Path('/Users/loay/Desktop/3kg/SClinic')
OUT = BASE / 'Docs & Planing' / 'deliverables'
OUT.mkdir(parents=True, exist_ok=True)
PDF_PATH = OUT / 'SClinic_UAE_Phase1_2_Week_Plan.pdf'

PAGE_W, PAGE_H = A4
M = 18 * mm
TOP_BAND_H = 18 * mm
FOOTER_Y = 10 * mm

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='TitleX',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=21,
    leading=25,
    textColor=colors.HexColor('#132238'),
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name='SectionTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=17,
    textColor=colors.HexColor('#1B2B49'),
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='BodyCopy',
    parent=styles['BodyText'],
    fontName='Helvetica',
    fontSize=10,
    leading=12.3,
    textColor=colors.HexColor('#4A5668'),
    spaceAfter=2,
))
styles.add(ParagraphStyle(
    name='BodySmall',
    parent=styles['BodyText'],
    fontName='Helvetica',
    fontSize=8.7,
    leading=10.8,
    textColor=colors.HexColor('#718096'),
    spaceAfter=1,
))
styles.add(ParagraphStyle(
    name='BulletCopy',
    parent=styles['BodyText'],
    fontName='Helvetica',
    fontSize=9,
    leading=11.2,
    leftIndent=12,
    firstLineIndent=-10,
    bulletIndent=0,
    textColor=colors.HexColor('#4A5668'),
    spaceAfter=1.2,
))
styles.add(ParagraphStyle(
    name='CardTitle',
    parent=styles['BodyText'],
    fontName='Helvetica-Bold',
    fontSize=12.4,
    leading=14.4,
    textColor=colors.HexColor('#1B2B49'),
))
styles.add(ParagraphStyle(
    name='DayPill',
    parent=styles['BodyText'],
    fontName='Helvetica-Bold',
    fontSize=8,
    leading=9.2,
    textColor=colors.white,
))

TASKS = [
    (
        'Day 1',
        'Access and review',
        [
            'Confirm access to the website, hosting, domain, analytics, and forms.',
            'Review the current website structure and confirm what can realistically be completed before launch.',
            'Agree on the urgent items and the items that can wait for Phase 2.',
        ],
        '#1B8C8B',
    ),
    (
        'Day 2',
        'Priority list and launch scope',
        [
            'Create a clear priority list for the launch version.',
            'Confirm the pages, services, and forms that matter most.',
            'Agree on the launch target and the minimum acceptable scope.',
        ],
        '#D7A643',
    ),
    (
        'Day 3',
        'Security and form checks',
        [
            'Fix the most important security issues.',
            'Test all contact and enquiry forms.',
            'Make sure submissions are protected and delivered correctly.',
        ],
        '#B24A4A',
    ),
    (
        'Day 4',
        'Content cleanup',
        [
            'Remove incomplete, duplicated, or placeholder content.',
            'Correct spelling, grammar, and unclear wording.',
            'Make clinic, service, contact, and location details more reliable.',
        ],
        '#4E79A7',
    ),
    (
        'Day 5',
        'Mobile and layout improvements',
        [
            'Improve the look and feel on phones and tablets.',
            'Fix spacing, alignment, and any broken or crowded sections.',
            'Make buttons, calls-to-action, and contact actions easier to use.',
        ],
        '#6B5B95',
    ),
    (
        'Day 6',
        'SEO essentials',
        [
            'Improve page titles, descriptions, and heading structure.',
            'Check redirects, canonical tags, and legacy URLs.',
            'Improve image text and search visibility basics.',
        ],
        '#2E7D5B',
    ),
    (
        'Day 7',
        'Speed and media improvements',
        [
            'Reduce delays on important pages.',
            'Compress and resize key images.',
            'Improve how media loads so pages feel faster.',
        ],
        '#009688',
    ),
    (
        'Day 8',
        'Ads and tracking readiness',
        [
            'Prepare the site for ad traffic.',
            'Confirm tracking and lead flow are in place.',
            'Make landing pages clear and conversion-focused.',
        ],
        '#5C6F8A',
    ),
    (
        'Day 9',
        'Final testing',
        [
            'Test the main pages on mobile and desktop.',
            'Test forms, WhatsApp, telephone links, and other contact actions.',
            'Check for broken links, layout issues, and confirmation messages.',
        ],
        '#1B2B49',
    ),
    (
        'Day 10',
        'Final review and launch support',
        [
            'Do a final quality check before handoff.',
            'Confirm the site is ready to launch.',
            'Support the launch and immediate post-launch checks.',
        ],
        '#8C8FA3',
    ),
]

TIMELINE_ROWS = [
    ('Access review', 1, 2, '#1B8C8B', 'Confirm access, scope, and priorities'),
    ('Security fixes', 2, 4, '#B24A4A', 'Fix urgent security items'),
    ('Content cleanup', 3, 5, '#4E79A7', 'Remove duplicates and tighten wording'),
    ('Design + mobile', 3, 6, '#D7A643', 'Improve layout and responsive behavior'),
    ('SEO basics', 5, 7, '#6B5B95', 'Titles, headings, redirects, and metadata'),
    ('Performance', 6, 8, '#2E7D5B', 'Image compression and speed fixes'),
    ('Forms + tracking', 4, 9, '#009688', 'Secure forms and confirm tracking'),
    ('QA + launch prep', 8, 10, '#1B2B49', 'Cross-device testing and launch readiness'),
    ('Launch support', 10, 10, '#5C6F8A', 'Final check and immediate post-launch support'),
]


def hexcolor(value: Any):
    if isinstance(value, str):
        if not value.startswith('#'):
            value = f'#{value}'
        return colors.HexColor(value)
    return value


def draw_paragraph(c: canvas.Canvas, text: str, x: float, y_top: float, width: float, style='BodyCopy', bullet_text: str | None = None) -> float:
    para = Paragraph(text, styles[style], bulletText=bullet_text)
    _, h = para.wrap(width, PAGE_H)
    para.drawOn(c, x, y_top - h)
    return h


def measure_paragraph(text: str, width: float, style='BodyCopy') -> float:
    para = Paragraph(text, styles[style])
    _, h = para.wrap(width, PAGE_H)
    return h


def draw_box(c: canvas.Canvas, x: float, y: float, w: float, h: float, fill=colors.white, stroke='#D8DEE9', radius=0, stroke_width=1):
    c.setFillColor(hexcolor(fill))
    c.setStrokeColor(hexcolor(stroke))
    c.setLineWidth(stroke_width)
    c.rect(x, y, w, h, fill=1, stroke=1)


def footer(c: canvas.Canvas, page_num: int, total_pages: int):
    y = 10 * mm
    c.setStrokeColor(hexcolor('#D8DEE9'))
    c.setLineWidth(0.5)
    c.line(M, 14 * mm, PAGE_W - M, 14 * mm)
    c.setFont('Helvetica', 8)
    c.setFillColor(hexcolor('#718096'))
    c.drawString(M, y, '3KG')
    c.linkURL('https://threekg.com', (M, y - 1, M + 14 * mm, y + 8), relative=0)
    c.drawString(M + 15 * mm, y, ' | SClinic client materials')
    c.drawRightString(PAGE_W - M, y, f'Page {page_num} of {total_pages}')


def title(c: canvas.Canvas, text: str, subtitle: str | None = None, dark_bg: bool = False, y_mm: float = 23, subtitle_y_mm: float = 29.8):
    c.setFont('Helvetica-Bold', 23)
    c.setFillColor(hexcolor('#FFFFFF' if dark_bg else '#132238'))
    c.drawString(M, PAGE_H - y_mm * mm, text)
    if subtitle:
        c.setFont('Helvetica', 11)
        c.setFillColor(hexcolor('#DCE6F3' if dark_bg else '#4A5668'))
        c.drawString(M, PAGE_H - subtitle_y_mm * mm, subtitle)


def card(c: canvas.Canvas, x: float, y: float, w: float, h: float, day: str, heading: str, bullets: list[str], accent: str):
    draw_box(c, x, y, w, h, fill=colors.white, stroke='#D8DEE9', radius=12)
    c.setFillColor(hexcolor(accent))
    c.roundRect(x + 7, y + h - 14, 26 * mm, 8, 4, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(x + 10, y + h - 11.2, day)
    draw_paragraph(c, heading, x + 8, y + h - 20, w - 16, 'CardTitle')
    cur = y + h - 31
    for bullet in bullets:
        bh = draw_paragraph(c, f'• {bullet}', x + 8, cur, w - 16, 'BodySmall')
        cur -= bh + 1.2 * mm


def draw_task_entry(c: canvas.Canvas, x: float, y_top: float, w: float, index: int, heading: str, bullets: list[str]) -> float:
    summary = ' '.join(bullets)
    text = f'<b>{index}. {heading}</b> {summary}'
    h = draw_paragraph(c, text, x, y_top, w, 'BodyCopy')
    return h


def page1(c: canvas.Canvas):
    c.setFillColor(hexcolor('#F5F7FA'))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(hexcolor('#132238'))
    c.rect(0, PAGE_H - TOP_BAND_H, PAGE_W, TOP_BAND_H, fill=1, stroke=0)
    c.setFillColor(hexcolor('#D7A643'))
    c.rect(0, PAGE_H - TOP_BAND_H, PAGE_W, 5, fill=1, stroke=0)
    title(c, 'Phase 1 task list', 'Detailed tasks for the 2-week UAE website plan', dark_bg=False, y_mm=25, subtitle_y_mm=31.5)
    draw_paragraph(c, 'The tasks below are arranged to overlap where possible so the launch target stays inside the two-week window.', M, PAGE_H - 39 * mm, PAGE_W - 2 * M, 'BodyCopy')

    cols = [TASKS[:5], TASKS[5:]]
    gap_x = 10 * mm
    col_w = (PAGE_W - 2 * M - gap_x) / 2
    x_positions = [M, M + col_w + gap_x]
    start_y = PAGE_H - 52 * mm
    block_gap = 3.8 * mm

    for col_idx, items in enumerate(cols):
        cur_y = start_y
        for item_idx, (_, heading, bullets, _) in enumerate(items, start=1 + col_idx * 5):
            h = draw_task_entry(c, x_positions[col_idx], cur_y, col_w, item_idx, heading, bullets)
            cur_y -= h + block_gap

    footer(c, 1, 2)


def page2(c: canvas.Canvas):
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    title(c, 'Action Plan timeline')
    c.setFillColor(hexcolor('#4A5668'))
    c.setFont('Helvetica', 9.2)
    c.drawString(M, PAGE_H - 31 * mm, 'Overlapping tasks are intentional so the launch target stays inside the 2-week window.')

    left = M
    label_w = 48 * mm
    grid_x = left + label_w
    grid_w = PAGE_W - M - grid_x
    cols = 10
    col_w = grid_w / cols
    row_h = 12 * mm
    start_y = PAGE_H - 40 * mm

    box_y = 40 * mm
    box_h = 218 * mm
    draw_box(c, M, box_y, PAGE_W - 2 * M, box_h, fill=colors.white, stroke='#D8DEE9', radius=12)

    header_y = start_y
    c.setFillColor(hexcolor('#F5F7FA'))
    c.rect(grid_x, header_y - 8 * mm, grid_w, 8 * mm, fill=1, stroke=0)
    c.setStrokeColor(hexcolor('#D8DEE9'))
    for i in range(cols + 1):
        x = grid_x + i * col_w
        c.line(x, box_y, x, header_y)
        if i < cols:
            c.setFillColor(hexcolor('#1B2B49'))
            c.setFont('Helvetica-Bold', 8.2)
            c.drawCentredString(x + col_w / 2, header_y - 5.5 * mm, f'Day {i+1}')

    row_specs = []
    for label, start_day, end_day, color, note in TIMELINE_ROWS:
        combined = f'<b>{label}</b><br/>{note}'
        content_h = measure_paragraph(combined, label_w - 12, 'BodySmall')
        row_h = max(12 * mm, content_h + 6 * mm)
        row_specs.append((label, start_day, end_day, color, note, combined, row_h))

    cursor = header_y - 8 * mm - 2.5 * mm
    for idx, (label, start_day, end_day, color, note, combined, row_h) in enumerate(row_specs):
        row_top = cursor
        row_bottom = row_top - row_h
        c.setStrokeColor(hexcolor('#E5EAF0'))
        c.line(left, row_top, PAGE_W - M, row_top)
        c.line(left, row_bottom, PAGE_W - M, row_bottom)

        label_para = Paragraph(combined, styles['BodySmall'])
        label_para.wrapOn(c, label_w - 12, row_h)
        label_para.drawOn(c, left + 6, row_bottom + row_h - measure_paragraph(combined, label_w - 12, 'BodySmall'))

        bar_x = grid_x + (start_day - 1) * col_w + 1.2
        bar_w = (end_day - start_day + 1) * col_w - 2.4
        if bar_w < 6:
            bar_w = 6
        c.setFillColor(hexcolor(color))
        c.roundRect(bar_x, row_bottom + 2.0 * mm, bar_w, row_h - 4.0 * mm, 4, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont('Helvetica-Bold', 7.3)
        tag = f'D{start_day}–D{end_day}' if start_day != end_day else f'D{start_day}'
        c.drawString(bar_x + 3, row_bottom + 4.3 * mm, tag)

        cursor = row_bottom

    c.setStrokeColor(hexcolor('#D8DEE9'))
    c.line(left, box_y, PAGE_W - M, box_y)

    c.setFillColor(hexcolor('#F5F7FA'))
    c.roundRect(M, 20 * mm, PAGE_W - 2 * M, 16 * mm, 8, fill=1, stroke=0)
    c.setFillColor(hexcolor('#4A5668'))
    c.setFont('Helvetica', 8.6)
    c.drawString(M + 8, 27.5 * mm, 'Overlapping workstreams keep content, design, SEO, and testing moving in parallel instead of waiting on one another.')

    footer(c, 2, 2)


def build(path: Path = PDF_PATH):
    c = canvas.Canvas(str(path), pagesize=A4)
    page1(c); c.showPage()
    page2(c); c.showPage()
    c.save()


if __name__ == '__main__':
    build()
