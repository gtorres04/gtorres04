# Gerlin Orlando Torres Saavedra

**Senior Java Software Engineer en Globant**
Cartagena de Indias, Bolívar, Colombia

## Contactar

- 643601249 (Mobile)
- gerlin.torres@gmail.com
- www.linkedin.com/in/gerlin-orlando-torres-saavedra (LinkedIn)

## Aptitudes principales

- java 21
- kafka
- open api

## Languages

- Español

## Certifications

- Curso de desarrollo de una API REST con Spring Boot
- Jenkins para la IC/DC de aplicaciones Dockerizadas
- Curso de Introducción a Docker
- Oracle Certified Associate, Java SE 7 Programmer
- Desarrollo Web

## Extracto

Soy Ingeniero de Software especializado en backend y arquitecturas distribuidas, con más de una década implementando plataformas críticas para banca, inversión, pagos electrónicos y grandes corporaciones. He liderado y desarrollado soluciones basadas en microservicios, arquitectura hexagonal y DDD, gestionando dominios complejos como jerarquías globales de producto (Inditex), integración financiera ISO-8583/ MasterCard (EVOLVE), fondos de pensiones (SPIRIT, Protección) y portales institucionales de alto tráfico.

Mi fortaleza está en el diseño y construcción de servicios robustos, escalables y event-driven con Java 11–21, Spring Boot 3, integrando ecosistemas como Kafka, PostgreSQL, CosmosDB/Gremlin, MongoDB o MySQL, y desplegando en OpenShift, Kubernetes o entornos cloud (Azure). Complemento este trabajo con prácticas modernas de ingeniería (CI/CD con GitHub Actions y Jenkins, code review, TDD, pruebas E2E con Karate, observabilidad con Kibana/Prometheus/Grafana). También he trabajado en frontend con SPA (React, Angular) y microfrontends.

Como líder técnico he guiado equipos multidisciplinares, definiendo arquitectura, revisando diseño, elevando estándares de calidad, acompañando a desarrolladores y asegurando entregables alineados con negocio, normativa y seguridad. Me apasionan los sistemas de alto rendimiento, los flujos reactivos y el aprendizaje continuo: actualmente profundizo en Go, Kotlin, Rust, Quarkus, Vert.x y bases de datos columnares.

Mi foco es crear software claro, mantenible y resiliente que genere impacto real en el negocio.

## Experiencia

### Globant

**Senior Java Software Engineer**
agosto de 2023 - Present (3 años)
Cartagena de Indias, Bolívar, Colombia

Desarrollo y lidero soluciones backend con Java 21 y Spring Boot 3 bajo arquitectura hexagonal, integrando modelos en Cosmos DB y grafos Gremlin junto con PostgreSQL, y aplicando DDD y Clean Architecture para un dominio modular y escalable. Diseño flujos de mensajería con Kafka en pub/sub y gestiono despliegues continuos mediante OpenShift y GitHub Actions.

En el proyecto corporativo de Inditex construyo una plataforma que modela y explota la jerarquía global de producto mediante un backend basado en Amiga Java y Spring Boot, habilitando el cálculo dinámico de KPIs desde el nivel prenda hasta el corporativo. El reto principal es definir un modelo jerárquico complejo sobre Cosmos DB capaz de representar departamentos, categorías y productos, garantizando consistencia y rendimiento en un entorno con alto volumen de eventos y cálculos mensuales, semestrales y anuales. La complejidad técnica incluye orquestar procesamiento intensivo, mantener integridad entre Cosmos DB, PostgreSQL y Redis y optimizar el ciclo de vida del dato para asegurar tiempos de respuesta estables incluso ante picos de carga. A nivel de negocio, la plataforma debe proporcionar una visión unificada y precisa del desempeño, asegurando trazabilidad y disponibilidad continua.

