from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER

doc = SimpleDocTemplate("/home/user/Indicator/Tradex_Algo_Guide_v2.pdf",
    pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)

GOLD   = colors.HexColor('#FFD700')
CYAN   = colors.HexColor('#00ffd5')
PINK   = colors.HexColor('#ff3cac')
GREEN  = colors.HexColor('#00ff88')
RED    = colors.HexColor('#ff4444')
GRAY   = colors.HexColor('#888888')
WHITE  = colors.HexColor('#ffffff')
DARK   = colors.HexColor('#0f0f1a')
MID    = colors.HexColor('#16213e')
DARKER = colors.HexColor('#1a1a2e')
ORANGE = colors.HexColor('#FFA500')
TEAL   = colors.HexColor('#00CED1')
PURPLE = colors.HexColor('#7b00ff')
YELLOW = colors.HexColor('#ffd700')

styles = getSampleStyleSheet()
def S(name, **kw): return ParagraphStyle(name, parent=styles['Normal'], **kw)

title_s = S('T', fontSize=22, textColor=GOLD, backColor=DARKER, alignment=TA_CENTER, spaceAfter=4, leading=28, borderPad=10)
sub_s   = S('S', fontSize=10, textColor=GRAY, alignment=TA_CENTER, spaceAfter=10)
h1_s    = S('H1', fontSize=12, textColor=GOLD, backColor=MID, spaceBefore=12, spaceAfter=5, leading=18, borderPad=6)
h2_s    = S('H2', fontSize=10.5, textColor=CYAN, spaceBefore=8, spaceAfter=3, leading=15)
body_s  = S('B', fontSize=9, textColor=WHITE, backColor=DARK, spaceAfter=4, leading=13)
note_s  = S('N', fontSize=8.5, textColor=WHITE, backColor=colors.HexColor('#1e3a1e'), spaceAfter=5, leading=12, leftIndent=8, rightIndent=8, borderPad=6)
warn_s  = S('W', fontSize=8.5, textColor=WHITE, backColor=colors.HexColor('#3a1e1e'), spaceAfter=5, leading=12, leftIndent=8, rightIndent=8, borderPad=6)
tip_s   = S('TP', fontSize=8.5, textColor=WHITE, backColor=colors.HexColor('#1a1a3e'), spaceAfter=5, leading=12, leftIndent=8, rightIndent=8, borderPad=6)
new_s   = S('NW', fontSize=8.5, textColor=colors.HexColor('#111100'), backColor=YELLOW, spaceAfter=5, leading=12, leftIndent=8, rightIndent=8, borderPad=6)
foot_s  = S('F', fontSize=7.5, textColor=GRAY, alignment=TA_CENTER)

def h1(t): return Paragraph(t, h1_s)
def h2(t): return Paragraph(t, h2_s)
def body(t): return Paragraph(t, body_s)
def note(t): return Paragraph(t, note_s)
def warn(t): return Paragraph(t, warn_s)
def tip(t):  return Paragraph(t, tip_s)
def new(t):  return Paragraph("🆕 NEW: " + t, new_s)
def sp(h=.25): return Spacer(1, h*cm)
def hr(): return HRFlowable(width="100%", thickness=1, color=colors.HexColor('#333366'), spaceAfter=5)

def tbl(data, widths, extra=None):
    base = [
        ('BACKGROUND',(0,0),(-1,0), MID), ('TEXTCOLOR',(0,0),(-1,0), GOLD),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'), ('FONTSIZE',(0,0),(-1,0), 8.5),
        ('ALIGN',(0,0),(-1,-1),'CENTER'), ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('GRID',(0,0),(-1,-1), 0.5, colors.HexColor('#333366')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[DARKER, MID]),
        ('TEXTCOLOR',(0,1),(-1,-1), WHITE), ('FONTSIZE',(0,1),(-1,-1), 8),
        ('FONTNAME',(0,1),(-1,-1),'Helvetica'),
        ('ROWHEIGHT',(0,0),(-1,-1), 17), ('TOPPADDING',(0,0),(-1,-1), 3), ('BOTTOMPADDING',(0,0),(-1,-1), 3),
    ]
    if extra: base += extra
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle(base))
    return t

story = []

