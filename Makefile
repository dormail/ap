SUBDIRS := $(sort $(wildcard */))

all:
	$(foreach dir, $(SUBDIRS), $(MAKE) -C $(dir); )

clean:
	$(foreach dir, $(SUBDIRS), $(MAKE) -C $(dir) clean;)
