---
title: "Auditoría de IA: ¿quién aprobó el mensaje?"
description: "La ARA quiere que un humano con licencia responda por los mensajes que envía la IA. Este es el rastro de auditoría que un sistema no guarda, y por qué importa."
date: 2026-11-14
image: "/images/blog/ai-generated/ai-audit-trail-who-approved-the-message.jpg"
tags: ["Birky Studio", "Agente de IA", "Cumplimiento", "Flujo de trabajo"]
lang: "es"
author: "Luna Jerney"
---

## La regla no es la parte difícil

El 12 de noviembre alguien publicó esto en r/RealEstateTechnology:

> "The rule only works if someone defines 'licensed work.' Answering a buyer's question about a listing, booking a showing, and discussing price all sit at different points on that line. For anyone building lead-response or assistant tools, the practical side is the audit trail. You'd need a record of which messages the AI sent, which a licensee approved, and what the agent could see when they signed off."

El titular es la propuesta: la American Real Estate Association (ARA) quiere lenguaje con un licenciatario en el circuito, un humano con licencia que siga respondiendo por la IA que realiza trabajo con licencia. No existe una licencia federal, así que el plan es un texto modelo que se lleva a las legislaturas estatales una por una.

Pero lee la cita otra vez. De ahí salen dos problemas, y solo uno de ellos tiene que ver con la ley.

El primero es que "licensed work" no está definido. Responder una pregunta sobre un listing, agendar una visita y hablar del precio son tres cosas distintas que están en tres puntos distintos de la misma línea, y todavía nadie ha trazado la línea. El segundo problema es que el registro no existe. Una regla que dice que un licenciatario debe aprobar el mensaje es imposible de hacer cumplir, y de probar, si ningún sistema puede mostrar qué mensajes salieron y quién los vio antes de que salieran.

El primer problema lo resolverá alguien con un comité y un departamento legal. El segundo es tuyo, en tu propia bandeja de entrada, esta semana.

## Una semana normal

*La lista de abajo es un compuesto, armado con hilos de mensajes que he leído y escrito en mi propio flujo de prospectos. Los nombres cambian. El patrón no.*

```
Una semana de mensajes de un sistema de respuesta a prospectos

Lun 08:12  ¿La casa en Elm sigue disponible?        [asistencia]              enviado, sin aprobación registrada
Lun 09:40  ¿Podemos verla el sábado en la mañana?   [asistencia]              enviado, sin aprobación registrada
Lun 14:05  ¿Cuánto ofrecerías por ella?             [necesita licencia]       enviado, sin aprobación registrada
Mar 11:20  ¿Cuánto son las cuotas de la HOA?        [asistencia]              enviado, sin aprobación registrada
Mar 16:48  ¿Crees que el avalúo llegará al precio?  [necesita licencia]       enviado, sin aprobación registrada
Mié 10:02  ¿El vendedor ha tenido otras ofertas?    [necesita licencia]       enviado, sin aprobación registrada
Jue 13:30  ¿Me puedes enviar el plano?              [asistencia]              enviado, sin aprobación registrada
Vie 09:15  ¿Debería renunciar a la inspección?      [actividad con licencia]  enviado, sin aprobación registrada
Vie 17:44  ¿Qué harías tú en mi lugar?              [actividad con licencia]  enviado, sin aprobación registrada
```

Nueve mensajes en cinco días. Cuatro de ellos son pura logística: disponibilidad, una hora, un documento, una tarifa que está escrita en las notas del listing y se puede consultar en diez segundos. Tres están en el medio, donde la respuesta honesta empieza a apoyarse en tu lectura del trato. Dos son consejo sobre una decisión que le toca al comprador y que un licenciatario tiene que respaldar.

Ahora lee otra vez la última columna, de arriba a abajo. Dice lo mismo nueve veces.