# COVER
story += [sp(1.5), Paragraph("TRADEX ALGO", title_s),
    Paragraph("Complete User Guide v2 — XAUUSD Scalping Indicator", sub_s), sp(.2), hr(),
    body("Platform: TradingView &nbsp;|&nbsp; Asset: XAUUSD (Gold) &nbsp;|&nbsp; Timeframe: 5 Minutes"),
    hr(), sp(.5),
    new("Bagong feature: Flip Warning System — advanced early detection ng signal switch"),
    sp(.8)]

# ── PART 1: VISUALS ──────────────────────────────────────────────────────────
story += [h1("PART 1 — ANG VISUAL DESIGN NG TRADEX ALGO"), sp(.2),
body("Ang Tradex Algo ay dinisenyo para sa <b>clean, premium na look</b>. White candles ang ginagamit para mas malinaw ang visual elements ng indicator."), sp(.2)]

story += [h2("1. Candle Colors — White/Silver"), sp(.1),
body("Walang green/red na candle coloring. Puting kulay ang lahat ng candles para hindi masyadong busy ang chart at mas matututukan mo ang cloud at signals."), sp(.3)]

story += [h2("2. Background Color — Trend Indicator"), sp(.1)]
story += [tbl([
    ["Background",       "Kulay",         "Ibig Sabihin"],
    ["Dark Teal glow",   "#003d2e",       "Bullish — Supertrend pataas"],
    ["Dark Purple glow", "#1a0030",       "Bearish — Supertrend pababa"],
    ["Gold/Yellow flash","#ffd700",       "⚠ FLIP WARNING — malapit na mag-switch!"],
], [4*cm, 3.5*cm, 8.5*cm], [
    ('TEXTCOLOR',(0,1),(0,1), CYAN), ('TEXTCOLOR',(0,2),(0,2), colors.HexColor('#bb88ff')),
    ('TEXTCOLOR',(0,3),(0,3), YELLOW),
]), sp(.3)]

story += [h2("3. Cloud Ribbon — EMA 9 / EMA 21"), sp(.1),
body("Ang cloud ribbon ay ginawa mula sa dalawang EMA na nag-fo-form ng ribbon. Nagbabago ng kulay depende sa trend direction."), sp(.1)]
story += [tbl([
    ["Cloud",          "Trend",    "Ibig Sabihin"],
    ["Teal (#00ffd5)", "Bullish",  "Trend pataas — safe para sa BUY"],
    ["Violet (#7b00ff)","Bearish", "Trend pababa — safe para sa SELL"],
    ["Makapal ribbon", "Any",      "Malakas ang trend — ok pumasok"],
    ["Manipis/flat",   "Any",      "Nagbabago ng direksyon — mag-ingat"],
], [3.5*cm, 3*cm, 9.5*cm], [
    ('TEXTCOLOR',(0,1),(0,1), CYAN), ('TEXTCOLOR',(0,2),(0,2), colors.HexColor('#bb88ff')),
]), sp(.3)]

story += [h2("4. Supertrend Line"), sp(.1),
body("Ang Supertrend line ay nagiging iba ang kulay at kapal depende sa kondisyon:"), sp(.1)]
story += [tbl([
    ["State",           "Kulay",        "Kapal",   "Ibig Sabihin"],
    ["Bullish",         "Teal",         "Normal",  "Trend safe — manatili sa BUY"],
    ["Bearish",         "Pink",         "Normal",  "Trend safe — manatili sa SELL"],
    ["Near Flip ⚠",    "Gold/Yellow",  "Thicker", "Mag-ingat — malapit mag-switch!"],
], [3.5*cm, 3*cm, 2.5*cm, 7*cm], [
    ('TEXTCOLOR',(1,1),(1,1), CYAN), ('TEXTCOLOR',(1,2),(1,2), PINK),
    ('TEXTCOLOR',(1,3),(1,3), YELLOW), ('TEXTCOLOR',(0,3),(0,3), YELLOW),
]), sp(.5)]

# ── PART 2: SIGNALS ──────────────────────────────────────────────────────────
story += [h1("PART 2 — MGA SIGNALS"), sp(.2)]

