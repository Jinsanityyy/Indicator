from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT

doc = SimpleDocTemplate(
    "/home/user/Indicator/Tradex_Algo_Guide.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

# ── COLORS ────────────────────────────────────────────────────────────────────
GOLD    = colors.HexColor('#FFD700')
CYAN    = colors.HexColor('#00d4ff')
GREEN   = colors.HexColor('#00ff88')
RED     = colors.HexColor('#ff4444')
GRAY    = colors.HexColor('#888888')
WHITE   = colors.HexColor('#ffffff')
DARK    = colors.HexColor('#0f0f1a')
MID     = colors.HexColor('#16213e')
DARKER  = colors.HexColor('#1a1a2e')
ORANGE  = colors.HexColor('#FFA500')
TEAL    = colors.HexColor('#00CED1')
PURPLE  = colors.HexColor('#9B59B6')

# ── STYLES ────────────────────────────────────────────────────────────────────
title_style = ParagraphStyle('Title',
    fontSize=22, textColor=GOLD,
    backColor=DARKER, alignment=TA_CENTER,
    spaceAfter=4, spaceBefore=4, leading=28, borderPad=10)

subtitle_style = ParagraphStyle('Subtitle',
    fontSize=10, textColor=GRAY,
    alignment=TA_CENTER, spaceAfter=10)

h1_style = ParagraphStyle('H1',
    fontSize=12, textColor=GOLD,
    backColor=MID, spaceBefore=12, spaceAfter=5,
    leading=18, borderPad=6, leftIndent=0)

h2_style = ParagraphStyle('H2',
    fontSize=10.5, textColor=CYAN,
    spaceBefore=8, spaceAfter=3, leading=15)

body_style = ParagraphStyle('Body',
    fontSize=9, textColor=WHITE,
    backColor=DARK, spaceAfter=4, leading=13)

note_style = ParagraphStyle('Note',
    fontSize=8.5, textColor=WHITE,
    backColor=colors.HexColor('#1e3a1e'),
    spaceAfter=5, leading=12,
    leftIndent=8, rightIndent=8, borderPad=6)

warn_style = ParagraphStyle('Warn',
    fontSize=8.5, textColor=WHITE,
    backColor=colors.HexColor('#3a1e1e'),
    spaceAfter=5, leading=12,
    leftIndent=8, rightIndent=8, borderPad=6)

tip_style = ParagraphStyle('Tip',
    fontSize=8.5, textColor=WHITE,
    backColor=colors.HexColor('#1a1a3e'),
    spaceAfter=5, leading=12,
    leftIndent=8, rightIndent=8, borderPad=6)

footer_style = ParagraphStyle('Footer',
    fontSize=7.5, textColor=GRAY, alignment=TA_CENTER)

def h1(t): return Paragraph(t, h1_style)
def h2(t): return Paragraph(t, h2_style)
def body(t): return Paragraph(t, body_style)
def note(t): return Paragraph(t, note_style)
def warn(t): return Paragraph(t, warn_style)
def tip(t):  return Paragraph(t, tip_style)
def sp(h=0.25): return Spacer(1, h*cm)
def hr(): return HRFlowable(width="100%", thickness=1, color=colors.HexColor('#333366'), spaceAfter=5)

def base_ts(extra=None):
    ts = [
        ('BACKGROUND', (0,0), (-1,0), MID),
        ('TEXTCOLOR',  (0,0), (-1,0), GOLD),
        ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0,0), (-1,0), 8.5),
        ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#333366')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [DARKER, MID]),
        ('TEXTCOLOR',  (0,1), (-1,-1), WHITE),
        ('FONTSIZE',   (0,1), (-1,-1), 8),
        ('FONTNAME',   (0,1), (-1,-1), 'Helvetica'),
        ('ROWHEIGHT',  (0,0), (-1,-1), 17),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]
    if extra:
        ts += extra
    return TableStyle(ts)

# ══════════════════════════════════════════════════════════════════════════════
story = []

# ── COVER ─────────────────────────────────────────────────────────────────────
story += [sp(1.5), Paragraph("TRADEX ALGO", title_style),
          Paragraph("Complete User Guide — XAUUSD Scalping Indicator", subtitle_style),
          sp(0.2), hr(),
          body("Platform: TradingView &nbsp;|&nbsp; Asset: XAUUSD (Gold) &nbsp;|&nbsp; Primary Timeframe: 5 Minutes"),
          hr(), sp(0.8)]

# ══════════════════════════════════════════════════════════════════════════════
# PART 1: HOW IT WORKS
# ══════════════════════════════════════════════════════════════════════════════
story += [h1("PART 1 — PAANO GUMAGANA ANG TRADEX ALGO"), sp(0.2)]

