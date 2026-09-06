from client import SmartCitationCredibilityScorerClient

def main():
    client = SmartCitationCredibilityScorerClient()
    res = client.score_citation_credibility()
    print('Citation Credibility: ' + res['credibility_audit_id'] + ' (' + res['citation_badge'] + ')')
    print('Smart Index: ' + str(res['smart_citation_index']) + ' | Supporting: ' + str(res['supporting_citations_count']))
    print('Telemetry URL: ' + res['scite_telemetry_url'])

if __name__ == '__main__':
    main()
