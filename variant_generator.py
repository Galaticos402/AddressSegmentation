class VariantGenerator:
    def __init__(self):
        self.PROVINCE_PREFIXES = ["tp", "thanhpho"]
        self.PROVINCE_POSTFIXES = ["c", "city"]
        self.WARD_PREFIXES = ["p", "phuong", "quan", "q"]
        self.WARD_POSTFIXES = ["ward", "w"]
        self.STREET_PREFIXES = ["d", "duong"]
        self.STREET_POSTFIXES = ["street", "str", "st", "s"]

    def generateVariants(self, s: str, type: str):
        if type == "PROVINCE":
            return self._generateProvinceVariants(s)
        if type == "WARD":
            return self._generateWardVariants(s)
        if type == "STREET":
            return self._generateStreetVariants(s)
        return [s]

    def _generateStreetVariants(self,street: str):
        variants = [street]
        for prefix in self.STREET_PREFIXES:
            if street.startswith(prefix):
                variants.append(street[len(prefix):])
        for postfix in self.STREET_POSTFIXES:
            if street.endswith(postfix):
                variants.append(street[:-len(postfix)])
                        
        variants.extend(
            pattern
            for variant in variants.copy()
            for pattern in (
                f"p{variant}",
                f"phuong{variant}",
                f"{variant}ward",
                f"{variant}w",
            )
        )
        return variants


    def _generateWardVariants(self,ward: str):
        variants = [ward]
        for prefix in self.WARD_PREFIXES:
            if ward.startswith(prefix):
                variants.append(ward[len(prefix):])
        for postfix in self.WARD_POSTFIXES:
            if ward.endswith(postfix):
                variants.append(ward[:-len(postfix)])
                        
        variants.extend(
            pattern
            for variant in variants.copy()
            for pattern in (
                f"p{variant}",
                f"phuong{variant}",
                f"{variant}ward",
                f"{variant}w",
            )
        )
        return variants

    def _generateProvinceVariants(self, province: str):
        variants = [province]
        for prefix in self.PROVINCE_PREFIXES:
            if province.startswith(prefix):
                variants.append(province[len(prefix):])

        for postfix in self.PROVINCE_POSTFIXES:
            if province.endswith(postfix):
                variants.append(province[:-len(postfix)])
                
        variants.extend(
            pattern
            for variant in variants.copy()
            for pattern in (
                f"tp{variant}",
                f"thanhpho{variant}",
                f"{variant}city",
                f"{variant}c",
            )
        )
        return variants