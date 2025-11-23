# Database Schema Diagram

```mermaid
graph TD
Countries[Countries Table<br/>- country_id (PK)<br/>- country_name<br/>- region]
Metrics[Education Metrics Table<br/>- id (PK)<br/>- country_id (FK)<br/>- year<br/>- literacy_rate<br/>- primary_enrollment<br/>- secondary_enrollment<br/>- gender_parity_index]

Countries --> Metrics
```