La solución se ejecuta sobre Kubernetes en la plataforma PaaS de Inditex, utilizando PostgreSQL como base transaccional, Cosmos DB para grafos, Redis como acelerador de lectura y Kafka como sistema de eventos. El ciclo de desarrollo integra GitHub, GitHub Actions y Argo Workflows para CI/CD, además de Docker para empaquetado. La calidad se garantiza con JUnit, Karate e ICaRUS para pruebas unitarias, integración, E2E, carga y caos. La observabilidad se soporta con Grafana, Prometheus, Zipkin y Grafana Cloud Tempo, unificando métricas, logs y trazas distribuidas.

El resultado es una plataforma robusta, escalable y eficiente que permite calcular KPIs críticos en tiempo casi real, fortaleciendo la analítica y la toma de decisiones.

### Paradigma Digital

**Senior Software Development Engineer**
abril de 2021 - marzo de 2024 (3 años)
Madrid, Comunidad de Madrid, España

Lideré técnicamente equipos backend en proyectos institucionales y corporativos, definiendo arquitecturas, estándares y decisiones clave en plataformas críticas para administraciones públicas y grandes empresas.

En Programa.cat, consolidé un backend Java/Spring Boot con arquitectura hexagonal para una plataforma que unifica la gestión de ayudas culturales entre Generalitat y diputaciones. El reto principal fue integrar datos y criterios heterogéneos, garantizar coherencia semántica en la información cultural y mantener un sistema flexible para distintos convenios administrativos, asegurando trazabilidad e integridad en los procesos.

La solución incorporó Java 17, Spring Boot, PostgreSQL con JPA/Hibernate, Kafka, eventos de dominio y generación OpenAPI, reforzada con pipelines en Jenkins, SonarQube, mutation tests y despliegues automatizados en OpenShift. El resultado fue una plataforma robusta, modular y alineada con estándares institucionales.

En Inditex – Proyecto AIDANA, actué como Líder Técnico del microservicio estratégico de parametrización que orquesta datos entre AidAnalytics y múltiples dominios internos y externos. Los principales retos fueron unificar información dispersa, asegurar consistencia en un entorno distribuido y mantener latencias mínimas bajo alta carga. Implementé Amiga Java (Spring Boot), Redis, Kafka PIPE, testing avanzado con JUnit, Karate e ICaRUS, CI/CD con GitHub Actions y despliegues en Sentinel/Kubernetes con observabilidad completa mediante Grafana, Tempo y Zipkin. El servicio se consolidó como una pieza crítica y altamente fiable del ecosistema de datos.

En EVOLVE – El Corte Inglés, desarrollé el backend para la modernización del procesamiento MasterCard, integrando mensajes ISO 8583 vía Netty y MongoDB en un entorno de misión crítica. Superé el reto de combinar reglas de negocio propias sin comprometer compatibilidad con el protocolo, reforzando estabilidad, precisión transaccional y cumplimiento financiero.

### Grupo Ditech

**Arquitecto Java**
octubre de 2019 - abril de 2021 (1 año 7 meses)
Madrid, Madrid, España

Actué como Arquitecto Java y Líder Técnico en Grupo Ditech para Evo Banco y Bankinter, garantizando calidad, coherencia arquitectónica y gobernanza de plataformas críticas.

En Evo Banco, el principal reto fue integrar múltiples APIs de terceros en el API Gateway corporativo, imponiendo estándares RESTful, normalizando contratos inconsistentes y corrigiendo malas prácticas sin degradar seguridad, cumplimiento ni rendimiento. En paralelo, lideré el diseño y desarrollo de un microfrontend de simulación hipotecaria, alineando arquitectura y procesos de negocio para mantener consistencia funcional, baja latencia y trazabilidad. En Bankinter, dirigí la construcción de una plataforma de gestión y versionado de configuración para microservicios, capaz de manipular parámetros sensibles sin comprometer la estabilidad de los entornos, integrando Consul como fuente única de configuración y reduciendo errores por desalineaciones entre servicios y versiones.

Las soluciones se implementaron con Java 8 y Spring Boot en los backends, ReactJS y Angular 9 en los frontends y un API Gateway corporativo desplegado en Azure Cloud para Evo Banco. Se utilizó Consul como repositorio centralizado de configuración, GitHub para control de versiones, Jenkins para CI/CD, Docker y Azure App Services para contenedorización y despliegues, y Azure API Management para gobierno de APIs. El trabajo se organizó bajo Scrum, con integración continua, code reviews, testing automatizado y prácticas como pair programming y coordinación estrecha con arquitectura, QA y negocio.

