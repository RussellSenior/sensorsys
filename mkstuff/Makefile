
SHELL=/bin/sh

.PHONY : all

all : $(patsubst %.log,%.sum,$(wildcard *.log)) $(patsubst %.log,%.json,$(wildcard *.log))

include multiplier.mk

%.sum : %.log
	@echo "Making $@"
	@K=${K} /home/russell/src/ingest/summarize.pl $^ | sort > $@

%.json : %.log
	@echo "Making $@"
	@K=${K} /home/russell/src/ingest/summarize2.pl $^ > $@

