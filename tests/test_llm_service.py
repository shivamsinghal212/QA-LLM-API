import unittest
from unittest.mock import patch, MagicMock
from src.llm_service import LLMChain, get_llm_chain_obj


class TestLLMChain(unittest.TestCase):
    def setUp(self):
        self.llm_obj = MagicMock()
        self.document = "test document" * 100
        self.llm_chain = LLMChain(self.document, self.llm_obj)

    def test_set_pages(self):
        with patch("src.llm_service.RecursiveCharacterTextSplitter") as mock_splitter:
            self.llm_chain.set_pages()
            mock_splitter.assert_called()

    def test_set_embedding(self):
        mock_embedding = MagicMock()
        self.llm_chain.set_embedding(mock_embedding)
        self.assertEqual(self.llm_chain.embedding, mock_embedding)


class TestGetLLMChainObj(unittest.TestCase):
    def test_get_llm_chain_obj(self):
        with patch("src.llm_service.LLMChain") as mock_llm_chain:
            get_llm_chain_obj("test document")
            mock_llm_chain.assert_called()
