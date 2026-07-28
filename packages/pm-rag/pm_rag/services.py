from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class TextChunk:
    ordinal: int
    text: str
    citation: dict[str, object]


@dataclass(frozen=True)
class RetrievalResult:
    chunk_id: object
    score: float
    text: str
    citation: dict[str, object]


def chunk_text(text: str, *, max_chars: int = 1200, overlap: int = 120, source_label: str = "") -> list[TextChunk]:
    normalized = " ".join((text or "").split())
    if not normalized:
        return []
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    if overlap < 0 or overlap >= max_chars:
        raise ValueError("overlap must be non-negative and smaller than max_chars")

    chunks: list[TextChunk] = []
    start = 0
    while start < len(normalized):
        end = min(len(normalized), start + max_chars)
        if end < len(normalized):
            boundary = normalized.rfind(" ", start, end)
            if boundary > start + max_chars // 2:
                end = boundary
        chunk = normalized[start:end].strip()
        if chunk:
            chunks.append(TextChunk(
                ordinal=len(chunks),
                text=chunk,
                citation={"source": source_label, "offset_start": start, "offset_end": end},
            ))
        start = max(end - overlap, end if end == len(normalized) else end)
        if end == len(normalized):
            break
    return chunks


def normalize_retrieval_results(rows: Iterable[Mapping[str, object]], *, limit: int = 8) -> list[RetrievalResult]:
    results = [
        RetrievalResult(
            chunk_id=row.get("id") or row.get("chunk_id"),
            score=float(row.get("score") or 0),
            text=str(row.get("text") or ""),
            citation=dict(row.get("citation") or {}),
        )
        for row in rows
    ]
    return sorted(results, key=lambda item: item.score, reverse=True)[:max(0, limit)]


def build_cited_answer_payload(answer: str, results: Sequence[RetrievalResult]) -> dict[str, object]:
    citations = []
    seen = set()
    for result in results:
        key = tuple(sorted(result.citation.items()))
        if key in seen:
            continue
        seen.add(key)
        citations.append(result.citation)
    return {"answer": answer, "citations": citations, "context_count": len(results)}
