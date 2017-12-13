# Mozilla Change Integration Service PersonAPI

__Description:__

This API will return profiles as they are stored in the dynamodb table.  Currently only two scopes for non
interactive clients are supported.  But more scopes and search features are planned for the future.

# Deployment Container

```
docker run --rm -ti \
-v ~/.aws:/root/.aws \
-v ~/workspace/person-api/:/workspace \
mozillaiam/docker-sls:latest \
/bin/bash
```

# Locations

Highly subject to change.

__Prod__ : https://uhbz4h3wa8.execute-api.us-west-2.amazonaws.com/prod/

__Dev__ : https://295w5a6tu1.execute-api.us-west-2.amazonaws.com/dev/

__Scopes Supported:__
  - read:email
  - read:profile

# Calling the Profile Endpoint

1. Get an access token from the OAuth authorizer (i.e. https://auth.mozilla.auth0.com/oauth/token) with the required scopes for your query. This token is valid 24h.

- Out of browser?
- OAuth dance?
- scopes?

2. Use the access token to retrieve data from the API.

```HTTP
GET /profile/{userid}
Authorization: Bearer $ACCESS_TOKEN

{
    ...
    example ?
}
```

> Make sure you urlencode the user id (`user.user_id`).

Example:

```
curl --request GET --url https://295w5a6tu1.execute-api.us-west-2.amazonaws.com/dev/profile/ad%7CMozilla-LDAP-Dev%7Ckangtest --header 'authorization: Bearer N0-hV2n33aCiXYZ'`
```
