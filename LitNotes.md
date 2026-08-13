
Zero-trust for AI agents means **never trust, always verify**. Every action an agent takes requires authentication and authorization in real-time. Access is granted based on current context, not static permissions.


*DESCRIBING DATA TO AGENT*
- Data definition language https://www.techtarget.com/whatis/definition/Data-Definition-Language-DDL
- mock data: same schema, plausible value distributions, no real records
- R package to "minimize" sensitive data: https://www.synthpop.org.uk/about-synthpop.html

THINGS ONE SHOULD PROVIDE:
- what type of data? surveys, text data, etc.
- language matters, for example, text data: german has umlaute, etc. which can break a code
- dataframe structure, variable names + types?
- what are the rows/ units?
- ID column?

*ON THE PROCEDURE / CONCEPT ITSELF*
- code-to-data paradigm: the sensitive data never moves and is never exposed; instead, analysis code travels to where the data lives, runs there, and only vetted results come back out
- federated
