# Sukima Labs · reglas de marca (identidad 04, entrega v1.1)

Resumen operativo de los 8 manuales de la entrega del 08-11-2026 (kDrive de la organización:
`Marca/v1.1 - Entrega integral logotipo 04/02_MANUALES/`). Cada regla cita manual y página. Lo que
cada regla exige y dónde se aplica, regla por regla, está en [COBERTURA.md](COBERTURA.md).

Abreviaturas: **LM** 00 Lámina maestra · **MM** 01 Manual de marca · **MIV** 02 Manual de identidad
visual · **MA** 03 Manual de aplicaciones · **MC** 04 Manual de comunicación y voz · **MP** 05 Manual
de producción y artes finales · **MDA** 06 Manual digital y accesibilidad · **MG** 07 Manual de
gobernanza y licencias. Todos tienen una página salvo MIV, que tiene dos.

> **Estado (MG p1, `07_GOBERNANZA/Control_de_aprobaciones.md`):** los dos fundadores eligieron el
> candidato 04, pero el vector es una *reconstrucción* desde una imagen y falta la validación de
> fidelidad y la aprobación final de uso comercial por ambos. Hasta entonces, nada de esto es
> definitivo ni se publica sin el visto bueno de los dos.

## Cómo usarlo en un proyecto

```html
<link rel="stylesheet" href="https://sukima-labs.github.io/marca/marca.css">
```

Solo define variables `--sk-*` y la letra; no da estilo a nada. Logotipos en
`https://sukima-labs.github.io/marca/logo/`. Un producto (Finde, Descargo, ATLAS…) es una submarca:
conserva su propio nombre y su estilo, y lleva el isotipo matriz sin alterarlo (MM p1 «Audiencias»).

## Nombre y mensajes

1. Se escribe siempre **Sukima Labs**. Nunca «Sumika», «Sukina» ni variantes, y no se traduce
   (MM p1 «Arquitectura verbal»; MA p1 «Uso internacional»). `sukima-labs` solo en URL y en GitHub.
2. Eslogan institucional: **«El espacio donde nacen nuevas posibilidades.»** El de campaña,
   «Donde otros ven un vacío, nosotros vemos posibilidades.», solo en campañas y manifiestos. Nunca
   los dos debajo del logotipo a la vez (MM p1 «Promesa», «Arquitectura verbal»; MC p1 «Mensajes»;
   MIV p2 «Usos prohibidos»).
3. Descripción corta propuesta (texto editorial, no descripción societaria): «Sukima Labs explora
   los espacios entre ideas, disciplinas y necesidades para crear nuevas posibilidades» (MC p1).
4. No encerrar la marca en un sector, un país o un continente (MM p1 «Identidad», MC p1 «Principios»).

## Tono de voz (MC p1; MM p1 «Personalidad»)

5. Claro, preciso, curioso y humano. Sin grandilocuencia, sin lenguaje vacío y sin prometer
   impacto que no esté demostrado.
6. Puede ser rebelde y geek, nunca excluyente ni agresiva. Comunicación inclusiva, respetuosa y
   verificable.
7. Titulares breves, una idea central por pieza, contraste fuerte y **una sola llamada a la
   acción**. Pocos colores y un solo eslogan a la vez.
8. Evitar los clichés de ONG, hospital, institución médica, empresa de seguridad o software
   genérico, y las imágenes que reduzcan la humanidad a una sola región.

## Logotipo: sí

9. Archivo maestro: `logo/isotipo_color.svg`, lienzo de 200 × 200 (MIV p1 «Construcción»). Versiones
   oficiales: isotipo, logotipo horizontal y vertical, con y sin eslogan, en color, negro y blanco
   (MIV p1 «Versiones»). En una sola tinta, el panel cian toma la tinta principal.
10. Fondos: color sobre marfil o blanco, blanco sobre grafito, negro sobre claro (MIV p1 «Fondos»).
    En la web, `--sk-logo-marco` y `--sk-logo-panel` ya cambian solos con el tema.
