from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Avoid the Hermes venv Pillow build interfering with reportlab.
sys.path = [p for p in sys.path if '/.hermes/hermes-agent/venv/' not in p]

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas

BASE = Path('/Users/loay/Desktop/3kg/SClinic')
OUT = BASE / 'Docs & Planing' / 'deliverables'
OUT.mkdir(parents=True, exist_ok=True)
PDF_PATH = OUT / 'SClinic_Phase2_Website_Redesign_Brand_Identity_Plan.pdf'

PAGE_W, PAGE_H = A4
M = 18 * mm
TOP_BAND_H = 18 * mm

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
    fontSize=9.7,
    leading=12.1,
    textColor=colors.HexColor('#4A5668'),
    spaceAfter=1.5,
))
styles.add(ParagraphStyle(
    name='BodySmall',
    parent=styles['BodyText'],
    fontName='Helvetica',
    fontSize=8.6,
    leading=10.7,
    textColor=colors.HexColor('#718096'),
    spaceAfter=1,
))
styles.add(ParagraphStyle(
    name='CardTitle',
    parent=styles['BodyText'],
    fontName='Helvetica-Bold',
    fontSize=12.2,
    leading=14,
    textColor=colors.HexColor('#1B2B49'),
))

PHASE2_STRATEGY = [
    'UAE-first digital experience, not a copy of the Turkish site',
    'premium clinic positioning with stronger trust and clarity',
    'designed to adapt to other markets later if needed',
]

STRATEGIC_QUESTIONS = [
    'Who are the primary patient segments?',
    'What is the clearest value proposition for the UAE website?',
    'Which treatments and pages need priority visibility?',
    'How should S’CLINIC differentiate itself in Dubai?',
    'What should the website communicate beyond individual treatments?',
]

CORE_SCOPE = {
    'Brand identity refresh': [
        'logo direction if needed',
        'color palette',
        'typography system',
        'spacing and layout rules',
        'icon style',
        'visual tone and image style',
    ],
    'Website redesign': [
        'homepage redesign',
        'internal page redesign',
        'service or treatment page templates',
        'contact and conversion pages',
        'header, footer, and navigation updates',
        'mobile-first layout improvements',
        'clearer patient journey flow',
        'premium clinic storytelling sections',
    ],
    'Design system': [
        'reusable buttons',
        'cards and content blocks',
        'section patterns',
        'CTA styles',
        'forms and input styles',
        'trust and credibility sections',
    ],
    'Content presentation': [
        'clearer hierarchy',
        'better readability',
        'stronger calls to action',
        'better visual balance',
        'less clutter, more breathing room',
    ],
}

OPTIONAL_FEATURES = [
    'additional landing pages',
    'blog or content hub',
    'advanced SEO content expansion',
    'appointment or booking enhancements',
    'WhatsApp integration improvements',
    'CRM integration',
    'booking management dashboard',
    'automated patient communication',
    'AI-assisted enquiry filtering',
    'interactive components',
    'multilingual extensions',
    'Arabic readiness or future Arabic expansion',
    'testimonial or before/after sections',
    'animation or motion enhancements',
    'special campaign pages',
    'e-commerce functionality',
    'scalable international rollout templates',
]

PLATFORM_NOTES = {
    'Platform questions': [
        'Should the site remain on WordPress or move to another platform?',
        'What setup best supports scalability and maintainability?',
        'How will treatments, doctors, locations, and markets be structured in the CMS?',
        'What staging, testing, and deployment process should be used?',
    ],
    'Integration considerations': [
        'existing booking platform connection',
        'custom booking integration',
        'WhatsApp communication flow',
        'CRM linkage',
        'analytics and tracking setup',
        'security, backup, and maintenance requirements',
    ],
    'Feasibility note': [
        'The more advanced booking and patient-communication ideas should be treated as separate feasibility items before they become part of the main redesign scope.',
    ],
}

WORK_PHASES = {
    'Phase 2.1: Discovery and direction': [
        'review the current website and brand',
        'define what should change',
        'establish visual goals',
        'identify the key pages that must be redesigned first',
    ],
    'Phase 2.2: Brand identity development': [
        'create the visual direction',
        'define color, typography, and style rules',
        'approve the brand look and feel',
    ],
    'Phase 2.3: UX and page structure': [
        'map the new page hierarchy',
        'define section flow for main pages',
        'plan navigation and CTA placement',
    ],
    'Phase 2.4: High-fidelity design': [
        'design the main pages',
        'finalize component styles',
        'make the layout consistent across desktop and mobile',
    ],
    'Phase 2.5: Handoff or build preparation': [
        'organize assets',
        'document style rules',
        'prepare the redesign for implementation',
    ],
}

