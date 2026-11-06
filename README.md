# sukima-labs.github.io

Portada de la organización [sukima-labs](https://github.com/sukima-labs): <https://sukima-labs.github.io/>.

HTML estático a mano, sin generador, sobre la plantilla gratuita [Mercer Lite](https://github.com/mikesmithdesign/mercer-lite) de Mike Smith Design (licencia en `LICENSE-plantilla.md`: uso comercial libre, no se puede revender la plantilla). Cambios: acento azul de Finde, sin Lenis ni ningún script de terceros, fuentes alojadas aquí (Archivo, IBM Plex Mono y Chakra Petch, las tres con licencia SIL OFL 1.1: sus textos están en `fonts/OFL-*.txt` y tienen que viajar con los ficheros). Cada proyecto con GitHub Pages cuelga de aquí (`/finde/` lo sirve el repo `finde`), así que la propiedad de Google Search Console de la raíz los cubre a todos.

- **No quitar** la etiqueta `google-site-verification` de `index.html`: es la verificación de Search Console.
- Proyecto nuevo publicado → un `<article class="proj">` en `index.html` (imagen 1200×630 en `img/`, sirve la de compartir del proyecto) y línea en `sitemap.xml`.

- La vista previa al compartir el enlace (WhatsApp, redes) es `img/og.jpg`, que sale de `herramientas/og.html`: si cambia el titular o los colores, se regenera fotografiando esa página a 1200×630.
