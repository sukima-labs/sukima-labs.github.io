# sukima-labs.github.io

Portada de la organización [sukima-labs](https://github.com/sukima-labs): <https://sukimalabs.com/> (dominio propio desde el 11-11-2026, registrado en la cuenta de Cloudflare `sukima-labs`; el fichero `CNAME` lo fija y los proyectos cuelgan de él: `sukimalabs.com/finde/`, `/descargo/`, `/atlasonu/`; las direcciones `sukima-labs.github.io/...` redirigen solas).

HTML estático a mano, sin generador, sobre la plantilla gratuita [Mercer Lite](https://github.com/mikesmithdesign/mercer-lite) de Mike Smith Design (licencia en `LICENSE-plantilla.md`: uso comercial libre, no se puede revender la plantilla). Cambios: acento azul de Finde, sin Lenis ni ningún script de terceros, fuentes alojadas aquí. **11-11-2026: aplicado el manual de marca** (`sukima-labs/marca`, tokens de `03_DIGITAL/Web/brand_tokens.css`): colores grafito `#10131C`, cian `#14C6D4`, violeta `#7148F5` (solo como relleno con letra blanca) y marfil `#F5F4F0`, y tipografía oficial **DejaVu Sans** (regular y bold en `fonts/DejaVuSans*.ttf`, licencia en `fonts/DEJAVU-LICENSE.txt`; se usa en cuerpo y títulos, con IBM Plex Mono solo en las etiquetas pequeñas). Archivo y Chakra Petch siguen alojadas en `fonts/` (con sus textos OFL) por si se revierte. El isotipo blanco de la marca entra en cabecera y pie (`img/isotipo_white.svg`, del manual: avatar = isotipo sin eslogan). **Pendiente:** regenerar `img/og.jpg` (lleva los colores anteriores; se fotografía `herramientas/og.html` a 1200×630). Cada proyecto con GitHub Pages cuelga de aquí (`/finde/` lo sirve el repo `finde`), así que la propiedad de Google Search Console de la raíz los cubre a todos.


## Marca

`marca/` es la fuente única de la identidad v1.1 para todos los proyectos de Sukima Labs (traída del PR #3; la portada en sí la aplicó el #4):

- `marca/marca.css`: tokens (`--sk-*`: colores, letra, tamaños mínimos, área de seguridad, tema claro y oscuro). Los demás proyectos enlazan <https://sukimalabs.com/marca/marca.css> en vez de copiarlo.
- `marca/logo/`: isotipo y logotipos en SVG (el texto ya convertido a trazos, para que no dependa de la letra instalada) y los favicons.
- `marca/fuentes/`: DejaVu Sans en woff2 (subconjunto latino) y su licencia, que tiene que viajar con los ficheros.
- `marca/REGLAS.md` y `marca/COBERTURA.md`: las reglas del manual, cada una con su página, y cuáles están aplicadas.

- **No quitar** el fichero `CNAME`: es lo que sirve la web (y todos los proyectos) en `sukimalabs.com`. El DNS vive en la zona de Cloudflare `sukima-labs` y el dominio está verificado en la org (Settings → Pages), así que nadie más puede apuntarlo a otra web de GitHub.
- **No quitar** la etiqueta `google-site-verification` de `index.html`: es la verificación de Search Console.
- Proyecto nuevo publicado → un `<article class="proj">` en `index.html` (imagen 1200×630 en `img/`, sirve la de compartir del proyecto) y línea en `sitemap.xml`.

- La vista previa al compartir el enlace (WhatsApp, redes) es `img/og.jpg`, que sale de `herramientas/og.html`: si cambia el titular o los colores, se regenera fotografiando esa página a 1200×630.