DELIVERABLES = [
    'brand direction summary',
    'color palette',
    'typography guidance',
    'redesigned homepage concept',
    'redesigned internal page concepts',
    'reusable component patterns',
    'UI style references',
    'responsive design direction',
    'final design handoff notes',
    'platform direction recommendation',
    'separate feasibility note for booking, WhatsApp, CRM, and AI-related ideas',
]

SUCCESS = [
    'the website looks clearly redesigned',
    'the brand feels more consistent and refined',
    'the structure is easier to navigate',
    'key actions stand out better',
    'the design is mobile-friendly',
    'the identity feels ready for future growth',
    'optional items remain separate from the core redesign scope',
]

PAGE1_SECTIONS = [
    ('Phase 2 strategy', PHASE2_STRATEGY, '#1B8C8B', 1),
    ('Strategic questions', STRATEGIC_QUESTIONS, '#D7A643', 1),
    (
        'Core scope',
        [
            'Brand identity refresh: logo direction, color palette, typography, spacing, icon style, visual tone, and image style',
            'Website redesign: homepage, internal pages, treatment templates, contact pages, navigation, and mobile-first improvements',
            'Design system: reusable buttons, cards, section patterns, CTA styles, forms, and trust sections',
            'Content presentation: clearer hierarchy, better readability, stronger calls to action, better balance, and less clutter',
        ],
        '#4E79A7',
        2,
    ),
    (
        'Design system',
        [
            'reusable buttons',
            'cards and content blocks',
            'section patterns',
            'CTA styles',
            'forms and input styles',
            'trust and credibility sections',
        ],
        '#6B5B95',
        2,
    ),
    (
        'Brand identity direction',
        [
            'visual personality, tone of voice, color system, typography rules, image style, icon style, and spacing rules',
            'goal: a clear, recognizable, and more professional clinic presence',
        ],
        '#2E7D5B',
        1,
    ),
    (
        'What this phase should achieve',
        [
            'modern and premium look',
            'medically trustworthy feel',
            'clearer brand communication',
            'easier-to-find key actions',
        ],
        '#009688',
        2,
    ),
]

PAGE2_SECTIONS = [
    ('Optional features', OPTIONAL_FEATURES, '#1B8C8B', 2),
    (
        'Platform and development considerations',
        [
            'Should the site remain on WordPress or move to another platform?',
            'What setup best supports scalability and maintainability?',
            'How will treatments, doctors, locations, and markets be structured in the CMS?',
            'What staging, testing, and deployment process should be used?',
            'existing booking platform connection, custom booking integration, WhatsApp communication flow, CRM linkage, analytics and tracking, security, backup, and maintenance',
        ],
        '#D7A643',
        1,
    ),
    (
        'Recommended work phases',
        [
            'discovery and direction',
            'brand identity development',
            'UX and page structure',
            'high-fidelity design',
            'handoff or build preparation',
        ],
        '#4E79A7',
        1,
    ),
    ('Deliverables', DELIVERABLES, '#6B5B95', 2),
    ('Success criteria', SUCCESS, '#2E7D5B', 1),
]


def hexcolor(value: Any):
    if isinstance(value, str):
        if not value.startswith('#'):
            value = f'#{value}'
        return colors.HexColor(value)
    return value


def draw_paragraph(c: canvas.Canvas, text: str, x: float, y_top: float, width: float, style='BodyCopy') -> float:
    para = Paragraph(text, styles[style])
    _, h = para.wrap(width, PAGE_H)
    para.drawOn(c, x, y_top - h)
    return h


def measure_paragraph(text: str, width: float, style='BodyCopy') -> float:
    para = Paragraph(text, styles[style])
    _, h = para.wrap(width, PAGE_H)
    return h


def draw_box(c: canvas.Canvas, x: float, y: float, w: float, h: float, fill=colors.white, stroke='#D8DEE9', stroke_width=1):
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


def title(c: canvas.Canvas, text: str, subtitle: str | None = None, dark_bg: bool = False, y_mm: float = 23, subtitle_y_mm: float = 29.6):
    c.setFont('Helvetica-Bold', 22)
    c.setFillColor(hexcolor('#FFFFFF' if dark_bg else '#132238'))
    c.drawString(M, PAGE_H - y_mm * mm, text)
    if subtitle:
        c.setFont('Helvetica', 11)
        c.setFillColor(hexcolor('#DCE6F3' if dark_bg else '#4A5668'))
        c.drawString(M, PAGE_H - subtitle_y_mm * mm, subtitle)