El resultado fue un ecosistema de integraciones más robusto y estandarizado, una gestión de configuración fiable y un simulador hipotecario moderno que mejoró la experiencia de cliente y redujo incidencias operativas en ambos bancos.

### Makers Solutions S.A.S

**Lider tecnico Java**
noviembre de 2018 - octubre de 2019 (1 año)
Medellín, Antioquia, Colombia

Dirigí técnicamente el proyecto SPIRIT para el fondo de pensiones Protecciones, una plataforma diseñada para registrar, valorizar y consolidar diariamente las acciones financieras del portafolio de inversión, garantizando datos precisos, consistentes y disponibles para la operativa del día siguiente. El principal reto consistió en asegurar la coherencia entre las operaciones ejecutadas durante la jornada y su valor de cierre diario, manteniendo integridad en los cálculos, sincronización temporal y ausencia de discrepancias entre sistemas internos y fuentes de mercado. Fue necesario definir flujos de valorización fiables, capaces de procesar ventanas críticas al final del día y soportar picos de carga sin comprometer exactitud ni tiempos de entrega.

Como Líder Técnico coordiné un equipo de cuatro personas —QA, analista funcional y dos desarrolladores— definiendo criterios arquitectónicos, priorización funcional y estándares de calidad. Impulsé la mejora continua mediante retrospectivas, revisión sistemática de código y adopción de prácticas alineadas con Scrum, asegurando una ejecución ordenada y una comunicación fluida entre negocio y equipo técnico.

La solución se implementó con Java 8 bajo arquitectura modular JEE con CDI, desarrollando servicios REST y SOAP para interoperabilidad y un frontend en ReactJS para la interacción de usuarios internos. El ciclo de calidad se aseguró mediante pruebas unitarias, validaciones E2E manuales, análisis estático con SonarQube y automatización de pipelines en Jenkins dentro de un proceso CI/CD. Se gestionó el versionado con Git, estableciendo revisiones de código sistemáticas y controles para mantener consistencia técnica en cada entrega.

El resultado fue una plataforma confiable que permitió a Protecciones disponer de una valorización diaria precisa de su portafolio, redujo incidencias operativas y mejoró significativamente la calidad y disponibilidad de la información utilizada en la toma de decisiones de inversión.

### Personalsoft S.A.S

**Analista ingeniería de Software**
noviembre de 2017 - octubre de 2018 (1 año)
Antioquia, Colombia

Diseñé y desarrollé para Bancolombia una API REST de consulta documental que centraliza y expone de forma unificada los documentos escaneados de clientes integrados con Oracle WebCenter Content (WCC). El reto principal fue comprender a profundidad el API propietario del gestor documental, mapear sus operaciones internas y transformar modelos y estructuras heterogéneas en contratos REST estandarizados y alineados con las normas arquitectónicas del banco. También debí resolver diferencias de formatos, validar metadatos y asegurar un comportamiento consistente ante solicitudes de alto volumen provenientes de múltiples canales internos.

A nivel de negocio, el desafío se centró en garantizar tiempos de respuesta estables, cumplir estrictas políticas de seguridad y auditoría sobre información sensible y ofrecer trazabilidad exhaustiva de cada consulta realizada. Esto implicó diseñar mecanismos de control, registro y validación que permitieran rastrear operaciones de inicio a fin, manteniendo integridad, confidencialidad y cumplimiento normativo en todo el flujo.

La solución se implementó con Java 6 y JEE, exponiendo servicios REST y SOAP sobre WebSphere Application Server, integrándose con el gestor documental mediante las APIs específicas de Oracle WCC. El proyecto se acompañó de pruebas automatizadas y funcionales ejecutadas con VSTS, control de versiones y despliegues en entornos corporativos gestionados de manera iterativa, en coordinación directa con arquitectura, seguridad y los equipos funcionales del banco para validar casos de uso y ajustar los contratos de servicio.

