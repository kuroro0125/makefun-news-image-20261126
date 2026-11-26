#!/usr/bin/env python3
"""Draw the 26 November 2026 world-news front page (1024x1024).

Renders a clean newspaper front page with PIL: masthead naming the day,
one lead story and six story cards plus an 'also today' strip. The image
is written to entry.png next to this file. Run: python3 draw.py
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (24, 24, 24)
NAVY = (20, 38, 74)
NAVY_LIGHT = (31, 58, 110)
RED = (179, 49, 42)
GOLD = (217, 164, 65)
GREY = (90, 88, 82)
CARD_BG = (255, 255, 255)
CARD_LINE = (216, 210, 196)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width` px."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_globe(draw, cx, cy, r):
    """Simple line globe: circle, meridians and parallels."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=4)
    draw.ellipse([cx - r // 3, cy - r, cx + r // 3, cy + r],
                 outline=NAVY_LIGHT, width=3)
    for k in (-0.5, 0.5):
        y = cy + k * r
        half = int((r * r - (k * r) ** 2) ** 0.5)
        draw.line([cx - half, y, cx + half, y], fill=NAVY_LIGHT, width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=NAVY_LIGHT, width=3)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 148], fill=NAVY)
    title = "THE WORLD IN ONE DAY"
    tf = SERIF_B(56)
    d.text(((W - d.textlength(title, font=tf)) / 2, 22), title,
           font=tf, fill=(255, 255, 255))
    date_line = "T H U R S D A Y   ·   2 6   N O V E M B E R   2 0 2 6"
    df = SANS_B(24)
    d.text(((W - d.textlength(date_line, font=df)) / 2, 96), date_line,
           font=df, fill=GOLD)
    d.rectangle([0, 148, W, 154], fill=RED)

    # ---- Lead story ----
    lx, lw = 36, 640
    y = 176
    d.text((lx, y), "LEAD  ·  TRADE", font=SANS_B(20), fill=RED)
    y += 30
    head = "Tariffs, Act Two"
    hf = SERIF_B(52)
    d.text((lx, y), head, font=hf, fill=INK)
    y += 66
    deck = ("Trump proposes sweeping new tariffs on 14 trade partners — "
            "China, the EU and Japan in the firing line — aimed at factory "
            "overcapacity.")
    for line in wrap(d, deck, SANS(23), lw):
        d.text((lx, y), line, font=SANS(23), fill=(52, 52, 52))
        y += 30

    # Globe at the right of the lead
    draw_globe(d, 852, 252, 78)
    cap = "The day in one page"
    cf = SANS(18)
    d.text((852 - d.textlength(cap, font=cf) / 2, 344), cap,
           font=cf, fill=GREY)

    d.line([36, 386, W - 36, 386], fill=CARD_LINE, width=2)

    # ---- Story cards: 2 columns x 3 rows ----
    cards = [
        ("UKRAINE  ·  WAR", (179, 49, 42),
         "Kyiv strikes Russian air base",
         "Ukraine says five warplanes were damaged; Poland urges NATO "
         "to act."),
        ("NORTH KOREA", (109, 40, 217),
         "Kim expands nuclear arsenal",
         "Kim Jong Un calls for tactical nuclear weapons in more "
         "domains."),
        ("EGYPT", (15, 118, 110),
         "30 killed in Cairo tanker fire",
         "A fuel tanker crash ignites a blaze above a Giza tunnel; "
         "15 people are injured."),
        ("UNITED STATES", (31, 58, 110),
         "Thanksgiving parade postponed",
         "New York's 100th Macy's parade moves to Saturday as severe "
         "weather hits the US."),
        ("TECHNOLOGY", (180, 83, 9),
         "Nvidia chips reached China",
         "China got Nvidia AI chips despite the rules; SpaceX wins "
         "approval to orbit data centres."),
        ("UNITED STATES", (31, 58, 110),
         "Birthright order blocked again",
         "A second judge blocks Trump's newest order curtailing "
         "birthright citizenship."),
    ]
    cw, ch, gap = 464, 138, 16
    x0, y0 = 36, 404
    for i, (tag, colour, headline, body) in enumerate(cards):
        cx = x0 + (i % 2) * (cw + gap)
        cy = y0 + (i // 2) * (ch + gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=CARD_BG,
                    outline=CARD_LINE, width=2)
        d.rectangle([cx, cy, cx + 6, cy + ch], fill=colour)
        tx = cx + 20
        ty = cy + 12
        d.text((tx, ty), tag, font=SANS_B(17), fill=colour)
        ty += 26
        for line in wrap(d, headline, SERIF_B(24), cw - 34)[:1]:
            d.text((tx, ty), line, font=SERIF_B(24), fill=INK)
            ty += 30
        for line in wrap(d, body, SANS(19), cw - 34)[:2]:
            d.text((tx, ty), line, font=SANS(19), fill=(52, 52, 52))
            ty += 25

    # ---- Also today strip ----
    ay = y0 + 3 * ch + 2 * gap + 14
    d.line([36, ay, W - 36, ay], fill=CARD_LINE, width=2)
    ay += 12
    d.text((36, ay), "ALSO TODAY", font=SANS_B(18), fill=RED)
    ay += 28
    also = [
        ("Hong Kong", "remembers the 168 victims of its housing-complex fire."),
        ("Culture", "Duran Duran guitarist Andy Taylor dies at 65."),
        ("Germany", "Merz: \u201cRussia wants more than Ukraine\u201d as he defends aid for Kyiv."),
    ]
    for label, text in also:
        d.text((52, ay), "\u2022", font=SANS_B(19), fill=RED)
        d.text((72, ay), label + " — ", font=SANS_B(19), fill=INK)
        off = 72 + d.textlength(label + " — ", font=SANS_B(19))
        d.text((off, ay), text, font=SANS(19), fill=(52, 52, 52))
        ay += 27

    # ---- Footer ----
    foot = "26 November 2026  ·  The world's news in one image"
    ff = SANS(17)
    d.text(((W - d.textlength(foot, font=ff)) / 2, H - 34), foot,
           font=ff, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
