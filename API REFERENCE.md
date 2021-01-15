# API REFERENCE (v 1.0)

## ENDPOINT

 - TBC

## STATUSES

 - For all successsful requests response's status is `200 OK`. Exception is token revokation `204 NO CONTENT` and registration of a new user `201 CREATED`.
 
 - For requests supplied with wrong credentials response's status is `401 UNAUTHORIZED`. If you try to access resource without proper permissions (e.g. modify other user's info), response's status will be `403 FORBIDDEN`.

 - For requests supplied with invalid data based on internal app's checks (i.e. modify username with name already reserved by another user or register user with exisitng username or email address), response's status will be `400 BAD REQUEST` with below body:

	```
	{
	    "error": "Bad Request",
	    "message": <error-description>
	}
	```
 - For non-existing resources response's status is `404 NOT FOUND`.
 
## TOKEN

### DESCRIPTION

\# | Method | URL| Header| Description 
--- | --- | --- | --- | ---
1 | `POST` | */api/tokens* | `"Authorization: Basic <username>:<password>"` <sup>1</sup> | Get authentication token
2 | `DELETE` | */api/tokens* | `"Authorization: Bearer <token-to-be-revoked>"` | Delete authentication token

<sup>1</sup> Credentials must be [base64][1] encoded.

### REQUEST EXAMPLE

1. Get authentication token:
	-  `POST http://localhost:5000/api/tokens "Authorization: Basic <username>:<password>"`
2. Delete authentication token: 
	- `DELETE http://localhost:5000/api/tokens "Authorization: Bearer <token-to-be-revoked>"`

### RESPONSE EXAMPLE

1. Get authentication token:
	```
	{
		"token": "<your-new-token>"
	}
	```
1. Delete authentication token:
	```
	response with no body
	```
	
## USER

### DESCRIPTION

\# | Method | URL| Header | Description
--- | --- | --- | --- | ---
1 | `GET` | */api/users/\<id\>* |`"Authorization: Bearer <token>"`| Return a user
2 | `GET` | */api/users* |`"Authorization: Bearer <token>"`| Return a collection of all users
3 | `GET` | */api/users/\<id\>/followers* |`"Authorization: Bearer <token>"`| Return the followers of a user
4 | `GET` | */api/users/\<id\>/followed* |`"Authorization: Bearer <token>"`| Return the users a user is following
5 | `POST` | */api/users* |No authorization required| Register a new user
6 | `PUT` | */api/users/\<id\>* |`"Authorization: Bearer <token>"`| Modify a user

### REQUEST EXAMPLE

1. Return a user:
	- `GET http://localhost:5000/api/users/<id> "Authorization: Bearer <token>"`
2. Return a collection of all users:
	- `GET http://localhost:5000/api/users "Authorization: Bearer <token>"`
3. Return the followers of a user:
	- `GET http://localhost:5000/api/users/<id>/followers "Authorization: Bearer <token>"`
4. Return the users a user is following:
	- `GET http://localhost:5000/api/users/<id>/followed "Authorization: Bearer <token>"`
5. Register a new user:
	- `POST http://localhost:5000/api/users username=<username> password=<password> email=<email> "about_me=<modified-value>"`
6. Modify a user:
	- `PUT http://localhost:5000/api/users/<id> "Authorization: Bearer <token>" "<field>=<modified-value>"`

### RESPONSE EXAMPLE

1. Return a user:
	```
	{
	    "_links": {
	        "avatar": <gravatar-link>,
	        "followed": "/api/users/<id>/followed",
	        "followers": "/api/users/<id>/followers",
	        "self": "/api/users/<id>"
	    },
	    "about_me": <text>,
	    "followed_count": <n_followed>,
	    "follower_count": <n_followers>,
	    "id": <id>,
	    "last_seen": <timestamp>,
	    "post_count": <n_posts>,
	    "username": <username>
	}
	```
1. Return a collection of all users:
	- Metadata about response is followed by users' info
	- Users' info is in the same format as in #1
	- Results are paginated: defalt is 10 users per page
	```
	{
	    "_links": {
	        "next": "/api/users?page=<next-page-number>&per_page=<users-per-page>", // or null
	        "prev": "/api/users?page=<previous-page-number>&per_page=<users-per-page>", // or null
	        "self": "/api/users?page=<current-page-number>&per_page=<users-per-page>"
	    },
	    "_meta": {
	        "page": <current-page-number>,
	        "per_page": <users-per-page>,
	        "total_items": <total-number-users>,
	        "total_pages": <total-number-pages>
	    },
	    "items": [
	        {
				1st user. The same format as in #1.
	        },
	        {
				2nd user. The same format as in #1.
	        },
	        {
				And so on.
	        }
	    ]
	}
	```
1. Return the followers of a user:
	- The same format as in #2.
1. Return the users a user is following:
	- The same format as in #2.
1. Register a new user:
	- The same format as in #1.
1. Modify a user:
	 - The same format as in #1.

[1]: https://www.base64encode.org/
