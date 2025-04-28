from variantlib.models.provider import VariantFeatureConfig
from variantlib.models.variant import VariantDescription
from variantlib.protocols import PluginType
from variantlib.protocols import VariantPropertyType


class BlasPlugin(PluginType):
    namespace = "blas"

    def get_all_configs(self) -> list[VariantFeatureConfig]:
        return [
            VariantFeatureConfig("variant", ["mkl", "openblas"])
        ]

    def get_supported_configs(self) -> list[VariantFeatureConfig]:
        return []

    def get_variant_labels(self, variant_desc: VariantDescription) -> list[str]:
        for meta in variant_desc:
            if meta.namespace == "blas" and meta.key == "variant":
                return [meta.value]
        return []
