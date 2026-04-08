from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

doc = SimpleDocTemplate(
    "/home/user/Indicator/BOS_CHoCH_Guide.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title', parent=styles['Title'],
    fontSize=20, textColor=colors.HexColor('#FFD700'),
    backColor=colors.HexColor('#1a1a2e'), alignment=TA_CENTER,
    spaceAfter=6, spaceBefore=6, leading=26,
    borderPad=10)

subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
    fontSize=11, textColor=colors.HexColor('#aaaaaa'),
    alignment=TA_CENTER, spaceAfter=12)

h1_style = ParagraphStyle('H1', parent=styles['Heading1'],
    fontSize=13, textColor=colors.HexColor('#FFD700'),
    backColor=colors.HexColor('#16213e'),
    spaceBefore=14, spaceAfter=6, leading=18,
    borderPad=6, leftIndent=0)

h2_style = ParagraphStyle('H2', parent=styles['Heading2'],
    fontSize=11, textColor=colors.HexColor('#00d4ff'),
    spaceBefore=10, spaceAfter=4, leading=16)

body_style = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=9.5, textColor=colors.HexColor('#dddddd'),
    spaceAfter=4, leading=14,
    backColor=colors.HexColor('#0f0f1a'))

note_style = ParagraphStyle('Note', parent=styles['Normal'],
    fontSize=9, textColor=colors.HexColor('#ffffff'),
    backColor=colors.HexColor('#1e3a1e'),
    spaceAfter=6, leading=13, leftIndent=10, rightIndent=10,
    borderPad=8)

warn_style = ParagraphStyle('Warn', parent=styles['Normal'],
    fontSize=9, textColor=colors.HexColor('#ffffff'),
    backColor=colors.HexColor('#3a1e1e'),
    spaceAfter=6, leading=13, leftIndent=10, rightIndent=10,
    borderPad=8)

def section_header(text):
    return Paragraph(text, h1_style)

def sub_header(text):
    return Paragraph(text, h2_style)

def body(text):
    return Paragraph(text, body_style)

def note(text):
    return Paragraph(text, note_style)

def warn(text):
    return Paragraph(text, warn_style)

def spacer(h=0.3):
    return Spacer(1, h*cm)

def hr():
    return HRFlowable(width="100%", thickness=1, color=colors.HexColor('#333366'), spaceAfter=6)

# ── TABLE STYLE HELPERS ────────────────────────────────────────────────────────
dark_bg   = colors.HexColor('#1a1a2e')
mid_bg    = colors.HexColor('#16213e')
gold      = colors.HexColor('#FFD700')
cyan      = colors.HexColor('#00d4ff')
green_c   = colors.HexColor('#00ff88')
red_c     = colors.HexColor('#ff4444')
gray_c    = colors.HexColor('#888888')
white_c   = colors.HexColor('#ffffff')

def base_table_style():
    return [
        ('BACKGROUND', (0,0), (-1,0), mid_bg),
        ('TEXTCOLOR',  (0,0), (-1,0), gold),
        ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0,0), (-1,0), 9),
        ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#333366')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [dark_bg, mid_bg]),
        ('TEXTCOLOR',  (0,1), (-1,-1), white_c),
        ('FONTSIZE',   (0,1), (-1,-1), 8.5),
        ('FONTNAME',   (0,1), (-1,-1), 'Helvetica'),
        ('ROWHEIGHT',  (0,0), (-1,-1), 18),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]

# ══════════════════════════════════════════════════════════════════════════════
story = []

# COVER
story.append(spacer(1.5))
story.append(Paragraph("BOS CHoCH Gold Scalper", title_style))
story.append(Paragraph("XAUUSD 15-Minute Indicator — User Guide", subtitle_style))
story.append(spacer(0.3))
story.append(hr())
story.append(body("Platform: TradingView &nbsp;|&nbsp; Timeframe: 15 Minutes &nbsp;|&nbsp; Asset: XAUUSD (Gold)"))
story.append(hr())
story.append(spacer(1))

