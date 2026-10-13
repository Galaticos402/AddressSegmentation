class VariantGenerator:
    def __init__(self):
        self.PROVINCE_PREFIXES = ["tp", "thanhpho", "tinh", "t"]
        self.PROVINCE_POSTFIXES = ["c", "city", "province"]
        self.WARD_PREFIXES = ["p", "phuong", "quan", "q"]
        self.WARD_POSTFIXES = ["ward", "w", "district"]
        self.STREET_PREFIXES = ["d", "duong"]
        self.STREET_POSTFIXES = ["street", "str", "st", "s"]
        self.COMMON_ABBREVIATION_DICT={
            "hochiminh": "hcm",
            "hanoi": "hn",
            "lythuongkiet": "ltk",
            "longan": "la",
            "angiang": "ag",
            "bariavungtau": "brvt",
            "cantho": "ct", 
            "suvanhanh": "svh",
        }

        self.REVERSE_ABBREVIATION_DICT = {
            abbreviation: full_name for full_name, abbreviation in self.COMMON_ABBREVIATION_DICT.items()
        }

    def generateVariants(self, s: str, type: str):
        if type == "PROVINCE":
            return self._generateProvinceVariants(s)
        if type == "WARD":
            return self._generateWardVariants(s)
        if type == "STREET":
            return self._generateStreetVariants(s)
        return [s]

    def _generateStreetVariants(self,street: str):
        variants = {street}
        if self.COMMON_ABBREVIATION_DICT.get(street) is not None:
            variants.add(self.COMMON_ABBREVIATION_DICT.get(street))

        if self.REVERSE_ABBREVIATION_DICT.get(street) is not None:
            variants.add(self.REVERSE_ABBREVIATION_DICT.get(street))

        for prefix in self.STREET_PREFIXES:
            if street.startswith(prefix):
                actual_street = street[len(prefix):]
                variants.add(actual_street)
                if self.COMMON_ABBREVIATION_DICT.get(actual_street) is not None:
                    variants.add(self.COMMON_ABBREVIATION_DICT.get(actual_street))

                if self.REVERSE_ABBREVIATION_DICT.get(actual_street) is not None:
                    print(f"Adding reverse abbreviation for street '{actual_street}': {self.REVERSE_ABBREVIATION_DICT.get(actual_street)}")
                    variants.add(self.REVERSE_ABBREVIATION_DICT.get(actual_street))

        for postfix in self.STREET_POSTFIXES:
            if street.endswith(postfix):
                actual_street = street[:-len(postfix)]
                variants.add(actual_street)
                if self.COMMON_ABBREVIATION_DICT.get(actual_street) is not None:
                    variants.add(self.COMMON_ABBREVIATION_DICT.get(actual_street))

                if self.REVERSE_ABBREVIATION_DICT.get(actual_street) is not None:
                    print(f"Adding reverse abbreviation for street '{actual_street}': {self.REVERSE_ABBREVIATION_DICT.get(actual_street)}")
                    variants.add(self.REVERSE_ABBREVIATION_DICT.get(actual_street))  

        variants.update(
            pattern
            for variant in variants.copy()
            for pattern in (
                f"d{variant}",
                f"duong{variant}",
                f"{variant}street",
                f"{variant}st",
            )
        )
        print(f"Generated variants for street '{street}': {variants}")
        return variants


    def _generateWardVariants(self,ward: str):
        variants = {ward}
        if self.COMMON_ABBREVIATION_DICT.get(ward) is not None:
            variants.add(self.COMMON_ABBREVIATION_DICT.get(ward))

        for prefix in self.WARD_PREFIXES:
            if ward.startswith(prefix):
                actual_ward = ward[len(prefix):]
                variants.add(actual_ward)
                if self.COMMON_ABBREVIATION_DICT.get(actual_ward) is not None:
                    variants.add(self.COMMON_ABBREVIATION_DICT.get(actual_ward))

                if self.REVERSE_ABBREVIATION_DICT.get(actual_ward) is not None:
                    variants.add(self.REVERSE_ABBREVIATION_DICT.get(actual_ward))

        for postfix in self.WARD_POSTFIXES:
            if ward.endswith(postfix):
                actual_ward = ward[:-len(postfix)]
                variants.add(actual_ward)
                if self.COMMON_ABBREVIATION_DICT.get(actual_ward) is not None:
                    variants.add(self.COMMON_ABBREVIATION_DICT.get(actual_ward))

                if self.REVERSE_ABBREVIATION_DICT.get(actual_ward) is not None:
                    variants.add(self.REVERSE_ABBREVIATION_DICT.get(actual_ward))   

        variants.update(
            pattern
            for variant in variants.copy()
            for pattern in (
                f"p{variant}",
                f"phuong{variant}",
                f"q{variant}",
                f"quan{variant}",
                f"{variant}ward",
                f"{variant}w",
            )
        )
        print(f"Generated variants for ward '{ward}': {variants}")
        return variants

    def _generateProvinceVariants(self, province: str):
        variants = {province}
        if self.COMMON_ABBREVIATION_DICT.get(province) is not None:
            variants.add(self.COMMON_ABBREVIATION_DICT.get(province))

        for prefix in self.PROVINCE_PREFIXES:
            if province.startswith(prefix):
                actual_province = province[len(prefix):]
                variants.add(actual_province)
                if self.COMMON_ABBREVIATION_DICT.get(actual_province) is not None:
                    variants.add(self.COMMON_ABBREVIATION_DICT.get(actual_province))

                if self.REVERSE_ABBREVIATION_DICT.get(actual_province) is not None:
                    variants.add(self.REVERSE_ABBREVIATION_DICT.get(actual_province))

        for postfix in self.PROVINCE_POSTFIXES:
            if province.endswith(postfix):
                actual_province = province[:-len(postfix)]
                variants.add(actual_province)
                if self.COMMON_ABBREVIATION_DICT.get(actual_province) is not None:
                    variants.add(self.COMMON_ABBREVIATION_DICT.get(actual_province))

                if self.REVERSE_ABBREVIATION_DICT.get(actual_province) is not None:
                    variants.add(self.REVERSE_ABBREVIATION_DICT.get(actual_province))                

        variants.update(
            pattern
            for variant in variants.copy()
            for pattern in (
                f"tp{variant}",
                f"thanhpho{variant}",
                f"tinh{variant}",
                f"t{variant}",
                f"{variant}city",
                f"{variant}c",
            )
        )
        print(f"Generated variants for province '{province}': {variants}")
        return variants