El resultado fue un punto único, estandarizado y confiable para la consulta documental de clientes, que redujo tiempos de acceso, disminuyó errores operativos derivados de integraciones individuales y facilitó la reutilización del servicio en nuevos procesos, canales y aplicaciones internas de Bancolombia.

### integ.ro

**Desarrollador Senior Java**
septiembre de 2017 - noviembre de 2017 (3 meses)
Medellin, Colombia

Desarrollé una billetera digital para el mercado estadounidense en Integ.ro, orientada a habilitar pagos y micro-ahorros automáticos mediante un mecanismo de redondeo inteligente de transacciones. El principal reto técnico consistió en implementar un módulo de pago capaz de redondear importes a dos decimales y transferir automáticamente la diferencia a un bolsillo de ahorro rentable, garantizando integridad transaccional, exactitud financiera y plena consistencia entre movimientos de débito y abono.

A nivel de negocio, la complejidad radicó en asegurar un flujo de pago confiable, transparente y trazable para el usuario final, cumpliendo requisitos regulatorios y manteniendo visibilidad completa del ciclo de vida de cada operación.

La solución se desarrolló con microservicios en Java 8 y Spring Boot sobre MySQL, aplicando pruebas unitarias, de integración y principios de diseño orientados a resiliencia. En frontend trabajé con Angular y React Native, construyendo componentes modulares y reutilizables. El proyecto utilizó Docker para contenedorización, despliegues en cloud, CI/CD con GitHub, Sonar, Jira y pipelines automatizados; además, se aplicaron prácticas TDD, pruebas funcionales y validaciones manuales para reforzar la calidad.

La organización del trabajo siguió Scrum, gestionando las tareas mediante historias de usuario, realizando retrospectivas periódicas y aplicando mejora continua en todos los procesos del ciclo de desarrollo. También participé en el diseño y evolución de los servicios web REST, asegurando estándares coherentes en la comunicación entre microservicios y la aplicación móvil.

El resultado fue un módulo de pagos y micro-ahorros estable, seguro y totalmente alineado con los requisitos operativos del producto financiero, mejorando la experiencia del usuario y fortaleciendo la confiabilidad del ecosistema digital de la billetera.

### everis

**Senior Solutions Analyst**
noviembre de 2016 - septiembre de 2017 (11 meses)
Bogotá D.C., Colombia

Participé en el desarrollo del portal VUCE del Ministerio de Comercio, Industria y Turismo de Colombia, plataforma nacional que centraliza y digitaliza trámites de importación, exportación y certificaciones del comercio exterior. El principal reto fue mantener y evolucionar un sistema crítico construido sobre una arquitectura legacy en Java 7 y JEE, garantizando continuidad operativa en un entorno en el que convergen múltiples entidades gubernamentales. La complejidad incluía integraciones SOAP heterogéneas con organismos como DIAN, INVIMA, ICA, MinDefensa y MinAmbiente, manejando contratos estrictos, validaciones regulatorias y flujos normativos cambiantes que debían mantenerse sincronizados y auditables.

Además de desarrollar módulos sensibles —registros, certificaciones y trámites de comercio exterior— asumí tareas de análisis funcional y técnico, estimación de esfuerzos, supervisión de entregables, diseño de planes de pruebas, ejecución de validaciones unitarias y de integración, seguimiento de actividades del equipo y planificación continua bajo estándares gubernamentales. También consolidé y transferí conocimiento técnico, metodológico y funcional para asegurar la correcta operación del sistema y la alineación con los lineamientos del proyecto.

La solución se implementó con Java 7, JEE, servicios SOAP, JSF con PrimeFaces, Oracle 8 y Tomcat 8, operando sobre infraestructura on-premise con despliegues manuales. Se utilizó Git para control de versiones, revisión de código, coordinación técnica con equipos funcionales y comunicación continua con entidades externas para garantizar la coherencia de los procesos y la disponibilidad del servicio.

El resultado fue una plataforma estable, segura y confiable que consolidó trámites críticos de comercio exterior, mejoró la eficiencia operativa y garantizó continuidad a miles de usuarios públicos y privados en todo el país.

