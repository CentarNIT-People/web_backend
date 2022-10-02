import httpx
from collections import Counter

def get_github_language_percentages(username):
    percentages = []
    languages = [x["language"] for x in httpx.get(
        f"https://api.github.com/users/{username}/repos").json()]

    for name, pct in {x: int(float(y) / len(languages) * 100)
                      for x, y in Counter(languages).items()}.items():
        percentages.append({"language": name, "percentage": pct})
    
    return sorted(
        percentages, key=lambda d: d['percentage'])[::-1][0:3]

def get_github_avatar_url(username):
    return httpx.get(
        f"https://api.github.com/users/{user.github}").json()["avatar_url"]
    