# ── STEP 1 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 1 — Swing High / Low Detection"))
story.append(spacer(0.2))
story.append(body(
    "Ang indicator ay awtomatikong naghahanap ng mga <b>pivot points</b> — "
    "ang pinakamataas (Swing High) at pinakamababa (Swing Low) ng presyo "
    "sa loob ng 5 candles bawat side. Ito ang pundasyon ng lahat ng "
    "structure analysis."
))
story.append(spacer(0.2))

t1 = Table([
    ["Label", "Ibig Sabihin", "Kulay"],
    ["HH",    "Higher High — mas mataas na swing high",  "Teal"],
    ["HL",    "Higher Low — mas mataas na swing low",    "Teal"],
    ["LH",    "Lower High — mas mababa na swing high",   "Orange"],
    ["LL",    "Lower Low — mas mababa na swing low",     "Orange"],
], colWidths=[2.5*cm, 10*cm, 3.5*cm])
ts = base_table_style()
ts += [
    ('TEXTCOLOR', (2,1), (2,2), colors.HexColor('#00d4ff')),
    ('TEXTCOLOR', (2,3), (2,4), colors.HexColor('#FFA500')),
]
t1.setStyle(TableStyle(ts))
story.append(t1)
story.append(spacer(0.4))

# ── STEP 2 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 2 — Market Structure (BOS at CHoCH)"))
story.append(spacer(0.2))
story.append(sub_header("BOS — Break of Structure"))
story.append(body(
    "Nangyayari ang BOS kapag ang <b>close price</b> ay lumampas sa pinakabagong "
    "swing high (Bullish BOS) o bumagsak sa ibaba ng swing low (Bearish BOS). "
    "Ipinapakita ito ng <b>blue 'BOS' label</b> sa chart."
))
story.append(spacer(0.2))
story.append(sub_header("CHoCH — Change of Character"))
story.append(body(
    "Espesyal na uri ng BOS. Nangyayari kapag <b>nagbago ang direksyon ng trend</b>:"
))
story.append(spacer(0.1))
t2 = Table([
    ["Event",       "Kondisyon",                          "Label sa Chart"],
    ["CHoCH Bull",  "Bearish bias dati → Bullish BOS",   "Lime Green 'CHoCH'"],
    ["CHoCH Bear",  "Bullish bias dati → Bearish BOS",   "Red 'CHoCH'"],
], colWidths=[3.5*cm, 8.5*cm, 4*cm])
ts2 = base_table_style()
ts2 += [
    ('TEXTCOLOR', (2,1), (2,1), green_c),
    ('TEXTCOLOR', (2,2), (2,2), red_c),
]
t2.setStyle(TableStyle(ts2))
story.append(t2)
story.append(spacer(0.2))
story.append(note("IMPORTANTENG TANDAAN: Ang CHoCH ang pinaka-importanteng signal — ito ang nagpapalit ng bias (direksyon ng trade)."))
story.append(spacer(0.4))

# ── STEP 3 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 3 — Bias (Trading Direction)"))
story.append(spacer(0.2))
story.append(body(
    "Pagkatapos ng BOS o CHoCH, awtomatikong nagse-set ang indicator ng <b>BIAS</b> "
    "na siyang magsasabi kung anong direksyon pwede kang pumasok."
))
story.append(spacer(0.1))
t3 = Table([
    ["BIAS Value",   "Ibig Sabihin",        "Pwedeng Trade"],
    ["Bullish",      "Pataas ang trend",    "BUY lang"],
    ["Bearish",      "Pababa ang trend",    "SELL lang"],
    ["Neutral",      "Walang BOS pa",       "WAIT — huwag pumasok"],
], colWidths=[3.5*cm, 6.5*cm, 6*cm])
ts3 = base_table_style()
ts3 += [
    ('TEXTCOLOR', (0,1), (0,1), green_c),
    ('TEXTCOLOR', (0,2), (0,2), red_c),
    ('TEXTCOLOR', (0,3), (0,3), gray_c),
]
t3.setStyle(TableStyle(ts3))
story.append(t3)
story.append(spacer(0.4))

