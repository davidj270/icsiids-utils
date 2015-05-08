# icsiids-utils/testsuite Makefile.am

testfiles =  a1.test a2.test a3.test
CLEANFILES = $(testfiles)

prep: $(testfiles)

a1.test:
	dd if=/dev/zero of=$@ bs=1024 count=1024
	touch -t 201505061020 $@

a2.test:
	dd if=/dev/zero of=$@ bs=1024 count=2048
	touch -t 201505061016 $@

a3.test:
	dd if=/dev/zero of=$@ bs=1024 count=3096
	touch -t 201505061018 $@