11. Área de seguridad: un margen libre del **15 % del ancho del isotipo** por cada lado, sin texto,
    bordes ni fotos dentro (MIV p1; regla provisional). `--sk-area-seguridad: 0.15`.
12. Tamaño mínimo digital del isotipo: **32 px de ancho**; 16 px solo tras comprobar que se lee.
    Sin eslogan en tamaños diminutos (MIV p1 «Tamaño mínimo»; MDA p1 «Avatar»: revisar a 16, 32, 64 y 512 px).
13. Avatar y GitHub: isotipo sin eslogan, centrado, 512 px o más. Favicon: icono de 16/32 px.
    Banners: nombre y un solo eslogan (MA p1 «Identidad digital»).
14. En `logo/`, el texto de los logotipos ya está convertido a trazos (DejaVu Sans), así que no
    depende de la letra instalada: es lo que pide MIV p2 «Producción» para preimpresión, aplicado
    también a la web. La geometría del isotipo no se ha tocado.

## Logotipo: no (MIV p2 «Usos prohibidos»)

15. No estirar, inclinar, rotar ni recortar; no añadir sombras; no convertirlo en globo; no cambiar
    proporciones; no poner degradados en el símbolo ni en lugar del cian; no superponer los dos
    eslóganes.
16. **No usar ®**: no hay registro concedido (MIV p2; MG p1 «Registro»).
17. No poner cian sobre fondos parecidos, fotografías complejas o texturas de poco contraste
    (MIV p1 «Fondos»). No alterar el isotipo para adaptarlo a una letra (MIV p1 «Tipografía»).

## Color y letra

18. Grafito `#10131C` (principal), cian `#14C6D4` (acento del umbral), violeta `#7148F5`
    (comunicación, nunca en el símbolo), marfil `#F5F4F0` (fondo); blanco y negro, versiones técnicas
    (MIV p1 «Colores»; LM p1). No hay equivalencias Pantone ni CMYK certificadas (MIV p1; MP p1).
19. Letra: **DejaVu Sans** (MIV p1 «Tipografía»). Inter queda como exploración para lo digital,
    pendiente de validar licencia y disponibilidad: aquí no se usa.

## Accesibilidad (MDA p1; MA p1 «Criterios de calidad»)

20. Contraste **WCAG 2.2 AA** medido con herramienta antes de publicar. Pares medidos en
    `marca.css`. En claro: texto grafito, enlaces y foco violeta (4,8:1), botón violeta con texto
    blanco (5,3:1). En oscuro: texto marfil, enlaces, foco y botón cian (8,9:1, botón con texto grafito).
21. **El cian no lleva texto ni marca nada esencial sobre fondo claro** (1,9:1 sobre marfil). Sobre
    grafito, el violeta solo vale para texto grande o bordes (3,5:1).
22. Títulos claros y texto alternativo. Para el símbolo: «Sukima Labs, símbolo de umbrales anidados
    con abertura cian» (MDA p1 «Metadatos»). Los SVG de `logo/` ya lo llevan en `<title>`.
23. Foco siempre visible: `outline` con `--sk-foco`, de 3:1 como mínimo contra el fondo.

## Licencias y gobernanza (MG p1)

24. Verificar la licencia de letras, fotos, iconos y software de terceros antes de distribuir
    archivos editables. DejaVu Sans: licencia Bitstream Vera / Arev, libre, en `fuentes/LICENSE-DejaVu.txt`;
    tiene que viajar con los ficheros de letra.
25. Los archivos maestros se publican con control de versiones (este repositorio), cada cambio
    documentado, y con copia de seguridad (el kDrive de la organización).
26. Antes de registrar o producir en serie: búsqueda de anterioridades OEPM/EUIPO, pruebas físicas y
    aprobación final de ambos fundadores (MM p1 «Gobernanza»; MG p1). Eso es de los fundadores, no de
    cada proyecto.
