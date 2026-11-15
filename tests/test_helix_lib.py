import pytest
import torch
from helix_lib import HELIXLib, create_helix_lib

class TestHELIXLib:
    def test_init(self):
        m = HELIXLib(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = HELIXLib(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_helix_lib()
        assert isinstance(m, HELIXLib)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
