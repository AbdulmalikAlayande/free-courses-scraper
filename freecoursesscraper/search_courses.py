#!/usr/bin/env python3
import json
import sys
from difflib import SequenceMatcher
from collections import defaultdict


class CourseSearcher:
    def __init__(self, json_file="courses.json"):
        """Initialize the searcher with course data"""
        self.courses = []
        self.load_courses(json_file)

    def load_courses(self, json_file):
        """Load courses from JSON file"""
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                self.courses = json.load(f)
            print(f"✓ Loaded {len(self.courses)} courses")
        except FileNotFoundError:
            print(f"Error: {json_file} not found. Run the scraper first!")
            sys.exit(1)

    def similarity_score(self, str1, str2):
        """Calculate similarity between two strings (0-1)"""
        return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

    def search(self, query, min_score=0.3):
        """Search courses by keyword or name with fuzzy matching"""
        query_lower = query.lower()
        results = []

        for course in self.courses:
            title = course["title"]
            title_lower = title.lower()

            # highest priority matching - exact substring
            if query_lower in title_lower:
                score = 1.0
            else:
                # Fuzzy matching
                score = self.similarity_score(query, title)

            if score >= min_score:
                results.append({"score": score, "course": course})

        # Sorting by highest score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results

    def search_by_keywords(self, keywords):
        """Search by multiple keywords (AND logic)"""
        keyword_list = [k.strip().lower() for k in keywords.split(",")]
        results = []

        for course in self.courses:
            title_lower = course["title"].lower()
            matches = sum(1 for kw in keyword_list if kw in title_lower)

            if matches > 0:
                score = matches / len(keyword_list)
                results.append({"score": score, "course": course, "matches": matches})

        results.sort(key=lambda x: (x["matches"], x["score"]), reverse=True)
        return results

    def search_by_category(self):
        """Group courses by category"""
        categories = defaultdict(list)

        category_keywords = {
            "Python": ["python"],
            "JavaScript": ["javascript", "js", "node", "react", "vue"],
            "Excel": ["excel", "spreadsheet"],
            "Design": ["photoshop", "illustrator", "canva", "figma", "design"],
            "Video Editing": [
                "premiere",
                "after effects",
                "filmora",
                "capcut",
                "video editing",
            ],
            "AI & Machine Learning": [
                "ai",
                "machine learning",
                "chatgpt",
                "deep learning",
                "neural",
            ],
            "Business": ["business", "management", "leadership", "marketing"],
            "Finance": ["financial", "accounting", "finance", "investment"],
            "Web Development": ["web", "html", "css", "php", "wordpress"],
            "Database": ["sql", "mysql", "database", "mongodb"],
            "Cloud": ["aws", "azure", "cloud", "gcp"],
            "Cybersecurity": [
                "security",
                "ethical hacking",
                "penetration",
                "cybersecurity",
            ],
        }

        for course in self.courses:
            title_lower = course["title"].lower()
            matched = False

            for category, keywords in category_keywords.items():
                if any(kw in title_lower for kw in keywords):
                    categories[category].append(course)
                    matched = True
                    break

            if not matched:
                categories["Other"].append(course)

        return categories

    def display_results(self, results, limit=20):
        """Display search results in a formatted way"""
        if not results:
            print("\\nNo courses found matching your query.")
            return

        print(f"\\n{'='*100}")
        print(f"Found {len(results)} courses (showing top {min(limit, len(results))})")
        print(f"{'='*100}\\n")

        for i, result in enumerate(results[:limit], 1):
            course = result["course"]
            score = result.get("score", 0)

            print(f"{i}. {course['title']}")
            print(f"   Match: {score*100:.1f}% | Date: {course['date']}")
            print(f"   URL: {course['url']}")
            print(f"   {'-'*98}\\n")

    def display_categories(self, categories):
        """Display courses grouped by category"""
        print(f"\\n{'='*100}")
        print(f"COURSES BY CATEGORY")
        print(f"{'='*100}\\n")

        for category, courses in sorted(
            categories.items(), key=lambda x: len(x[1]), reverse=True
        ):
            print(f"\\n{category} ({len(courses)} courses)")
            print("-" * 100)
            for i, course in enumerate(courses[:5], 1):  # Show top 5 per category
                print(f"  {i}. {course['title']}")
            if len(courses) > 5:
                print(f"  ... and {len(courses) - 5} more")
            print()


def main():
    """Main function to run interactive search"""
    searcher = CourseSearcher()

    print("\\n" + "=" * 100)
    print(" UDEMY FREE COURSES SEARCH TOOL ".center(100))
    print("=" * 100)

    while True:
        print("\\nOptions:")
        print("1. Search by keyword/name")
        print("2. Search by multiple keywords (comma-separated)")
        print("3. Browse by category")
        print("4. Show all courses")
        print("5. Exit")

        choice = input("\\nEnter your choice (1-5): ").strip()

        if choice == "1":
            query = input("\\nEnter search term: ").strip()
            if query:
                results = searcher.search(query)
                searcher.display_results(results)

        elif choice == "2":
            keywords = input("\\nEnter keywords (comma-separated): ").strip()
            if keywords:
                results = searcher.search_by_keywords(keywords)
                searcher.display_results(results)

        elif choice == "3":
            categories = searcher.search_by_category()
            searcher.display_categories(categories)

        elif choice == "4":
            print(f"\\nTotal courses: {len(searcher.courses)}")
            searcher.display_results(
                [{"course": c, "score": 1.0} for c in searcher.courses], limit=50
            )

        elif choice == "5":
            print("\\nGoodbye!")
            break

        else:
            print("\\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
