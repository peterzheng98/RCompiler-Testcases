MAIN=$(PWD)/check/src/main.rs
USE=$(PWD)/check/src/use.txt
DIR=$(PWD)/semantic-2/src
CHECK=$(PWD)/check

load:
ifeq ($(name),)
	$(error Please specify data point, e.g. make load name=array1)
endif
	@echo "Loading $(name).rx into main.rs..."
	@cp $(USE) $(MAIN)
	@cat $(DIR)/$(name)/$(name).rx >> $(MAIN)

store:
ifeq ($(name),)
	$(error Please specify data point, e.g. make store name=array1)
endif
	@echo "Storing main.rs into $(name).rx..."
	tail -n +$$(($$(wc -l < $(USE))+1)) $(MAIN) > $(DIR)/$(name)/$(name).rx

ans:
ifeq ($(name),)
	$(error Please specify data point, e.g. make ans name=array1)
endif
	@echo "Showing answer for $(name).rx..."
	@cd $(CHECK) && cargo run < $(DIR)/$(name)/$(name).in > $(DIR)/$(name)/$(name).out && cd ..

clean:
	@echo "Clearing main.rs..."
	@echo "" > $(MAIN)

.PHONY: load store clean
.DEFAULT_GOAL := load
