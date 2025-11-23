# System Architecture Diagram

```mermaid
graph TD
User[User] --> FE[Streamlit Dashboard]
FE --> API[FastAPI Backend]
API --> DB[(SQLite Database)]
ETL[Python ETL Script] --> Raw[World Bank / UNESCO Data]
ETL --> DB
```
