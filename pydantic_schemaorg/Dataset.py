from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import datetime
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Dataset(CreativeWork):
    """A body of structured information describing some topic(s) of interest.

    See: https://schema.org/Dataset
    Model depth: 3
    """

    type_: str = Field(default="Dataset", alias="@type", const=True)
    catalog: Optional[
        Union[List[Union["DataCatalog", str]], "DataCatalog", str]
    ] = Field(
        default=None,
        description="A data catalog which contains this dataset.",
    )
    datasetTimeInterval: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the"
        "year 2011 (in ISO 8601 time interval format).",
    )
    variableMeasured: Optional[
        Union[List[Union[str, "Text", "PropertyValue"]], str, "Text", "PropertyValue"]
    ] = Field(
        default=None,
        description="The variableMeasured property can indicate (repeated as necessary) the variables"
        "that are measured in some dataset, either described as text or as pairs of identifier"
        "and description using PropertyValue.",
    )
    includedDataCatalog: Optional[
        Union[List[Union["DataCatalog", str]], "DataCatalog", str]
    ] = Field(
        default=None,
        description="A data catalog which contains this dataset (this property was previously 'catalog',"
        "preferred name is now 'includedInDataCatalog').",
    )
    measurementTechnique: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="A technique or technology used in a [[Dataset]] (or [[DataDownload]], [[DataCatalog]]),"
        "corresponding to the method used for measuring the corresponding variable(s) (described"
        "using [[variableMeasured]]). This is oriented towards scientific and scholarly dataset"
        "publication but may have broader applicability; it is not intended as a full representation"
        "of measurement, but rather as a high level summary for dataset discovery. For example,"
        "if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]]"
        'could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence".'
        'If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]]'
        'could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory". If there are'
        "several [[variableMeasured]] properties recorded for some given data object, use"
        "a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]].",
    )
    distribution: Optional[
        Union[List[Union["DataDownload", str]], "DataDownload", str]
    ] = Field(
        default=None,
        description="A downloadable form of this dataset, at a specific location, in a specific format. This"
        "property can be repeated if different variations are available. There is no expectation"
        "that different downloadable distributions must contain exactly equivalent information"
        "(see also [DCAT](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution) on"
        "this point). Different distributions might include or exclude different subsets of"
        "the entire dataset, for example.",
    )
    includedInDataCatalog: Optional[
        Union[List[Union["DataCatalog", str]], "DataCatalog", str]
    ] = Field(
        default=None,
        description="A data catalog which contains this dataset.",
    )
    issn: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
        "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
        "for, this serial publication.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.DataCatalog import DataCatalog
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DataDownload import DataDownload
