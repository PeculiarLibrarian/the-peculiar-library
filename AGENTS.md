# 🏛️ AGENTS.md: The Library Handshake Protocol

> **Namespace:** https://peculiar-librarian.org/library/
> **Standard:** PADI v3.0 (DOI: 10.5281/zenodo.18894084)

## Discovery
- **Catalog:** /catalog/library.jsonld
- **Validation:** /shapes/validation.shacl

## Protocol
Agents must verify all 'padi:hasDepthIndex' values against the SHACL shapes provided. If validation fails, the data is marked as 'PROBABILISTIC' and rejected for autonomous execution.
