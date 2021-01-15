## Introduction
***Bloggger*** is a web app for a microblogging platform. It is written mainly in Python (with some JavaScript parts) using Flask framework. Feel free to explore and use!

## Main Features
* Public Posting
* Private Messaging
* Personalized Posts Feed

## Supplementary Features
* Authentication and Authorization
* User Profile
* Notifications
* User Interface in Several Languages (EN, PL, RU, UK - more to come)
* Posts Translation (any language)
* Posts Full-Text Search
* Posts Export
* API Support

## Development Stack
* Web Framework:
	* [Flask][1]
* Visual Design / Rendering:
	* [Bootstrap][2]
	* [Jinja][3]
	* [WTForms][4]
* Web Server:
	* [Flask Development Server][21] *(v0)*
	* [gunicorn][22] *(v1)*
* Hosting:
	* [Heroku][20]
* Database:
	* [SQLite][16] *(v0)*
	* [PostgreSQL][23] *(v1)*
	* [SQLAlchemy][17]
	* [Alembic][18]
* Authentication and Authorization:
	* [Werkzeug][6]
	* [JWT][7]
* Search Engine:
	* [Elasticsearch][8]
* Background Jobs (e.g. Posts Export / Mail Sending):
	* [Redis][13]
	* [rq][14]
	* [threading][15]
* Translation (e.g. UI / Posts):
	* [Babel][10]
	* [guess_language][11]
	* [Microsoft Translator][12]
* Testing:
	* [unittest][9]
	
## Acknowledgments
This project wouldn't be possible without the great work done by ***Miguel Grinberg*** in his [Flask Web Development][19] book and tutorials. Highly encourage everyone to check it out!

[1]: https://flask.palletsprojects.com/en/1.1.x/
[2]: https://getbootstrap.com/
[3]: https://jinja.palletsprojects.com/en/2.11.x/
[4]: https://wtforms.readthedocs.io/en/2.3.x/
[6]: https://werkzeug.palletsprojects.com/en/1.0.x/utils/
[7]: https://jwt.io/
[8]: https://www.elastic.co/guide/en/elasticsearch/reference/7.10/elasticsearch-intro.html
[9]: https://docs.python.org/3/library/unittest.html#module-unittest
[10]: http://babel.pocoo.org/en/latest/
[11]: https://pypi.org/project/guess-language/
[12]: https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-info-overview
[13]: https://redis.io/
[14]: https://python-rq.org/
[15]: https://docs.python.org/3/library/threading.html
[16]: https://www.sqlite.org/index.html
[17]: https://www.sqlalchemy.org/
[18]: https://alembic.sqlalchemy.org/en/latest/tutorial.html
[19]: https://www.oreilly.com/library/view/flask-web-development/9781491991725/
[20]: https://heroku.com/
[21]: https://flask.palletsprojects.com/en/1.1.x/server/
[22]: https://gunicorn.org/
[23]: https://www.postgresql.org/