# ── STEP 4 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 4 — Supply at Demand Zones (mga Kahon sa Chart)"))
story.append(spacer(0.2))
story.append(body(
    "Awtomatikong nagdadrawing ang indicator ng mga zona batay sa swing points:"
))
story.append(spacer(0.1))
t4 = Table([
    ["Zone",          "Kulay",       "Ibig Sabihin"],
    ["Supply Zone",   "Red Box",     "Lugar ng potential na SELL — galing sa swing highs"],
    ["Demand Zone",   "Green Box",   "Lugar ng potential na BUY — galing sa swing lows"],
], colWidths=[3.5*cm, 3*cm, 9.5*cm])
ts4 = base_table_style()
ts4 += [
    ('TEXTCOLOR', (1,1), (1,1), red_c),
    ('TEXTCOLOR', (1,2), (1,2), green_c),
]
t4.setStyle(TableStyle(ts4))
story.append(t4)
story.append(spacer(0.2))
story.append(body(
    "Ang indicator ay nag-che-check kung ang kasalukuyang candle ay "
    "<b>nasa loob ng zone</b> bago mag-signal. Hindi mag-ffire ng BUY kung "
    "hindi ka malapit sa Demand Zone, at hindi mag-ffire ng SELL kung hindi "
    "ka malapit sa Supply Zone."
))
story.append(spacer(0.4))

# ── STEP 5 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 5 — AMD Phase (Accumulation / Manipulation / Distribution)"))
story.append(spacer(0.2))
story.append(body(
    "Tinitingnan ng indicator ang <b>range ng presyo sa nakaraang 20 candles</b> "
    "kumpara sa ATR (Average True Range) para malaman kung anong phase ng merkado:"
))
story.append(spacer(0.1))
t5 = Table([
    ["Phase",          "Kondisyon",           "Kulay",  "Pwede bang Mag-trade?"],
    ["ACCUMULATION",   "Range < 2.5x ATR",    "Blue",   "HINDI — NO TRADE"],
    ["MANIPULATION",   "Range 2.5x–5x ATR",   "Red",    "HINDI — NO TRADE"],
    ["DISTRIBUTION",   "Range > 5x ATR",      "Green",  "OO — Pwede"],
], colWidths=[3.5*cm, 4*cm, 2.5*cm, 6*cm])
ts5 = base_table_style()
ts5 += [
    ('TEXTCOLOR', (0,1), (0,1), colors.HexColor('#4444ff')),
    ('TEXTCOLOR', (0,2), (0,2), red_c),
    ('TEXTCOLOR', (0,3), (0,3), green_c),
    ('TEXTCOLOR', (3,1), (3,2), red_c),
    ('TEXTCOLOR', (3,3), (3,3), green_c),
]
t5.setStyle(TableStyle(ts5))
story.append(t5)
story.append(spacer(0.2))
story.append(warn("BABALA: Kapag MANIPULATION o ACCUMULATION ang Phase, ang SIGNAL ay magiging 'NO TRADE' kahit pumasa pa ang ibang filters."))
story.append(spacer(0.4))

# ── STEP 6 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 6 — Mga Filter na Kailangan Pumasa para Mag-Signal"))
story.append(spacer(0.2))
story.append(body("Kailangan ng <b>lahat</b> ng sumusunod na kondisyon para lumabas ang BUY o SELL signal:"))
story.append(spacer(0.1))

