# Postman Testing Checklist (Social Media API)

## 1) One-time setup

- Start your Django server from project root:
  - `source venv/bin/activate`
  - `python manage.py runserver`
- Open Postman.
- Import collection file:
  - `postman/Social_Media_API.postman_collection.json`
- Import environment file:
  - `postman/Local.postman_environment.json`
- Select environment: **Local Django API**.

## 2) Environment values to verify

- `base_url` = `http://127.0.0.1:8000`
- `username` = test username (change if needed)
- `password` = strong password you will use
- `token` = keep empty initially (auto-filled after Register/Login)

## 3) Manual endpoint checklist

### A. Register
- Request: `Auth -> Register`
- Expected:
  - Status `201`
  - JSON has `token`
  - JSON has `user.id`
- Auto side-effect:
  - `token` and `user_id` environment variables are saved by test script.

### B. Login
- Request: `Auth -> Login`
- Expected:
  - Status `200`
  - JSON has `token`
- Auto side-effect:
  - `token` environment variable refreshed.

### C. Get Profile
- Request: `Profile -> Get Profile (auth)`
- Header used: `Authorization: Token {{token}}`
- Expected:
  - Status `200`
  - JSON includes `username`

### D. Update Profile
- Request: `Profile -> Update Profile (auth)`
- Expected:
  - Status `200`
  - Response includes updated `bio`

## 4) Common failure checks

- `401 Unauthorized` on profile endpoints:
  - Re-run `Login` and confirm `token` is populated in environment.
- `400 Bad Request` on register:
  - Username may already exist, or password may be too weak.
- Connection refused:
  - Ensure server is running on `127.0.0.1:8000`.

## 5) Collection Runner (GUI)

- In Postman, open **Collection Runner**.
- Choose collection: **Social Media API**.
- Choose environment: **Local Django API**.
- Run in order:
  1. Register
  2. Login
  3. Get Profile (auth)
  4. Update Profile (auth)

## 6) CLI automated run with Newman (optional)

Install Newman once:
- `npm install -g newman`

Run tests from project root:
- `newman run postman/Social_Media_API.postman_collection.json -e postman/Local.postman_environment.json`

Useful report format:
- `newman run postman/Social_Media_API.postman_collection.json -e postman/Local.postman_environment.json -r cli,htmlextra`

## 7) Suggested per-feature testing routine

When you add a new endpoint:
- Add request to the collection under a relevant folder.
- Add at least 2 tests:
  - Correct status code
  - One key field assertion
- Update this checklist with expected behavior and failure cases.
