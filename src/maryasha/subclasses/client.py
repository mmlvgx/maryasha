# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2023 mmlvgx
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from traceback import print_exception
from ..constants import EMBED_ERR_COLOR, EMBED_ERR_TITLE

from crescent import Client, Context, GatewayTraits
from hikari import Embed


class SubClient(Client):
    def __init__(self, app: GatewayTraits) -> None:
        super().__init__(app)

    async def on_crescent_command_error(
        self, exc: Exception, ctx: Context, was_handled: bool
    ) -> None:
        if not was_handled:
            embed = Embed(
                title=EMBED_ERR_TITLE,
                description=f"`{exc.__class__.__name__}: {exc}`",
                color=EMBED_ERR_COLOR,
            )

            await ctx.respond(embed=embed)
            print_exception(exc.__class__, exc, exc.__traceback__)