Ese es el fallo, y no es un fallo de la IA. La herramienta contestó los nueve, rápido, que es exactamente para lo que se compró. El fallo es que, después de los hechos, nadie en esa cadena puede responder dos preguntas muy comunes. ¿Qué envió? ¿Y quién aprobó eso?

Hazle esas dos preguntas a un sistema típico y las respuestas son: probablemente puedas desplazarte lo suficiente para encontrar algunos, y nadie sabe. Si un bróker te pide mostrar tu trabajo de un mensaje del viernes, estarías leyendo un hilo de chat en voz alta y esperando que las marcas de tiempo cuadren.

## Lo que el registro de verdad tiene que cargar

Un registro de mensajes no es una transcripción. Una transcripción te dice qué se dijo. Lo que una regla con un licenciatario en el circuito necesita son cinco datos pegados a cada mensaje que sale con tu nombre:

1. **Cuál mensaje fue**, y si salió sin editar o como borrador.
2. **Quién o qué lo envió**, es decir, el agente o el humano, con nombre.
3. **Qué licenciatario lo aprobó**, si hacía falta una aprobación humana.
4. **Qué podía ver esa persona cuando dio el visto bueno**: la pregunta del cliente, las notas de donde salió la respuesta, y la respuesta misma.
5. **Cuándo pasó todo eso**, en una sola línea de tiempo.

Cuatro de esos cinco son baratos. El que ningún sistema tiene es el cuarto, porque "qué podía ver el agente al dar el visto bueno" es una decisión de diseño, no un campo que puedas agregar después. Si la IA le pasa a un humano un borrador sin la fuente adjunta, el humano aprueba una oración, no una decisión, y no hay ningún registro que distinga las dos cosas.

## Lo que escribe el nuestro

Cuando el agente dirige un mensaje a un humano, este es el registro que guarda. Este es un mensaje real de la misma clase de semana, acortado:

```
Registro de mensaje, viernes

redactado      09:15:22   agente de IA, solo borrador, no entregado
dirigido       09:15:23   marcado: consejo sobre la contingencia de inspección
aprobado       09:26:10   aprobación del licenciatario registrada
lo que vio     la pregunta del comprador, las notas de inspección del listing, el borrador de la respuesta
entregado      09:27:04   respuesta enviada, sin editar
```

Cinco datos, una línea de tiempo, y la línea que dice lo que vio es la que importa. La aprobación va pegada a una pregunta y a una fuente, no a una oración que flota en una ventana de chat.

