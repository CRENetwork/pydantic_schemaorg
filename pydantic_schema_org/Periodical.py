from pydantic import Field
from pydantic_schema_org.CreativeWorkSeries import CreativeWorkSeries


class Periodical(CreativeWorkSeries):
    """A publication in any medium issued in successive parts bearing numerical or chronological"
     "designations and intended, such as a magazine, scholarly journal, or newspaper to continue"
     "indefinitely. See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    See https://schema.org/Periodical.

    """

    locals().update({"@type": Field("Periodical", const=True)})


Periodical.update_forward_refs()
