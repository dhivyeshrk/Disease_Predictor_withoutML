from textblob import TextBlob

# testData = """I have abnormal involuntary movements, sharp chest pain, dizziness and arm cramp"""
testData = """i have insomnia and sharp chest pain"""

# does not detect adjectives and adverbs like anxious, nervousness
blob = TextBlob(testData)
print(blob.noun_phrases)
# [unnatural language processing', 'nlp', u'computer science', u'artificial intelligence', u'computational linguistics']
