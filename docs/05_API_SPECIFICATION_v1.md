\# AI-MAM API Specification



Version: 1.0



Status: Draft



Product: AI Media Asset Manager (AI-MAM)



\---



\# 1. API Overview



Base URL:



/api/v1



Architecture:



Frontend (Next.js)

&#x20;       ↓

FastAPI REST API

&#x20;       ↓

PostgreSQL

OpenSearch

MinIO



Authentication:



JWT Access Token

JWT Refresh Token



Content Type:



application/json



\---



\# 2. Authentication API



\## Login



POST /auth/login



Request



{

&#x20; "email": "admin@aimam.com",

&#x20; "password": "password123"

}



Response



{

&#x20; "access\_token": "...",

&#x20; "refresh\_token": "...",

&#x20; "token\_type": "bearer"

}



\---



\## Refresh Token



POST /auth/refresh



Response



{

&#x20; "access\_token": "..."

}



\---



\## Logout



POST /auth/logout



\---



\## Current User



GET /auth/me



Response



{

&#x20; "id":"uuid",

&#x20; "email":"admin@aimam.com",

&#x20; "full\_name":"Administrator",

&#x20; "role":"admin"

}



\---



\# 3. User API



\## Get Users



GET /users



\---



\## Create User



POST /users



\---



\## Update User



PUT /users/{id}



\---



\## Delete User



DELETE /users/{id}



\---



\# 4. Asset API



\## Upload Asset



POST /assets/upload



Multipart Form Data



Fields:



file

title

description



Response



{

&#x20; "id":"uuid",

&#x20; "status":"uploaded"

}



\---



\## Get Asset List



GET /assets



Query:



?page=1

\&limit=20

\&status=ready



\---



\## Get Asset Detail



GET /assets/{id}



\---



\## Update Asset



PUT /assets/{id}



\---



\## Delete Asset



DELETE /assets/{id}



\---



\# 5. Asset Version API



GET /assets/{id}/versions



POST /assets/{id}/versions



\---



\# 6. Transcript API



GET /assets/{id}/transcripts



Response



\[

&#x20; {

&#x20;   "start\_time":0.0,

&#x20;   "end\_time":3.5,

&#x20;   "text":"Hello world"

&#x20; }

]



\---



\# 7. Scene API



GET /assets/{id}/scenes



Response



\[

&#x20; {

&#x20;   "scene\_number":1,

&#x20;   "start\_time":0,

&#x20;   "end\_time":15,

&#x20;   "thumbnail\_url":"..."

&#x20; }

]



\---



\# 8. Metadata API



\## Get Tags



GET /assets/{id}/tags



\---



\## Add Tag



POST /assets/{id}/tags



\---



\## Delete Tag



DELETE /assets/{id}/tags/{tag\_id}



\---



\## Get Keywords



GET /assets/{id}/keywords



\---



\# 9. AI Knowledge API



GET /assets/{id}/knowledge



Response



{

&#x20; "summary":"Economic speech by President",



&#x20; "people":\["Prabowo"],



&#x20; "organizations":\["Ministry of Finance"],



&#x20; "locations":\["Jakarta"],



&#x20; "topics":\["Economy"],



&#x20; "objects":\["podium"],



&#x20; "events":\["Economic Forum"]

}



\---



\# 10. Search API



\## Keyword Search



GET /search?q=economy



\---



\## Semantic Search



GET /search/semantic?q=president speech



\---



\## Natural Language Search



GET /search/natural?q=video presiden bicara ekonomi



Response



{

&#x20; "results":\[]

}



\---



\# 11. Job API



\## Get Jobs



GET /jobs



\---



\## Get Job Detail



GET /jobs/{id}



\---



\## Retry Job



POST /jobs/{id}/retry



\---



\# 12. Dashboard API



GET /dashboard/stats



Response



{

&#x20; "total\_assets":1000,

&#x20; "total\_storage":"5TB",

&#x20; "processing\_jobs":12,

&#x20; "completed\_jobs":950

}



\---



\# 13. Health Check API



GET /health



Response



{

&#x20; "status":"healthy"

}



\---



\# 14. Future APIs



Planned Endpoints:



/faces

/speakers

/logos

/ocr

/clips

/collections

/playlists

/workflows

/assistant



\---



\# 15. API Versioning Strategy



Current:



/api/v1



Future:



/api/v2



\---



\# 16. MVP APIs



Required:



Auth

Assets

Search

Knowledge

Jobs

Dashboard



Version: MVP v1.0

