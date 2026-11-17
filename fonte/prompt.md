# Prompt — folha de posições da salat (IA)

Usado para gerar as imagens deste repositório. Gere **uma única imagem quadrada (1:1), na maior resolução disponível**, anexando a referência de postura abaixo.

**Referência de postura (CC0, livre):** Ayman Alhasan, *Salat or Muslim Prayers — Illustration showing the sequence and recitations made in each posture*, Wikimedia Commons —
https://upload.wikimedia.org/wikipedia/commons/6/60/Salat_or_Muslim_Prayers_-_Illustration_showing_the_sequence_and_recitations_made_in_each_posture.jpg

As imagens do Depositphotos **não** são enviadas à IA: são material licenciado, e as prévias só podem ser usadas para avaliação. Delas veio apenas a ideia (lista de posições e o "certo × errado").

## Prompt

```
Educational character sheet: a clean 3x3 grid of 9 equal square panels separated by thin cream gutters, showing the postures of the Islamic prayer (salah), drawn as a flat vector illustration with soft shading and clean dark outlines, friendly and respectful style, consistent proportions in every panel.

Use the reference image ONLY as a guide for correct body postures (the overlapping silhouettes on its left side). Ignore all of its text, colors and layout.

CHARACTER (identical in all 9 panels): an adult man in his late 20s, light-brown skin, short neat black beard, calm expression, eyes looking down; wearing a long plain white thobe (ankle-length robe) and a small white knitted kufi cap; barefoot.

EVERY PANEL: the same deep maroon prayer rug with a thin gold border lying flat on the floor; plain warm cream background (#f6f1e7); full body visible with margin; no text, no letters, no numbers, no labels, no arrows, no extra people.

Panels 1 to 7 are a strict SIDE VIEW (profile) with the man facing toward the RIGHT edge of the panel. Panels 8 and 9 are a FRONT VIEW.

1 (top-left) Standing upright and still, feet slightly apart, both arms hanging relaxed at his sides, gaze lowered to the floor.
2 (top-middle) Opening takbir: standing, both arms raised with elbows bent, the two hands held APART, one on each side of the head beside the ears, palms open and facing forward (toward the right), fingers pointing straight up, thumbs level with the earlobes. The hands do NOT touch each other and are NOT joined in front of the face.
3 (top-right) Standing, right hand placed over the left wrist on the chest, gaze lowered.
4 (middle-left) Bowing (ruku): legs straight and vertical, upper body bent forward exactly 90 degrees so the back is FLAT and HORIZONTAL like a table top, head level in line with the back (not hanging down), arms straight with both palms gripping the kneecaps, fingers spread.
5 (center) Prostration (sujud): forehead and nose touching the rug, both palms flat on the rug beside the head, FOREARMS LIFTED off the floor and elbows away from the body, both knees on the rug, toes of both feet touching the rug and bent forward, hips raised higher than the head.
6 (middle-right) Sitting between prostrations: kneeling and sitting on his left foot laid flat under him, right foot upright behind him with toes bent forward on the rug, back straight, both hands resting flat on the thighs near the knees.
7 (bottom-left) Tashahhud: same sitting position as panel 6; BOTH hands stay RESTING ON THE THIGHS; on the right hand only the index finger is lifted slightly, pointing forward, the other fingers closed; the arm is NOT extended and he is NOT pointing at anyone.
8 (bottom-middle) Final greeting to the right: front view, sitting in the same kneeling position, hands on thighs, head turned clearly toward HIS OWN RIGHT shoulder (the viewer's LEFT side of the image).
9 (bottom-right) Final greeting to the left: front view, same sitting position, hands on thighs, head turned clearly toward HIS OWN LEFT shoulder (the viewer's RIGHT side of the image).
```

## Depois de gerar

Salvar a folha em `fonte/folha-chatgpt-vN.png` e rodar, na raiz do repositório:

```
python3 fonte/crop_sheet.py fonte/folha-chatgpt-vN.png posicoes
```

Conferir cada posição antes de publicar (a IA erra detalhes — ver histórico abaixo).

## Prompt de correção — só o rukuʿ

Na mesma conversa em que a folha foi gerada:

```
Redraw ONLY panel 4 (ruku) as a single square image, same man, same white thobe and kufi, same maroon rug and cream background, same flat vector style, side view facing right. Correct the posture: legs straight and vertical, upper body bent forward exactly 90 degrees so the back is completely FLAT and HORIZONTAL like a table top, parallel to the floor; head level in line with the back, not hanging down and not raised; arms straight and vertical, palms gripping the kneecaps with fingers spread.
```

Salvar como `fonte/ruku-chatgpt-v1.png`.

## Histórico

- 2026-11-17 — 1ª tentativa (OpenArt, Nano Banana 2, 30 créditos, plano grátis). Saiu com **marca d'água "OpenArt"** sobre a fileira do meio e 3 erros: takbir com as mãos juntas na frente do rosto, rukuʿ com as costas curvadas e as mãos abaixo dos joelhos, tashahhud apontando com o braço esticado. Acertou: em pé, qiyam, sujud (com antebraços no chão — corrigido no prompt), jalsah e as duas saudações. O prompt acima já inclui as correções.
- 2026-11-17 — 2ª tentativa (ChatGPT, folha 1254 px, `fonte/folha-chatgpt-v1.png`). **8 de 9 corretas**: em pé, takbir (mãos separadas ao lado das orelhas), qiyam, sujud, jalsah, tashahhud (mão na coxa, indicador levantado) e as duas saudações (virada de cabeça sutil, mas para o lado certo). **Rukuʿ errado**: costas inclinadas (~35°) em vez de horizontais — guardado em `erros/ruku-costas-inclinadas.webp` como exemplo do erro comum.
