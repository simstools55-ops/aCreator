# Editorial Core Architecture

Version: 1.0
Status: Implemented in v0.4.0

## Purpose

Editorial Core is the product heart of SIMS Article Creator. It transforms a keyword into an approved publication package through explicit planning, evidence and editorial review stages. Article generation is not considered complete until the Publication Gate returns an approvable status.

## Five stages

1. Editorial Intelligence
2. Content Architecture
3. Evidence and Safety
4. Writing
5. Editorial Review and Publication Gate

## Core modules

- Keyword Intelligence Engine
- Search Intent Intelligence Engine
- Reader Intelligence Engine
- Editorial Brief Engine
- Coverage Engine
- Reader Journey Engine
- Evidence Planning Engine
- Structure Design Engine
- Writing Engine
- Editorial Review Engine
- Publication Readiness Engine

## Mandatory rule

No engine may skip directly from keyword input to final article. The Editorial Brief, Coverage Map and Evidence Plan are mandatory intermediate artifacts.
