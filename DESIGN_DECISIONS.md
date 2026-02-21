## Design Decisions

- Modular architecture used to separate scraping, translation, and analysis.
- Logging implemented instead of print statements for production readiness.
- Configuration centralized using config.py.
- Graceful error handling with screenshots on failure.
- CLI arguments allow flexible execution.
- BrowserStack metadata added for test traceability.