story += [h2("BUY at SELL Signals"), sp(.1),
body("Lalabas ang signal kapag <b>nagbago ang Supertrend direction (flip)</b>. Awtomatikong kino-compute ang Entry, SL, at TP."), sp(.1)]
story += [tbl([
    ["Signal", "Shape",       "Kulay",  "Kailan Lalabas"],
    ["BUY ▲",  "Label Up",   "Teal",   "Supertrend flip: Bearish → Bullish"],
    ["SELL ▼", "Label Down", "Pink",   "Supertrend flip: Bullish → Bearish"],
], [2.5*cm, 3*cm, 2.5*cm, 8*cm], [
    ('TEXTCOLOR',(0,1),(0,1), CYAN), ('TEXTCOLOR',(0,2),(0,2), PINK),
]), sp(.2),
note("RULE: Pumasok LAMANG sa signal candle. Hindi pwedeng pumasok kapag lumipas na ang signal at malayo na ang presyo."), sp(.3)]

story += [h2("⚠ Flip Warning Signal — BAGONG FEATURE"), sp(.1),
body("Ito ang pinakaimportanteng bagong feature. Nag-de-detect ito kapag ang presyo ay <b>malapit na sa Supertrend line</b> at posibleng magbago na ang direksyon."), sp(.1)]
story += [tbl([
    ["Indicator",              "Paano Makikilala"],
    ["Background = Gold/Yellow","Background nagbabago ng kulay"],
    ["Supertrend line = Gold",  "Ang Supertrend line nagiging gold at mas makapal"],
    ["Diamond dots ◆",         "Maliliit na gold diamonds izaas/ibaba ng candles"],
    ["Dashboard FLIP = ⚠ NEAR","Ang Flip row sa dashboard nagpapakita ng warning"],
    ["Alert: ⚠ Near Flip",     "Pwedeng mag-set ng TradingView alert para dito"],
], [5*cm, 11*cm]), sp(.2),
new("Kapag nakita mo ang Flip Warning — HUWAG magbukas ng bagong trade. Hintayin kung saan mag-fi-flip ang Supertrend para malaman ang susunod na direksyon."), sp(.3)]

# ── PART 3: ENTRY/SL/TP ──────────────────────────────────────────────────────
story += [h1("PART 3 — ENTRY / STOP LOSS / TAKE PROFIT"), sp(.2),
body("Kapag lumabas ang BUY o SELL signal, awtomatikong nagdadraw ang indicator ng mga horizontal lines:"), sp(.1)]
story += [tbl([
    ["Level",     "Kulay",          "Formula",              "Gamit"],
    ["Entry",     "Orange dashed",  "Close ng signal candle","Pumasok dito"],
    ["Stop Loss", "Red solid",      "Supertrend line",       "I-cut loss dito"],
    ["TP 1",      "Teal dotted",    "Entry ± 1.5x Risk",    "Partial profit — 50% close"],
    ["TP 2",      "Teal dotted",    "Entry ± 2.5x Risk",    "Main target — full close"],
    ["TP 3",      "Teal dotted",    "Entry ± 3.5x Risk",    "Maximum profit"],
], [2.5*cm, 3.5*cm, 4.5*cm, 5.5*cm], [
    ('TEXTCOLOR',(1,1),(1,1), ORANGE), ('TEXTCOLOR',(1,2),(1,2), RED),
    ('TEXTCOLOR',(1,3),(1,5), TEAL),
]), sp(.2),
warn("Kapag na-hit na ang TP2, HUWAG nang pumasok kahit may signal pa. Hintayin ang bagong flip na may sariwang Entry/SL/TP."), sp(.5)]

# ── PART 4: DASHBOARD ────────────────────────────────────────────────────────
story += [h1("PART 4 — DASHBOARD (Top Right)"), sp(.2),
body("Ipinapakita ng dashboard ang real-time na estado ng lahat ng timeframes at ang Flip Warning. May 10 rows na ngayon."), sp(.1)]
story += [tbl([
    ["Row",   "Ibig Sabihin"],
    ["1",     "1-minute Supertrend — Up (teal) o Dn (red)"],
    ["5",     "5-minute Supertrend — primary timeframe"],
    ["15",    "15-minute Supertrend"],
    ["30",    "30-minute Supertrend"],
    ["1H",    "1-hour Supertrend"],
    ["1D",    "Daily Supertrend — big picture"],
    ["AVG",   "Bullish = 4+ TFs Up / Bearish = 4+ TFs Dn"],
    ["Vol",   "Hi = volume above average / Lo = volume below average"],
    ["Flip",  "⚠ NEAR = malapit mag-flip! / Safe = malayo pa"],
], [2.5*cm, 13.5*cm], [
    ('TEXTCOLOR',(0,9),(0,9), YELLOW),
]), sp(.2),
new("Bagong row: FLIP — kapag ⚠ NEAR ang nakikita, mag-prepare ka na. Posibleng magbago na ang direksyon."), sp(.5)]