def card_height(lines: list[str], w: float, cols: int = 1) -> float:
    content_w = w - 14
    if cols <= 1:
        content_h = bullet_list_height(lines, content_w, 'BodySmall')
    else:
        gap = 6 * mm
        col_w = (content_w - gap * (cols - 1)) / cols
        columns: list[list[str]] = [[] for _ in range(cols)]
        for idx, line in enumerate(lines):
            columns[idx % cols].append(line)
        content_h = max((bullet_list_height(col, col_w, 'BodySmall') for col in columns), default=0.0)
    return 24 * mm + content_h


def draw_card_auto(c: canvas.Canvas, x: float, y_top: float, w: float, heading: str, lines: list[str], accent: str, cols: int = 1) -> float:
    h = card_height(lines, w, cols)
    y = y_top - h
    draw_box(c, x, y, w, h, fill=colors.white, stroke='#D8DEE9')
    c.setFillColor(hexcolor(accent))
    c.rect(x, y + h - 5, 26 * mm, 5, fill=1, stroke=0)
    c.setFillColor(hexcolor('#1B2B49'))
    c.setFont('Helvetica-Bold', 12)
    c.drawString(x + 7, y + h - 18, heading)

    inner_x = x + 7
    inner_y = y + h - 25
    inner_w = w - 14
    if cols <= 1:
        cur_top = inner_y
        for idx, line in enumerate(lines):
            h_line = draw_paragraph(c, '• ' + line, inner_x, cur_top, inner_w, 'BodySmall')
            cur_top -= h_line + (1.1 * mm if idx < len(lines) - 1 else 0)
    else:
        gap = 6 * mm
        col_w = (inner_w - gap * (cols - 1)) / cols
        columns: list[list[str]] = [[] for _ in range(cols)]
        for idx, line in enumerate(lines):
            columns[idx % cols].append(line)
        for col_idx, col_lines in enumerate(columns):
            cur_top = inner_y
            x0 = inner_x + col_idx * (col_w + gap)
            for idx, line in enumerate(col_lines):
                h_line = draw_paragraph(c, '• ' + line, x0, cur_top, col_w, 'BodySmall')
                cur_top -= h_line + (0.7 * mm if idx < len(col_lines) - 1 else 0)

    return h


def bullet_list_height(lines: list[str], width: float, style='BodySmall'):
    total = 0.0
    for idx, line in enumerate(lines):
        total += measure_paragraph('• ' + line, width, style)
        if idx < len(lines) - 1:
            total += 1.1 * mm
    return total


def page1(c: canvas.Canvas):
    c.setFillColor(colors.HexColor('#F5F7FA'))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#132238'))
    c.rect(0, PAGE_H - TOP_BAND_H, PAGE_W, TOP_BAND_H, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#D7A643'))
    c.rect(0, PAGE_H - TOP_BAND_H, PAGE_W, 5, fill=1, stroke=0)

    title(c, 'Phase 2 website redesign plan', 'Website full redesign + brand identity', dark_bg=False, y_mm=25, subtitle_y_mm=31.5)
    draw_paragraph(c, 'Phase 2 focuses on a new digital experience for the UAE market: a complete redesign, refreshed brand identity, and a clearer conversion path. Optional features are separated from the core scope so the main redesign stays focused.', M, PAGE_H - 39 * mm, PAGE_W - 2 * M, 'BodyCopy')

    cur_top = PAGE_H - 57 * mm
    gap = 5 * mm
    full_w = PAGE_W - 2 * M
    for heading, lines, accent, cols in PAGE1_SECTIONS:
        h = draw_card_auto(c, M, cur_top, full_w, heading, lines, accent, cols=cols)
        cur_top -= h + gap

    footer(c, 1, 2)


def page2(c: canvas.Canvas):
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    title(c, 'Phase 2 implementation details')
    c.setFillColor(hexcolor('#4A5668'))
    c.setFont('Helvetica', 9.2)
    c.drawString(M, PAGE_H - 31 * mm, 'The redesign should keep the core scope focused while leaving advanced features for later evaluation.')

    cur_top = PAGE_H - 45 * mm
    gap = 5 * mm
    full_w = PAGE_W - 2 * M
    for heading, lines, accent, cols in PAGE2_SECTIONS:
        h = draw_card_auto(c, M, cur_top, full_w, heading, lines, accent, cols=cols)
        cur_top -= h + gap

    footer(c, 2, 2)


def build(path: Path = PDF_PATH):
    c = canvas.Canvas(str(path), pagesize=A4)
    page1(c)
    c.showPage()
    page2(c)
    c.showPage()
    c.save()


if __name__ == '__main__':
    build()
