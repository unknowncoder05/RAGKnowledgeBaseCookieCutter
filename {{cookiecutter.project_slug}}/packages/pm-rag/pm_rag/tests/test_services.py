from unittest import TestCase

from pm_rag.services import build_cited_answer_payload, chunk_text, normalize_retrieval_results


class RagServiceTests(TestCase):
    def test_chunk_text_creates_ordered_chunks_with_citations(self):
        chunks = chunk_text("Alpha beta gamma delta epsilon zeta", max_chars=18, overlap=3, source_label="doc")

        self.assertGreater(len(chunks), 1)
        self.assertEqual(chunks[0].ordinal, 0)
        self.assertEqual(chunks[0].citation["source"], "doc")
        self.assertIn("offset_start", chunks[0].citation)

    def test_normalize_retrieval_results_sorts_by_score_and_limits(self):
        results = normalize_retrieval_results([
            {"id": 1, "score": 0.2, "text": "low"},
            {"id": 2, "score": 0.9, "text": "high"},
            {"id": 3, "score": 0.5, "text": "mid"},
        ], limit=2)

        self.assertEqual([item.chunk_id for item in results], [2, 3])

    def test_build_cited_answer_payload_deduplicates_citations(self):
        results = normalize_retrieval_results([
            {"id": 1, "score": 1, "text": "a", "citation": {"source": "same"}},
            {"id": 2, "score": 0.8, "text": "b", "citation": {"source": "same"}},
        ])
        payload = build_cited_answer_payload("Answer", results)

        self.assertEqual(payload["answer"], "Answer")
        self.assertEqual(payload["context_count"], 2)
        self.assertEqual(payload["citations"], [{"source": "same"}])
