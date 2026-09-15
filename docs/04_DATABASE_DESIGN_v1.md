\# AI-MAM Database Design Document



Version: 1.0



Status: Draft



Product: AI Media Asset Manager (AI-MAM)



\---



\# 1. Overview



Dokumen ini mendefinisikan desain database untuk AI-MAM (AI Media Asset Manager).



Tujuan utama:



\- Menyimpan aset media

\- Menyimpan metadata hasil AI

\- Mendukung pencarian cepat

\- Mendukung workflow AI processing

\- Mendukung skalabilitas enterprise



Database utama menggunakan PostgreSQL.



Search Engine menggunakan OpenSearch.



Object Storage menggunakan MinIO.



\---



\# 2. Architecture Principles



\## UUID First



Semua Primary Key menggunakan UUID.



Contoh:



```sql

id UUID PRIMARY KEY

```



Keuntungan:



\- Aman untuk distributed systems

\- Cocok untuk microservices

\- Mendukung multi-node deployment



\---



\## Metadata Driven



Seluruh aset harus memiliki metadata yang dapat dicari.



\---



\## AI First



Metadata tidak hanya dibuat manusia tetapi juga dihasilkan AI.



\---



\## Search First



Data harus mudah diindeks ke OpenSearch.



\---



\# 3. Core Entities



\## Users



Menyimpan data pengguna sistem.



\## Roles



Menyimpan role dan permission.



\## Assets



Menyimpan informasi file media.



\## Asset Versions



Menyimpan versi aset.



\## Transcripts



Menyimpan hasil speech-to-text.



\## Scenes



Menyimpan hasil scene detection.



\## Tags



Menyimpan tag metadata.



\## Keywords



Menyimpan keyword hasil AI.



\## AI Knowledge



Knowledge layer hasil AI analysis.



\## Jobs



Queue processing AI.



\## Audit Logs



Aktivitas pengguna.



\---



\# 4. Entity Relationship Diagram (ERD)



Users

│

├── Assets

│

├── Jobs

│

└── Audit Logs



Assets

│

├── Asset Versions

├── Transcripts

├── Scenes

├── Tags

├── Keywords

└── AI Knowledge



\---



\# 5. Database Tables



\## users



| Column | Type |

|----------|----------|

| id | UUID |

| email | VARCHAR(255) |

| password\_hash | TEXT |

| full\_name | VARCHAR(255) |

| is\_active | BOOLEAN |

| created\_at | TIMESTAMP |

| updated\_at | TIMESTAMP |



\---



\## roles



| Column | Type |

|----------|----------|

| id | UUID |

| name | VARCHAR(100) |

| description | TEXT |



Examples:



\- Admin

\- Editor

\- Viewer



\---



\## assets



| Column | Type |

|----------|----------|

| id | UUID |

| title | VARCHAR(500) |

| description | TEXT |

| filename | VARCHAR(500) |

| file\_path | TEXT |

| file\_size | BIGINT |

| duration | FLOAT |

| resolution | VARCHAR(50) |

| media\_type | VARCHAR(50) |

| status | VARCHAR(50) |

| created\_by | UUID |

| created\_at | TIMESTAMP |

| updated\_at | TIMESTAMP |



Status:



\- uploaded

\- processing

\- ready

\- failed



\---



\## asset\_versions



| Column | Type |

|----------|----------|

| id | UUID |

| asset\_id | UUID |

| version\_number | INTEGER |

| file\_path | TEXT |

| created\_at | TIMESTAMP |



\---



\## transcripts



| Column | Type |

|----------|----------|

| id | UUID |

| asset\_id | UUID |

| start\_time | FLOAT |

| end\_time | FLOAT |

| text | TEXT |

| language | VARCHAR(20) |

| confidence | FLOAT |

| created\_at | TIMESTAMP |



\---



\## scenes



| Column | Type |

|----------|----------|

| id | UUID |

| asset\_id | UUID |

| scene\_number | INTEGER |

| start\_time | FLOAT |

| end\_time | FLOAT |

| thumbnail\_path | TEXT |

| created\_at | TIMESTAMP |



\---



\## tags



| Column | Type |

|----------|----------|

| id | UUID |

| asset\_id | UUID |

| tag\_name | VARCHAR(255) |

| source | VARCHAR(50) |



Source:



\- manual

\- ai



\---



\## keywords



| Column | Type |

|----------|----------|

| id | UUID |

| asset\_id | UUID |

| keyword | VARCHAR(255) |

| score | FLOAT |



\---



\## ai\_knowledge



Tabel paling penting dalam AI-MAM.



| Column | Type |

|----------|----------|

| id | UUID |

| asset\_id | UUID |

| summary | TEXT |

| people | JSONB |

| organizations | JSONB |

| locations | JSONB |

| topics | JSONB |

| objects | JSONB |

| events | JSONB |

| sentiment | VARCHAR(50) |

| language | VARCHAR(20) |

| confidence | FLOAT |

| created\_at | TIMESTAMP |



Contoh:



```json

{

&#x20; "people":\["Prabowo"],

&#x20; "organizations":\["Ministry of Finance"],

&#x20; "locations":\["Jakarta"],

&#x20; "topics":\["Economy"],

&#x20; "objects":\["podium","microphone"],

&#x20; "events":\["Economic Forum"]

}

```



\---



\## jobs



| Column | Type |

|----------|----------|

| id | UUID |

| asset\_id | UUID |

| job\_type | VARCHAR(100) |

| status | VARCHAR(50) |

| progress | INTEGER |

| started\_at | TIMESTAMP |

| completed\_at | TIMESTAMP |



Job Types:



\- transcription

\- scene\_detection

\- object\_detection

\- keyword\_extraction

\- knowledge\_extraction



\---



\## audit\_logs



| Column | Type |

|----------|----------|

| id | UUID |

| user\_id | UUID |

| action | VARCHAR(255) |

| entity\_type | VARCHAR(100) |

| entity\_id | UUID |

| created\_at | TIMESTAMP |



\---



\# 6. OpenSearch Index Strategy



\## asset\_index



Asset metadata.



\## transcript\_index



Transcript search.



\## knowledge\_index



Knowledge layer search.



\---



\# 7. MinIO Storage Structure



assets-original/



assets-proxy/



assets-thumbnail/



assets-scene-thumbnail/



assets-temp/



\---



\# 8. Future Enterprise Extensions



Planned Tables:



\- faces

\- speakers

\- logos

\- ocr\_text

\- clips

\- collections

\- playlists

\- workflows



\---



\# 9. MVP Scope



Tables Required:



\- users

\- roles

\- assets

\- transcripts

\- scenes

\- ai\_knowledge

\- jobs



Version: MVP v1.0

