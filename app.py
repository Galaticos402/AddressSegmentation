from storage import Storage
from mock_data import STREETS, WARDS, PROVINCE
from sentence_processor import SentenceProcessor
from variant_generator import VariantGenerator
from typo_generator import TypoGenerator

street_dict = Storage()
ward_dict = Storage()
province_dict = Storage()

sentence_processor = SentenceProcessor()
variant_generator = VariantGenerator()
typo_generator = TypoGenerator()

if __name__ == '__main__':
    # Init data in Trie
    for street in STREETS:
        street_normalized = sentence_processor.normalize(street)
        variants = variant_generator.generateVariants(street_normalized, "STREET")
        for v in variants:
            word = sentence_processor.normalize(v[::-1])
            street_dict.add(word, original_word=street)
            typos = typo_generator.generate_typos(word)
            for typo in typos:
                street_dict.add(typo, original_word=street)

    for ward in WARDS:
        ward_normalized = sentence_processor.normalize(ward)
        variants = variant_generator.generateVariants(ward_normalized, "WARD")
        for v in variants:
            word = sentence_processor.normalize(v[::-1])
            ward_dict.add(word, original_word=ward)
            typos = typo_generator.generate_typos(word)
            for typo in typos:
                ward_dict.add(typo, original_word=ward)

    for province in PROVINCE:
        province_normalized = sentence_processor.normalize(province)
        variants = variant_generator.generateVariants(province_normalized, "PROVINCE")
        for v in variants:
            word = sentence_processor.normalize(v[::-1])
            province_dict.add(word, original_word=province)
            typos = typo_generator.generate_typos(word)
            for typo in typos:
                province_dict.add(typo, original_word=province)
                
    print("Street Dictionary:")
    print(street_dict.getAllWords())
    print("Ward Dictionary:")
    print(ward_dict.getAllWords())
    print("Province Dictionary:")
    print(province_dict.getAllWords())

    address = "268 duong 5u van hanh phường Hoa hung, tLA"
    normalized_address = sentence_processor.normalize(address[::-1])
    possible_provinces = sentence_processor.possibleMatches(normalized_address, province_dict) or [None]
    combinations = []

    for province in possible_provinces:
        address_without_province = normalized_address
        if province is not None:   
            address_without_province = normalized_address.replace(
                province["word"], "", 1
            )
        print(f"Address without province: {address_without_province}")
        possible_wards = sentence_processor.possibleMatches(
            address_without_province, ward_dict
        ) or [None]

        for ward in possible_wards:
            address_without_ward = address_without_province
           
            print(f"Address without ward: {address_without_ward}")
            if ward is not None:
                address_without_ward = address_without_province.replace(
                    ward["word"], "", 1
                )

            possible_streets = sentence_processor.possibleMatches(
                address_without_ward, street_dict
            ) or [None]

            for street in possible_streets:
                combinations.append({
                    "province": province["original_word"] if province is not None else None,
                    "ward": ward["original_word"] if ward is not None else None,
                    "street": street["original_word"] if street is not None else None
                })

    most_reasonable_combination = sentence_processor.getMostReasonableCombination(combinations, normalized_address)
    print("Most Reasonable Combination:")
    print(most_reasonable_combination)