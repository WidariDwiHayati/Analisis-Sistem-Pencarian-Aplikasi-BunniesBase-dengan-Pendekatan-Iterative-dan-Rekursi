class BunniesBase:
    def __init__(self):
        self.songs = {
            "Attention": "New Jeans",
            "Hype Boy": "New Jeans",
            "Cookie": "New Jeans",
            "Hurt": "New Jeans",
            "Ditto": "Ditto",
            "OMG": "OMG",
            "Ditto": "OMG",
            "Tell Me (FRNK Remix)": "Tell Me",
            "Zero": "Zero",
            "Be Who You Are (ft. Jon Batiste, Camilo & J.I.D)": "Be Who You Are",
            "Zero (J.I.D Remix)": "Zero (Remix)",
            "New Jeans": "NewJeans (Super Shy)",
            "Super Shy": "NewJeans (Super Shy)",
            "New Jeans": "Get Up",
            "Super Shy": "Get Up",
            "ETA": "Get Up",
            "Cool With You": "Get Up",
            "Get Up": "Get Up",
            "ASAP": "Get Up",
            "Beautiful Restriction": "A Time Called You (Original Soundtrack From the Netflix Series)",
            "Gods": "Gods (New Jeans X League of Legends)",
            "우리의 밤은 당신의 낮보다 아름답다 (Our Night is more beautiful than your Day)": "NewJeans x MY DEMON",
            "우리의 밤은 당신의 낮보다 아름답다 (Our Night is more beautiful than your Day) (Inst.)": "NewJeans x MY DEMON",
            "Ditto (250 Remix)": "NJWMX",
            "OMG (FRNK Remix)": "NJWMX",
            "Attention (250 Remix)": "NJWMX",
            "Hype Boy (250 Remix)": "NJWMX",
            "Cookie (FRNK Remix)": "NJWMX",
            "Hurt (250 Remix)": "NJWMX",
            "Ditto (250 Remix) (Inst.)": "NJWMX",
            "OMG (FRNK Remix) (Inst.)": "NJWMX",
            "Attention (250 Remix) (Inst.)": "NJWMX",
            "Hype Boy (250 Remix) (Inst.)": "NJWMX",
            "Cookie (FRNK Remix) (Inst.)": "NJWMX",
            "Hurt (250 Remix) (Inst.)": "NJWMX",
            "How Sweet": "How Sweet",
            "Bubble Gum": "How Sweet",
            "How Sweet (Inst.)": "How Sweet",
            "Bubble Gum (Inst.)": "How Sweet",
            "Supernatural": "Supernatural",
            "Right Now": "Supernatural",
            "Supernatural (Inst.)": "Supernatural",
            "Right Now (Inst.)": "Supernatural"
        }

    def search_iterative(self, search_term):
        result = []
        for song, album in self.songs.items():
            if search_term.lower() in song.lower() or search_term.lower() in album.lower():
                result.append((song, album))
        return result

    def search_recursive(self, search_term, song_list=None, index=0, result=None):
        if result is None:
            result = []
        if song_list is None:
            song_list = list(self.songs.items())

        if index >= len(song_list):
            return result

        song, album = song_list[index]
        if search_term.lower() in song.lower() or search_term.lower() in album.lower():
            result.append((song, album))

        return self.search_recursive(search_term, song_list, index + 1, result)

    def display_results(self, results):
        if not results:
            print("No songs found.")
        else:
            print("Search results:")
            for song, album in results:
                print(f"Song: {song}, Album: {album}")

if __name__ == "__main__":
    app = BunniesBase()
    search_term = input("Enter search term: ")

    print("\nIterative search results:")
    iterative_results = app.search_iterative(search_term)
    app.display_results(iterative_results)

    print("\nRecursive search results:")
    recursive_results = app.search_recursive(search_term)
    app.display_results(recursive_results)
