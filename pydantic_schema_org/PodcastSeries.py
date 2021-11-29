from pydantic import AnyUrl, Field
from pydantic_schema_org.DataFeed import DataFeed
from typing import Any, Optional, Union, List
from pydantic_schema_org.Person import Person
from pydantic_schema_org.CreativeWorkSeries import CreativeWorkSeries


class PodcastSeries(CreativeWorkSeries):
    """A podcast is an episodic series of digital audio or video files which a user can download"
     "and listen to.

    See https://schema.org/PodcastSeries.

    """

    webFeed: Optional[Union[List[Union[AnyUrl, DataFeed]], Union[AnyUrl, DataFeed]]] = Field(
        None,
        description="The URL for a feed, e.g. associated with a podcast series, blog, or series of date-stamped"
     "updates. This is usually RSS or Atom.",
    )
    actor: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    locals().update({"@type": Field("PodcastSeries", const=True)})


PodcastSeries.update_forward_refs()