# ── PART 5: HOW TO USE ───────────────────────────────────────────────────────
story += [h1("PART 5 — STEP-BY-STEP: PAANO GAMITIN"), sp(.2)]

story += [h2("Para sa SELL trade:"), sp(.1)]
steps_sell = [
    ["1","Hintayin ang SELL signal (pink ▼ arrow)"],
    ["2","I-check ang Dashboard — AVG dapat = Dn"],
    ["3","Vol = Hi (kailangan may volume)"],
    ["4","FLIP row = Safe (hindi ⚠ NEAR)"],
    ["5","Background = dark purple/violet"],
    ["6","Pumasok sa Entry price"],
    ["7","SL = Stop loss line (itaas ng entry)"],
    ["8","Target TP1 → TP2 → TP3"],
]
t_sell = Table(steps_sell, colWidths=[1*cm, 15*cm])
t_sell.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,-1), DARKER), ('TEXTCOLOR',(0,0),(0,-1), PINK),
    ('TEXTCOLOR',(1,0),(1,-1), WHITE), ('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),
    ('FONTSIZE',(0,0),(-1,-1), 8.5), ('GRID',(0,0),(-1,-1),0.5, colors.HexColor('#333366')),
    ('ALIGN',(0,0),(0,-1),'CENTER'), ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('ROWHEIGHT',(0,0),(-1,-1), 17), ('TOPPADDING',(0,0),(-1,-1), 3), ('BOTTOMPADDING',(0,0),(-1,-1), 3),
]))
story += [t_sell, sp(.2)]

story += [h2("Para sa BUY trade:"), sp(.1)]
steps_buy = [
    ["1","Hintayin ang BUY signal (teal ▲ arrow)"],
    ["2","I-check ang Dashboard — AVG dapat = Up"],
    ["3","Vol = Hi (kailangan may volume)"],
    ["4","FLIP row = Safe (hindi ⚠ NEAR)"],
    ["5","Background = dark teal/green"],
    ["6","Pumasok sa Entry price"],
    ["7","SL = Stop loss line (ibaba ng entry)"],
    ["8","Target TP1 → TP2 → TP3"],
]
t_buy = Table(steps_buy, colWidths=[1*cm, 15*cm])
t_buy.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,-1), DARKER), ('TEXTCOLOR',(0,0),(0,-1), CYAN),
    ('TEXTCOLOR',(1,0),(1,-1), WHITE), ('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),
    ('FONTSIZE',(0,0),(-1,-1), 8.5), ('GRID',(0,0),(-1,-1),0.5, colors.HexColor('#333366')),
    ('ALIGN',(0,0),(0,-1),'CENTER'), ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('ROWHEIGHT',(0,0),(-1,-1), 17), ('TOPPADDING',(0,0),(-1,-1), 3), ('BOTTOMPADDING',(0,0),(-1,-1), 3),
]))
story += [t_buy, sp(.3)]

story += [h2("Kapag Lumabas ang ⚠ Flip Warning:"), sp(.1)]
flip_steps = [
    ["1","HUWAG magbukas ng bagong trade"],
    ["2","Kung may bukas na trade, mag-ingat — baka mag-reverse"],
    ["3","Hintayin kung saan mag-fi-flip — pataas (BUY) o pababa (SELL)"],
    ["4","Kapag nag-flip na at lumabas ang signal — doon ka pumasok"],
    ["5","Huwag anticipate — hintayin ang confirmation (signal arrow)"],
]
t_flip = Table(flip_steps, colWidths=[1*cm, 15*cm])
t_flip.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,-1), colors.HexColor('#1a1500')), ('TEXTCOLOR',(0,0),(0,-1), YELLOW),
    ('TEXTCOLOR',(1,0),(1,-1), WHITE), ('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),
    ('FONTSIZE',(0,0),(-1,-1), 8.5), ('GRID',(0,0),(-1,-1),0.5, colors.HexColor('#444400')),
    ('ALIGN',(0,0),(0,-1),'CENTER'), ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('ROWHEIGHT',(0,0),(-1,-1), 17), ('TOPPADDING',(0,0),(-1,-1), 3), ('BOTTOMPADDING',(0,0),(-1,-1), 3),
]))
story += [t_flip, sp(.5)]

