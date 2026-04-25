import re
from collections import Counter

def score_content(text, topic):
    """Comprehensive content scoring"""
    score = {
        'total': 0,
        'length': 0,
        'relevance': 0,
        'readability': 0,
        'structure': 0
    }
    
    text_lower = text.lower()
    topic_words = set(re.findall(r'\w+', topic.lower()))
    
    # Length score
    word_count = len(text.split())
    if 200 <= word_count <= 800:
        score['length'] = min(word_count / 400, 1.0) * 25
    
    # Relevance score
    text_words = [w for w in re.findall(r'\w+', text_lower) if len(w) > 3]
    common_words = set(topic_words) & set(text_words)
    score['relevance'] = min(len(common_words) * 10, 25)
    
    # Readability (sentence variety)
    sentences = len(re.findall(r'[.!?]+', text))
    if sentences > 3:
        score['readability'] = min(sentences * 5, 25)
    
    # Structure score
    has_paragraphs = text.count('\n\n') > 1
    score['structure'] = 25 if has_paragraphs else 10
    
    score['total'] = sum(score.values())
    return score