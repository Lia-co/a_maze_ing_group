#!/usr/bin/env python3

import sys
#???what is Any?
from typing import Any
#???why mlx is not resolved?
from mlx import Mlx
#from mazegen.prim import grid

CELL = 30
COLOR_WALL = 0xFFFFFF   # White
COLOR_ENTRY = 0x00FF00  # Green
COLOR_EXIT = 0xFF0000   # Red


class MazeVisualizer:
    def __init__(self, maze: list, config: Any, solution: set) -> None:
        self.maze = maze
        self.config = config
        self.solution = solution

        # 1. Instancia de MLX
        self.m = Mlx()

        # 2. Aliases 
        self.ptr = self.m.mlx_init()
        self.win = self.m.mlx_new_window(
            self.ptr,
            config.width * CELL,
            config.height * CELL,
            "A-Maze-ing"
        )

        # 3. Loop de renderizado
        self.m.mlx_loop_hook(self.ptr, self.draw_once, None)
    
        # 4. Manejo de eventos
        self.m.mlx_hook(self.win, 2, 1, self.on_key, None)
        self.m.mlx_hook(self.win, 17, 0, self.close, None)

    def on_key(self, keycode: int, *args: Any) -> int:
        """Captura las teclas presionadas (ESC, 'q', 'Q') para salir."""
        # ESC (53 en Mac / 65307 en Linux), 'q' (113), 'Q' (81)
        if keycode in (53, 65307, 113, 81):
            self.close()
        return 0

    def close(self, *args: Any) -> int:
        """Destruye la ventana en el servidor X11 y finaliza el proceso."""
        try:
            # Destruir la ventana de MiniLibX explícitamente
            if hasattr(self.m, "mlx_destroy_window") and self.ptr and self.win:
                self.m.mlx_destroy_window(self.ptr, self.win)

            # Detener el loop si la librería implementa mlx_loop_end
            if hasattr(self.m, "mlx_loop_end") and self.ptr:
                self.m.mlx_loop_end(self.ptr)
        except Exception:
            pass

        # Salir del programa
        sys.exit(0)

    def draw_once(self, *args: Any) -> int:
        """Dibuja el laberinto una sola vez en el primer frame disponible."""
        if not self.is_drawn:
            self.render_maze()
            self.is_drawn = True
        return 0

    def put_pixel(self, data, x, y, color):
        offset = y * self.size_line + x * 4
        data[offset:offset + 4] = bytes([
            color & 0xFF,
            (color >> 8) & 0xFF,
            (color >> 16) & 0xFF,
            0
        ])

    def render_maze(self) -> None:
        """Dibuja el laberinto una sola vez en la ventana."""
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                px, py = x * CELL, y * CELL

                # Dibujar entrada y salida
                if (x, y) == self.config.entry:
                    self.m.mlx_pixel_put(
                        self.ptr, self.win, px + 5, py + 5, COLOR_ENTRY
                    )
                elif (x, y) == self.config.exit:
                    self.m.mlx_pixel_put(
                        self.ptr, self.win, px + 5, py + 5, COLOR_EXIT
                    )

                # Dibujar paredes
                if getattr(cell, 'north', True):
                    for i in range(CELL):
                        self.m.mlx_pixel_put(
                            self.ptr, self.win, px + i, py, COLOR_WALL
                        )
                if getattr(cell, 'west', True):
                    for i in range(CELL):
                        self.m.mlx_pixel_put(
                            self.ptr, self.win, px, py + i, COLOR_WALL
                        )

    def start(self) -> None:
        self.m.mlx_loop(self.ptr)

                    
    def start(self) -> None:
        self.render_maze()
        self.m.mlx_loop(self.ptr)
    
    def start(self) -> None:
        img = self.m.mlx_new_image(self.ptr, 500, 500)

        data, bpp, size_line, fmt = self.m.mlx_get_data_addr(img)

        print("bpp:", bpp)
        print("size_line:", size_line)
        print("format:", fmt)

        # Pintar TODO rojo
        for y in range(100):
            for x in range(100):
                offset = y * size_line + x * 4
                data[offset:offset + 4] = bytes([255, 255, 255, 255])

        self.m.mlx_put_image_to_window(
            self.ptr,
            self.win,
            img,
            0,
            0
        )

        self.m.mlx_loop(self.ptr)

