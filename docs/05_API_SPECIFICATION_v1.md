# AI-MAM API Specification

Version: 1.0

Status: Draft

Product: AI Media Asset Manager (AI-MAM)

---

# 1. API Overview

Base URL:

/api/v1

Architecture:

Frontend (Next.js)
        ↓
FastAPI REST API
        ↓
PostgreSQL
OpenSearch
MinIO

Authentication:

JWT Access Token
JWT Refresh Token

Content Type:

application/json

---

# 2. Authentication API

## Login

POST /auth/login

Request

{
  "email": "admin@aimam.com",
  "password": "password123"
}

Response

{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}

---

## Refresh Token

POST /auth/refresh

Response

{
  "access_token": "..."
}

---

## Logout

POST /auth/logout

---

## Current User

GET /auth/me

Response

{
  "id":"uuid",
  "email":"admin@aimam.com",
  "full_name":"Administrator",
  "role":"admin"
}

---

# 3. User API

## Get Users

GET /users

---

## Create User

POST /users

---

## Update User

PUT /users/{id}

---

## Delete User

DELETE /users/{id}

---

# 4. Asset API

## Upload Asset

POST /assets/upload

Multipart Form Data

Fields:

file
title
description

Response

{
  "id":"uuid",
  "status":"uploaded"
}

---

## Get Asset List

GET /assets

Query:

?page=1
&limit=20
&status=ready

---

## Get Asset Detail

GET /assets/{id}

---

## Update Asset

PUT /assets/{id}

---

## Delete Asset

DELETE /assets/{id}

---

# 5. Asset Version API

GET /assets/{id}/versions

POST /assets/{id}/versions

---

# 6. Transcript API

GET /assets/{id}/transcripts

Response

[
  {
    "start_time":0.0,
    "end_time":3.5,
    "text":"Hello world"
  }
]

---

# 7. Scene API

GET /assets/{id}/scenes

Response

[
  {
    "scene_number":1,
    "start_time":0,
    "end_time":15,
    "thumbnail_url":"..."
  }
]

---

# 8. Metadata API

## Get Tags

GET /assets/{id}/tags

---

## Add Tag

POST /assets/{id}/tags

---

## Delete Tag

DELETE /assets/{id}/tags/{tag_id}

---

## Get Keywords

GET /assets/{id}/keywords

---

# 9. AI Knowledge API

GET /assets/{id}/knowledge

Response

{
  "summary":"Economic speech by President",

  "people":["Prabowo"],

  "organizations":["Ministry of Finance"],

  "locations":["Jakarta"],

  "topics":["Economy"],

  "objects":["podium"],

  "events":["Economic Forum"]
}

---

# 10. Search API

## Keyword Search

GET /search?q=economy

---

## Semantic Search

GET /search/semantic?q=president speech

---

## Natural Language Search

GET /search/natural?q=video presiden bicara ekonomi

Response

{
  "results":[]
}

---

# 11. Job API

## Get Jobs

GET /jobs

---

## Get Job Detail

GET /jobs/{id}

---

## Retry Job

POST /jobs/{id}/retry

---

# 12. Dashboard API

GET /dashboard/stats

Response

{
  "total_assets":1000,
  "total_storage":"5TB",
  "processing_jobs":12,
  "completed_jobs":950
}

---

# 13. Health Check API

GET /health

Response

{
  "status":"healthy"
}

---

# 14. Future APIs

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

---

# 15. API Versioning Strategy

Current:

/api/v1

Future:

/api/v2

---

# 16. MVP APIs

Required:

Auth
Assets
Search
Knowledge
Jobs
Dashboard

Version: MVP v1.0
