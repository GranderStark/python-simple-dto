"""
Tests for dto
"""
from unittest import TestCase

from src.python_simple_dto.dto import DTO, BaseDTO
from src.tests.test_data.constants import (
    ATTRIBUTE_A,
    ATTRIBUTE_B,
    BASIC_DTO_TEST,
    COMPLEX_DTO_TEST,
    DICT_ATTRIBUTE,
    DTO_ATTRIBUTE,
)


class DtoTestCase(TestCase):
    """
    DTO tests
    """

    def test_basic_dto(self):
        """
        test BaseDTO with simple "flat" dict
        """
        result = BaseDTO(BASIC_DTO_TEST)
        self.assertEqual(result, BASIC_DTO_TEST)
        self.assertEqual(result.name, BASIC_DTO_TEST["name"])

    def test_complex_dto(self):
        """
        test DTO with complex dict and setting data trough __init__
        """
        result = DTO(COMPLEX_DTO_TEST)
        self.assertEqual(result, COMPLEX_DTO_TEST)
        self.assertEqual(result.users[0].name, COMPLEX_DTO_TEST["users"][0]["name"])

    def test_complex_dto_update(self):
        """
        test updating DTO with complex dict
        """
        result = DTO(COMPLEX_DTO_TEST)
        result.attribute_a = ATTRIBUTE_A
        result["attribute_b"] = ATTRIBUTE_B
        self.assertEqual(result["attribute_a"], ATTRIBUTE_A)
        self.assertEqual(result.attribute_b, ATTRIBUTE_B)

        result.dict_attribute = DICT_ATTRIBUTE
        self.assertEqual(result.dict_attribute, DICT_ATTRIBUTE)
        result.dto_attribute = DTO(DTO_ATTRIBUTE)
        self.assertEqual(result.dto_attribute, DTO(DTO_ATTRIBUTE))
        self.assertEqual(result.dto_attribute, DTO_ATTRIBUTE)
