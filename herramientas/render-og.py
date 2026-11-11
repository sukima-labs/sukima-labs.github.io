#!/usr/bin/env python3
"""Genera img/og-v2.png (1200x630) con la identidad de Sukima Labs."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
GRAFITO = (16, 19, 28)
MARFIL = (245, 244, 240)
CIAN = (20, 198, 212)
VIOLETA = (113, 72, 245)
QUIET = (160, 158, 155)

F = "/home/hermes/.hermes/cache/scratch/portada/fonts/"
f_bold36 = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 36)
f_bold86 = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 84)
f_reg22 = ImageFont.truetype(F + "DejaVuSans.ttf", 22)
f_mono24 = ImageFont.truetype(F + "DejaVuSansMono.ttf", 24)
f_mono22 = ImageFont.truetype(F + "DejaVuSansMono.ttf", 22)
f_mono13 = ImageFont.truetype(F + "DejaVuSansMono.ttf", 13)

img = Image.new("RGB", (W, H), GRAFITO)

# halo violeta arriba (elipses concéntricas con alfa decreciente)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
steps = 70
for i in range(steps, 0, -1):
    r = int(1500 * i / steps)
    a = int(30 * (1 - i / steps) ** 1.5)
    if a < 1:
        continue
    gd.ellipse([W // 2 - r, int(-H * 0.45) - r, W // 2 + r, int(-H * 0.45) + r],
               fill=VIOLETA + (a,))
img = Image.alpha_composite(img.convert("RGBA"), glow)

# rejilla tron cian tenue
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
for x in range(0, W + 48, 48):
    gd.line([(x, 0), (x, H)], fill=CIAN + (9,), width=1)
for y in range(0, H + 48, 48):
    gd.line([(0, y), (W, y)], fill=CIAN + (9,), width=1)
img = Image.alpha_composite(img, grid)

d = ImageDraw.Draw(img)

# cabecera
d.text((72, 32), "Sukima Labs.", font=f_bold36, fill=MARFIL)
d.line([(0, 104), (W, 104)], fill=MARFIL + (56,), width=3)
tw = d.textlength("sukimalabs.com", font=f_mono24)
d.text((W - 72 - tw, 38), "sukimalabs.com", font=f_mono24, fill=QUIET)

# kicker
d.text((72, 236), "laboratorio global de posibilidades", font=f_mono22, fill=CIAN)

# titular con halo cian (doble pasada desplazada) y salto manual
h1 = "El espacio donde nacen nuevas posibilidades."
lines = []
cur = ""
for word in h1.split():
    t = (cur + " " + word).strip()
    if d.textlength(t, font=f_bold86) <= 1000:
        cur = t
    else:
        lines.append(cur)
        cur = word
lines.append(cur)
y = 292
for ln in lines:
    halo = ImageDraw.Draw(img, "RGBA")
    for dx, dy in ((-3, 0), (3, 0), (0, -3), (0, 3), (2, 2), (-2, -2)):
        halo.text((72 + dx, y + dy), ln, font=f_bold86, fill=CIAN + (28,))
    d.text((72, y), ln, font=f_bold86, fill=MARFIL)
    y += int(84 * 1.06)

# barra inferior cian
d.rectangle([0, H - 72, W, H], fill=CIAN)
d.rectangle([72, H - 72 + 29, 86, H - 72 + 43], fill=GRAFITO)
d.text((100, H - 72 + 22), "exploración, diseño y ejecución", font=f_mono24, fill=GRAFITO)
tw = d.textlength("sin analítica propia", font=f_mono24)
d.text((W - 72 - tw, H - 72 + 22), "sin analítica propia", font=f_mono24, fill=GRAFITO)

img.convert("RGB").save("/home/hermes/.hermes/cache/scratch/portada/img/og-v2.png", optimize=True)
print("og-v2.png generado")
