# Análisis de Brechas — Software Engineer Java (Sector Energía, Ref. 1025)

> Comparación entre **todo el repositorio de experiencia** (`work-experience/**`, `README.md` principal y la variante [cv-software-engineer-java-energia.md](cv-software-engineer-java-energia.md)) y la oferta Ref. 1025. Objetivo: identificar brechas de habilidades y proponer qué **añadir**, **aprender** o **reformular** para mejorar las probabilidades de encaje.
>
> Principio rector: honestidad. Cada afirmación se ancla en un README real del repositorio. Las brechas se declaran de forma explícita, no se maquillan.

**Fecha de análisis:** 2026-07-17

---

## 1. Resumen ejecutivo

| Proyecto de la oferta | Nivel de encaje | Veredicto |
|---|---|---|
| **Proyecto 1** — Plataforma de analítica para contact center (Senior, full time) | **Alto (≈80%)** | Stack Java/Kafka/reactivo/Redis/SQL cubierto con experiencia de producción reciente. Brechas puntuales en Data Warehouse fact/dim explícito y Reactor/WebFlux. |
| **Proyecto 2** — Migración de CRM legacy (Mid, part time 4h/día) | **Medio-Alto (≈70%)** | Diseño de dominio (DDD, agregados, máquina de estados, audit log, integridad transaccional) muy sólido. Brechas en integraciones de mensajería (SMS/WhatsApp) y en LOPD/RGPD nominal. |

**Conclusión:** eres un candidato fuerte para **ambos** proyectos, con mejor ajuste técnico al Proyecto 1. Las brechas son de **terminología/dominio específico**, no de fundamentos. Todas son abordables con reformulación honesta del CV y, en dos casos, con estudio previo a la entrevista.

---

## 2. Matriz de requisitos vs. evidencia real del repositorio

| Requisito de la oferta | ¿Cubierto? | Evidencia en el repo (fuente real) |
|---|---|---|
| Java 17+ | ✅ Sí | Java 21 (Globant), Java 17 (Paradigma Digital) en producción |
| Programación reactiva (Vert.x / RxJava2) | ✅ Sí | Microservicios reactivos con **Vert.x** en producción (MasOrange, telco) |
| Programación reactiva (Reactor / WebFlux) | ⚠️ Parcial | Sin Reactor/WebFlux documentado; base reactiva sólida con Vert.x **transferible** |
| Kafka / event-driven / consumers | ✅ Sí | Pub/sub y Kafka PIPE (Globant, Paradigma Digital), consumers (MasOrange) |
| Redis | ✅ Sí | Acelerador de lectura/cache (Globant, Paradigma, MasOrange) |
| RDS / MySQL / SQL | ✅ Sí (RDS ⚠️) | MySQL (Integ.ro), PostgreSQL (Globant, Paradigma, MasOrange). **RDS** como servicio gestionado no está nombrado, pero es solo la capa cloud sobre motores que ya dominas |
| DDD / arquitectura hexagonal | ✅ Sí | Estándar aplicado en Globant, Paradigma, MasOrange |
| Agregados, value objects, invariantes | ✅ Sí | Modelo con invariantes financieras estrictas (SPIRIT/Makers); jerarquía global de producto (Globant) |
| Endpoints BFF sobre tablas ya pobladas | ✅ Sí | APIs REST/BFF sobre modelos existentes (Personalsoft/Bancolombia, Grupo Ditech/Evo Banco) |
| Data Warehouse / analítica | ⚠️ Parcial | **BigQuery + Looker Studio** en MasOrange (data warehouse columnar + BI). Falta modelado **fact/dim (star schema) explícito** |
| Jobs batch de roll-up y agregación | ⚠️ Parcial | Cálculos de KPI mensuales/semestrales/anuales de alto volumen (Globant); ventanas de cierre diario y consolidación (SPIRIT/Makers). Transferible, aunque no rotulado como "roll-up de DW" |
| Optimización de consultas e índices | ✅ Sí | Optimización del ciclo de vida del dato y rendimiento bajo picos (Globant); modelado MySQL (Integ.ro) |
| Idempotencia / estados asíncronos | ✅ Sí | Módulo de pagos idempotente (Integ.ro); eventos de dominio Kafka (Globant, Paradigma, MasOrange) |
| Modelo Client/Contract/SaleEvent + multitenancy | ⚠️ Parcial | Modelado de jerarquías de dominio complejas (Globant); configuración multi-servicio con Consul (Bankinter). **Multitenancy** como tal no está documentado explícitamente |
| Máquina de estados del contrato + audit log | ✅ Sí (transferible) | Flujos de valorización con trazabilidad total y auditoría (SPIRIT/Makers, Personalsoft/Bancolombia). "Máquina de estados" no rotulada literalmente |
| Integridad transaccional + modelado MySQL | ✅ Sí | Pagos MySQL (Integ.ro); ISO 8583/MasterCard (EVOLVE); persistencia PostgreSQL (MasOrange) |
| Ventas, activaciones, recuperaciones, comisiones | ⚠️ Parcial | Dominio de **cobros/facturación telco** (MasOrange, *mas-collections*) y valorización financiera (SPIRIT). Dominio CRM comercial específico no documentado |
| Integraciones SMS / email / WhatsApp / webhooks / callbacks | ⚠️ Parcial | Integraciones SOAP/REST heterogéneas con terceros (everis: DIAN/INVIMA/ICA; Evo Banco). Canales de **mensajería (SMS/WhatsApp)** no documentados |
| Consentimiento LOPD / RGPD | ⚠️ Parcial | Cumplimiento de auditoría y seguridad sobre datos sensibles de clientes (Bancolombia, everis). **LOPD/RGPD nominal** no documentado |

