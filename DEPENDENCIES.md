## INSTALL DEPENDENCIES

`conda env create --prefix ./venv --file environment.yml`

## SET-UP ENVIRONMENT VARIABLES

It can be done in terminal or .env file (`python-dotenv` package).

`MAIL_SERVER` [string]
`MAIL_PORT` [integer]
`MAIL_USE_TLS` [boolean]
`MAIL_USERNAME` [string]
`MAIL_PASSWORD` [string]
`ADMINS` [string]
`MS_TRANSLATOR_KEY` [string]
`ELASTICSEARCH_URL` [string]

## SET-UP EMAIL CONFIGURATION

1. Make sure you are logged-in into ONE account only.
1. Your app's configuration:
	- Host (`MAIL_SERVER`): smtp.gmail.com
	- Port (`MAIL_PORT`): 587 or 465 (587 for TLS, 465 for SSL)
	- Protocol (`MAIL_USE_TLS`): TLS or SSL
	- User (`MAIL_USERNAME`): YOUR_USERNAME@gmail.com
	- Password (`MAIL_PASSWORD`): YOUR_PASSWORD
1. Your Gmail's account configuration:
	- If 2-Step Verification is turned on - you need to set-up and use [App Password][10]
	- If it's off:
		- Allow [Less Secure Apps][11] to access your account
		- Visit this [page][12] and confirm your identity
		- If you still have errors check app's logs and visit the page from error description: ` smtplib.SMTPAuthenticationError: (534, <link-goes-here> Please log in via your web browser and then try again)`

## SET-UP SEARCH ENGINE

1. Install [elasticsearch][1].
1. Run it from command line before starting your app: `.\bin\elasticsearch.bat`.

## SET-UP TASK QUEUE

1. Install Redis message queue:
	 - [Linux / Mac OS][2]
	 - [Windows][3]
1. RQ task queue will be installed from ***INSTALL DEPENDENCIES*** step.
1. If you are using Windows, please note: *RQ workers will only run on systems that implement fork(). Most notably, this means it is not possible to run the workers on Windows without using the [Windows Subsystem for Linux][4] and running in a bash shell.*

## PREPARE TRANSLATIONS

Already done - FYI only.

1. Extract the text to be translated:
	- `pybabel extract -F babel.cfg -k _l -o messages.pot .`

1. Create a language catalog:
	- Long command: `pybabel init -i messages.pot -d app/translations -l <language-code>`
	- Short command (cli): `flask translate init <language-code>`

1. Once you finish translating messages.po file, compile final translation:
	- Long command: `pybabel compile -d app/translations`
	- Short command (cli): `flask translate compile`

1. If you wish to update translation (intelligent merge):
	- `pybabel extract -F babel.cfg -k _l -o messages.pot .`
	- Long command: `pybabel update -i messages.pot -d app/translations`
	- Short command (cli): `flask translate update`

## PREPARE APP FOR DEPLOYMENT

1. Install [git][5] and [set it up][6]. 
1. Create [Heroku][8] account and add your [credit card][9].
1. Install [Heroku CLI][7] and login to Heroku:
	- `heroku login`
1. Create Heroku app:
	- On terminal navigate to a root directory of the app (git repository)
	- `heroku apps:create bloggger` (app's name must be unique)
	- This will add an additional remote to your repository, hosted by Heroku:
		- To check list of remotes: `git remote -v`
1. Add a Postgres database to your app:
	- `heroku addons:add heroku-postgresql:hobby-dev`
	- Database url will be assigned to `DATABASE_URL` env variable (the same we use in our app)
1. Add a Elasticsearch to your app:
	- There are different providers available, we will use SearchBox
	- `heroku addons:create searchbox:starter`
	- Elasticsearch url will be assigned to `SEARCHBOX_URL` env variable (we use a different one in our app)
	- To get this url use command:
		- `heroku config:get SEARCHBOX_URL`
1. Add a Redis queue to your app:
	- `heroku addons:create heroku-redis:hobby-dev`
	- Redis url will be assigned to `REDIS_URL` env variable (the same we use in our app)
1. Set-up environment variables:
	- `heroku config:set`
	- Required:
		- All vars from ***SET-UP ENVIRONMENT VARIABLES***
		- `ELASTICSEARCH_URL=<elasticsearch-url>`
		- `FLASK_APP=bloggger.py`
		- `LOG_TO_STDOUT=1`
	- Set-up with defaults:
		- `DATABASE_URL`
		- `REDIS_URL`
		- `PORT`
		- `WEB_CONCURRENCY`
1. Do deployment:
	- `git push heroku main`
1. Start a worker for export posts task:
	- `heroku ps:scale worker=1`
1. Add search engine index:
	- Go to SearchBox Elasticsearch add-on from your app's dashboard
	- Choose Dashboard-Indices and add new `post` index
	
[1]: https://www.elastic.co/guide/en/elasticsearch/reference/7.10/zip-windows.html
[2]: https://redis.io/
[3]: https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504
[4]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
[5]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[6]: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
[7]: https://devcenter.heroku.com/articles/heroku-cli
[8]: https://heroku.com/
[9]: https://heroku.com/verify
[10]: https://support.google.com/accounts/answer/185833
[11]: https://support.google.com/accounts/answer/6010255
[12]: http://www.google.com/accounts/DisplayUnlockCaptcha
