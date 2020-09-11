from src.utilities import text_logger, constants
from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

logger = text_logger.get_logger("Singleton")


class Singletons:
    __instance = None
    model = None
    tokenizer = None
    device = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Singletons.__instance is None:
            logger.info("Calling Singletone private constructor")
            Singletons()
        return Singletons.__instance

    def __init__(self):
        if Singletons.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            logger.info(" Loading Summarization model")
            self.model = AutoModelWithLMHead.from_pretrained(constants.fetch_constant("model_path"))
            logger.info(" Loading Tokenizer for the model")
            self.tokenizer = AutoTokenizer.from_pretrained(constants.fetch_constant("model_path"))
            logger.info("Checking CUDA availability")
            if torch.cuda.is_available():
                logger.info("Transferring model to gpu")
                self.device = "cuda"
                self.model.to(self.device)
            else:
                logger.info("CUDA not found using CPU")
                self.device = "cpu"

        Singletons.__instance = self

    def get_model(self):
        return self.model

    def get_tokenizer(self):
        return self.tokenizer, self.device