---

## 3. Brechas reales (priorizadas)

### 🔴 Brechas significativas (requieren acción antes de la entrevista)

1. **Modelado Data Warehouse fact/dim (star schema) explícito.** Tienes BigQuery + Looker Studio (MasOrange) y cálculos de agregación de alto volumen (Globant), pero no un proyecto rotulado de modelado dimensional clásico (hechos/dimensiones). Es el requisito más específico del Proyecto 1.
2. **Project Reactor / Spring WebFlux.** Tu experiencia reactiva es con Vert.x. Los conceptos (streams, backpressure, no bloqueo) son equivalentes, pero la API de Reactor y su integración con Spring WebFlux son distintas y podrían evaluarse en la entrevista técnica.

### 🟡 Brechas menores (se cubren con reformulación honesta)

3. **Amazon RDS.** Es solo MySQL/PostgreSQL gestionado en AWS; dominas ambos motores. Basta con nombrarlo correctamente.
4. **Multitenancy explícito.** Has modelado dominios complejos y configuración multi-servicio, pero no hay un README que diga "multitenant". Reformulable con matices.
5. **Máquina de estados nominal.** Los flujos de valorización/contrato con transiciones controladas equivalen a una máquina de estados; falta usar el término.
6. **LOPD/RGPD nominal.** Cumplimiento regulatorio bancario real (auditoría, trazabilidad, datos sensibles), pero no rotulado como GDPR/LOPD.

### 🟢 Brechas de canal/dominio (declarar con transparencia)

7. **Integraciones SMS/WhatsApp.** Tienes integración con terceros heterogéneos, pero no con proveedores de mensajería (Twilio, WhatsApp Business API, etc.).
8. **Dominio CRM comercial (activaciones, recuperaciones, comisiones).** Tienes cobros telco (MasOrange) y finanzas, adyacentes pero no idénticos.

---

## 4. Qué AÑADIR

### Al repositorio (`work-experience/**`) y al CV

- **Aflora la experiencia de BigQuery + Looker Studio de MasOrange en la variante del CV.** Hoy está en el README de MasOrange pero **no** se destaca en [cv-software-engineer-java-energia.md](cv-software-engineer-java-energia.md). Es tu mejor activo contra la brecha de Data Warehouse/analítica → súbelo a "Con experiencia comprobada" y a un bullet de logro.
- **Un bullet de "agregación/roll-up" explícito** apoyado en los cálculos mensuales/semestrales/anuales de Globant y las ventanas de cierre diario de SPIRIT, usando el vocabulario de la oferta ("jobs de agregación por ventanas temporales") sin inventar un DW clásico.
- **Métricas cuantitativas reales** en los logros (volumen de eventos/día, latencias p95, nº de microservicios, tamaño de datasets, reducción de tiempos). Hoy los logros son cualitativos; una sola cifra real por rol multiplica el impacto ATS y en entrevista. *(Requiere que aportes las cifras; no deben inventarse.)*
- **Palabras clave de dominio del Proyecto 2** que sí tienes: "audit log", "integridad transaccional", "consolidación diaria", "trazabilidad regulatoria" — ya presentes, reforzar consistencia.

### A tu preparación (no al CV)

- Un **proyecto personal o repaso guiado** de un star schema mínimo (tabla de hechos + 2-3 dimensiones) sobre PostgreSQL/BigQuery, para poder hablar con propiedad de fact/dim en la entrevista.

---

## 5. Qué APRENDER (repaso dirigido, priorizado)

