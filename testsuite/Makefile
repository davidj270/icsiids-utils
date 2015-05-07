default:

always:

prep: a1 a2 a3

a1: always
	dd if=/dev/zero of=$@ bs=1024 count=1024
	touch -t 201505061020 $@

a2: always
	dd if=/dev/zero of=$@ bs=1024 count=2048
	touch -t 201505061016 $@

a3: always
	dd if=/dev/zero of=$@ bs=1024 count=3096
	touch -t 201505061018 $@
