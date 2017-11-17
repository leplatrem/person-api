# Mozilla Change Integration Service PersonAPI

This is a proof of concept.  Not ready for use outside of Core IAM team.

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

__Prod__ : https://uhbz4h3wa8.execute-api.us-west-2.amazonaws.com/prod/profile/
__Dev__ : https://295w5a6tu1.execute-api.us-west-2.amazonaws.com/dev/profile/

__Scopes Supported:__
  - read:email
  - read:profile

# Calling the Profile Endpoint

 curl --request GET --url https://295w5a6tu1.execute-api.us-west-2.amazonaws.com/dev/profile/ad%7CMozilla-LDAP-Dev%7Ckangtest --header 'authorization: Bearer YOURBEARERTOKENHERE'

> Make sure you urlencode the authzero_id.
