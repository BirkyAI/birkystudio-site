---
title: "Auditoría SEO: 443 títulos rotos de 481"
description: "Auditamos 481 páginas en dos sitios. 443 títulos truncados en Google, 16 páginas huérfanas activas y 11 imágenes muertas. Nada de eso se veía."
date: 2026-09-16
image: "/images/blog/ai-generated/seo-audit-481-pages.jpg"
tags: ["Birky Studio", "SEO", "Caso de Estudio", "Auditoría Web"]
lang: "es"
author: "Luna Jerney"
---

Sabes cómo el auto del propio mecánico siempre es el peor de la calle?

Ese éramos nosotros. La semana pasada.

Vendemos SEO y trabajo de sitios web. Y cuando finalmente hicimos una auditoría real de nuestras dos propiedades, este sitio y nuestro sitio de desarrollo inmobiliario, encontramos **443 títulos de página rotos.** De 481 páginas. El noventa y dos por ciento del sitio estaba roto en silencio de una forma que nadie podía ver.

Quiero ser honesto sobre cómo se sintió eso, porque creo que la honestidad te sirve más que una vuelta de victoria.

## La parte de la que nadie te advierte

No hay un bucle de retroalimentación en este trabajo. Publicas algo y luego esperas seis semanas para saber si tomaste la decisión correcta. Para cuando lo descubres, ya tomaste cuarenta decisiones más encima.

La documentación de Google cambia constantemente. Las reglas que de verdad importan no están en un solo lugar. Para arreglar nuestro propio sitio, tuve que sacar información de dos páginas distintas de Google, dos patrones distintos de Schema.org y nuestros propios datos de Search Console, y armarlo todo.

Eso no es un problema de dueño de pequeño negocio. Es un problema de *nadie-tiene-tiempo-para-esto*. Las agencias cobran cuatro cifras al mes y aun así entregan estas cosas rotas.

Así que si alguna vez miraste tu sitio web, sentiste una inquietud vaga y cerraste la pestaña, no eres malo en esto. Eres una persona normal reaccionando correctamente ante algo genuinamente irrazonable.

## Lo que la auditoría realmente encontró

Rastreamos cada URL en ambos sitios. Aquí está la lista real, sin editar:

**443 títulos de página estaban cortados en los resultados de búsqueda de Google.**
Google trunca los títulos en aproximadamente 60 caracteres, y corta desde el *final*, justo donde está tu diferenciador. El nuestro era el nombre del sitio, repetido en casi cada página. Así que Google les mostraba a los clientes cosas como "AI Recepcionista de Voz for Small Businesses. Rea" y luego nada. Cada resultado de búsqueda de nuestro negocio se veía sin terminar.

**16 páginas de propiedades se estaban promocionando activamente a Google.**
Esta es peor de lo que suena. En nuestro sitio inmobiliario, 16 listings habían sido marcados como vendidos u ocultos. Las páginas de los listings los ocultaban correctamente. Pero las *páginas de detalle* todavía se seguían construyendo y todavía se enviaban a Google en el sitemap. Así que estábamos anunciando propiedades que ya no estaban, en un sitio donde los compradores no podían llegar a ellas desde ningún lugar. Sin enlaces internos. Sin ruta de menú. Solo páginas huérfanas por ahí juntando polvo en los resultados de búsqueda.

Si alguna vez te preguntaste por qué un sitio de listings se siente desactualizado, normalmente es por eso. Nadie lo está revisando.

**11 imágenes que se muestran al compartir tus páginas estaban muertas.**
Cada vez que alguien compartía nuestras páginas en LinkedIn, Facebook o WhatsApp, la tarjeta de vista previa salía en blanco. El enlace al archivo de imagen apuntaba a algo que no existía. Siete semanas, en una página, antes de que alguien lo notara.

**Un post del blog había estado publicado con una imagen principal rota.**
El archivo se guardó como `outsourced-isa-prospecting-zero-deals.jpg`. El post apuntaba a `outsourced-prospecting-zero-deals.jpg`. Una palabra de diferencia. La imagen daba 404, el post se veía roto, y nuestro auto-publicador de Facebook lo había publicado en silencio solo como texto, sin ninguna imagen.

**Nuestra página de inicio no tenía señal de marca.**
Técnicamente: sin schema `WebSite`, sin `og:site_name`. En la práctica: nada que le dijera a Google "este sitio web es un negocio llamado Birky Studio". Google estaba adivinando.

## Lo que esto te cuesta (y lo que no voy a afirmar)

Aquí es donde voy a tener cuidado, porque la mayoría de las agencias no lo tendría.

No te puedo decir "arreglar los títulos aumentó nuestro tráfico un 47%". Arreglamos esto un martes. El SEO tarda semanas en moverse, y si te citara un número hoy me lo estaría inventando. Vas a notar que mucho texto de marketing hace exactamente eso.

Lo que *sí* te puedo decir es qué hace un título truncado, mecánicamente:

