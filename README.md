# Cheil Studio

Página do Cheil Studio (Creative Production Hub), em português e inglês.

- `docs/` é o que vai ao ar. Português em `/`, inglês em `/en/`.
- `build.py` gera os dois HTMLs a partir de um template só. Os textos PT e EN ficam no dicionário `T`, no começo do arquivo.
- `sizes.json` guarda largura e altura das imagens, usadas pelo `build.py`.

## Editar

1. Mude o texto em `build.py`.
2. Rode `python3 build.py`.
3. Faça commit e push na `main`. O GitHub Pages publica sozinho em um ou dois minutos.

Estilo e animações ficam em `docs/assets/site.css`. O comportamento (vídeos, entradas no scroll, barra de progresso) fica em `docs/assets/site.js`.

## Vídeos

Os três filmes ficam no YouTube (canal Cheil Brasil). O player só carrega quando a pessoa clica no pôster, para a página abrir leve. Os IDs ficam em `VIDEOS`, no `build.py`.

## Hospedagem

GitHub Pages, publicando a pasta `docs` da branch `main`. Endereço: https://femenge.github.io/cheil-studio/

## Fontes

Bodoni Moda e IBM Plex Sans, as duas sob SIL Open Font License, servidas de `docs/assets/fonts/`.
