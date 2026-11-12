#!/usr/bin/env python3
"""Miniaturas de marca de la portada (1200x630): ATLAS, Finde, Descargo y J.A.R.V.I.S.
Estética og-v2: grafito, rejilla tron 48px, halo violeta, isotipo grande, DejaVu.
Paleta EXACTA del manual: #10131C, #F5F4F0, #14C6D4, #7148F5."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
F = "/home/hermes/.hermes/cache/scratch/portada/fonts/"
GRAFITO = (16, 19, 28)
MARFIL = (245, 244, 240)
CIAN = (20, 198, 212)
VIOLETA = (113, 72, 245)

def isotipo(d, ox, oy, s, alfa_m=255, alfa_c=255):
    mar = MARFIL + (alfa_m,)
    cian = CIAN + (alfa_c,)
    for pts, fill in [
        ("18 174 18 38 180 14 180 174 160 174 160 39 38 57 38 174", mar),
        ("52 170 52 80 142 59 142 79 72 96 72 170", mar),
        ("96 167 96 109 143 93 143 173", cian),
    ]:
        n = [int(v) for v in pts.split()]
        d.polygon([(ox + n[k] * s, oy + n[k + 1] * s) for k in range(0, len(n), 2)], fill=fill)

def base(nombre, tagline, url, pildora=None, jarvis=False, out="x.png"):
    img = Image.new("RGB", (W, H), GRAFITO)
    d = ImageDraw.Draw(img)
    # rejilla tron
    for x in range(0, W + 48, 48):
        d.line([(x, 0), (x, H)], fill=(20, 198, 212, 9), width=1)
    for y in range(0, H + 48, 48):
        d.line([(0, y), (W, y)], fill=(20, 198, 212, 9), width=1)
    # halo violeta arriba derecha
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for i in range(60, 0, -1):
        r = int(760 * i / 60)
        a = int(34 * (1 - i / 60) ** 1.5)
        if a >= 1:
            gd.ellipse([W - 320 - r, -r - 160, W - 320 + r, r - 160], fill=VIOLETA + (a,))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    d = ImageDraw.Draw(img)

    f_kicker = ImageFont.truetype(F + "DejaVuSansMono.ttf", 23)
    f_h1 = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 64)
    f_t = ImageFont.truetype(F + "DejaVuSans.ttf", 33)
    f_p = ImageFont.truetype(F + "DejaVuSansMono.ttf", 22)
    f_mini = ImageFont.truetype(F + "DejaVuSansMono.ttf", 19)

    d.text((72, 64), "SUKIMA LABS", font=f_kicker, fill=CIAN)
    # isotipo grande a la derecha
    isotipo(d, W - 480, 90, 1.55, alfa_m=200, alfa_c=255)
    # barra cian bajo el kicker
    d.rectangle([72, 104, 72 + 320, 108], fill=CIAN)

    y = 250
    d.text((72, y), nombre, font=f_h1, fill=MARFIL)
    y += 92
    # tagline con salto limpio (sin espacios sueltos que descentren)
    lineas = []
    cur = ""
    for word in tagline.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=f_t) <= 660:
            cur = t
        else:
            lineas.append(cur)
            cur = word
    if cur:
        lineas.append(cur)
    for linea in lineas:
        d.text((72, y), linea, font=f_t, fill=(180, 184, 190))
        y += 46
    y += 24

    if pildora:
        bx = d.textbbox((0, 0), pildora, font=f_p)
        tw = bx[2] - bx[0]
        th = bx[3] - bx[1]
        d.rounded_rectangle([72, y, 72 + tw + 44, y + th + 26], radius=22, outline=VIOLETA, width=3)
        d.text((94, y + 11 - bx[1]), pildora, font=f_p, fill=CIAN)
    elif jarvis:
        txt = "EN DESARROLLO · LANZAMIENTO FUTURO"
        bx = d.textbbox((0, 0), txt, font=f_p)
        tw = bx[2] - bx[0]
        th = bx[3] - bx[1]
        d.rounded_rectangle([72, y, 72 + tw + 44, y + th + 26], radius=22, outline=VIOLETA, width=3)
        d.text((94, y + 11 - bx[1]), txt, font=f_p, fill=VIOLETA)

    d.text((72, H - 72), url, font=f_mini, fill=(120, 126, 134))
    img.save(out, optimize=True)
    print(out)

base("ATLAS ONU", "Buscador de documentos de derechos humanos de la ONU.", "sukimalabs.com/atlasonu", "publicado · búsqueda por frase exacta", out="img/atlas.jpg")
base("Finde", "Escapadas de sábado a domingo desde Madrid, en coche o en tren.", "sukimalabs.com/finde", "19 rutas · 195 lugares · sin registro", out="img/finde.jpg")
base("Descargo", "Prueba de autoría frente a detectores de plagio e IA.", "sukimalabs.com/descargo", "todo ocurre en tu navegador", out="img/descargo.jpg")
base("J.A.R.V.I.S.", "Asistente de escritorio para Windows con voz, HUD y memoria local.", "proyecto privado de Sukima Labs", jarvis=True, out="img/jarvis.jpg")