- Tu título es tu anuncio. Es el titular que Google muestra al momento de decidir si alguien hace clic. El nuestro estaba cortado a mitad de palabra, así que la decisión se tomaba sobre una frase sin terminar.
- Una página sin enlaces internos es una página en la que Google eventualmente deja de confiar. Le estábamos pidiendo a Google que posicionara páginas a las que nosotros mismos no enlazaríamos.
- Una tarjeta para compartir en blanco significa que cada vez que un cliente reenviaba tu enlace, se veía como spam.
- Una señal de marca ausente significa que Google muestra una suposición en lugar de tu nombre.

Ninguna de estas cosas es dramática. Ese es el punto. No rompen tu sitio. Solo le cobran un impuesto silencioso a cada visitante, para siempre, y tú nunca te enterarías.

## Por qué esto le pasa a buenos negocios

Tres razones, y ninguna es flojera:

1. **Nada lo obliga a cumplirse.** Puedes escribir un título de 97 caracteres y el sitio lo publica contento. Sin error, sin advertencia. Se ve bien en tu pantalla porque los navegadores no truncan, solo lo hace la página de resultados de Google.
2. **Es invisible.** Un enlace roto da 404 y te das cuenta. Un título truncado se renderiza *perfectamente.* Solo se corta cuando un cliente lo ve. Tú eres la única persona que nunca lo va a notar.
3. **Está disperso.** Los límites de título viven en los documentos de Google. Las rutas de las imágenes viven en tu código. La lógica del sitemap vive en tu build. No hay un solo panel que diga "tu sitio no está bien".

## Qué cambiamos

Arreglamos los 443 títulos. Reescribimos la lógica del sitemap para que los listings vendidos y ocultos se excluyan solos automáticamente, en lugar de depender de que alguien se acuerde. Pusimos las páginas ocultas en `noindex` para que sigan siendo accesibles para cualquiera con un enlace viejo, pero dejen de competir en búsqueda. Generamos las imágenes faltantes y apuntamos las referencias rotas a archivos que de verdad existen. Agregamos el schema de marca.

Luego hicimos lo que de verdad importa: **instalamos un vigilante.**

Cada lunes por la mañana, un script rastrea las 481 páginas y revisa títulos, descripciones, imágenes, canónicas e indexación. Si todo está limpio, se queda callado y no me entero de nada. Si algo se rompe, recibo una alerta.

Ese es el arreglo real. No las 443 reescrituras, esas se van a erosionar. El arreglo es que **ya nadie tiene que acordarse.** Dejé de ser la integración entre mis propios sistemas, que es lo mismo que le digo a cada cliente.

## La conclusión honesta

Probablemente tienes alguna versión de esto en tu sitio ahora mismo. No porque hicieras algo mal, sino porque este trabajo es genuinamente irrazonable para sostenerlo en una sola cabeza humana, y no hay ninguna alarma que suene cuando algo sale mal.

La buena noticia: todo es arreglable. Todo. Solo es invisible hasta que alguien mira.

Así que aquí tienes una forma gratis de empezar a mirar.

## Pruébalo, es gratis

**Primero toma la plantilla Quick Log.** Es gratis, toma dos minutos, y es la herramienta de admisión exacta que usamos para detectar qué prospectos se están enfriando, el mismo punto ciego que esconde los problemas de SEO esconde los problemas de seguimiento:

👉 **[Obtén la plantilla Quick Log gratis](https://birkystudio.com/quick-log-template/)**

**¿No sabes qué tan sano está realmente tu sitio web?** Haz el Quiz de Preparación para IA de 2 minutos, te dice qué le falta a tu sitio en silencio y si un agente de IA se pagaría solo:

👉 **[Haz el Quiz de Preparación para IA de 2 minutos](https://birkystudio.com/ai-readiness-quiz/)**

**¿Quieres escuchar cómo suena un agente bien construido?** Llámalo. Sin formulario, sin llamada de ventas, sin enlace de calendario, responde como una recepcionista real y le puedes preguntar lo que sea:

👉 **[Llama a la demo de voz de IA en vivo](https://birkystudio.com/voice-demo/)**

**O simplemente escríbele.** Esta es a la que te mandaría si solo haces una cosa. Es lo real, corriendo en producción, y va a responder preguntas que un chatbot no tiene por qué saber contestar:

👉 **[Escríbele al agente de IA por WhatsApp, +502 3477 5110](https://wa.me/50234775110)**

Si prefieres que alguien revise tu sitio y te diga qué está roto, eso es lo que hacemos. **[Cuéntanos sobre tu negocio](https://birkystudio.com/es/contacto/)** y te respondemos dentro de la hora con una respuesta directa, incluidas las partes que no vale la pena que nos pagues por arreglar.

Lectura relacionada: [5 victorias simples de SEO que la mayoría de los pequeños negocios se pierde](/es/blog/5-simple-seo-tips-small-business/) y [las señales de que tu sitio web te está costando clientes](/es/blog/signs-website-costing-clients/).
