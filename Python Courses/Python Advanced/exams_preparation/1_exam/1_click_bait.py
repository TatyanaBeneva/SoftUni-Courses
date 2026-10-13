from collections import deque

suggested_links = deque([int(el) for el in input().split()])
featured_articles = [int(el) for el in input().split()]
target_engagement_value = int(input())
final_collection = []

while suggested_links and featured_articles:
    link_el = suggested_links.popleft()
    article_el = featured_articles.pop()

    if link_el == article_el:
        final_collection.append(0)

    elif link_el > article_el:
        remainder = link_el % article_el
        final_collection.append(-remainder)

        if remainder != 0:
            suggested_links.append(remainder * 2)

    else:
        remainder = article_el % link_el
        final_collection.append(remainder)

        if remainder != 0:
            featured_articles.append(remainder * 2)

total_engagement_value = sum(final_collection)

print(f"Final Feed: {', '.join([str(el) for el in final_collection])}")

if total_engagement_value < target_engagement_value:
    print(f"Goal not achieved! Short by: {target_engagement_value - total_engagement_value}")
else:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")