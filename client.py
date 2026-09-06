class SmartCitationCredibilityScorerClient:
    def score_citation_credibility(self, paper_title='Attention Is All You Need', total_citations=145000, supporting_citations_ratio=0.88):
        return {
            'credibility_audit_id': 'cit_crd_8812',
            'paper_title': paper_title,
            'total_citations_analyzed': total_citations,
            'supporting_citations_count': int(total_citations * supporting_citations_ratio),
            'disputing_citations_count': int(total_citations * 0.02),
            'mentioning_citations_count': int(total_citations * 0.10),
            'smart_citation_index': 0.96,
            'citation_badge': 'HIGHLY_REPRODUCED_BENCHMARK',
            'scite_telemetry_url': 'https://research.science.genpark.ai/citations/cit_crd_8812.json'
        }