# Component 1: Supertrend
story += [h2("1. Supertrend (Core Engine)"), sp(0.1),
body("Ang Supertrend ang puso ng indicator. Ito ay nagco-compute ng ATR (Average True Range) para malaman kung saan ang trend."),
sp(0.1)]

t = Table([
    ["State",            "Kondisyon",                  "Candle Color"],
    ["Bullish (Up)",     "Presyo nasa ITAAS ng line",  "Green"],
    ["Bearish (Down)",   "Presyo nasa IBABA ng line",  "Red"],
], colWidths=[4*cm, 8*cm, 4*cm])
t.setStyle(base_ts([
    ('TEXTCOLOR', (2,1), (2,1), GREEN),
    ('TEXTCOLOR', (2,2), (2,2), RED),
]))
story += [t, sp(0.3)]

# Component 2: Cloud
story += [h2("2. Cloud Ribbon (EMA 9 / EMA 21)"), sp(0.1),
body("Ang purple/fuchsia ribbon ay ginawa mula sa dalawang EMA. Ito ang nagpapakita ng trend strength."),
sp(0.1)]

t2 = Table([
    ["Cloud Behavior",         "Ibig Sabihin"],
    ["Makapal, malakas kulay", "Malakas ang trend — ok pumasok"],
    ["Manipis, nagkukrus",     "Nagbabago ng direksyon — mag-ingat"],
    ["Flat at patag",          "Choppy/ranging — huwag pumasok"],
], colWidths=[6*cm, 10*cm])
t2.setStyle(base_ts())
story += [t2, sp(0.3)]

# Component 3: Background
story += [h2("3. Background Color"), sp(0.1),
body("Nagbibigay ng subtle na kulay sa buong chart para madaling makita ang overall trend."),
sp(0.1)]

t3 = Table([
    ["Background",   "Supertrend",   "Ibig Sabihin"],
    ["Teal tint",    "Bullish",      "BUY bias — trend pataas"],
    ["Purple tint",  "Bearish",      "SELL bias — trend pababa"],
], colWidths=[4*cm, 4*cm, 8*cm])
t3.setStyle(base_ts([
    ('TEXTCOLOR', (0,1), (0,1), TEAL),
    ('TEXTCOLOR', (0,2), (0,2), PURPLE),
]))
story += [t3, sp(0.3)]

# Component 4: Signals
story += [h2("4. BUY / SELL Signals"), sp(0.1),
body("Lalabas ang signal kapag <b>nagbago ang Supertrend direction</b> (flip). Isa sa pinaka-importanteng parte ng indicator."),
sp(0.1)]

t4 = Table([
    ["Signal",  "Kailan Lalabas",                     "Arrow"],
    ["BUY",     "Supertrend flip: Bearish → Bullish", "Green arrow below candle"],
    ["SELL",    "Supertrend flip: Bullish → Bearish", "Red arrow above candle"],
], colWidths=[2*cm, 9*cm, 5*cm])
t4.setStyle(base_ts([
    ('TEXTCOLOR', (0,1), (0,1), GREEN),
    ('TEXTCOLOR', (0,2), (0,2), RED),
]))
story += [t4, sp(0.2),
note("IMPORTANTENG TANDAAN: Pumasok LAMANG sa signal candle. Kapag lumipas na ang signal at malayo na ang presyo, SKIP na at hintayin ang susunod na signal."),
sp(0.3)]

# Component 5: Entry/SL/TP
story += [h2("5. Entry / Stop Loss / Take Profit Levels"), sp(0.1),
body("Kapag lumabas ang signal, awtomatikong kino-compute at ini-draw ng indicator ang mga levels:"),
sp(0.1)]

t5 = Table([
    ["Level",       "Kulay",          "Formula",               "Gamit"],
    ["Entry",       "Orange dashed",  "Close ng signal candle", "Pumasok dito"],
    ["Stop Loss",   "Red solid",      "Supertrend line",        "Cut loss dito"],
    ["TP1",         "Teal dotted",    "Entry ± 1.5x Risk",     "Partial profit"],
    ["TP2",         "Teal dotted",    "Entry ± 2.5x Risk",     "Main target"],
    ["TP3",         "Teal dotted",    "Entry ± 3.5x Risk",     "Max target"],
], colWidths=[2*cm, 3.5*cm, 4.5*cm, 6*cm])
t5.setStyle(base_ts([
    ('TEXTCOLOR', (1,1), (1,1), ORANGE),
    ('TEXTCOLOR', (1,2), (1,2), RED),
    ('TEXTCOLOR', (1,3), (1,4), TEAL),
    ('TEXTCOLOR', (1,5), (1,5), TEAL),
]))
story += [t5, sp(0.2),
warn("BABALA: Kapag na-hit na ang TP2, HUWAG nang pumasok kahit Sell/Buy signal pa ang nakikita. Ang risk-reward ay hindi na maganda. Hintayin ang bagong signal."),
sp(0.3)]

