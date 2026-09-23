# Fund Custard — Collective Savings Fund

🇬🇧 [English](#english) · 🇪🇸 [Español](#español)

---

## English

**Type:** Independent personal project  
**Repository:** [github.com/gtorres04/fund-custard](https://github.com/gtorres04/fund-custard)

Fund Custard is a monorepo for an annually managed collective savings fund. I designed and developed a full-stack platform with a Java 25 and Spring Boot 4.1.0 WebFlux backend and a React 19.2.0 frontend.

### Contributions and technical scope

- Built a reactive backend with Spring WebFlux, applying modular and Clean Architecture principles to separate domain, application, infrastructure, and delivery concerns.
- Implemented financial domain capabilities for funds, members, contributions, monthly closing, reports, credits, payments, and product relationships.
- Integrated PostgreSQL through reactive data access and Liquibase-managed database migrations.
- Designed REST APIs under the `/api/v1` boundary and protected production access with OAuth2 resource-server authorization and scoped permissions.
- Built the frontend with React and Vite, including responsive management views, authentication flows, pagination, reporting, and operational dashboards.
- Established automated verification with unit, integration, component, and Playwright end-to-end tests, supported by Docker Compose, Maven, npm, and Taskfile workflows.

### Tech Stack

- **Backend:** Java 25, Spring Boot 4.1.0, Spring WebFlux, Maven
- **Frontend:** React 19.2.0, TypeScript, Vite
- **Data and security:** PostgreSQL, R2DBC, Liquibase, OAuth2 Resource Server
- **Testing and delivery:** JUnit, integration testing, Playwright, Docker Compose, go-task
- **Engineering practices:** reactive programming, modular architecture, Clean Architecture, SOLID, automated testing, and API versioning

---

## Español

**Tipo:** Proyecto personal independiente  
**Repositorio:** [github.com/gtorres04/fund-custard](https://github.com/gtorres04/fund-custard)

Fund Custard es un monorepo para un fondo de ahorro colectivo gestionado anualmente. Diseñé y desarrollé una plataforma full-stack con backend en Java 25 y Spring Boot 4.1.0 WebFlux, y frontend en React 19.2.0.

### Contribuciones y alcance técnico

- Construí un backend reactivo con Spring WebFlux, aplicando principios de arquitectura modular y Clean Architecture para separar dominio, aplicación, infraestructura y entrega.
- Implementé capacidades del dominio financiero para fondos, afiliados, aportes, cierres mensuales, reportes, créditos, pagos y relaciones entre productos.
- Integré PostgreSQL mediante acceso reactivo y migraciones de base de datos gestionadas con Liquibase.
- Diseñé APIs REST bajo el límite `/api/v1` y protegí el acceso productivo mediante autorización OAuth2 Resource Server y permisos basados en scopes.
- Construí el frontend con React y Vite, incluyendo vistas responsive de gestión, flujos de autenticación, paginación, reportes y paneles operativos.
- Establecí verificación automatizada con pruebas unitarias, de integración, de componentes y end-to-end con Playwright, apoyada en Docker Compose, Maven, npm y flujos con Taskfile.

### Stack tecnológico

- **Backend:** Java 25, Spring Boot 4.1.0, Spring WebFlux, Maven
- **Frontend:** React 19.2.0, TypeScript, Vite
- **Datos y seguridad:** PostgreSQL, R2DBC, Liquibase, OAuth2 Resource Server
- **Pruebas y entrega:** JUnit, pruebas de integración, Playwright, Docker Compose, go-task
- **Prácticas de ingeniería:** programación reactiva, arquitectura modular, Clean Architecture, SOLID, testing automatizado y versionado de APIs

---

← [Back to Independent Projects / Volver a Proyectos Independientes](../README.md)
