---
title: 'The QuTech Software Maturity Model (QSMM)'
teaching: 15
exercises: 10
---

## QSMM

We frame our effort in this course in the context of the QuTech Software Maturity Model (QSMM). A software maturity model
consists of structured levels that describes how well the behaviors, practices and processes of software development an
organization can reliably and sustainably produce required outcomes. QSMM is a software maturity model specifically
tailored for QuTech, based on TNO guidelines. QSMM consists of two sub-models:

- the software product maturity model
- the software development process maturity model

The purpose of this episode is to explain how software developed by researchers should fit into these models.

## Software Product Maturity

This consists of the following levels:

| Category  | Type       |  Purpose  | Example |
| :-------- | :--------- | :---------------|:----------------------------------|
| 1         | Prototype  | Software developed for a specific analysis or to implement a concept (to generate feedback). | Small software product, a single (one-off) component created by one developer also being the primary user. The software may be reused by the developer but is not intended to be used by others and is not managed/maintained for the long term. |
| 2         | Proven     | Software for engineering feasibility demonstrations (prove that a technology works) or developed as part of a research project or output of a research project. | Small software product consisting of 1 or few components that are used by a limited number of internal users (e.g., a project or research group). Long term maintenance is more important because the software is distributed wider and has a lifespan longer than the setting in which it was developed.  |
| 3         | Mature     | Strategic, business/research objectives driven systems internally used over a longer period.  | Small projects delivering reliable software products that are used by a group of users and is often mission critical. When successful, the user base of an internal product may optionally be extended to external users. The software may also be used in hackathons. Long term maintenance is needed but organized within the user-group.  |
| 4         | Commercial-like | Products (operational environment, external facing) | Large projects with complex, public facing software products developed within separate software development teams. Long term software maintenance is done, often by different software engineers than the original developers. |

## Software Development Process Maturity

This consists of the following levels:

| Level | Name        |  Description  |
| :----- | :---------- | :------------------------------------------------|
| 1      | Undefined   | Undefined level, no policies or procedures established for the software process. Ad hoc unpredictable software development. Poorly controlled and reactive. Success is effort of individuals (local heroes). |
| 2      | Repeatable  | Repeatable level, basic project management established for software development (to track cost, functionality, and time). Development process decisions made are often reactive and based on intuition or experience instead of executing a predefined plan. The process is at least documented sufficiently such that repeating the same steps may be attempted.
| 3      | Mature      | Mature level. Software development process for management and engineering is documented. At this level, the software development process is defined clearly while at organizational level the processes are not standardized.
| 4      | Defined     | Defined level. Software development process for management and engineering are integrated in the organization. Projects tailor their processes from organization’s standards. The processes are qualitative measured and scored.
| 5      | Managed     | Managed level. The quality of the software process is quantitatively measured, so it can be evaluated and adjusted when necessary.
| 6      | Optimizing  | Optimizing level - continuous process improvement (based on data collected as described in the managed level, as well as investing in innovation).

## Goals for Research-Developed Software

- Most software developed by researchers will fall in the Category 1 and 2 in the Software Product Maturity levels.
Goal is to make it possible to transition this to Category 3 and 4 if ever needed
- With respect to process maturity:
    - Goal of this course is to make researches aware of development process levels, and the way they should be used
    - Level 1 development should only apply to ad-hoc projects, typically developed over at most few days.
    - For any other software development activities, researches should strive for at least Level 2, ideally Level 3 practices.

:::::::::::::::::::::::::::::::::::::::::  callout

### Group exercise

- List all libraries, software products that are used within your research group
- Categorize the components into home made and commercial
- Why do you pay for a certain commercial product?
- What level are the homemade libraries in? what level should they be in?


::::::::::::::::::::::::::::::::::::::::::::::::::



