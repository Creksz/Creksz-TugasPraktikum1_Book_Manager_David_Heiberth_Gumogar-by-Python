import unittest
from typing import List

# ==========
# CLASS BOOK
# ==========

class Book:
    def __init__(self, title, author, year):
        if title is None or not title.strip():
            raise ValueError("Judul tidak boleh kosong")
        if author is None or not author.strip():
            raise ValueError("Penulis tidak boleh kosong")
        if year < 2000 or year > 2100:
            raise ValueError("Tahun hanya bisa diisi dari tahun 2000 sampai 2100")

        self.title = title.strip()
        self.author = author.strip()
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self.title == other.title and
            self.author == other.author and
            self.year == other.year
        )

    def __hash__(self):
        return hash((self.title, self.author, self.year))


# ==================
# CLASS BOOK MANAGER
# ==================

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        if book is None:
            raise ValueError("Buku tidak boleh kosong")
        self.books.append(book)

    def remove_book(self, title: str) -> bool:
        if title is None or not title.strip():
            raise ValueError("Judul tidak boleh kosong")
        title_lower = title.strip().lower()
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title_lower]
        return len(self.books) < initial_count

    def get_all_books(self) -> List[Book]:
        return self.books.copy()

    def find_books_by_author(self, author: str) -> List[Book]:
        if author is None or not author.strip():
            raise ValueError("Penulis tidak boleh kosong")
        author_lower = author.strip().lower()
        return [book for book in self.books if book.author.lower() == author_lower]

    def find_books_by_year(self, year: int) -> List[Book]:
        if year < 2000 or year > 2100:
            raise ValueError("Tahun hanya bisa diisi dari tahun 2000 sampai 2100")
        return [book for book in self.books if book.year == year]

    def get_book_count(self) -> int:
        return len(self.books)

    def contains(self, title: str) -> bool:
        if title is None or not title.strip():
            raise ValueError("Judul tidak boleh kosong")
        title_lower = title.strip().lower()
        return any(book.title.lower() == title_lower for book in self.books)

    def clear_all_books(self) -> None:
        self.books.clear()


# =========
# UNIT TEST
# =========

class TestBookManager(unittest.TestCase):

    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Tidak Ada Buku")
        self.assertFalse(removed)

    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        b1 = Book("AI", "Budi", 2021)
        b2 = Book("ML", "Budi", 2022)
        b3 = Book("IoT", "Citra", 2022)

        self.book_manager.add_book(b1)
        self.book_manager.add_book(b2)
        self.book_manager.add_book(b3)

        result = self.book_manager.find_books_by_author("Budi")
        self.assertEqual(2, len(result))
        for book in result:
            self.assertEqual("Budi", book.author)

    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        books = [
            Book("Judul A", "Penulis A", 2020),
            Book("Judul B", "Penulis B", 2021),
        ]
        for book in books:
            self.book_manager.add_book(book)

        all_books = self.book_manager.get_all_books()
        self.assertEqual(2, len(all_books))
        self.assertListEqual(books, all_books)


# ================
# MENJALANKAN TEST
# ================

if __name__ == "__main__":
    unittest.main()
