## INSTALL DEPENDENCIES

`conda env create --prefix ./venv --file environment.yml`

## SET-UP ENVIRONMENT VARIABLES

It can be done in terminal or .env file (`python-dotenv` package).

`MAIL_SERVER`  [string]
`MAIL_PORT` [integer]
`MAIL_USE_TLS` [boolean]
`MAIL_USERNAME` [string]
`MAIL_PASSWORD` [string]
`ADMINS` [string]

`MS_TRANSLATOR_KEY` [string]
`ELASTICSEARCH_URL` [string]

## SET-UP SEARCH ENGINE

1. Install [elasticsearch][1].
1. Run it from command line before starting your app: `.\bin\elasticsearch.bat`.

## SET-UP TASK QUEUE

1. Install redis message queue:
	 - [Linux / Mac OS ][2]
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

1. Once you finish translating messages.po file, compile final translation
	- Long command: `pybabel compile -d app/translations`
	- Short command (cli): `flask translate compile`

1. If you wish to update translation (intelligent merge):
	- `pybabel extract -F babel.cfg -k _l -o messages.pot .`
	- Long command: `pybabel update -i messages.pot -d app/translations`
	- Short command (cli): `flask translate update`

[1]: https://www.elastic.co/guide/en/elasticsearch/reference/7.10/zip-windows.html
[2]: https://redis.io/
[3]: https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504
[4]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