t6 = Table([
    ["#", "Filter",    "Para sa BUY",                  "Para sa SELL"],
    ["1", "BIAS",      "Bullish",                       "Bearish"],
    ["2", "EMA Trend", "e5 > e20 > e50 (Bull Stack)",  "e5 < e20 < e50 (Bear Stack)"],
    ["3", "RSI",       "50 hanggang 70",                "30 hanggang 50"],
    ["4", "MACD",      "Histogram positive, tumataas",  "Histogram negative, bumababa"],
    ["5", "Zone",      "Candle malapit sa Demand Zone", "Candle malapit sa Supply Zone"],
    ["6", "Candle",    "Bullish (close > open)",        "Bearish (close < open)"],
    ["7", "Volume",    "Above average volume",          "Above average volume"],
    ["8", "AMD Phase", "Distribution lang",             "Distribution lang"],
    ["9", "Cooldown",  "5+ bars mula sa huli signal",   "5+ bars mula sa huli signal"],
], colWidths=[0.7*cm, 3*cm, 6.7*cm, 5.6*cm])
ts6 = base_table_style()
ts6 += [
    ('TEXTCOLOR', (2,1), (2,-1), green_c),
    ('TEXTCOLOR', (3,1), (3,-1), red_c),
    ('FONTSIZE',  (0,1), (-1,-1), 8),
]
t6.setStyle(TableStyle(ts6))
story.append(t6)
story.append(spacer(0.4))

# ── STEP 7 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 7 — Risk Management (SL / TP)"))
story.append(spacer(0.2))
story.append(body(
    "Kapag lumabas ang signal, awtomatikong kino-compute ng indicator ang "
    "mga levels batay sa <b>ATR (Average True Range)</b>:"
))
story.append(spacer(0.1))

t7 = Table([
    ["Level",   "Formula",              "Multiplier"],
    ["SL",      "Entry ± ATR × 1.5",   "1.5x ATR"],
    ["TP1",     "Entry ± ATR × 2.0",   "2.0x ATR"],
    ["TP2",     "Entry ± ATR × 3.0",   "3.0x ATR"],
    ["R:R",     "TP1 distance / SL distance", "~1.33"],
], colWidths=[2.5*cm, 7*cm, 6.5*cm])
ts7 = base_table_style()
ts7 += [
    ('TEXTCOLOR', (0,1), (0,1), red_c),
    ('TEXTCOLOR', (0,2), (0,3), green_c),
]
t7.setStyle(TableStyle(ts7))
story.append(t7)
story.append(spacer(0.2))
story.append(body(
    "Sa chart, makikita ang mga <b>dashed lines</b> — pula para sa SL, "
    "berde para sa TP1 at TP2. May price labels din para sa exact na values."
))
story.append(spacer(0.4))

# ── STEP 8 ────────────────────────────────────────────────────────────────────
story.append(section_header("STEP 8 — Dashboard (Top Right ng Chart)"))
story.append(spacer(0.2))
story.append(body(
    "Ang dashboard ay nagpapakita ng <b>real-time na estado</b> ng lahat ng filters. "
    "Ito ang pinaka-madaling paraan para malaman kung pwede ka nang pumasok."
))
story.append(spacer(0.1))

t8 = Table([
    ["Row",        "Nagpapakita ng..."],
    ["SIGNAL",     "BUY / SELL / NO TRADE / WAIT — ang pinaka-importanteng row"],
    ["PHASE",      "Accumulation / Manipulation / Distribution"],
    ["BIAS",       "Bullish / Bearish / Neutral — direksyon ng market structure"],
    ["TREND",      "Bull Stack / Bear Stack / Mixed — EMA alignment"],
    ["MACD",       "Bullish / Bearish / Bull Cross / Bear Cross"],
    ["RSI",        "Kasalukuyang RSI value (50–70 para BUY, 30–50 para SELL)"],
    ["VOLUME",     "Above Avg / Below Avg"],
    ["ATR",        "Kasalukuyang ATR value — ginagamit para sa SL/TP computation"],
    ["ENTRY",      "Entry price ng pinakabagong signal"],
    ["SL",         "Stop Loss level ng pinakabagong signal"],
    ["TP1",        "Take Profit 1 level (2x ATR)"],
    ["TP2",        "Take Profit 2 level (3x ATR)"],
    ["R:R",        "Risk-to-Reward ratio"],
    ["STRUCTURE",  "Pinakabagong BOS o CHoCH event"],
], colWidths=[3*cm, 13*cm])
ts8 = base_table_style()
ts8 += [
    ('FONTNAME',  (0,1), (0,1), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0,1), (0,1), gold),
    ('BACKGROUND',(0,1), (-1,1), colors.HexColor('#2a2a0e')),
]
t8.setStyle(TableStyle(ts8))
story.append(t8)
story.append(spacer(0.4))

