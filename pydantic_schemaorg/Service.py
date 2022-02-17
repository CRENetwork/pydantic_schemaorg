from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Service(Intangible):
    """A service provided by an organization, e.g. delivery service, print services, etc.

    See: https://schema.org/Service
    Model depth: 3
    """
    type_: str = Field("Service", alias='@type')
    offers: Optional[Union[List[Union['Demand', 'Offer', str]], 'Demand', 'Offer', str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    areaServed: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'AdministrativeArea', 'Place']], str, 'Text', 'GeoShape', 'AdministrativeArea', 'Place']] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    serviceOutput: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    providerMobility: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates the mobility of a provided service (e.g. 'static', 'dynamic').",
    )
    aggregateRating: Optional[Union[List[Union['AggregateRating', str]], 'AggregateRating', str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    award: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    termsOfService: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Human-readable terms of service documentation.",
    )
    produces: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    brand: Optional[Union[List[Union['Organization', 'Brand', str]], 'Organization', 'Brand', str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    slogan: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    isSimilarTo: Optional[Union[List[Union['Product', 'Service', str]], 'Product', 'Service', str]] = Field(
        default=None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    serviceType: Optional[Union[List[Union[str, 'Text', 'GovernmentBenefitsType']], str, 'Text', 'GovernmentBenefitsType']] = Field(
        default=None,
        description="The type of service being offered, e.g. veterans' benefits, emergency relief, etc.",
    )
    logo: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        default=None,
        description="An associated logo.",
    )
    audience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    serviceArea: Optional[Union[List[Union['AdministrativeArea', 'GeoShape', 'Place', str]], 'AdministrativeArea', 'GeoShape', 'Place', str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    hasOfferCatalog: Optional[Union[List[Union['OfferCatalog', str]], 'OfferCatalog', str]] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    isRelatedTo: Optional[Union[List[Union['Product', 'Service', str]], 'Product', 'Service', str]] = Field(
        default=None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    hoursAvailable: Optional[Union[List[Union['OpeningHoursSpecification', str]], 'OpeningHoursSpecification', str]] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    review: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="A review of the item.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    availableChannel: Optional[Union[List[Union['ServiceChannel', str]], 'ServiceChannel', str]] = Field(
        default=None,
        description="A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).",
    )
    broker: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    serviceAudience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        default=None,
        description="The audience eligible for this service.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.OfferCatalog import OfferCatalog
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.ServiceChannel import ServiceChannel
