CC := gcc
CFLAGS := -Wall -Wextra -m64 -O2 
BIN_DIR := bin
LIBS := -lsqlite3 -lm
SRC := $(wildcard src/*.c)

build: $(SRC) | $(BIN_DIR)
	$(CC) $(CFLAGS) $^ -o $(BIN_DIR)/MontyHall $(LIBS)

.PHONY: clean
clean: 
	rm -r $(BIN_DIR)/*

$(BIN_DIR):
	mkdir -p $(BIN_DIR)