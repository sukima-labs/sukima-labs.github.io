# sukima-labs.github.io

Portada de la organización [sukima-labs](https://github.com/sukima-labs): <https://sukimalabs.com/> (dominio propio desde el 11-11-2026, registrado en la cuenta de Cloudflare `sukima-labs`; el fichero `CNAME` lo fija y los proyectos cuelgan de él: `sukimalabs.com/finde/`, `/descargo/`, `/atlasonu/`; las direcciones `sukima-labs.github.io/...` redirigen solas).

HTML estático a mano, sin generador, sobre la plantilla gratuita [Mercer Lite](https://github.com/mikesmithdesign/mercer-lite) de Mike Smith Design (licencia en `LICENSE-plantilla.md`: uso comercial libre, no se puede revender la plantilla). Cambios: acento azul de Finde, sin Lenis ni ningún script de terceros, fuentes alojadas aquí (Archivo, IBM Plex Mono y Chakra Petch, las tres con licencia SIL OFL 1.1: sus textos están en `fonts/OFL-*.txt` y tienen que viajar con los ficheros). Cada proyecto con GitHub Pages cuelga de aquí (`/finde/` lo sirve el repo `finde`), así que la propiedad de Google Search Console de la raíz los cubre a todos.

- **No quitar** el fichero `CNAME`: es lo que sirve la web (y todos los proyectos) en `sukimalabs.com`. El DNS vive en la zona de Cloudflare `sukima-labs` y el dominio está verificado en la org (Settings → Pages), así que nadie más puede apuntarlo a otra web de GitHub.
- **No quitar** la etiqueta `google-site-verification` de `index.html`: es la verificación de Search Console.
- Proyecto nuevo publicado → un `<article class="proj">` en `index.html` (imagen 1200×630 en `img/`, sirve la de compartir del proyecto) y línea en `sitemap.xml`.

- La vista previa al compartir el enlace (WhatsApp, redes) es `img/og-v2.png`, generada desde `herramientas/og.html` (diseño) con `herramientas/render-og.py` (script PIL, usa las DejaVu de `fonts/`; requiere el Python de las herramientas de Hermes). Si cambia el titular o los colores, se regenera el script y se sube la imagen nueva (el nombre con versión — og-v2, og-v3… — evita la caché de WhatsApp).
