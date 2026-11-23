#!/usr/bin/env python3
"""Gera o site Cheil Studio (PT em /, EN em /en/) a partir de um template único."""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
SZ = json.load(open(os.path.join(ROOT, "sizes.json")))

VIDEOS = {
    "rugged": "Mpg3vCMuUq4",
    "frame": "--p7Br24lgE",
    "halloween": "gDC9ayivP5s",
}

T = {
    "pt": {
        "lang": "pt-BR",
        "title": "Cheil Studio | Creative Production Hub",
        "desc": "Cheil Studio conecta craft, 3D, produção e inteligência artificial para transformar conceitos em imagens, conteúdos e experiências.",
        "skip": "Ir para o conteúdo",
        "lk1_s": "O que", "lk1_b": "Fazemos",
        "intro1": 'Conectamos <b>craft</b>, <b>3D</b>, <b>produção</b> e <b>inteligência artificial</b> para transformar conceitos em imagens, conteúdos e experiências.',
        "intro2": "Criação e produção trabalham juntas desde o início, combinando visão criativa e expertise técnico para explorar novas possibilidades, testar abordagens e encontrar novas formas de materializar cada ideia.",
        "intro3": 'Onde <b>criatividade</b>, <b>tecnologia</b> e <b>produção</b> dão vida a novas histórias.',
        "intro4a": "Com eficiência sem perder qualidade.", "intro4b": "Escalando sem perder controle.",
        "bg_h": "Background",
        "bg_p": "Trabalhamos na junção de 3D com CGI antes mesmo deste boom da IA.",
        "df_h": "Diferencial",
        "df_p": "Com background de 3D, conseguimos garantir a fidelidade dos produtos mesmo nos assets gerados com IA.",
        "alt_sam": "Imagem da SAM criada pelo Cheil Studio",
        "alt_home": "Imagem criada pelo Cheil Studio com produto em ambiente doméstico",
        "lk2_s1": "O que já", "lk2_b": "Fizemos", "lk2_s2": "até aqui",
        "alt_kv1": "Key visual da TV Samsung Mini LED",
        "alt_kv2": "Key visual da fábrica MG Motor no Brasil",
        "film_h": "O primeiro filme",
        "film_p1": "Este é o primeiro filme produzido pelo Cheil Studio, desenvolvido por meio de um processo completo de produção com Inteligência Artificial.",
        "film_p2": "Para garantir a máxima fidelidade visual ao produto, desenvolvemos um LoRA exclusivo a partir de imagens de referência, em um processo minucioso e essencial para a consistência das imagens geradas.",
        "film_p3": "O resultado é um filme com linguagem cinematográfica, que explora movimentos de câmera e transições dinâmicas para transformar uma apresentação de produto em uma experiência visual mais envolvente.",
        "prod_l": "Imagens do produto",
        "alt_prod": "Imagem de referência do produto",
        "alt_ds": "Dataset de imagens usado no treinamento do LoRA",
        "alt_out": "Imagem do produto gerada com o LoRA",
        "play": "Assistir",
        "v_rugged": "Filme do smartphone robusto da Samsung",
        "v_frame": "The Frame", "v_halloween": "Halloween",
        "wf_h": "Workflow",
        "wf_g1": "Etapas de criação", "wf_g2": "Etapas de produção",
        "steps": [
            ("Briefing", "Análise do projeto, objetivos, referências e características dos produtos."),
            ("Conceito &amp; Roteiro", "Desenvolvimento do conceito, roteiro e linguagem cinematográfica."),
            ("Storyboard", "Planejamento dos planos, enquadramentos, composição e estética."),
            ("Assets &amp; LoRA", "Preparação de referências e, quando necessário, treinamento de LoRAs específicos para preservar a identidade visual dos produtos."),
            ("Geração de imagens", "Geração dos keyframes e refinamento de composição, iluminação e consistência."),
            ("Geração de vídeo", "Animação dos planos, movimentos de câmera, ações e transições."),
            ("Pós-produção", "Montagem, efeitos visuais, color grading, sound design e trilha sonora."),
            ("Finalização", "Revisão técnica e criativa, ajustes e exportação dos formatos finais."),
        ],
        "sv_h": "Serviços &amp; time",
        "services": [
            ("Cheil Zero", "Conteúdo em escala com IA",
             "Automação e desdobramento de peças para diferentes formatos, canais e mercados.",
             ["Abertura e desdobramento de peças", "Adaptação de formatos e canais",
              "Localização de campanhas para LATAM", "Geração de imagens e vídeos em escala"]),
            ("Imagens", "Criação visual generativa",
             "Desenvolvimento de imagens originais com direção de arte e olhar criativo.",
             ["Imagens publicitárias generativas", "Still de produto e lifestyle com 3D/IA",
              "Key Visuals e conceitos visuais", "Criação de cenários e ambientes",
              "Desenvolvimento de personagens", "LoRA e consistência visual de produtos",
              "Retoque, composição e upscale", "Criação de avatares e personagens como a SAM"]),
            ("Audiovisual", "Animações em 3D e filmes em IA",
             "Produção de vídeos de baixa e média complexidade, da concepção à finalização.",
             ["Filmes de produto e demonstração de features",
              ("Vídeos para campanhas digitais e social media",
               "Em caso de produção híbrida (IA + shooting), acionamos produtoras parceiras para a captação."),
              "Animação de imagens e Key Visuals", "Motion graphics e vinhetas",
              "Storyboard e animatics", "Edição, VFX, color grading e sound design"]),
        ],
        "team": [
            ("Direção de arte", "Conceito e curadoria"),
            ("Artista de 3D", "Modelagem, LookDev e render"),
            ("Animador 3D", "Animação 3D"),
            ("Artista de IA", "Imagem, vídeo e voz com IA"),
            ("Editor e pós", "Edição, cor, som e legendas"),
            ("Produção", "Prazo, fluxo e PMO"),
        ],
        "tks": "tks",
        "alt_lion": "",
    },
    "en": {
        "lang": "en",
        "title": "Cheil Studio | Creative Production Hub",
        "desc": "Cheil Studio connects craft, 3D, production and artificial intelligence to turn concepts into images, content and experiences.",
        "skip": "Skip to content",
        "lk1_s": "What", "lk1_b": "We do",
        "intro1": 'We connect <b>craft</b>, <b>3D</b>, <b>production</b> and <b>artificial intelligence</b> to turn concepts into images, content and experiences.',
        "intro2": "Creative and production work together from the start, combining creative vision and technical expertise to explore new possibilities, test approaches and find new ways to bring each idea to life.",
        "intro3": 'Where <b>creativity</b>, <b>technology</b> and <b>production</b> bring new stories to life.',
        "intro4a": "Efficient without losing quality.", "intro4b": "Scaling without losing control.",
        "bg_h": "Background",
        "bg_p": "We were combining 3D and CGI well before the AI boom.",
        "df_h": "Our edge",
        "df_p": "With a 3D background, we keep products true to the original even in AI-generated assets.",
        "alt_sam": "Image of SAM created by Cheil Studio",
        "alt_home": "Image created by Cheil Studio with a product in a home setting",
        "lk2_s1": "What we've", "lk2_b": "Done", "lk2_s2": "so far",
        "alt_kv1": "Key visual for the Samsung Mini LED TV",
        "alt_kv2": "Key visual for the MG Motor factory in Brazil",
        "film_h": "The first film",
        "film_p1": "This is the first film produced by Cheil Studio, made through an end-to-end AI production process.",
        "film_p2": "To keep the product as visually accurate as possible, we trained a dedicated LoRA on reference images, a meticulous process that is essential for consistency across the generated images.",
        "film_p3": "The result is a film with cinematic language, using camera moves and dynamic transitions to turn a product presentation into a more engaging visual experience.",
        "prod_l": "Product images",
        "alt_prod": "Product reference image",
        "alt_ds": "Image dataset used to train the LoRA",
        "alt_out": "Product image generated with the LoRA",
        "play": "Watch",
        "v_rugged": "Film for Samsung's rugged smartphone",
        "v_frame": "The Frame", "v_halloween": "Halloween",
        "wf_h": "Workflow",
        "wf_g1": "Creative stages", "wf_g2": "Production stages",
        "steps": [
            ("Briefing", "Review of the project, goals, references and product features."),
            ("Concept &amp; Script", "Development of the concept, script and cinematic language."),
            ("Storyboard", "Planning of shots, framing, composition and aesthetics."),
            ("Assets &amp; LoRA", "Preparing references and, when needed, training dedicated LoRAs to preserve the products' visual identity."),
            ("Image generation", "Generating keyframes and refining composition, lighting and consistency."),
            ("Video generation", "Animating shots, camera moves, actions and transitions."),
            ("Post-production", "Editing, visual effects, color grading, sound design and score."),
            ("Finishing", "Technical and creative review, adjustments and export of final formats."),
        ],
        "sv_h": "Services &amp; team",
        "services": [
            ("Cheil Zero", "Content at scale with AI",
             "Automating and adapting assets for different formats, channels and markets.",
             ["Asset rollout and adaptation", "Format and channel adaptation",
              "Campaign localization for LATAM", "Image and video generation at scale"]),
            ("Images", "Generative visual creation",
             "Original images developed with art direction and a creative eye.",
             ["Generative advertising images", "Product and lifestyle stills with 3D/AI",
              "Key visuals and visual concepts", "Scene and environment creation",
              "Character development", "LoRA and visual consistency for products",
              "Retouching, compositing and upscaling", "Avatars and characters such as SAM"]),
            ("Audiovisual", "3D animation and AI films",
             "Low- and mid-complexity video production, from concept to finishing.",
             ["Product films and feature demos",
              ("Videos for digital campaigns and social media",
               "For hybrid productions (AI + shooting), we bring in partner production companies for the shoot."),
              "Animation of images and key visuals", "Motion graphics and bumpers",
              "Storyboards and animatics", "Editing, VFX, color grading and sound design"]),
        ],
        "team": [
            ("Art direction", "Concept and curation"),
            ("3D artist", "Modeling, lookdev and rendering"),
            ("3D animator", "3D animation"),
            ("AI artist", "Image, video and voice with AI"),
            ("Editor &amp; post", "Editing, color, sound and subtitles"),
            ("Production", "Deadlines, workflow and PMO"),
        ],
        "tks": "tks",
        "alt_lion": "",
    },
}


