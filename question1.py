# Question 1 Task 1

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(review):
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())
    return review

print("Task 1: Keyword Highlighter")
for review in reviews:
    highlighted_review = highlight_keywords(review)
    print(highlighted_review)

# Question 1 Task 2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_sentiment(review):
    positive_count = 0
    negative_count = 0

    review_lower = review.lower()

    for word in positive_words:
        if word in review_lower:
            positive_count += review_lower.count(word)

    for word in negative_words:
        if word in review_lower:
            negative_count += review_lower.count(word)

    return positive_count, negative_count

print("\nTask 2: Sentiment Tally")
for index, review in enumerate(reviews, start=1):
    positive, negative = tally_sentiment(review)
    print(f"Review {index}: Positive words: {positive}, Negative words: {negative}")

# Question 1 Task 3
def create_summary(review):
    if len(review) <= 30:
        return review  

    last_space_index = review[:30].rfind(' ')
    
    if last_space_index != -1:
        summary = review[:last_space_index] + "..."
    else:
        summary = review[:30] + "..."
    
    return summary

print("\nTask 3: Review Summary")
for index, review in enumerate(reviews, start=1):
    summary = create_summary(review)
    print(f"Review {index} Summary: {summary}")
