# CUET_IOTRIX

Competition Phase 1

# Project README

# CUET IOTRIX

**A smart ride management system for Pullers and Admins.**

- **Backend:** FastAPI, SQLModel, Argon2 password hashing
- **Frontend:** React.js, Axios, SweetAlert2, React Router DOM

This project allows users to sign up, be approved by admins, request rides, and for pullers to accept/reject/completed rides with points as rewards.

---

## Features

- User signup/login (puller & admin)
- Admin can approve/reject pullers
- Pullers can see pending ride requests
- Accept, reject, complete rides
- Pullers earn points for completing rides
- Real-time dashboard updates
- Beautiful, modern UI with hover effects

---

## Tech Stack

**Backend:**

- Python 3.10+
- FastAPI [standard]
- SQLModel
- pwdlib[argon2]

**Frontend:**

- React.js
- Axios
- React Router DOM
- SweetAlert2

**Other:**

- Node.js 18+ (for frontend)

---

## Setup Instructions

### Backend

1. **Clone the repository:**

<pre class="overflow-visible!" data-start="1295" data-end="1362"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> <your-repo-url>
</span><span>cd</span><span> <your-repo-folder>/backend
</span></span></code></div></div></pre>

2. **Create a virtual environment:**

<pre class="overflow-visible!" data-start="1402" data-end="1433"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
</span></span></code></div></div></pre>

3. **Activate the environment:**

- Windows:

<pre class="overflow-visible!" data-start="1481" data-end="1514"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>venv\Scripts\activate
</span></span></code></div></div></pre>

- Linux / Mac:

<pre class="overflow-visible!" data-start="1532" data-end="1568"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>source</span><span> venv/bin/activate
</span></span></code></div></div></pre>

4. **Install dependencies:**

<pre class="overflow-visible!" data-start="1600" data-end="1643"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

5. **Run the backend server:**

<pre class="overflow-visible!" data-start="1677" data-end="1714"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>uvicorn main:app --reload
</span></span></code></div></div></pre>

> The backend will run at `http://127.0.0.1:8000`

---

### Frontend

1. **Navigate to the frontend folder:**

<pre class="overflow-visible!" data-start="1827" data-end="1853"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>cd</span><span> ../frontend
</span></span></code></div></div></pre>

2. **Install npm dependencies:**

<pre class="overflow-visible!" data-start="1889" data-end="1912"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>npm install
</span></span></code></div></div></pre>

3. **Run the frontend:**

<pre class="overflow-visible!" data-start="1940" data-end="1961"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>npm start
</span></span></code></div></div></pre>

> The frontend will run at `http://localhost:3000`

> Make sure the backend is running so the frontend can communicate with it.

---

## API Endpoints

**Auth:**

- `POST /auth/signup` → Create user account
- `POST /auth/login` → Login
- `GET /auth/me` → Get user details (optional)

**Admin:**

- `GET /admin/pending` → Get pending puller accounts
- `POST /admin/approve/{user_id}` → Approve puller
- `POST /admin/reject/{user_id}` → Reject puller

**Puller:**

- `GET /puller/requests` → Get pending ride requests
- `POST /puller/accept` → Accept ride request
- `POST /puller/reject` → Reject ride request
- `GET /puller/accepted` → Get accepted rides
- `POST /puller/complete` → Complete ride
- `GET /puller/completed` → Get completed rides

---

## Notes

- Points are awarded to pullers: **100 points per completed ride**
- Pullers can only accept pending rides
- Frontend uses React state to refresh dashboard every 2 seconds
