#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    print("Testing general/casual queries...")
    print("=" * 70)
    
    from rag.services.query_service import QueryService
    from rag.services.retriever_service import RetrieverService
    
    retriever = RetrieverService()
    query_service = QueryService()
    
    # Test with casual queries
    test_queries = [
        'hello',
        'thanks',
        'hi',
        'goodbye',
        'good morning',
    ]
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        print("-" * 70)
        
        # Check what's being retrieved
        docs, scores = zip(*retriever.retrieve_with_scores(query, k=3))
        print(f"Top 3 retrieval scores: {[f'{s:.4f}' for s in scores]}")
        
        # Check query response
        response = query_service.ask(query)
        is_fallback = "couldn't find this information" in response.answer.lower()
        
        print(f"Answer: {response.answer[:80]}...")
        print(f"Sources shown: {len(response.sources)}")
        print(f"Status: {'FALLBACK' if is_fallback else 'FOUND'}")
        
        if len(response.sources) > 0:
            print(f"  Sources: {[s.filename for s in response.sources]}")
    
    print("\n" + "=" * 70)
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