# Component 6: Dashboard
story += [h2("6. Dashboard (Top Right)"), sp(0.1),
body("Ipinapakita ng dashboard ang Supertrend direction ng <b>6 iba't ibang timeframes</b> para malaman ang overall market bias."),
sp(0.1)]

t6 = Table([
    ["Row",   "Ibig Sabihin"],
    ["1",     "1-minute Supertrend direction"],
    ["5",     "5-minute Supertrend (primary timeframe)"],
    ["15",    "15-minute Supertrend"],
    ["30",    "30-minute Supertrend"],
    ["1H",    "1-hour Supertrend"],
    ["1D",    "Daily Supertrend (big picture)"],
    ["AVG",   "Bullish kung 4 o higit pa ang Up, Bearish kung 4+ ang Dn"],
    ["Vol",   "Hi = volume above average / Lo = volume below average"],
], colWidths=[2.5*cm, 13.5*cm])
t6.setStyle(base_ts())
story += [t6, sp(0.3)]

# ══════════════════════════════════════════════════════════════════════════════
# PART 2: ENTRY RULES
# ══════════════════════════════════════════════════════════════════════════════
story += [sp(0.3), h1("PART 2 — RULES PARA SA ENTRY"), sp(0.2)]

story += [h2("Complete BUY Checklist"), sp(0.1)]
t7 = Table([
    ["#", "Kondisyon",                "Bakit Kailangan"],
    ["1", "BUY signal lumabas",       "Supertrend flip to bullish"],
    ["2", "Dashboard AVG = Up",       "Majority ng TFs pabor sa BUY"],
    ["3", "Vol = Hi",                 "May sapat na volume para sa move"],
    ["4", "Hindi pa na-hit ang TP2",  "Magandang R:R pa rin"],
    ["5", "Background = Teal",        "Overall trend bullish"],
], colWidths=[1*cm, 6.5*cm, 8.5*cm])
t7.setStyle(base_ts([('TEXTCOLOR', (0,1), (0,-1), GREEN)]))
story += [t7, sp(0.2)]

story += [h2("Complete SELL Checklist"), sp(0.1)]
t8 = Table([
    ["#", "Kondisyon",                "Bakit Kailangan"],
    ["1", "SELL signal lumabas",      "Supertrend flip to bearish"],
    ["2", "Dashboard AVG = Dn",       "Majority ng TFs pabor sa SELL"],
    ["3", "Vol = Hi",                 "May sapat na volume para sa move"],
    ["4", "Hindi pa na-hit ang TP2",  "Magandang R:R pa rin"],
    ["5", "Background = Purple",      "Overall trend bearish"],
], colWidths=[1*cm, 6.5*cm, 8.5*cm])
t8.setStyle(base_ts([('TEXTCOLOR', (0,1), (0,-1), RED)]))
story += [t8, sp(0.2),
note("GOLDEN RULE: Kapag hindi pumasa ang LAHAT ng 5 kondisyon, HUWAG pumasok. Hintayin ang setup na kumpleto ang lahat."),
sp(0.3)]

# ══════════════════════════════════════════════════════════════════════════════
# PART 3: DASHBOARD READING
# ══════════════════════════════════════════════════════════════════════════════
story += [sp(0.3), h1("PART 3 — PAANO BASAHIN ANG DASHBOARD"), sp(0.2)]

story += [h2("Scenario Examples"), sp(0.1)]
t9 = Table([
    ["Dashboard Reading",                    "Interpretation",       "Aksyon"],
    ["5/6 Up + Vol Hi + BUY signal",         "Strong BUY setup",     "PUMASOK — BUY"],
    ["5/6 Dn + Vol Hi + SELL signal",        "Strong SELL setup",    "PUMASOK — SELL"],
    ["Mixed (3 Up, 3 Dn) + any signal",      "Walang malinaw na bias","SKIP — hintayin"],
    ["Majority Dn + Vol Lo + SELL signal",   "Weak signal",          "WAIT — hintayin Vol Hi"],
    ["AVG Up pero 1m/5m Dn",                 "Counter-trend bounce", "SKIP — hindi pwede"],
], colWidths=[6.5*cm, 5*cm, 4.5*cm])
t9.setStyle(base_ts([
    ('TEXTCOLOR', (2,1), (2,1), GREEN),
    ('TEXTCOLOR', (2,2), (2,2), RED),
    ('TEXTCOLOR', (2,3), (2,5), GRAY),
]))
story += [t9, sp(0.3)]