Cada producto que lanzamos publica las reglas bajo las que funciona, y las reglas suelen ser cortas. El [Motor de Reseñas](https://birkystudio.com/es/products/review-engine/) es un buen ejemplo: no puede pedir una reseña positiva, no puede escribirle solo a los clientes contentos, y no enviará un mensaje de texto sin un consentimiento documentado. Esas no son configuraciones que puedas apagar. Son el producto, $497 para configurarlo y $97 al mes.

## Lo que hace el agente

- **Envía la logística por su cuenta.** Disponibilidad, horarios de visita, la tarifa que vive en las notas del listing. Cuatro de los nueve de esa semana nunca necesitaron a un humano para empezar, y salen en segundos, a las 08:12 de un lunes, cuando nadie está despierto para aprobar nada.
- **Estaciona la zona gris y el consejo.** Todo lo que toca el precio, la condición, las contingencias o lo que el comprador debería hacer se redacta, se marca y se retiene, con las notas de la fuente adjuntas.
- **Anota lo que vio el humano.** No que la aprobación ocurrió, sino qué pregunta y qué notas estaban en la pantalla cuando ocurrió.
- **Mantiene un registro continuo por cliente**, para que el hilo sea un archivo que puedes leer y no un desplazamiento que tienes que reconstruir.
- **Exporta cuando se lo pides.** Si un bróker, un cliente o un regulador pide una semana, entregas una lista en lugar de una memoria.
- **Reporta el hueco.** Si un mensaje estuvo sin responder dos días porque esperaba a un humano, el registro dice dos días.

Ya he escrito antes sobre los mensajes que nunca se registran y lo que cuestan después esas notas que faltan ([La nota que no escribiste te cuesta tratos](https://birkystudio.com/es/blog/phone-note-chaos-transaction-calls/)). Este es el mismo problema después de los hechos: la nota tiene que existir antes de que alguien la pida.

## Lo que no va a hacer

- **No te va a decir dónde está la línea de tu estado.** Nadie la ha trazado todavía. Cualquiera que te la trace durante una llamada de ventas te está vendiendo una certeza que no tiene.
- **El registro no te hace cumplir la norma.** Te hace capaz de mostrar tu trabajo. Son afirmaciones distintas y no las voy a mezclar.
- **No puede registrar la llamada que atendiste tú mismo** en tu propio teléfono en el carro. Si la decisión con licencia ocurrió ahí, ocurrió fuera del registro.
- **No va a decidir qué se puede enviar.** Tú fijas las reglas una vez, a propósito, y él las mantiene. Si quieres que el agente conteste preguntas de precio por su cuenta, esa es tu decisión y tu nombre va en ella.
- **Se niega a darte una cifra de riesgo de cumplimiento.** Nadie sabe cuánto te va a costar una regla que todavía no se ha escrito, y cualquiera que te dé un número se lo inventó.

## El orden honesto de las operaciones

Dos productos, y importa cuál va primero.

La Evaluación Personalizada cuesta $349 para un agente solo, o $999 con personal, y se acredita contra lo que construyas. Lo primero que hacemos en ella no es una recomendación, es una lectura: de qué están hechos tus mensajes, qué envía tu herramienta actual por su cuenta, y qué sería capaz de producir tu sistema si un bróker te preguntara por el martes pasado.

Después viene la construcción. El Agente Base empieza en $1,297 de pago único para una práctica en solitario, incluido el espacio de trabajo en Notion que guarda el registro, y desde $2,997 para un negocio con personal, con 30 días de soporte mientras se asienta. Mantenerlo funcionando cuesta $97 al mes, o $197 para un socio que lo va cambiando conforme cambian tus reglas. Si los mensajes salen por texto o WhatsApp, esa es la Recepcionista de Texto de $297; si quieres que tu propia línea se conteste y se registre, esa es la Recepcionista de Voz de $550.

Hemos rechazado trabajo antes cuando era la compra equivocada, y el razonamiento no ha cambiado ([No te vendo estos errores de agentes de IA](https://birkystudio.com/es/blog/we-refuse-to-sell-ai-agent-mistakes/)). Si tu volumen es de doce mensajes a la semana y los contestas todos tú mismo, todavía vale la pena tener un registro y no necesitas pagar por un robot que lo haga.

## Pruébalo

Empieza por la parte gratis. La [plantilla Quick Log](https://birkystudio.com/quick-log-template/) es el registro simple de una página que uso para exactamente esto, y toma unos cuatro minutos configurarlo. Leerla te dirá más sobre tus propios huecos de lo que puede este artículo.

Si prefieres escucharlo funcionando, llama a [Elliot, nuestra demo de agente de voz con IA](https://birkystudio.com/voice-demo/). Contesta, califica y agenda, sin necesidad de iniciar sesión. Después prueba el [agente de IA de WhatsApp](https://wa.me/50234775110) con algo incómodo de tu propio negocio y mira lo que anota.

Si quieres saber qué entregaría de verdad tu sistema actual, la [Evaluación Personalizada](https://birkystudio.com/es/products/custom-assessment/) es donde eso empieza, $349 para un agente solo o $999 con personal, y se acredita contra lo que construyas después.

Si prefieres simplemente mostrármelo, [mándame una nota](https://birkystudio.com/es/contacto/) y describe una semana de tus mensajes. Esa es la conversación con la que empieza la evaluación.
