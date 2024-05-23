import dataclasses
from enum import Enum
from typing import Any, Dict, List, Optional, Union, cast

from flet_core.alignment import Alignment
from flet_core.constrained_control import ConstrainedControl
from flet_core.control import OptionalNumber
from flet_core.ref import Ref
from flet_core.text_style import TextStyle
from flet_core.types import (
    AnimationValue,
    ImageFit,
    OffsetValue,
    PaddingValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
    TextAlign,
)
from flet_core.utils import deprecated


class Placeholder(ConstrainedControl):
    """
    A control that displays a video from a playlist.

    -----

    Online docs: https://flet.dev/docs/controls/placeholder
    """

    def __init__(
        self,
        on_loaded=None,
        on_enter_fullscreen=None,
        on_exit_fullscreen=None,
        on_error=None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        aspect_ratio: OptionalNumber = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.on_enter_fullscreen = on_enter_fullscreen
        self.on_exit_fullscreen = on_exit_fullscreen
        self.on_loaded = on_loaded
        self.on_error = on_error

    def _get_control_name(self):
        return "placeholder"

    def before_update(self):
        super().before_update()

    def change_color(self, color: int):
        self.invoke_method("change_color", {"color": int(color)})

    @deprecated(
        reason = "Use change_color instead",
        version = "0.21.0",
        delete_version = "1.0"
    )
    async def change_color_async(self, color: int):
        self.change_color(color)

    # on_error
    @property
    def on_error(self):
        return self._get_event_handler("error")

    @on_error.setter
    def on_error(self, handler):
        self._set_attr("onError", True if handler is not None else None)
        self._add_event_handler("error", handler)
