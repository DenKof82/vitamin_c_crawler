# Module 1 (Python Crash Course) Final Project


## General Requirements
- Adhere to the PEP 8 style guide. Use an auto-formatter for consistency.
- Aim for ~80% code coverage with well-designed test cases.
- The project must be pip-installable and available on PyPI.
- The project must be publicly available on GitHub with a clean Git history.
- Project structure should include: module directory, tests directory, README.md (with user guide or documentation), .gitignore, requirements.txt/pyproject.toml (specifying dependencies and Python version compatibility - ideally 3.9+).
- Organize the module directory efficiently. Avoid large files or unusual naming conventions.
- Maintain clean code. Exposed functions must have docstrings, clear naming, and type annotations.

## Specific Requirements
- Implement web crawling functionality returning well-structured data of multiple types (e.g., text, numeric, categorical, images, audio), with at least two data types.
- Access all functionality through a single function in the main module.
- Function capabilities:
  - Time limit for execution (e.g., 60 seconds).
  - Option to select the source for crawling (e.g., lrytas.lt, eurovaistine.lt). 
  - Different data presentation formats: CSV string and a dictionary of records. For non-CSV data (images, audio), use dict records.
  - Include sample crawled data.

  
### Example Code Snippets

1. **Calling main function**:

```python
crawl(time_limit=60, source='lrytas', return_format='csv')
```
2. **Example of checking code coverage with pytest**    

```bash
pytest --cov=my_module tests/
```