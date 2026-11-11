# sukima-labs.github.io

Portada de la organización [sukima-labs](https://github.com/sukima-labs): <https://sukimalabs.com/> (dominio propio desde el 11-11-2026, registrado en la cuenta de Cloudflare `sukima-labs`; el fichero `CNAME` lo fija y los proyectos cuelgan de él: `sukimalabs.com/finde/`, `/descargo/`, `/atlasonu/`; las direcciones `sukima-labs.github.io/...` redirigen solas).

## Marca

`marca/` es la fuente única de la identidad v1.1 para todos los proyectos de Sukima Labs:

- `marca/marca.css`: tokens (`--sk-*`: colores, letra, tamaños mínimos, área de seguridad, tema claro y oscuro). Los demás proyectos enlazan <https://sukima-labs.github.io/marca/marca.css> en vez de copiarlo.
- `marca/logo/`: isotipo y logotipos en SVG (el texto ya convertido a trazos, para que no dependa de la letra instalada) y los favicons.
- `marca/fuentes/`: DejaVu Sans en woff2 (subconjunto latino) y su licencia, que tiene que viajar con los ficheros.
- `marca/REGLAS.md`: reglas cortas, cada una con su manual y página. `marca/COBERTURA.md`: cada regla de los 8 manuales y dónde se aplica o por qué no.

Los manuales originales están en el kDrive de la organización (`Marca/v1.1 - Entrega integral logotipo 04/`), no aquí.

HTML estático a mano, sin generador, sobre la plantilla gratuita [Mercer Lite](https://github.com/mikesmithdesign/mercer-lite) de Mike Smith Design (licencia en `LICENSE-plantilla.md`: uso comercial libre, no se puede revender la plantilla). Cambios: colores, letra y logotipo de la identidad de marca v1.1 (`marca/`), sin Lenis ni ningún script de terceros. Cada proyecto con GitHub Pages cuelga de aquí (`/finde/` lo sirve el repo `finde`), así que la propiedad de Google Search Console de la raíz los cubre a todos.

- **No quitar** el fichero `CNAME`: es lo que sirve la web (y todos los proyectos) en `sukimalabs.com`. El DNS vive en la zona de Cloudflare `sukima-labs` y el dominio está verificado en la org (Settings → Pages), así que nadie más puede apuntarlo a otra web de GitHub.
- **No quitar** la etiqueta `google-site-verification` de `index.html`: es la verificación de Search Console.
- Proyecto nuevo publicado → un `<article class="proj">` en `index.html` (imagen 1200×630 en `img/`, sirve la de compartir del proyecto) y línea en `sitemap.xml`.

- La vista previa al compartir el enlace (WhatsApp, redes) es `img/og.jpg`, que sale de `herramientas/og.html`: si cambia el titular o los colores, se regenera fotografiando esa página a 1200×630.