# ── STEP 9 — HOW TO ENTER ─────────────────────────────────────────────────────
story.append(section_header("STEP 9 — Paano Malaman Kung Oras Na Para Pumasok?"))
story.append(spacer(0.2))

story.append(sub_header("Option A — Manual Monitoring"))
story.append(body(
    "Panoorin ang <b>SIGNAL row</b> ng dashboard. "
    "Kapag naging <b>BUY</b> (green) o <b>SELL</b> (red) na, "
    "pumasok ka sa <b>susunod na candle close</b>."
))
story.append(spacer(0.2))

story.append(sub_header("Option B — TradingView Alert (Inirekomenda)"))
story.append(body("I-setup ang alert para hindi mo na kailangang laging nakamasid sa screen:"))
story.append(spacer(0.1))
steps_data = [
    ["1", "Sa TradingView, i-click ang 'Alerts' (bell icon)"],
    ["2", "I-click ang 'Create Alert'"],
    ["3", "Sa Condition, piliin ang 'BOS CHoCH Gold Scalper' indicator"],
    ["4", "Piliin ang 'BUY Signal' o 'SELL Signal'"],
    ["5", "I-set ang notification (email, app, o SMS)"],
    ["6", "I-save ang alert"],
]
t9 = Table(steps_data, colWidths=[1*cm, 15*cm])
ts9 = [
    ('BACKGROUND', (0,0), (-1,-1), dark_bg),
    ('TEXTCOLOR',  (0,0), (0,-1), gold),
    ('TEXTCOLOR',  (1,0), (1,-1), white_c),
    ('FONTNAME',   (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0), (-1,-1), 9),
    ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#333366')),
    ('ALIGN',      (0,0), (0,-1), 'CENTER'),
    ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0), (-1,-1), 18),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]
t9 = Table(steps_data, colWidths=[1*cm, 15*cm])
t9.setStyle(TableStyle(ts9))
story.append(t9)
story.append(spacer(0.3))
story.append(note("TIP: I-set ng 'Once Per Bar Close' ang alert frequency para hindi mag-spam ng notifications sa loob ng isang candle."))
story.append(spacer(0.4))

# ── QUICK REFERENCE ───────────────────────────────────────────────────────────
story.append(section_header("QUICK REFERENCE — Signal Checklist"))
story.append(spacer(0.2))

t10 = Table([
    ["",          "BUY Signal",           "SELL Signal"],
    ["BIAS",      "Bullish",              "Bearish"],
    ["TREND",     "Bull Stack",           "Bear Stack"],
    ["MACD",      "Positive + Bullish",   "Negative + Bearish"],
    ["RSI",       "50 – 70",              "30 – 50"],
    ["VOLUME",    "Above Avg",            "Above Avg"],
    ["PHASE",     "Distribution",         "Distribution"],
    ["ZONE",      "Nasa Demand Zone",     "Nasa Supply Zone"],
    ["CANDLE",    "Bullish candle",       "Bearish candle"],
    ["DASHBOARD", "SIGNAL = BUY (green)", "SIGNAL = SELL (red)"],
], colWidths=[3*cm, 7*cm, 6*cm])
ts10 = base_table_style()
ts10 += [
    ('TEXTCOLOR', (1,1), (1,-1), green_c),
    ('TEXTCOLOR', (2,1), (2,-1), red_c),
    ('FONTNAME',  (0,0), (-1,0), 'Helvetica-Bold'),
]
t10.setStyle(TableStyle(ts10))
story.append(t10)
story.append(spacer(0.5))

story.append(hr())
story.append(Paragraph(
    "BOS CHoCH Gold Scalper — XAUUSD 15m &nbsp;|&nbsp; Para sa educational purposes lamang.",
    ParagraphStyle('Footer', parent=styles['Normal'],
        fontSize=7.5, textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER)
))

doc.build(story)
print("PDF generated: /home/user/Indicator/BOS_CHoCH_Guide.pdf")
