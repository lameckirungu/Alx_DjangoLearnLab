# 1. Define each endpoint contract

For each endpoint, write:

- input payload
- success o/p
- Auth requirements
- Side effects
- Error cases

## Exmple structure

- `POST /register`: unauthenticated, creates user, returns safe user fields
- `POST /login`: unauthenticated, validates credentials, returns token/session info
- `GET /profile`: authenticated, returns current user
- `PATCH /profile`: authenticated, updates allowed profile fields.

## 2.Derive serializer responsibilities from the contract

Ask:

- Is this endpoint input-heavy (validation/create)?
- Outpu-heavy (representation)?
- Both with different shapes?

Then choose:

- Register: write-focused serializer (create logic)
- Login: credential serializer
- Profile read/update: safe user/profile serializers

## 3. Choose view style based on endpoint complexity

- simple-CRUD behavior: DRF generics `CreateAPIView`
- Custom flow (login/token issuance): `APIView`
- Large resource sets: `ViewSet`

pick the smallest abstraction that matches endpoint behavior

## 4. Decide auth + permission per endpoint explicitly

For each endpoint, set:

- Authentication classes
- Permission classes

Typical mapping

- Register/Login: `AllowAny`
- Profile: `IsAuthenticated`

If this is not explicity, bugs usually follow

## 5. Bind serializer to action, not model

In each view, choose serializer by endpoint action.

- One model can map to multiple serializers
- View's job is orchestration: auth, validation, serializer call, response code

## 6. Define HTTP semantics before coding

Decide status codes and response envelope

- Register: 201
- Login: 200
- Profile (GET): 200
- Profile (PATCH): 200
- Validation/auth failures: 400/401

## 7. Implement in this order:

1. URL route and method
2. Permission/auth policy
3. Serializer wiring
4. Business operation (`create_user`, authenticate, get `request.user`)
5. Response shape + status
6. Tests for happy path + failure path

## 8. Validate with tests as design checks

Write tests from contracts:

- Register rejects weak/duplicate password/email
- Login rejects bad creds
- Profile requires auth
- Profile never exposes password/hash

if tests are hard to write, contract or view boundaries are unclear.