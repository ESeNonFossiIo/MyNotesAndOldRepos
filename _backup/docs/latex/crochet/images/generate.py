"""Generate cartoon placeholder JPEGs for the amigurumi patterns."""

from PIL import Image, ImageDraw

W, H = 800, 800
BG = (250, 246, 235)  # cream paper
OUTLINE = (40, 30, 20)


def ellipse(draw, cx, cy, rx, ry, fill, outline=OUTLINE, width=4):
    draw.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=fill, outline=outline, width=width)


def draw_dino(path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    green = (108, 158, 76)
    dark_green = (78, 118, 56)
    cream = (245, 226, 187)
    yellow = (240, 198, 92)

    # tail
    ellipse(d, 200, 540, 90, 70, green)
    # body
    ellipse(d, 400, 540, 200, 180, green)
    # belly patch
    ellipse(d, 400, 580, 110, 110, cream, outline=dark_green, width=2)
    # legs
    ellipse(d, 320, 700, 55, 45, green)
    ellipse(d, 480, 700, 55, 45, green)
    # arms
    ellipse(d, 240, 520, 40, 30, green)
    ellipse(d, 560, 520, 40, 30, green)
    # head
    ellipse(d, 420, 290, 180, 160, green)
    # muzzle
    ellipse(d, 470, 340, 95, 70, dark_green, outline=OUTLINE, width=3)
    # spikes along back
    for i, (cx, cy) in enumerate([(280, 360), (340, 300), (410, 270), (480, 280)]):
        d.polygon([(cx - 22, cy + 30), (cx + 22, cy + 30), (cx, cy - 35)],
                  fill=yellow, outline=OUTLINE)
    # eyes
    ellipse(d, 370, 250, 22, 22, (255, 255, 255), width=3)
    ellipse(d, 460, 250, 22, 22, (255, 255, 255), width=3)
    ellipse(d, 372, 254, 10, 10, OUTLINE, outline=OUTLINE)
    ellipse(d, 462, 254, 10, 10, OUTLINE, outline=OUTLINE)
    # nostrils
    ellipse(d, 445, 330, 5, 5, OUTLINE, outline=OUTLINE)
    ellipse(d, 475, 330, 5, 5, OUTLINE, outline=OUTLINE)
    # smile
    d.arc((430, 350, 510, 390), start=20, end=160, fill=OUTLINE, width=3)

    img.save(path, "JPEG", quality=88)


def draw_bear(path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    brown = (158, 110, 70)
    dark_brown = (110, 75, 45)
    cream = (245, 226, 187)
    red = (190, 60, 60)

    # legs
    ellipse(d, 320, 700, 70, 55, brown)
    ellipse(d, 480, 700, 70, 55, brown)
    ellipse(d, 320, 720, 35, 22, cream, outline=dark_brown, width=2)
    ellipse(d, 480, 720, 35, 22, cream, outline=dark_brown, width=2)
    # arms
    ellipse(d, 210, 500, 55, 75, brown)
    ellipse(d, 590, 500, 55, 75, brown)
    # body
    ellipse(d, 400, 520, 175, 170, brown)
    # bow tie (just below head)
    d.polygon([(360, 330), (340, 305), (340, 355)], fill=red, outline=OUTLINE)
    d.polygon([(440, 330), (460, 305), (460, 355)], fill=red, outline=OUTLINE)
    ellipse(d, 400, 330, 14, 14, red)
    # head
    ellipse(d, 400, 240, 175, 160, brown)
    # ears (outer + inner)
    ellipse(d, 280, 130, 55, 55, brown)
    ellipse(d, 520, 130, 55, 55, brown)
    ellipse(d, 280, 135, 28, 28, cream, outline=dark_brown, width=2)
    ellipse(d, 520, 135, 28, 28, cream, outline=dark_brown, width=2)
    # muzzle
    ellipse(d, 400, 285, 90, 65, cream, outline=dark_brown, width=3)
    # nose
    ellipse(d, 400, 260, 18, 13, OUTLINE)
    # mouth
    d.line((400, 273, 400, 295), fill=OUTLINE, width=3)
    d.arc((375, 285, 405, 315), start=0, end=90, fill=OUTLINE, width=3)
    d.arc((395, 285, 425, 315), start=90, end=180, fill=OUTLINE, width=3)
    # eyes
    ellipse(d, 345, 220, 16, 16, OUTLINE, outline=OUTLINE)
    ellipse(d, 455, 220, 16, 16, OUTLINE, outline=OUTLINE)
    ellipse(d, 349, 216, 5, 5, (255, 255, 255), outline=(255, 255, 255))
    ellipse(d, 459, 216, 5, 5, (255, 255, 255), outline=(255, 255, 255))

    img.save(path, "JPEG", quality=88)


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    draw_dino(os.path.join(here, "baby-dino.jpg"))
    draw_bear(os.path.join(here, "teddy-bear.jpg"))
    print("Generated baby-dino.jpg and teddy-bear.jpg")
