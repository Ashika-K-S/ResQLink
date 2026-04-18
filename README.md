# 🚑 ResQLink

ResQLink is an Emergency Response System where:

- 👤 Citizens can report emergencies  
- 🚑 Volunteers can accept emergencies  
- 🏛 Authorities can resolve emergencies  

---

## 🔁 Workflow

Citizen → Volunteer → Authority

---

## ⚙️ Tech Stack

- Backend: Django REST Framework  
- Frontend: React  
- Database: PostgreSQL  

---

## 🔗 API Endpoints

- POST `/api/token/` → Login  
- POST `/api/emergency/` → Create emergency  
- GET `/api/emergency/` → List emergencies  
- POST `/api/emergency/{id}/assign/` → Assign  
- PATCH `/api/emergency/{id}/update_status/` → Resolve  

---

## 🚀 Features

- Role-based access control  
- Emergency workflow management  
- Secure backend (env variables)  

---

## 📌 Status

Backend completed ✅  
Frontend in progress 🚧  