# ══════════════════════════════════════════════════════════════════════════════
# PART 4: SIGNAL FREQUENCY & BEST TIMES
# ══════════════════════════════════════════════════════════════════════════════
story += [sp(0.3), h1("PART 4 — FREQUENCY NG SIGNALS AT BEST TRADING HOURS"), sp(0.2)]

story += [h2("Signal Frequency (5m Chart)"), sp(0.1)]
t10 = Table([
    ["Market Condition",   "Signals per Day",  "Quality"],
    ["Trending market",    "3–8 signals",      "Maganda — sundin ang trend"],
    ["Ranging/choppy",     "10+ signals",      "Maraming false — mag-ingat"],
    ["Low volatility",     "1–3 signals",      "Mababa — hintayin ang session"],
], colWidths=[5.5*cm, 4*cm, 6.5*cm])
t10.setStyle(base_ts())
story += [t10, sp(0.2)]

story += [h2("Best Trading Hours (Manila Time / PHT)"), sp(0.1)]
t11 = Table([
    ["Session",              "Oras (PHT)",         "Signal Quality"],
    ["Asian Session",        "5:00 AM – 1:00 PM",  "Mahinang signals — mababang volatility"],
    ["London Open",          "3:00 PM – 5:00 PM",  "Magandang signals — lumalabas ang trend"],
    ["London-NY Overlap",    "9:00 PM – 1:00 AM",  "BEST — pinaka-malakas na signals"],
    ["NY Open",              "9:30 PM – 11:30 PM", "Malakas — mataas na volatility"],
    ["Late NY / After hrs",  "1:00 AM – 5:00 AM",  "Bumababa — maagang mag-stop"],
], colWidths=[4.5*cm, 4.5*cm, 7*cm])
t11.setStyle(base_ts([
    ('TEXTCOLOR', (2,3), (2,4), GREEN),
    ('TEXTCOLOR', (2,1), (2,1), GRAY),
]))
story += [t11, sp(0.2),
tip("TIP: Ang pinaka-magandang oras para gamitin ang Tradex Algo ay 9:00 PM – 1:00 AM (PHT). Ito ang London-NY overlap — dito pinaka-malakas ang moves ng XAUUSD."),
sp(0.3)]

# ══════════════════════════════════════════════════════════════════════════════
# PART 5: TRADE MANAGEMENT
# ══════════════════════════════════════════════════════════════════════════════
story += [sp(0.3), h1("PART 5 — TRADE MANAGEMENT"), sp(0.2)]

story += [h2("Entry at Exit Rules"), sp(0.1)]
t12 = Table([
    ["Sitwasyon",                          "Dapat Gawin"],
    ["Signal lalabas (BUY/SELL arrow)",    "I-check ang checklist → pumasok kapag kumpleto"],
    ["TP1 na-hit",                         "Pwedeng mag-partial close (50% ng position)"],
    ["TP2 na-hit",                         "Main profit — pwedeng fully close na"],
    ["TP3 na-hit",                         "Maximum profit — full close"],
    ["SL na-hit",                          "Accept ang loss — huwag mag-average down"],
    ["Lumipas na ang signal",              "SKIP — hintayin ang susunod na signal"],
    ["TP2 na-hit, bagong signal pa",       "SKIP — hintayin ang fresh setup"],
], colWidths=[7*cm, 9*cm])
t12.setStyle(base_ts())
story += [t12, sp(0.2)]

story += [h2("Kailan Hindi Pwedeng Pumasok"), sp(0.1)]
t13 = Table([
    ["Kondisyon",                         "Dahilan"],
    ["Vol = Lo",                          "Walang volume = pwedeng fake move"],
    ["Dashboard mixed (3 Up, 3 Dn)",      "Walang malinaw na bias"],
    ["TP2 na na-hit ng signal",           "R:R hindi na maganda"],
    ["Asian session (5AM-1PM PHT)",       "Mababang volatility, maraming false signals"],
    ["Counter-trend signal",              "Ex: BUY signal pero AVG = Dn — laban sa trend"],
], colWidths=[6.5*cm, 9.5*cm])
t13.setStyle(base_ts([('TEXTCOLOR', (0,1), (0,-1), RED)]))
story += [t13, sp(0.3)]

