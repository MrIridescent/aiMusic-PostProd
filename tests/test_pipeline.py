import unittest
import torch
import numpy as np
from src.pipeline.restoration import AudioRestorer, VocalNaturalizer
from src.pipeline.mixing import MixingEngine

class TestRestoration(unittest.TestCase):
    def setUp(self):
        self.restorer = AudioRestorer(device="cpu")
        self.naturalizer = VocalNaturalizer()
        self.sr = 44100
        self.dummy_audio = torch.randn(1, self.sr * 2) # 2 seconds of noise

    def test_vocal_masking(self):
        audio_np = self.dummy_audio.numpy()[0]
        masked = self.naturalizer.mask_quantization(audio_np, self.sr)
        self.assertEqual(masked.shape, audio_np.shape)
        self.assertFalse(np.array_equal(masked, audio_np))

    def test_prepare_audiosr(self):
        filtered = self.restorer.prepare_for_audiosr(self.dummy_audio[0], self.sr)
        self.assertEqual(filtered.shape, self.dummy_audio[0].shape)

class TestMixing(unittest.TestCase):
    def setUp(self):
        self.engine = MixingEngine(samplerate=44100)
        self.sr = 44100
        self.dummy_stems = {
            "drums": np.random.randn(self.sr * 1),
            "vocals": np.random.randn(self.sr * 1)
        }

    def test_mix_stems(self):
        mix = self.engine.mix_stems(self.dummy_stems)
        self.assertIsInstance(mix, np.ndarray)
        self.assertEqual(len(mix), self.sr * 1)

if __name__ == "__main__":
    unittest.main()
