import sys
from typing import Any
from mlx import Mlx

#amount of pixels x cell
CELL = 30

COLOR_WALL = 0xFFFFFF   #white
COLOR_ENTRY = 0x00FF00  #green
COLOR_EXIT = 0xFF0000   #red


class MazeVisualizer:

    def __init__(self, maze: list, config: Any, solution: set) -> None:
        self.maze = maze
        self.config = config
        self.solution = solution

        # create and init object
        self.m = Mlx()
        self.ptr = self.m.mlx_init()

        # create window
        self.win = self.m.mlx_new_window(
            self.ptr,
            config.width * CELL,
            config.height * CELL,
            "A-Maze-ing"
        )

        # create image dimensions
        self.img = self.m.mlx_new_image(
            self.ptr,
            config.width * CELL,
            config.height * CELL
        )

        # access image data (memory, bits x pixel, bytes x line, color format)
        (
            self.data,
            self.bpp,
            self.size_line,
            self.fmt
        ) = self.m.mlx_get_data_addr(self.img)

        # monitoring events
        self.m.mlx_key_hook(
            self.win,
            self.on_key,
            None
        )

        # call close method on presing ESC
        self.m.mlx_hook(
            self.win,
            17,
            0,
            self.close,
            None
        )

    # creates the pixels in the coordinates
    def put_pixel(self, x: int, y: int, color: int) -> None:

        # Avoids getting out of limits
        if x < 0 or x >= self.config.width * CELL:
            return

        if y < 0 or y >= self.config.height * CELL:
            return

        # coordinates * amount of bytes * bits per pixel(4)
        offset = y * self.size_line + x * 4

        # 3 bytes for RGB and 1 byte for alpha channel(opacity)
        self.data[offset:offset + 4] = bytes([
            color & 0xFF,
            (color >> 8) & 0xFF,
            (color >> 16) & 0xFF,
            255
        ])

    #draws vertical and horizontal lines on call
    def draw_horizontal(
        self,
        x: int,
        y: int,
        color: int
    ) -> None:

        for i in range(CELL):
            self.put_pixel(x + i, y, color)

    def draw_vertical(
        self,
        x: int,
        y: int,
        color: int
    ) -> None:

        for i in range(CELL):
            self.put_pixel(x, y + i, color)

    # renders the maze walls in the window
    def render_maze(self, *args: Any) -> int:
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):

                px = x * CELL
                py = y * CELL

                if cell.north:
                    self.draw_horizontal(
                        px,
                        py,
                        COLOR_WALL
                    )

                if cell.west:
                    self.draw_vertical(
                        px,
                        py,
                        COLOR_WALL
                    )

                if cell.south:
                    self.draw_horizontal(
                        px,
                        py + CELL - 1,
                        COLOR_WALL
                    )

                if cell.east:
                    self.draw_vertical(
                        px + CELL - 1,
                        py,
                        COLOR_WALL
                    )

                # entry point
                if (x, y) == self.config.entry:
                    for i in range(8):
                        for j in range(8):
                            self.put_pixel(
                                px + CELL // 2 - 4 + i,
                                py + CELL // 2 - 4 + j,
                                COLOR_ENTRY
                            )

                # exit point
                if (x, y) == self.config.exit:
                    for i in range(8):
                        for j in range(8):
                            self.put_pixel(
                                px + CELL // 2 - 4 + i,
                                py + CELL // 2 - 4 + j,
                                COLOR_EXIT
                            )

        # show image in window
        self.m.mlx_put_image_to_window(
            self.ptr,
            self.win,
            self.img,
            0,
            0
        )

        return 0

    def on_key(self, keycode: int, *args: Any) -> int:
        """detects ESC or Q keys"""

        if keycode in (53, 65307, 113, 81):
            self.close()

        return 0

    def close(self, *args: Any) -> int:
        """close processess in MLX."""

        try:
            if self.img:
                self.m.mlx_destroy_image(
                    self.ptr,
                    self.img
                )

            if self.win:
                self.m.mlx_destroy_window(
                    self.ptr,
                    self.win
                )

            if hasattr(self.m, "mlx_loop_exit"):
                self.m.mlx_loop_exit(self.ptr)

        except Exception:
            pass

        return 0

    def start(self) -> None:
        # renders the maze
        self.render_maze()
        # keeps it running until closed
        self.m.mlx_loop(self.ptr)