"""Recorta a folha 3x3 gerada por IA em 9 imagens de posição, em WebP para a web.

Uso:  python3 fonte/crop_sheet.py <folha.png> <pasta_saida> [--flip salam_right,salam_left]
      python3 fonte/crop_sheet.py <imagem.png> <pasta_saida> --single ruku   (uma posição só)

A IA não desenha os painéis em terços exatos, então as calhas brancas entre eles
são detectadas na imagem. Cada painel é aparado pela cor de fundo e centralizado
num quadrado com margem, para todas as posições ficarem no mesmo enquadramento.
"""
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageOps

ORDER = ["itidal", "takbir", "qiyam", "ruku", "sujud", "jalsa", "tashahhud", "salam_right", "salam_left"]
SIZE = 480  # lado final em pixels (~1,6x o tamanho exibido no site; a folha do ChatGPT tem painéis de ~400 px)


def trim(im: Image.Image, bg) -> Image.Image:
    diff = ImageChops.difference(im, Image.new(im.mode, im.size, bg))
    diff = ImageChops.add(diff, diff, 2.0, -18)  # ignora ruído leve do fundo
    box = diff.getbbox()
    return im.crop(box) if box else im


def bands(white_ratio, n_cells: int, length: int):
    """Intervalos [a, b) entre as calhas: linhas/colunas quase todas brancas."""
    is_gutter = [r > 0.85 for r in white_ratio]
    cells, start = [], None
    for i, g in enumerate(is_gutter + [True]):
        if not g and start is None:
            start = i
        elif g and start is not None:
            if i - start > length * 0.1:
                cells.append((start, i))
            start = None
    if len(cells) != n_cells:  # sem calhas visíveis: cai para terços
        step = length / n_cells
        cells = [(int(k * step), int((k + 1) * step)) for k in range(n_cells)]
    return cells


def gutters(sheet: Image.Image):
    gray = sheet.convert("L").point(lambda v: 255 if v > 246 else 0)
    w, h = gray.size
    px = gray.load()
    rows = [sum(px[x, y] for x in range(0, w, 4)) / (255 * len(range(0, w, 4))) for y in range(h)]
    cols = [sum(px[x, y] for y in range(0, h, 4)) / (255 * len(range(0, h, 4))) for x in range(w)]
    return bands(rows, 3, h), bands(cols, 3, w)


def main() -> None:
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    flip = set()
    if "--flip" in sys.argv:
        flip = set(sys.argv[sys.argv.index("--flip") + 1].split(","))
    out.mkdir(parents=True, exist_ok=True)
    sheet = Image.open(src).convert("RGB")
    if "--single" in sys.argv:
        name = sys.argv[sys.argv.index("--single") + 1]
        jobs = [(name, sheet)]
    else:
        rows, cols = gutters(sheet)
        print("linhas", rows, "colunas", cols)
        jobs = []
        for i, name in enumerate(ORDER):
            r, c = divmod(i, 3)
            (y0, y1), (x0, x1) = rows[r], cols[c]
            jobs.append((name, sheet.crop((x0 + 4, y0 + 4, x1 - 4, y1 - 4))))
    for name, cell in jobs:
        bg = cell.getpixel((6, 6))
        fig = trim(cell, bg)
        if name in flip:
            fig = ImageOps.mirror(fig)
        side = int(max(fig.size) * 1.12)
        canvas = Image.new("RGB", (side, side), bg)
        canvas.paste(fig, ((side - fig.width) // 2, side - fig.height - int(side * 0.05)))
        canvas = canvas.resize((SIZE, SIZE), Image.LANCZOS)
        canvas.save(out / f"{name}.webp", "WEBP", quality=86, method=6)
        print(name, fig.size)


main()
