SUBDIRS = src etc man test

rpmdirs:
	mkdir -p $(top_builddir)/rpm/SPECS
	mkdir -p $(top_builddir)/rpm/SOURCES
	mkdir -p $(top_builddir)/rpm/BUILD
	mkdir -p $(top_builddir)/rpm/RPMS
	mkdir -p $(top_builddir)/rpm/SRPMS

rpm: dist rpmdirs
	rpmbuild -ta --define "_topdir $(realpath $(top_builddir)/rpm)" $(DIST_ARCHIVES)

EXTRA_DIST = META rquota.spec DISCLAIMER
