VENV := .venv
PYUIC := $(VENV)/bin/pyside6-uic
PYRCC := $(VENV)/bin/pyside6-rcc

UI_DIR := ui
RESOURCES_DIR := ui

OUTPUT_UI_DIR := src/ui
OUTPUT_RESOURCES_DIR := src/ui

UI_FILES := $(wildcard $(UI_DIR)/*.ui)
UI_PY_FILES := $(patsubst $(UI_DIR)/%.ui, $(OUTPUT_UI_DIR)/%.py, $(UI_FILES))

RESOURCE_FILES := $(wildcard $(RESOURCES_DIR)/*.qrc)
RESOURCE_PY_FILES := $(patsubst $(RESOURCES_DIR)/%.qrc, $(OUTPUT_RESOURCES_DIR)/%_rc.py, $(RESOURCE_FILES))

compile-ui: $(UI_PY_FILES) $(RESOURCE_PY_FILES)

$(OUTPUT_UI_DIR)/%.py: $(UI_DIR)/%.ui
	$(PYUIC) -o $@ $<

$(OUTPUT_RESOURCES_DIR)/%_rc.py: $(RESOURCES_DIR)/%.qrc
	$(PYRCC) -o $@ $<

clean:
	rm -f $(UI_PY_FILES) $(RESOURCE_PY_FILES)