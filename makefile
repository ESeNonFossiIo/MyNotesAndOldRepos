.Phony: tests

tests:
	@./_utilities/test.py

# .ONESHELL:
GH_PAGES_SOURCES = _doc/source _doc/Makefile
gh-pages:
	@echo cd _doc && rm -rf source/lib.rst modules.rst
	@echo cd _doc && sphinx-apidoc -o source/ ..
	@echo "======================================================================"
	@echo " ---> Making documentation"
	@echo "======================================================================"
	@git checkout gh-pages
	@rm -rf *
	@git checkout master $(GH_PAGES_SOURCES)
	@git reset HEAD
	@cd "./_doc/"; make html
	@mv -fv _doc/build/html/* ./
	@rm -rf _doc/*
	@git add -A
	@git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push -f origin gh-pages
	@git checkout master
	@echo "======================================================================"