### PRAGMA S.A.

**Desarrollador de software**
enero de 2016 - noviembre de 2016 (11 meses)
Medellin, Colombia

Participé en el desarrollo del proyecto +Protección para la entidad de pensiones Protección, una solución corporativa construida sobre IBM WebSphere Portal 8 orientada a modernizar la experiencia transaccional mediante portlets Java y AngularJS ejecutados en servidores WAS on-premise. El principal reto fue comprender y modelar la arquitectura propia de WebSphere Portal, incluyendo el ciclo de vida de los portlets, la gestión de scopes, la navegabilidad interna y las restricciones del contenedor JSR, garantizando un comportamiento coherente y seguro entre vistas y módulos. A nivel técnico implicó resolver limitaciones del framework, gestionar contextos compartidos, asegurar aislamientos adecuados y mantener una integración fluida con los servicios internos expuestos por la entidad mediante componentes JEE y servicios REST.

También participé en el levantamiento y refinamiento de requisitos con el cliente, estimación de historias de usuario bajo el marco Scrum y diseño técnico de componentes modulares. Desarrollé backend en Java 7 con Spring, Hibernate y JUnit tanto en portlets del portal como en aplicaciones web adicionales. Implementé servicios REST bajo JEE7 y realicé desarrollo frontend en AngularJS, JQuery, CSS y JSP, garantizando consistencia entre capas y compatibilidad con las restricciones del runtime de WebSphere Portal.

El proceso incluyó pruebas unitarias, validaciones manuales, control de versiones con Git, despliegues en WebSphere Application Server y una gestión estricta de configuración. Además, se aplicaron prácticas de revisión de código, retrospectivas de mejora continua y ciclos de integración continua adaptados al entorno corporativo mediante Jenkins y SonarQube.

El resultado fue un conjunto de portlets estables, bien integrados y alineados con la arquitectura del portal, mejorando la navegabilidad, la solidez funcional y la eficiencia operativa para usuarios internos y afiliados de la entidad de pensiones Protección.

### ingemedic & Metrologia

**Analista Desarrollador Java**
octubre de 2013 - diciembre de 2015 (2 años 3 meses)
Medellin, Colombia

1. Levantamiento y refinamiento de requisitos.
2. Estimación de entregables.
3. Desarrollo de backend en componentes modulares en Java 7 (JEE7), usando Spring e Hibernate.
4. Desarrollo de frontend en componentes JSP, usando CSS y JQuery.

### Fundación Universitaria Tecnológico Comfenalco Cartagena (Oficina de Egresados)

**Docente de Dedicación Fundación Universitaria Tecnológico Comfenalco**
enero de 2011 - diciembre de 2015 (5 años)

Docente de Dedicación en los programas tecnológicos producción industrial y sistemas de información; y en los programas profesionales Ingeniería de Sistemas e ingeniería Industrial. Coordinador de Nuevas Tecnologia de la Información y Comunicación (NTICs) en el los programas Tecnológicos y Profesionales Industriales.

### Fundación Universitaria Tecnológico Comfenalco Cartagena

_2 años_

**Docente Catedrático**
2010 - 2010 (menos de un año)

Desarrolle las Cátedras de Desarrollo de Software StandAlone Orientada a Objeto

**Desarrollador Junior**
julio de 2008 - diciembre de 2009 (1 año 6 meses)
Cartagena de Indias

1. Análisis, diseño y desarrollo de aplicaciones Web con PHP, Flash (AS3) y Mysql.
2. Diseño y Desarrollo de objetos Multimedia.
3. Administración de LMS, CMS, DMS, PMS, etc.

## Educación

### Fundación Universitaria Tecnológico Comfenalco

Especialista en Ingenieria de Software, Ingeniería informática · (2010 - 2011)

### Politécnico Grancolombiano

Ingeniero de Sistemas, Informática · (2005 - 2009)

### Fundación Universitaria Tecnológico Comfenalco

Tecnología en Sistemas de Información, Informatica · (2005 - 2007)
