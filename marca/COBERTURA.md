# Cobertura de los manuales v1.1

Cada regla de los 8 manuales (9 páginas, leídas enteras en texto y en imagen el 08-11-2026), con su
estado en las webs de Sukima Labs. **Aplicada** = está en el código (dice dónde). **N/A** = no
corresponde a una web (dice por qué). **Pendiente** = corresponde, pero depende de otra persona o
de una validación que aún no existe (dice de quién). Abreviaturas de manuales en [REGLAS.md](REGLAS.md).

Sitios: **P** portada (`sukimalabs.com`), **F** Finde, **D** Descargo. Circularidad no tiene
web (repositorio privado sin Pages), así que no se aplica nada en él.

| # | Manual · pág. | Regla | Estado | Dónde / por qué |
|---|---|---|---|---|
| 1 | LM p1 | Eslogan institucional | Aplicada | P: titular, `<title>`, og:image |
| 2 | LM p1 | Eslogan de posicionamiento (acompaña en la lámina) | N/A | Reservado a campañas (MM p1); ninguna web es campaña |
| 3 | LM p1 | Paleta grafito/cian/violeta/marfil con sus HEX | Aplicada | `marca.css` (`--sk-*`) |
| 4 | LM p1 | Reconstrucción vectorial: verificar antes de registro o producción | Pendiente | Validación de los fundadores; issue abierta y PR sin fusionar |
| 5 | MM p1 | Sukima = hueco, intersticio | Aplicada | P: párrafo bajo el titular |
| 6 | MM p1 | Posicionamiento transversal, no limitar a un sector o país | Aplicada | P: se quita «madrid» de la franja y del pie |
| 7 | MM p1 | Eslogan principal y de posicionamiento (textos exactos) | Aplicada | REGLAS 2; P usa el principal literal |
| 8 | MM p1 | Valores; la estética cyberpunk es opcional | Aplicada | P deja Chakra Petch (letra «cyberpunk») por la de marca |
| 9 | MM p1 | Personalidad; evitar clichés de ONG, hospital, seguridad, software genérico | Aplicada | Texto de P revisado; REGLAS 8 |
| 10 | MM p1 | Escribir siempre «Sukima Labs», sin variantes | Aplicada | P (título, og, logo, pie), F (cabecera y créditos), D (og:site_name) |
| 11 | MM p1 | Principal en lo institucional, secundario solo en campañas | Aplicada | P solo usa el principal |
| 12 | MM p1 | No poner ambos eslóganes debajo del logotipo | Aplicada | Ningún sitio los junta |
| 13 | MM p1 | Submarcas distinguibles sin alterar el isotipo matriz | Aplicada | F y D conservan su identidad y llevan el isotipo intacto como aval |
| 14 | MM p1 | Validar proporción y pruebas físicas antes de registrar o producir | Pendiente | Fundadores (igual que 4) |
| 15 | MIV p1 | Isotipo maestro `isotipo_color.svg`, 200×200, sin tocar la geometría | Aplicada | `logo/`; los SVG en línea de P, F y D copian los mismos trazados |
| 16 | MIV p1 | Colores y su papel (principal, acento, comunicación, fondo) | Aplicada | `marca.css`; violeta solo en interfaz/comunicación, nunca en el símbolo |
| 17 | MIV p1 | Pantone/CMYK sin equivalencias certificadas | N/A | Solo impresión |
| 18 | MIV p1 | Versiones oficiales; en una tinta el cian toma la tinta principal | Aplicada | Tema oscuro de P, F y D: isotipo todo blanco |
| 19 | MIV p1 | Sin degradados en el símbolo | Aplicada | Rellenos planos en todos los SVG |
| 20 | MIV p1 | Área de seguridad del 15 % del ancho del isotipo | Aplicada | P: el margen interno del SVG ya supera el 15 %; F y D: separación ≥ 5 px a 32 px; `--sk-area-seguridad` |
| 21 | MIV p1 | Isotipo digital mínimo 32 px; 16 px solo tras verificar | Aplicada | P 35 px, F 32 px, D 32 px (antes 20 px) |
| 22 | MIV p1 | Favicon a 16 px | Pendiente | Se usa el favicon entregado; la prueba de reducción a 16 px sigue sin marcar en el control de aprobaciones |
| 23 | MIV p1 | Mínimos de impresión (12 mm, 35 mm) | N/A | Solo impresión |
| 24 | MIV p1 | Sin eslogan en aplicaciones diminutas | Aplicada | Favicons y avales sin eslogan |
| 25 | MIV p1 | Tipografía DejaVu Sans | Aplicada | P (alojada en `fuentes/`); F y D conservan la suya como submarcas (regla 13) |
| 26 | MIV p1 | Inter, solo si se valida licencia y disponibilidad | N/A | No se adopta; queda como exploración |
| 27 | MIV p1 | No alterar el isotipo para adaptarlo a la letra | Aplicada | Solo se convirtió a trazos el texto del logotipo, no el isotipo |
| 28 | MIV p1 | Color sobre marfil o blanco, blanco sobre grafito, negro sobre claro | Aplicada | P marfil/grafito, F blanco/oscuro, D claro/oscuro, con la versión que toca |
| 29 | MIV p1 | Nada de cian sobre fondos parecidos, fotos o texturas | Aplicada | Cian solo sobre grafito o como panel del isotipo |
| 30 | MIV p2 | Usos prohibidos (estirar, inclinar, rotar, recortar, sombras, globo, proporciones, degradados) | Aplicada | Solo escalado uniforme; comprobado en el código |
| 31 | MIV p2 | No superponer ambos eslóganes | Aplicada | Igual que 12 |
| 32 | MIV p2 | Sin ® mientras no haya registro | Aplicada | Ningún sitio lo usa |
| 33 | MIV p2 | Bordado con versión de una tinta y prueba física | N/A | Producción física |
| 34 | MIV p2 | Serigrafía/láser: SVG monocromo y texto a contornos | Aplicada | Texto de los logotipos convertido a trazos en `logo/` (también evita depender de la letra en la web) |
| 35 | MA p1 | GitHub: isotipo sin eslogan, centrado, ≥ 512 px | Pendiente | Avatar de la organización: lo administra maquina, y antes hace falta la aprobación de los fundadores |
| 36 | MA p1 | Favicon 16/32 px tras revisión | Aplicada | P: `favicon.ico` + SVG + 180 px (con la reserva de la 22) |
| 37 | MA p1 | Redes: avatar 512 px; banners con nombre y un solo eslogan | Aplicada | P: og:image nueva con un eslogan; los perfiles de redes son N/A (no hay cuentas) |
| 38 | MA p1 | Las imágenes de ejemplo son plantillas, sin legibilidad aprobada | Aplicada | No se usan los banners de ejemplo; la og:image se hizo con los SVG |
| 39 | MA p1 | Documentación (propuestas, membrete, tarjeta, firma, presentaciones) | N/A | No son webs |
| 40 | MA p1 | Prendas y objetos | N/A | Producción física |
| 41 | MA p1 | Calidad: contraste WCAG en texto digital | Aplicada | Ratios medidos en `marca.css`; todos los pares de texto ≥ 4,5:1 |
| 42 | MA p1 | Calidad: sangrado, perfiles de imprenta, bordado | N/A | Producción física |
| 43 | MA p1 | Calidad del SVG | Aplicada | SVG válidos, con `<title>`, sin texto vivo |
| 44 | MA p1 | El isotipo no depende del idioma; no traducir «Sukima Labs» | Aplicada | F en inglés mantiene «Sukima Labs» |
| 45 | MA p1 | Traducir mensajes solo con versión aprobada | Aplicada | El eslogan no se traduce en ningún sitio en inglés |
| 46 | MC p1 | Tono claro, preciso, curioso, humano; sin grandilocuencia | Aplicada | Texto de P revisado; sin promesas de impacto |
| 47 | MC p1 | Rebelde y geek sin ser excluyente ni agresiva | Aplicada | Texto de P |
| 48 | MC p1 | Mensaje institucional y de campaña | Aplicada | Igual que 11 |
| 49 | MC p1 | Descripción corta propuesta | Aplicada | P: meta description |
| 50 | MC p1 | No asociar a un continente, sector o demografía | Aplicada | Igual que 6 |
| 51 | MC p1 | Comunicación inclusiva, respetuosa, verificable, accesible | Aplicada | Igual que 41 y 58 |
| 52 | MC p1 | Evitar imágenes que reduzcan la humanidad a una región | N/A | Las webs no usan fotos de personas |
| 53 | MC p1 | Titulares breves, una idea por pieza, contraste fuerte, una sola llamada a la acción | Aplicada | P: un titular y un botón en la portada; el cierre tiene su único enlace |
| 54 | MC p1 | Pocos colores y un solo eslogan a la vez | Aplicada | P: paleta de marca y un eslogan |
| 55 | MP p1 | Maestro en SVG/PDF; no ampliar PNG de baja resolución | Aplicada | Web con SVG; los PNG solo a su tamaño nativo (favicons) |
| 56 | MP p1 | PDF vectorial para artes finales; perfil ICC | N/A | Impresión |
| 57 | MP p1 | CMYK, tintas planas, sangrado, troquel; sin Pantone certificado | N/A | Impresión |
| 58 | MP p1 | Textil y bordado: monocromo, muestra física | N/A | Producción física |
| 59 | MP p1 | Serigrafía a una tinta, prueba de registro | N/A | Producción física |
| 60 | MP p1 | Control de archivos: vector frente a raster; las piezas comerciales son simulaciones | N/A | Informativo; en la web no se muestran piezas comerciales |
| 61 | MDA p1 | Avatar: isotipo sin eslogan con área de seguridad, revisado a 16/32/64/512 | Pendiente | Avatar de la org (igual que 35). Además, el `apple_touch_icon_180.png` entregado no deja el 15 % de margen: hay que rehacerlo en la entrega |
| 62 | MDA p1 | Contraste WCAG 2.2 AA verificado con herramienta | Aplicada | Fórmula WCAG sobre cada par; foco ≥ 3:1 en P, F y D |
| 63 | MDA p1 | Tokens de `03_DIGITAL/Web/brand_tokens.css/.json` | Aplicada | `marca.css` contiene los mismos valores y añade los de tema y accesibilidad |
| 64 | MDA p1 | Isotipo consistente con los SVG de 01_LOGO | Aplicada | Mismos trazados en todos los sitios |
| 65 | MDA p1 | Títulos claros y alt «Sukima Labs, símbolo de umbrales anidados con abertura cian» | Aplicada | `<title>` de los SVG, og:image:alt de P, etiquetas accesibles en F y D |
| 66 | MG p1 | Fidelidad del vector y aprobación final de uso comercial | Pendiente | Ambos fundadores: los PR quedan abiertos para su revisión |
| 67 | MG p1 | Búsquedas OEPM/EUIPO y análisis jurídico | Pendiente | Fundadores; fuera de las webs |
| 68 | MG p1 | No usar ® sin registro | Aplicada | Igual que 32 |
| 69 | MG p1 | Verificar licencias de letras, fotos, iconos y software | Aplicada | DejaVu (Bitstream Vera/Arev) verificada y con su licencia; Archivo, Chakra Petch y Plex Mono se retiran con sus OFL; Mercer Lite sigue acreditada |
| 70 | MG p1 | Archivos maestros con control de versiones, cambios documentados, copia de seguridad | Aplicada | `marca/` en git, cambios en el PR; la copia sigue en el kDrive |

**Totales: 70 reglas · 49 aplicadas · 14 N/A · 7 pendientes.** (Las de F y D se cumplen al fusionar sus PR.)
