# Software development

!!! abstract "Overview"

    - How can non-functional requirements be defined for software and its development?
    - When are these non-functional requirements relevant?

Each piece of software can have different quality criteria. When you're writing a small script for a friend, 
these criteria will be less strict compared to a complex feature at a large software company, for example.
A large part is covered in its technical requirements, after all, the software is of no use when it cannot perform its intended functions.

However, an often overlooked part is its development. Should multiple developers be able to work on it? Should it be maintainable for an extensive period?
These requirements do not affect the technical capabilities, but have a profound impact on its development.
The QuTech software maturity model (QSMM) has been developed to help new projects understand what is demanded of their products from a software engineering perspective.

## Software product maturity

Who is going to use this software? Will this be a single person or the entire company?
How long is the software going to be run? Is it used once to generate a result, or will it run for a few years?
The software product maturity model links these non-functional requirements to a software category, which can subsequently be used
to determine its recommended software development maturity category.

| Category   | Type            | Purpose                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                    |
|:-----------|:----------------|:------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1          | Prototype       | Software developed for a specific analysis or to implement a concept.                                       | Small software product, a single component created by one developer also being the primary user. The software may be reused by the developer but is not intended to be used by others and is not managed/maintained for the long term.                                                                                                     |
| 2          | Proven          | Software developed primarily to prove that a technology works, or developed as part of a research project.  | Small software product consisting of a few components that are used by a limited number of internal users (e.g., a project or research group). Long-term maintenance has to be considered, as it is distributed and has a lifespan longer than the setting in which it was developed.                                                      |
| 3          | Mature          | Strategic, business/research objectives driven systems internally used over a longer period.                | Small projects delivering reliable software products that are used by a group of users and is often mission critical. When successful, the user base of an internal product may optionally be extended to external users. Long term maintenance is needed but organized within the user-group.                                             |
| 4          | Commercial-like | Products (operational environment, external facing)                                                         | Large projects with complex, public facing software products developed within separate software development teams. Long term software maintenance is done, often by different software engineers than the original developers.                                                                                                             |

## Software development maturity

Using the analogy of writing a script for a friend, storing this script in a repository with full test coverage could be regarded as overengineering.
But, at the same time, when this piece of software is used across a large company, this process could prove insufficient. What if one colleague runs it on Windows? While another uses Ubuntu?
Will the code run in both cases? Will it still work after a few years? The software development maturity categories link the product category to the recommended development category.

| Product category | Development category | Name       | Description                                                                                                                                                                                                                                                                                                                                     |
|:-----------------|----------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                | 1                    | Undefined  | No policies or procedures established for the software process. Ad hoc unpredictable software development. Poorly controlled and reactive. Success depends on the effort of individuals.                                                                                                                                                        |
| 2                | 2                    | Repeatable | Basic project management established for software development (to track cost, functionality, and time). Development process decisions made are often reactive and based on intuition or experience instead of executing a predefined plan. The process is at least documented sufficiently such that repeating the same steps may be attempted. |
| 3                | 3                    | Mature     | Software development process for management and engineering is documented. At this level, the software development process is defined clearly while at organizational level the processes are not standardized.                                                                                                                                 |
| 4                | 4                    | Defined    | Software development process for management and engineering are integrated in the organization. Projects tailor their processes from organization’s standards. The processes are qualitative measured and scored.                                                                                                                               |
| 4                | 5                    | Managed    | The quality of the software process is quantitatively measured, so it can be evaluated and adjusted when necessary.                                                                                                                                                                                                                             |
| 4                | 6                    | Optimizing | Continuous process improvement (based on data collected as described in the managed level, as well as investing in innovation).                                                                                                                                                                                                                 |

Additionally, a software development template is available. By asking questions similar to those used in this chapter,
it can help new projects find potential bottlenecks before development starts, instead of during. 
Both QSMM and the template can be found in the shared Teams channel of the workshop. For questions related to these documents, 
or software development in general, contact the [software development support team](https://qutech.support/contact/).