# ══════════════════════════════════════════════════════════════════════════════
# PART 6: ALERTS SETUP
# ══════════════════════════════════════════════════════════════════════════════
story += [sp(0.3), h1("PART 6 — PAANO MAG-SET NG ALERTS"), sp(0.2)]

story += [body("May 4 alert conditions ang Tradex Algo na pwede mong i-set sa TradingView:"), sp(0.1)]

t14 = Table([
    ["Alert Name",             "Kailan Mag-fi-fire",                    "Inirekomenda"],
    ["BUY Signal",             "Bawat Supertrend flip pataas",          "Pangalawa"],
    ["SELL Signal",            "Bawat Supertrend flip pababa",          "Pangalawa"],
    ["BUY Confirmed (MTF)",    "BUY flip + 4+ timeframes bullish",      "PANGUNAHIN"],
    ["SELL Confirmed (MTF)",   "SELL flip + 4+ timeframes bearish",     "PANGUNAHIN"],
], colWidths=[4.5*cm, 8*cm, 3.5*cm])
t14.setStyle(base_ts([
    ('TEXTCOLOR', (2,3), (2,4), GREEN),
    ('TEXTCOLOR', (2,1), (2,2), GRAY),
]))
story += [t14, sp(0.2)]

story += [h2("Step-by-Step Alert Setup sa TradingView"), sp(0.1)]
steps = [
    ["1", "I-click ang 'Alerts' button (bell icon) sa TradingView toolbar"],
    ["2", "I-click ang 'Create Alert'"],
    ["3", "Sa 'Condition', i-select ang 'Tradex Algo' indicator"],
    ["4", "Piliin ang 'SELL Confirmed (MTF)' o 'BUY Confirmed (MTF)'"],
    ["5", "Sa 'Trigger', piliin ang 'Once Per Bar Close'"],
    ["6", "I-set ang notification — Email, App notification, o SMS"],
    ["7", "I-click ang 'Create' para i-save ang alert"],
]
ta_ = Table(steps, colWidths=[1*cm, 15*cm])
ta_.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), DARKER),
    ('TEXTCOLOR',  (0,0), (0,-1), GOLD),
    ('TEXTCOLOR',  (1,0), (1,-1), WHITE),
    ('FONTNAME',   (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0), (-1,-1), 8.5),
    ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#333366')),
    ('ALIGN',      (0,0), (0,-1), 'CENTER'),
    ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0), (-1,-1), 17),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story += [ta_, sp(0.2),
tip("TIP: I-set ang 'SELL Confirmed (MTF)' at 'BUY Confirmed (MTF)' para mas mababa ang false alerts. Hindi ka na kailangang laging nakamasid sa screen."),
sp(0.3)]

# ══════════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE CARD
# ══════════════════════════════════════════════════════════════════════════════
story += [sp(0.3), h1("QUICK REFERENCE — Cheat Sheet"), sp(0.2)]

t15 = Table([
    ["",             "BUY Setup",              "SELL Setup"],
    ["Signal",       "BUY arrow (green)",       "SELL arrow (red)"],
    ["Background",   "Teal tint",               "Purple tint"],
    ["Dashboard",    "AVG = Up",                "AVG = Dn"],
    ["Volume",       "Vol = Hi",                "Vol = Hi"],
    ["Entry",        "Close ng signal candle",  "Close ng signal candle"],
    ["Stop Loss",    "Supertrend line (below)",  "Supertrend line (above)"],
    ["TP1",          "Entry + 1.5x Risk",       "Entry - 1.5x Risk"],
    ["TP2",          "Entry + 2.5x Risk",       "Entry - 2.5x Risk"],
    ["TP3",          "Entry + 3.5x Risk",       "Entry - 3.5x Risk"],
    ["Best Time",    "London-NY (9PM-1AM PHT)", "London-NY (9PM-1AM PHT)"],
    ["SKIP kapag",   "TP2 na na-hit / Vol Lo",  "TP2 na na-hit / Vol Lo"],
], colWidths=[3.5*cm, 7*cm, 5.5*cm])
t15.setStyle(base_ts([
    ('TEXTCOLOR', (1,1), (1,-1), GREEN),
    ('TEXTCOLOR', (2,1), (2,-1), RED),
    ('FONTNAME',  (0,0), (-1,0), 'Helvetica-Bold'),
]))
story += [t15, sp(0.5), hr(),
Paragraph("TRADEX ALGO — XAUUSD Scalping Indicator &nbsp;|&nbsp; Para sa educational purposes lamang. Trading involves risk.", footer_style)]

doc.build(story)
print("PDF generated: /home/user/Indicator/Tradex_Algo_Guide.pdf")
