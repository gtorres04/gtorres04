# Globant

🇬🇧 [English](#english) · 🇪🇸 [Español](#español)

---

## English

**Role:** Senior Java Software Engineer
**Period:** August 2023 - Present (3 years)
**Location:** Cartagena de Indias, Bolívar, Colombia

---

I develop and lead backend solutions with Java 21, Spring Boot 3, and Spring Cloud under hexagonal architecture, applying DDD, Clean Architecture, and SOLID principles for a modular and scalable domain. I integrate models in Cosmos DB and Gremlin graphs along with PostgreSQL, design Kafka pub/sub messaging flows, and manage continuous deployments via OpenShift and GitHub Actions. The Inditex delivery pipeline also uses Artifactory for artifact management.

Within the Inditex corporate project, I use **GitHub Copilot** and **OpenCode** as part of the development workflow, with Copilot integrated into the corporate **SDD** process. I configure and refine their harnesses and project instructions so LLM assistance follows the team's process and my engineering conventions, while I retain responsibility for design, review, testing, and final integration.

In the Inditex corporate project I build a platform that models and exploits the global product hierarchy through a backend based on Amiga Java and Spring Boot, enabling dynamic KPI calculation from garment to corporate level. The main challenge is defining a complex hierarchical model over Cosmos DB capable of representing departments, categories, and products, guaranteeing consistency and performance in a high-event-volume environment with monthly, semi-annual, and annual calculations. The technical complexity includes orchestrating intensive processing, maintaining integrity between Cosmos DB, PostgreSQL and Redis, and optimizing the data lifecycle to ensure stable response times even under peak load. At the business level, the platform must provide a unified and accurate view of performance, ensuring traceability and continuous availability.

The solution runs on Kubernetes on Inditex's PaaS platform, using PostgreSQL as the transactional database, Cosmos DB for graphs, Redis as a read accelerator, and Kafka as the event system. Spring Cloud supports the distributed-service ecosystem. The development cycle integrates GitHub, GitHub Actions, Argo Workflows, and Artifactory for CI/CD and artifact management, plus Docker for packaging. Quality is guaranteed with JUnit, Karate, and ICaRUS for unit, integration, E2E, load, and chaos testing. Observability is supported with Grafana, Prometheus, Zipkin, and Grafana Cloud Tempo, unifying metrics, logs, and distributed traces.

The result is a robust, scalable, and efficient platform that enables near real-time calculation of critical KPIs, strengthening analytics and decision-making.

### Tech Stack

- **Languages:** Java 21
- **Frameworks:** Spring Boot 3, Spring Cloud, Amiga Java
- **Architecture:** Hexagonal, DDD, Clean Architecture, SOLID
- **Data:** Cosmos DB / Gremlin, PostgreSQL, Redis
- **Messaging:** Kafka
- **Deployment:** Kubernetes (Inditex PaaS), OpenShift, Docker
- **CI/CD and artifacts:** GitHub Actions, Argo Workflows, Artifactory
- **Testing:** JUnit, Karate, ICaRUS
- **Observability:** Grafana, Prometheus, Zipkin, Grafana Cloud Tempo
- **AI-Assisted Development:** GitHub Copilot, OpenCode, corporate SDD workflow, LLM harness configuration

---

## Español

**Cargo:** Senior Java Software Engineer
**Período:** agosto de 2023 - Presente (3 años)
**Ubicación:** Cartagena de Indias, Bolívar, Colombia

---

Desarrollo y lidero soluciones backend con Java 21, Spring Boot 3 y Spring Cloud bajo arquitectura hexagonal, aplicando DDD, Clean Architecture y principios SOLID para un dominio modular y escalable. Integro modelos en Cosmos DB y grafos Gremlin junto con PostgreSQL, diseño flujos de mensajería con Kafka en pub/sub y gestiono despliegues continuos mediante OpenShift y GitHub Actions. El pipeline de entrega de Inditex también utiliza Artifactory para la gestión de artefactos.

En el proyecto corporativo de Inditex utilizo **GitHub Copilot** y **OpenCode** como parte del flujo de desarrollo, con Copilot integrado en el proceso corporativo de **SDD**. Configuro y ajusto sus harnesses y las instrucciones del proyecto para que la asistencia del LLM siga el proceso del equipo y mis convenciones de ingeniería, conservando la responsabilidad sobre el diseño, la revisión, las pruebas y la integración final.

En el proyecto corporativo de Inditex construyo una plataforma que modela y explota la jerarquía global de producto mediante un backend basado en Amiga Java y Spring Boot, habilitando el cálculo dinámico de KPIs desde el nivel prenda hasta el corporativo. El reto principal es definir un modelo jerárquico complejo sobre Cosmos DB capaz de representar departamentos, categorías y productos, garantizando consistencia y rendimiento en un entorno con alto volumen de eventos y cálculos mensuales, semestrales y anuales. La complejidad técnica incluye orquestar procesamiento intensivo, mantener integridad entre Cosmos DB, PostgreSQL y Redis y optimizar el ciclo de vida del dato para asegurar tiempos de respuesta estables incluso ante picos de carga. A nivel de negocio, la plataforma debe proporcionar una visión unificada y precisa del desempeño, asegurando trazabilidad y disponibilidad continua.

La solución se ejecuta sobre Kubernetes en la plataforma PaaS de Inditex, utilizando PostgreSQL como base transaccional, Cosmos DB para grafos, Redis como acelerador de lectura y Kafka como sistema de eventos. Spring Cloud soporta el ecosistema de servicios distribuidos. El ciclo de desarrollo integra GitHub, GitHub Actions, Argo Workflows y Artifactory para CI/CD y gestión de artefactos, además de Docker para empaquetado. La calidad se garantiza con JUnit, Karate e ICaRUS para pruebas unitarias, integración, E2E, carga y caos. La observabilidad se soporta con Grafana, Prometheus, Zipkin y Grafana Cloud Tempo, unificando métricas, logs y trazas distribuidas.

El resultado es una plataforma robusta, escalable y eficiente que permite calcular KPIs críticos en tiempo casi real, fortaleciendo la analítica y la toma de decisiones.

## Stack tecnológico

- **Lenguajes:** Java 21
- **Frameworks:** Spring Boot 3, Spring Cloud, Amiga Java
- **Arquitectura:** Hexagonal, DDD, Clean Architecture, SOLID
- **Datos:** Cosmos DB / Gremlin, PostgreSQL, Redis
- **Mensajería:** Kafka
- **Despliegue:** Kubernetes (PaaS Inditex), OpenShift, Docker
- **CI/CD y artefactos:** GitHub Actions, Argo Workflows, Artifactory
- **Testing:** JUnit, Karate, ICaRUS
- **Observabilidad:** Grafana, Prometheus, Zipkin, Grafana Cloud Tempo
- **Desarrollo asistido por IA:** GitHub Copilot, OpenCode, flujo corporativo SDD, configuración de harnesses para desarrollo con LLM

---

← [Back to Work Experience / Volver a Work Experience](../README.md)
