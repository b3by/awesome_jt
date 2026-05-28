"""
MatrixGenerator

@author: Antonio Bevilacqua
@email: b3by.in.th3.sky@gmail.com
@created_at: 2026-05-28 17:12:27

This node generates noise matrixes of a given shape, at a given rate.
"""
import typing

import numpy as np

from juturna.components import Node
from juturna.components import Message

from juturna.payloads import ImagePayload


class MatrixGenerator(Node[ImagePayload, ImagePayload]):
    """Node implementation class"""

    def __init__(
            self,
            interval_ms: int,
            width: int,
            height: int,
            **kwargs):
        """
        Parameters
        ----------
        interval_ms : int
            Interval between data points, in milliseconds.
        width : int
            Width of the generated matrix.
        height : int
            Height of the generated matrix.
        kwargs : dict
            Supernode arguments.

        """
        super().__init__(**kwargs)

        self._interval_ms = interval_ms
        self._width = width
        self._height = height

        self.set_source(
            self._gen_data,
            mode='pre',
            by=self._interval_ms / 1000
        )

    def configure(self):
        """Configure the node"""
        ...

    def warmup(self):
        """Warmup the node"""
        ...

    def set_on_config(self, prop: str, value: typing.Any):
        """Hot-swap node properties"""
        ...

    def start(self):
        """Start the node"""
        # after custom start code, invoke base node start
        super().start()

    def stop(self):
        """Stop the node"""
        # after custom stop code, invoke base node stop
        super().stop()

    def destroy(self):
        """Destroy the node"""
        ...

    def update(self, message: Message[ImagePayload]):
        """Receive data from upstream, transmit data downstream"""
        self.transmit(message)

    def _gen_data(self):
        message = Message[ImagePayload](
            creator=self.name,
            payload=ImagePayload(
                image=np.random.rand(self._width, self._height),
                width=self._width,
                height=self._height
            )
        )

        message.version = message.id

        return message