def img(name, alt, base, cls="", eager=False):
    w, h = SZ[name]
    c = f' class="{cls}"' if cls else ""
    load = "" if eager else ' loading="lazy" decoding="async"'
    return f'<img src="{base}assets/img/{name}.webp" width="{w}" height="{h}" alt="{html.escape(alt, quote=True)}"{c}{load}>'


def strip(names, alt, base):
    out = []
    for i, n in enumerate(names):
        w, h = SZ[n]
        out.append(f'<li style="--ar:{w / h:.4f};--i:{i}" data-reveal="img">{img(n, alt, base)}</li>')
    return "\n          ".join(out)


def video(key, label, t, base):
    vid = VIDEOS[key]
    w, h = SZ[f"poster-{key}"]
    return f'''<a class="video" href="https://youtube.com/shorts/{vid}" data-yt="{vid}" data-title="{html.escape(label, quote=True)}" target="_blank" rel="noopener">
          <img src="{base}assets/img/poster-{key}.webp" width="{w}" height="{h}" alt="" loading="lazy" decoding="async">
          <span class="play" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22"><path d="M8 5v14l11-7z" fill="currentColor"/></svg></span>
          <span class="sr">{t["play"]}: {label}</span>
        </a>'''


def render(code):
    t = T[code]
    base = "" if code == "pt" else "../"
    pt_href = "./" if code == "pt" else "../"
    en_href = "en/" if code == "pt" else "./"
    cur = lambda c: ' aria-current="true"' if c == code else ""
    langnav = (f'<a href="{pt_href}" lang="pt-BR" hreflang="pt-BR"{cur("pt")}>PT</a>'
               f'<span aria-hidden="true">/</span>'
               f'<a href="{en_href}" lang="en" hreflang="en"{cur("en")}>EN</a>')

    steps = []
    for i, (h3, p) in enumerate(t["steps"], 1):
        if i == 1:
            steps.append(f'<li class="wf-group g1" data-reveal="up"><span>{t["wf_g1"]}</span></li>')
        if i == 4:
            steps.append(f'<li class="wf-group g2" data-reveal="up" style="--i:3"><span>{t["wf_g2"]}</span></li>')
        steps.append(f'<li class="step s{i}" data-reveal="up" style="--i:{(i - 1) % 4}"><span class="num">{i:02d}</span><h3>{h3}</h3><p>{p}</p></li>')
    steps = "\n        ".join(steps)

    services = []
    for si, (label, h3, lead, items) in enumerate(t["services"]):
        lis = []
        for it in items:
            if isinstance(it, tuple):
                lis.append(f'<li>{it[0]}<small>{it[1]}</small></li>')
            else:
                lis.append(f"<li>{it}</li>")
        services.append(f'''<article class="service" data-reveal="up" style="--i:{si}">
          <p class="kicker">{label}</p>
          <h3>{h3}</h3>
          <p class="lead">{lead}</p>
          <ul>{"".join(lis)}</ul>
        </article>''')
    services = "\n        ".join(services)

    team = "\n          ".join(f'<li data-reveal="up" style="--i:{i}"><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(t["team"]))

    prod = "".join(img(n, t["alt_prod"], base).replace("<img ", f'<img style="--i:{i}" ', 1) for i, n in enumerate(
                   ["p-front", "p-back", "p-side-l", "p-back-l", "p-front-l", "p-back-r", "p-side-r", "p-front-r"]))

    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#000000">
<link rel="alternate" hreflang="pt-BR" href="{pt_href}">
<link rel="alternate" hreflang="en" href="{en_href}">
<link rel="icon" href="{base}assets/img/favicon.png" type="image/png">
<link rel="preload" href="{base}assets/fonts/bodoni-moda-latin-900-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{base}assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{base}assets/site.css">
<script>
(function (d) {{
  d.classList.add("js");
  document.addEventListener("DOMContentLoaded", function () {{
    requestAnimationFrame(function () {{ d.classList.add("ready"); }});
  }});
}})(document.documentElement);
</script>
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">{t["skip"]}</a>
<nav class="lang" aria-label="Idioma / Language">{langnav}</nav>

<header class="hero">
  <div class="hero-brand">
    <img src="{base}assets/img/cheil-studio.png" width="1365" height="301" alt="Cheil Studio, Creative Production Hub">
  </div>
  <div class="hero-copy">
    <h1 class="lockup">
      <span class="lk-s">{t["lk1_s"]}</span>
      <span class="lk-b">{t["lk1_b"]}</span>
      <span class="lk-q">?</span>
    </h1>
    <div class="intro">
      <p>{t["intro1"]}</p>
      <p>{t["intro2"]}</p>
      <p>{t["intro3"]}</p>
      <p class="close">{t["intro4a"]}<br>{t["intro4b"]}</p>
    </div>
  </div>
</header>

<main id="main">

  <section class="light proof">
    <div class="proof-row">
      <h2 class="rule-left" data-reveal="title"><span>{t["bg_h"]}</span></h2>
      <div class="proof-body">
        <p data-reveal="up">{t["bg_p"]}</p>
        <ul class="strip">
          {strip(["bg-1", "bg-2", "bg-3", "bg-4", "bg-5"], t["alt_sam"], base)}
        </ul>
      </div>
    </div>
    <div class="proof-row">
      <h2 class="rule-right" data-reveal="title"><span>{t["df_h"]}</span></h2>
      <div class="proof-body">
        <p data-reveal="up">{t["df_p"]}</p>
        <ul class="strip">
          {strip(["df-1", "df-2", "df-3", "df-4", "df-5"], t["alt_home"], base)}
        </ul>
      </div>
    </div>
  </section>

  <section class="dark work">
    <h2 class="lockup lockup-2" data-reveal="lockup">
      <span class="lk-s">{t["lk2_s1"]}</span>
      <span class="lk-b">{t["lk2_b"]}</span>
      <span class="lk-s lk-s2">{t["lk2_s2"]}</span>
      <span class="lk-q">?</span>
    </h2>
    <figure class="kv" data-reveal="wipe">{img("kv-samsung", t["alt_kv1"], base)}</figure>
    <figure class="kv" data-reveal="wipe">{img("kv-mg", t["alt_kv2"], base)}</figure>

    <div class="film">
      <div class="film-video" data-reveal="img">
        {video("rugged", t["v_rugged"], t, base)}
      </div>
      <div class="film-text">
        <h2 data-reveal="title"><span>{t["film_h"]}</span></h2>
        <p data-reveal="up" style="--i:1">{t["film_p1"]}</p>
        <p data-reveal="up" style="--i:2">{t["film_p2"]}</p>
        <p data-reveal="up" style="--i:3">{t["film_p3"]}</p>
      </div>
      <figure class="film-product" data-reveal="phones">
        <figcaption>{t["prod_l"]}</figcaption>
        <div class="phones">{prod}</div>
      </figure>
      <div class="film-lora">
        <figure data-reveal="up">
          <figcaption>LoRA <span>/</span> <b>Dataset</b></figcaption>
          {img("lora-dataset", t["alt_ds"], base)}
        </figure>
        <figure data-reveal="up" style="--i:1">
          <figcaption>LoRA <span>/</span> <b>Output</b></figcaption>
          {img("lora-output", t["alt_out"], base)}
        </figure>
      </div>
    </div>

    <div class="shorts">
      <div class="short" data-reveal="short">
        <h2><span>{t["v_frame"]}</span></h2>
        {video("frame", t["v_frame"], t, base)}
      </div>
      <div class="short" data-reveal="short" style="--i:1">
        <h2><span>{t["v_halloween"]}</span></h2>
        {video("halloween", t["v_halloween"], t, base)}
      </div>
    </div>
  </section>

  <section class="light workflow">
    <h2 class="rule-left" data-reveal="title"><span>{t["wf_h"]}</span></h2>
    <ol class="steps">
        {steps}
    </ol>
  </section>

  <section class="light services">
    <h2 class="rule-left" data-reveal="title"><span>{t["sv_h"]}</span></h2>
    <div class="service-grid">
        {services}
    </div>
    <ul class="team">
          {team}
    </ul>
  </section>

</main>

<footer class="end">
  <img class="end-logo" src="{base}assets/img/cheil.png" width="400" height="123" alt="Cheil">
  <p class="lockup lockup-end" aria-label="Thanks!" data-reveal="lockup">
    <span class="lk-b">{t["tks"]}</span>
    <span class="lk-q">!</span>
  </p>
  <img class="end-lion" data-reveal="lion" src="{base}assets/img/lion.webp" width="{SZ["lion"][0]}" height="{SZ["lion"][1]}" alt="" loading="lazy" decoding="async">
  <nav class="lang-end" aria-label="Idioma / Language">{langnav}</nav>
  <div class="end-strip" aria-hidden="true"></div>
</footer>

<script src="{base}assets/site.js" defer onerror="document.documentElement.classList.remove('js')"></script>
</body>
</html>
'''


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "en"), exist_ok=True)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(render("pt"))
    open(os.path.join(OUT, "en", "index.html"), "w", encoding="utf-8").write(render("en"))
    print("ok")
