CC := gcc
CFLAGS := -Wall -m64 -O2 
BIN_DIR := bin
LIBS := -lsqlite3 -lm
SRC := $(wildcard src/*.c)

build: $(SRC) | $(BIN_DIR)
	$(CC) $(CFLAGS) $^ -o $(BIN_DIR)/MontyHall

clean: 
	rm -rf $(BIN_DIR)/*

$(BIN_DIR):
	mkdir -p $(BIN_DIR)