from unittest import TestCase

from task_2 import Toy, AssemblyLine, Elf, AssemblerElf, PainterElf, WrapperElf, Santa


class Task2Test(TestCase):

    def setUp(self):
        self.toy1 = Toy("Toy1")
        self.toy2 = Toy("Toy2")

        self.line = AssemblyLine([self.toy1, self.toy2])

        self.assembler = AssemblerElf()
        self.painter = PainterElf()
        self.wrapper = WrapperElf()

        self.santa = Santa()

    def test_toy_init(self):
        self.assertTrue(hasattr(self.toy1, "is_assembled"), "You must initialize the is_assembled variable for Toy")
        self.assertFalse(self.toy1.is_assembled, "is_assembled seems wrong")

    def test_toy_is_complete(self):
        self.assertTrue(hasattr(self.toy1, "is_complete"), "You must implement is_complete() for Toy")
        self.assertFalse(self.toy1.is_complete(), "is_complete seems wrong")

    def test_assembly_line_get_toys(self):
        self.assertTrue(hasattr(self.line, "get_toys"), "You must implement get_toys for AssemblyLine")
        self.assertEqual(self.line.get_toys(), [self.toy1, self.toy2], "get_toys seems wrong")

    def test_assembly_line_get_number_of_toys(self):
        self.assertTrue(hasattr(self.line, "get_number_of_toys"), "You must implement get_number_of_toys for AssemblyLine")
        self.assertEqual(self.line.get_number_of_toys(), 2, "get_number_of_toys seems wrong")

    def test_assembly_line_take_toy(self):
        self.assertTrue(hasattr(self.line, "take_toy"), "You must implement take_toy for AssemblyLine")

        self.assertEqual(self.line.take_toy(), self.toy1, "take_toy seems wrong")

    def test_assembly_line_put_toy_back(self):
        self.assertTrue(hasattr(self.line, "put_toy_back"), "You must implement put_toy_back for AssemblyLine")

        toy = self.line.take_toy()
        self.line.put_toy_back(toy)
        self.assertEqual(self.line.get_toys(), [self.toy2, self.toy1], "Toys should be put back at the end of the line")

    def test_elf_inheritance(self):
        self.assertTrue(isinstance(self.assembler, Elf), "AssemblerElf must inherit from Elf")
        self.assertTrue(isinstance(self.painter, Elf), "PainterElf must inherit from Elf")
        self.assertTrue(isinstance(self.wrapper, Elf), "WrapperElf must inherit from Elf")

    def test_assembler_take_from(self):
        self.assertTrue(hasattr(self.assembler, "take_from"), "You must implement take_from in AssemblerElf")

        self.assembler.take_from(self.line)
        self.assertEqual(self.assembler._toy_working_on, self.toy1, "take_from seems wrong")
        self.assertEqual(self.line.get_toys(), [self.toy2])

    def test_assembler_put_back(self):
        self.assertTrue(hasattr(self.assembler, "put_back"), "You must implement put_back in AssemblerElf")

        self.assembler.take_from(self.line)
        self.assembler.put_back(self.line)
        self.assertEqual(self.assembler._toy_working_on, None, "put_back seems wrong")
        self.assertEqual(self.line.get_toys(), [self.toy2, self.toy1], "put_back seems wrong")

    def test_wrapper_do_job_unsuccessful(self):
        self.assertTrue(hasattr(self.wrapper, "do_job"), "You must implement do_job in WrapperElf")

        self.wrapper.take_from(self.line)
        self.wrapper.do_job()
        self.assertFalse(self.toy1.is_assembled, "do_job seems wrong")

    def test_wrapper_do_job_successful(self):
        self.assertTrue(hasattr(self.wrapper, "do_job"), "You must implement do_job in WrapperElf")

        self.toy1.is_assembled = True
        self.toy1.is_painted = True

        self.wrapper.take_from(self.line)
        self.wrapper.do_job()
        self.assertTrue(self.toy1.is_assembled, "do_job seems wrong")

    def test_santa_verify(self):
        self.assertTrue(hasattr(self.santa, "verify"), "You must implement verify for Santa")

        self.assertFalse(self.santa.verify(self.line), "verify seems wrong")

        for toy in self.line.get_toys():
            toy.is_assembled = True
            toy.is_painted = True
            toy.is_wrapped = True

        self.assertTrue(self.santa.verify(self.line), "verify seems wrong")
