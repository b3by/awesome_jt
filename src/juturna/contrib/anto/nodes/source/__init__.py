from juturna.components._node_builder._utils import _lazy_node_loaders


_AVAILABLE_PLUGINS = {
    'MatrixGenerator': '._matrix_generator.matrix_generator',
}


__getattr__, __dir__ = _lazy_node_loaders(__name__, _AVAILABLE_PLUGINS)
__all__ = list(_AVAILABLE_PLUGINS.keys())
