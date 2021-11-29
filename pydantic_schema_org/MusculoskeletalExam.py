from pydantic import Field
from pydantic_schema_org.PhysicalExam import PhysicalExam


class MusculoskeletalExam(PhysicalExam):
    """Musculoskeletal system clinical examination.

    See https://schema.org/MusculoskeletalExam.

    """

    locals().update({"@type": Field("MusculoskeletalExam", const=True)})


MusculoskeletalExam.update_forward_refs()
