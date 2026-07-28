# pm-rag

Reusable ProjectMaker capability package for retrieval augmented generation and knowledge-base products.

It provides primitives for:

- Knowledge sources
- Document ingestion state
- Text chunks and citation metadata
- Retrieval result normalization
- Answer payloads with cited context

The package intentionally leaves provider-specific vector storage and embedding jobs configurable by the host template.