| Tema | Esfuerzo | Por qué | Apalanca lo que ya sabes |
|---|---|---|---|
| **Modelado dimensional (fact/dim, star/snowflake schema)** | Medio | Brecha #1 del Proyecto 1 | BigQuery/Looker (MasOrange), agregaciones (Globant) |
| **Project Reactor + Spring WebFlux** (`Mono`/`Flux`, operadores, backpressure) | Bajo-Medio | Brecha #2; la oferta lo valora | Vert.x reactivo (MasOrange) — conceptos equivalentes |
| **Amazon RDS** (parámetros, read replicas, backups) | Bajo | Nombrarlo con propiedad | MySQL/PostgreSQL ya dominados |
| **Jobs batch de roll-up en DW** (ETL/ELT, materialized views, agregación incremental) | Bajo-Medio | Requisito Proyecto 1 | Ventanas de cierre (SPIRIT), KPIs periódicos (Globant) |
| **Integración de mensajería** (Twilio/WhatsApp Business API, webhooks, callbacks idempotentes) | Bajo | Requisito Proyecto 2 | Normalización de terceros (everis, Evo Banco), idempotencia (Integ.ro) |
| **LOPD/RGPD** (bases de legitimación, consentimiento, minimización) | Bajo | Requisito Proyecto 2 | Auditoría/seguridad bancaria (Bancolombia, everis) |

---

## 6. Qué REFORMULAR

Reformulaciones **honestas** (misma experiencia real, vocabulario alineado a la oferta):

| En el CV dice… | Reformular a… | Justificación (real) |
|---|---|---|
| "Redis como acelerador de lectura y cache" | "…sirviendo endpoints BFF de baja latencia sobre datos ya poblados con Redis" | La oferta pide BFF sobre tablas pobladas; Globant/Bancolombia encajan |
| "cálculos mensuales, semestrales y anuales" (Globant) | "jobs de agregación y roll-up por ventanas temporales sobre datos de alto volumen" | Vocabulario del Proyecto 1, sin inventar DW |
| "análisis de datos con BigQuery y reportes en Looker Studio" (oculto en MasOrange) | Bullet visible: "modelé y exploté datos analíticos en un **data warehouse columnar (BigQuery)** con reporting en Looker Studio" | Es tu contra-argumento directo a la brecha de DW |
| "flujos de valorización diaria con integridad" (SPIRIT) | "**máquina de estados** de operaciones con transiciones auditadas y **audit log**" | Mismo flujo, término del Proyecto 2 |
| "persistencia transaccional en PostgreSQL/MySQL" | "modelado e **integridad transaccional** sobre MySQL/PostgreSQL gestionados en cloud (equivalente a **RDS**)" | Reduce la brecha RDS sin mentir |
| "programación reactiva con Vert.x" | Añadir: "base reactiva **transferible a Project Reactor/WebFlux** (streams, backpressure, no bloqueo)" | Honesto y conecta con lo que valora la oferta |

> ⚠️ **No reformular** hacia afirmar experiencia directa en: Data Warehouse fact/dim, Project Reactor, SMS/WhatsApp o LOPD/RGPD nominal. Esos siguen siendo brechas y deben tratarse como "transferible / en aprendizaje", nunca como dominio consolidado.

---

## 7. Plan de acción priorizado

1. **Editar la variante del CV** [cv-software-engineer-java-energia.md](cv-software-engineer-java-energia.md):
   - Subir BigQuery/Looker Studio a competencias comprobadas + un logro visible.
   - Añadir bullet de "agregación/roll-up por ventanas temporales" (Globant/SPIRIT).
   - Aplicar las reformulaciones honestas de la sección 6.
2. **Recopilar 1-2 métricas reales por rol** y pedírtelas para incorporarlas (no inventar).
3. **Repaso antes de entrevista:** star schema (fact/dim) + Project Reactor básico. Son las dos únicas brechas que pueden evaluarse técnicamente en vivo.
4. **Carta de presentación:** declarar con transparencia las brechas 🟢 (SMS/WhatsApp, LOPD/RGPD nominal) como "canal/marco nuevo sobre base técnica ya existente".
5. **Postular preferentemente al Proyecto 1** como encaje principal; ofrecer el Proyecto 2 en paralelo apoyándote en el diseño de dominio.

---

## 8. Veredicto final

Tu perfil **cumple los fundamentos** de ambos proyectos con experiencia real y reciente. Las brechas son de **nomenclatura de dominio** (fact/dim, RDS, multitenancy, máquina de estados) y de **dos tecnologías concretas** (Reactor/WebFlux, canales de mensajería) — ninguna es estructural. Con las reformulaciones honestas de la sección 6, aflorar BigQuery/Looker Studio y un repaso puntual de modelado dimensional y Reactor, pasas de "candidato válido" a "candidato fuerte" sin comprometer la veracidad del CV.

---

← [Volver a la variante del CV](cv-software-engineer-java-energia.md)
