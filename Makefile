PELICAN=bin/pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py


help:
	@echo 'Makefile for a pelican Web site                                     '
	@echo '                                                                    '
	@echo 'Usage:                                                              '
	@echo '   make html                        (re)generate the web site       '
	@echo '   make clean                       remove the generated files      '
	@echo '   make start                   	   start/restart develop_server.sh '
	@echo '   make stop                   	   stop develop_server.sh          '
	@echo '   github                           upload the web site via gh-pages'
	@echo '                                                                    '


html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'


clean:
	find $(OUTPUTDIR) -mindepth 1 -not \( -name .gitkeep \) -delete


start:
	$(BASEDIR)/develop_server.sh restart


stop:
	$(BASEDIR)/develop_server.sh stop


github:
	ghp-import -m "Update website from master branch for GitHub Pages" $(OUTPUTDIR)
	git push origin gh-pages


.PHONY: help html clean start stop github

