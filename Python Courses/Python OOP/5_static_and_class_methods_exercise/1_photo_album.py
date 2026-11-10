class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for page in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls((photos_count + 3) // 4)

    def add_photo(self, label: str):
        for page_number, page in enumerate(self.photos, start=1):
            if len(page) < 4:
                page.append(label)
                return (
                    f"{label} photo added successfully on page "
                    f"{page_number} slot {len(page)}"
                )

        return "No more free slots"

    def display(self):
        new_row = "-----------"
        result = [new_row]

        for page in self.photos:
            result.append(" ".join(["[]"] * len(page)))
            result.append(new_row)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
