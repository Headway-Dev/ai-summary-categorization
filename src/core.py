class Book:
    def __init__(
            self,
            firebase_document_path: str,
            title: str,
            overview: str | None = None,
            author: str | None = None,
            author_overview: str | None = None,
            learning_items: list[str] | None = None,
            categories: list[str] | None = None,
    ) -> None:
        self._firebase_document_path = firebase_document_path
        self._title = title
        self._overview = overview
        self._author = author
        self._author_overview = author_overview
        self._learning_items = [] if learning_items is None else learning_items
        self._categories = [] if categories is None else categories

    @property
    def book_id(self) -> str:
        return self._firebase_document_path.split('/')[-1]

    @property
    def firebase_document_path(self) -> str:
        return self._firebase_document_path 
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def overview(self) -> str | None:
        return self._overview
    
    @property
    def author(self) -> str | None:
        return self._author
    
    @property
    def author_overview(self) -> str | None:
        return self._author_overview
    
    @property
    def learning_itmes(self) -> list[str]:
        return self._learning_itmes
    
    @property
    def categories(self) -> list[str]:
        return self._categories
    
    @property
    def learning_items(self) -> list[str]:
        return self._learning_items
    
    def to_dict(self) -> dict:
        return {
            'firebase_document_path': self.firebase_document_path,
            'id': self.book_id,
            'title': self.title,
            'author': self.author,
            'overview': self.overview,
            'author_overview': self.author_overview,
            'categories': self.categories,
            'learning_items': self.learning_items,
        }
    
    @staticmethod
    def from_dict(d) -> 'Book':
        return Book(
            firebase_document_path=d['firebase_document_path'],
            title=d['title'],
            author=d['author'],
            overview=d['overview'],
            author_overview=d['author_overview'],
            categories=d['categories'],
            learning_items=d['learning_items']
        )

    def __str__(self) -> str:
        overview_preview = self.overview.replace("\n", "\\n")[:50] + "..." if self.overview else "None"
        author_overview_preview = self.author_overview.replace("\n", "\\n")[:50] + "..." if self.author_overview else "None"
        return (f'Book(id="{self.book_id}", title="{self.title}", author="{self.author}", '
                f'overview="{overview_preview}", author_overview="{author_overview_preview}", '
                f'categories={self.categories}, learning_items={self.learning_items})')


