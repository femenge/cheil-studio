// Cheil Studio — interações da página (sem bibliotecas).

// 1) Vídeos: o player do YouTube só carrega quando a pessoa clica no pôster,
//    então a página abre leve. Sem JavaScript, o link abre o vídeo no YouTube.
document.querySelectorAll('a.video[data-yt]').forEach(function (link) {
  link.addEventListener('click', function (event) {
    if (event.metaKey || event.ctrlKey || event.shiftKey) return;
    event.preventDefault();
    var frame = document.createElement('iframe');
    frame.src = 'https://www.youtube-nocookie.com/embed/' + link.dataset.yt +
      '?autoplay=1&rel=0&playsinline=1&modestbranding=1';
    frame.title = link.dataset.title || 'YouTube';
    frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    var box = document.createElement('div');
    box.className = 'video is-playing';
    var poster = link.querySelector('img');
    if (poster) box.appendChild(poster);
    box.appendChild(frame);
    link.replaceWith(box);
    frame.addEventListener('load', function () { box.classList.add('is-loaded'); });
    frame.focus();
  });
});

// 2) Entradas no scroll: cada bloco com data-reveal ganha a classe "in"
//    quando entra na tela. O CSS cuida do movimento.
//    As imagens desses blocos começam recortadas, e o navegador não carrega
//    imagem "lazy" que está 100% recortada. Por isso um segundo observador
//    adianta o carregamento um pouco antes de o bloco chegar na tela, e a
//    entrada só começa quando a imagem já está pronta.
(function () {
  var items = document.querySelectorAll('[data-reveal]');
  if (!('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('in'); });
    return;
  }
  function images(el) { return Array.prototype.slice.call(el.querySelectorAll('img')); }
  function ready(el) {
    var waits = images(el).map(function (img) {
      img.loading = 'eager';
      if (img.complete) return Promise.resolve();
      return img.decode ? img.decode().catch(function () {}) : Promise.resolve();
    });
    var limit = new Promise(function (resolve) { setTimeout(resolve, 1800); });
    return Promise.race([Promise.all(waits), limit]);
  }
  var preload = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      images(entry.target).forEach(function (img) { img.loading = 'eager'; });
      preload.unobserve(entry.target);
    });
  }, { rootMargin: '900px 0px 900px 0px' });
  var reveal = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      reveal.unobserve(el);
      ready(el).then(function () { el.classList.add('in'); });
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
  items.forEach(function (el) { preload.observe(el); reveal.observe(el); });
})();

// 3) Barra de progresso de leitura no topo (faixa de cores da Cheil).
(function () {
  var bar = document.querySelector('.progress');
  if (!bar) return;
  var ticking = false;
  function update() {
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
    bar.style.setProperty('--p', (p * 100).toFixed(2) + '%');
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  window.addEventListener('resize', update);
  update();
})();
