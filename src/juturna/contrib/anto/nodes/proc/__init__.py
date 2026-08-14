from juturna.components._node_builder._utils import _lazy_node_loaders


_AVAILABLE_PLUGINS = {
    'PassthroughIdentity': '._passthrough_identity.passthrough_identity',
}


__getattr__, __dir__ = _lazy_node_loaders(__name__, _AVAILABLE_PLUGINS)
__all__ = list(_AVAILABLE_PLUGINS.keys())
