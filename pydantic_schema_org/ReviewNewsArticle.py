from pydantic import Field
from pydantic_schema_org.CriticReview import CriticReview
from pydantic_schema_org.NewsArticle import NewsArticle


class ReviewNewsArticle(CriticReview, NewsArticle):
    """A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment"
     "of a service, product, performance, or artistic or literary work.

    See https://schema.org/ReviewNewsArticle.

    """

    locals().update({"@type": Field("ReviewNewsArticle", const=True)})


ReviewNewsArticle.update_forward_refs()
