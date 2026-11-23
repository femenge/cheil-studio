# Cheil Studio

Página do Cheil Studio (Creative Production Hub), em português e inglês.

- `site/` é o que vai ao ar. Português em `/`, inglês em `/en/`.
- `build.py` gera os dois HTMLs a partir de um template só. Os textos PT e EN ficam no dicionário `T`, no começo do arquivo.
- `sizes.json` guarda largura e altura das imagens, usadas pelo `build.py`.

## Editar

1. Mude o texto em `build.py`.
2. Rode `python3 build.py`.
3. Faça commit e push na `main`. O Render publica sozinho.

Estilo e animações ficam em `site/assets/site.css`. O comportamento (vídeos, entradas no scroll, barra de progresso) fica em `site/assets/site.js`.

## Vídeos

Os três filmes ficam no YouTube (canal Cheil Brasil). O player só carrega quando a pessoa clica no pôster, para a página abrir leve. Os IDs ficam em `VIDEOS`, no `build.py`.

## Render

Static Site, sem comando de build, com `site` como diretório de publicação.

## Fontes

Bodoni Moda e IBM Plex Sans, as duas sob SIL Open Font License, servidas de `site/assets/fonts/`.