# ── PART 6: ALERTS ───────────────────────────────────────────────────────────
story += [h1("PART 6 — ALERT SETUP SA TRADINGVIEW"), sp(.2),
body("May 5 alert conditions ang Tradex Algo:"), sp(.1)]
story += [tbl([
    ["Alert Name",           "Kailan",                              "Priority"],
    ["BUY Signal",           "Bawat Supertrend flip pataas",        "Secondary"],
    ["SELL Signal",          "Bawat Supertrend flip pababa",        "Secondary"],
    ["BUY Confirmed (MTF)",  "BUY flip + 4+ TFs bullish",          "PRIMARY"],
    ["SELL Confirmed (MTF)", "SELL flip + 4+ TFs bearish",         "PRIMARY"],
    ["⚠ Near Flip",          "Price malapit na sa Supertrend line", "WARNING"],
], [4.5*cm, 7*cm, 4.5*cm], [
    ('TEXTCOLOR',(2,3),(2,4), GREEN), ('TEXTCOLOR',(0,5),(0,5), YELLOW),
    ('TEXTCOLOR',(2,1),(2,2), GRAY),
]), sp(.2),
tip("Setup: Alerts → Create Alert → Condition → Tradex Algo → Piliin ang alert → Once Per Bar Close → Save"), sp(.5)]

# ── PART 7: BEST TIMES ───────────────────────────────────────────────────────
story += [h1("PART 7 — BEST TRADING HOURS (Manila Time)"), sp(.2)]
story += [tbl([
    ["Session",            "Oras (PHT)",         "Quality"],
    ["Asian Session",      "5:00 AM – 1:00 PM",  "Mahinang signals — mababang volatility"],
    ["London Open",        "3:00 PM – 5:00 PM",  "Magandang signals — lumalabas ang trend"],
    ["London-NY Overlap",  "9:00 PM – 1:00 AM",  "BEST — pinaka-malakas na signals"],
    ["NY Open",            "9:30 PM – 11:30 PM", "Malakas — mataas na volatility"],
    ["Late NY",            "1:00 AM – 5:00 AM",  "Bumababa — maagang mag-stop"],
], [4.5*cm, 4.5*cm, 7*cm], [
    ('TEXTCOLOR',(2,3),(2,4), GREEN), ('TEXTCOLOR',(2,1),(2,1), GRAY),
]), sp(.5)]

# ── QUICK REFERENCE ──────────────────────────────────────────────────────────
story += [h1("QUICK REFERENCE — Cheat Sheet"), sp(.2)]
story += [tbl([
    ["",            "BUY Setup",             "SELL Setup"],
    ["Signal",      "Teal ▲ arrow",          "Pink ▼ arrow"],
    ["Background",  "Dark teal",             "Dark purple"],
    ["Cloud",       "Teal ribbon",           "Violet ribbon"],
    ["Dashboard",   "AVG = Up",              "AVG = Dn"],
    ["Volume",      "Vol = Hi",              "Vol = Hi"],
    ["Flip row",    "Safe",                  "Safe"],
    ["SL",          "Supertrend (below)",    "Supertrend (above)"],
    ["TP1/TP2/TP3", "1.5x / 2.5x / 3.5x",  "1.5x / 2.5x / 3.5x"],
    ["SKIP kapag",  "Vol Lo / Flip ⚠ NEAR", "Vol Lo / Flip ⚠ NEAR"],
    ["Best Time",   "9PM–1AM PHT",           "9PM–1AM PHT"],
], [3.5*cm, 7*cm, 5.5*cm], [
    ('TEXTCOLOR',(1,1),(1,-1), CYAN), ('TEXTCOLOR',(2,1),(2,-1), PINK),
]), sp(.5), hr(),
Paragraph("TRADEX ALGO v2 — XAUUSD Scalping Indicator &nbsp;|&nbsp; Para sa educational purposes lamang.", foot_s)]

doc.build(story)
print("PDF generated: /home/user/Indicator/Tradex_Algo_Guide_v2.pdf")
