import tkinter as tk
from tkinter import ttk
import math


class VisualizerCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Visualizer Calculator - By Hassnain Rana")
        self.root.geometry("850x580")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")  # Dark theme background

        # State Variables
        self.current_expression = ""
        self.history = []

        self._setup_ui()

    def _setup_ui(self):
        # Title Header
        header_frame = tk.Frame(self.root, bg="#0f172a")
        header_frame.pack(fill="x", padx=15, pady=10)

        title_label = tk.Label(
            header_frame,
            text="PYTHON CALCULATOR",
            font=("Helvetica", 18, "bold"),
            fg="#38bdf8",
            bg="#0f172a"
        )
        title_label.pack(side="left")

        # Author Branding
        author_label = tk.Label(
            header_frame,
            text="Created by Hassnain Rana",
            font=("Helvetica", 11, "italic", "bold"),
            fg="#f43f5e",
            bg="#0f172a"
        )
        author_label.pack(side="right", pady=5)

        # Main Layout Frame
        main_container = tk.Frame(self.root, bg="#0f172a")
        main_container.pack(fill="both", expand=True, padx=15, pady=5)

        # Left Panel: Calculator UI
        calc_frame = tk.Frame(main_container, bg="#1e293b", bd=2, relief="flat")
        calc_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Right Panel: Visualization & History Area
        viz_frame = tk.Frame(main_container, bg="#1e293b", bd=2, relief="flat", width=320)
        viz_frame.pack(side="right", fill="both", expand=False)
        viz_frame.pack_propagate(False)

        self._build_calculator(calc_frame)
        self._build_visualizer(viz_frame)

    def _build_calculator(self, parent):
        # Display Screen
        display_frame = tk.Frame(parent, bg="#0f172a", bd=1)
        display_frame.pack(fill="x", padx=15, pady=15)

        self.expression_label = tk.Label(
            display_frame,
            text="",
            font=("Helvetica", 12),
            fg="#94a3b8",
            bg="#0f172a",
            anchor="e"
        )
        self.expression_label.pack(fill="x", padx=10, pady=(5, 0))

        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Helvetica", 28, "bold"),
            fg="#f8fafc",
            bg="#0f172a",
            anchor="e"
        )
        self.display.pack(fill="x", padx=10, pady=(0, 10))

        # Button Layout Grid
        buttons = [
            ("C", 1, 0, "#ef4444"), ("(", 1, 1, "#475569"), (")", 1, 2, "#475569"), ("/", 1, 3, "#0ea5e9"),
            ("7", 2, 0, "#334155"), ("8", 2, 1, "#334155"), ("9", 2, 2, "#334155"), ("*", 2, 3, "#0ea5e9"),
            ("4", 3, 0, "#334155"), ("5", 3, 1, "#334155"), ("6", 3, 2, "#334155"), ("-", 3, 3, "#0ea5e9"),
            ("1", 4, 0, "#334155"), ("2", 4, 1, "#334155"), ("3", 4, 2, "#334155"), ("+", 4, 3, "#0ea5e9"),
            ("0", 5, 0, "#334155"), (".", 5, 1, "#334155"), ("√", 5, 2, "#475569"), ("=", 5, 3, "#22c55e")
        ]

        grid_frame = tk.Frame(parent, bg="#1e293b")
        grid_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        for i in range(6):
            grid_frame.rowconfigure(i, weight=1)
        for j in range(4):
            grid_frame.columnconfigure(j, weight=1)

        for text, row, col, color in buttons:
            btn = tk.Button(
                grid_frame,
                text=text,
                font=("Helvetica", 14, "bold"),
                fg="#ffffff",
                bg=color,
                activebackground="#64748b",
                activeforeground="#ffffff",
                bd=0,
                relief="flat",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    def _build_visualizer(self, parent):
        viz_title = tk.Label(
            parent,
            text="DATA VISUALIZER",
            font=("Helvetica", 13, "bold"),
            fg="#38bdf8",
            bg="#1e293b"
        )
        viz_title.pack(anchor="w", padx=15, pady=(15, 5))

        # Canvas for Graphical Visualization
        self.canvas = tk.Canvas(parent, bg="#0f172a", highlightthickness=0, height=180)
        self.canvas.pack(fill="x", padx=15, pady=10)
        self.draw_placeholder_visual()

        # Step Process Label
        self.step_label = tk.Label(
            parent,
            text="Status: Ready",
            font=("Helvetica", 10, "italic"),
            fg="#a855f7",
            bg="#1e293b"
        )
        self.step_label.pack(anchor="w", padx=15, pady=2)

        # Calculation History List
        history_title = tk.Label(
            parent,
            text="Recent History Log",
            font=("Helvetica", 11, "bold"),
            fg="#94a3b8",
            bg="#1e293b"
        )
        history_title.pack(anchor="w", padx=15, pady=(10, 5))

        self.history_box = tk.Listbox(
            parent,
            bg="#0f172a",
            fg="#f8fafc",
            selectbackground="#334155",
            bd=0,
            font=("Consolas", 10),
            highlightthickness=0
        )
        self.history_box.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    def draw_placeholder_visual(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            140, 90,
            text="Visual Graph Area\nPerform a calculation\nto visualize values.",
            fill="#64748b",
            font=("Helvetica", 10),
            justify="center"
        )

    def visualize_result(self, val1, op, val2, result):
        self.canvas.delete("all")
        try:
            v1 = abs(float(val1))
            v2 = abs(float(val2))
            res = abs(float(result))
            max_val = max(v1, v2, res, 1)

            # Bar height scaling
            h1 = (v1 / max_val) * 120
            h2 = (v2 / max_val) * 120
            h3 = (res / max_val) * 120

            # Draw Bar 1
            self.canvas.create_rectangle(30, 150 - h1, 70, 150, fill="#38bdf8", outline="")
            self.canvas.create_text(50, 162, text="A", fill="#94a3b8", font=("Helvetica", 9))

            # Draw Operator
            self.canvas.create_text(100, 110, text=op, fill="#a855f7", font=("Helvetica", 14, "bold"))

            # Draw Bar 2
            self.canvas.create_rectangle(130, 150 - h2, 170, 150, fill="#f43f5e", outline="")
            self.canvas.create_text(150, 162, text="B", fill="#94a3b8", font=("Helvetica", 9))

            # Draw Equal Sign
            self.canvas.create_text(200, 110, text="=", fill="#a855f7", font=("Helvetica", 14, "bold"))

            # Draw Result Bar
            self.canvas.create_rectangle(230, 150 - h3, 270, 150, fill="#22c55e", outline="")
            self.canvas.create_text(250, 162, text="Res", fill="#94a3b8", font=("Helvetica", 9))

        except Exception:
            self.draw_placeholder_visual()

    def on_button_click(self, char):
        if char == "C":
            self.current_expression = ""
            self.display.config(text="0")
            self.expression_label.config(text="")
            self.step_label.config(text="Status: Cleared")
            self.draw_placeholder_visual()

        elif char == "=":
            self.calculate_result()

        elif char == "√":
            try:
                val = float(self.display.cget("text"))
                res = math.sqrt(val)
                expr = f"√({val})"
                self.expression_label.config(text=expr)
                self.display.config(text=str(res))
                self.add_to_history(expr, str(res))
                self.step_label.config(text="Status: Square Root Executed")
                self.current_expression = str(res)
            except Exception:
                self.display.config(text="Error")

        else:
            if self.display.cget("text") == "0" and char not in "+-*/.":
                self.current_expression = char
            else:
                self.current_expression += str(char)

            self.display.config(text=self.current_expression)

    def calculate_result(self):
        try:
            expr = self.current_expression
            result = eval(expr)

            # Update Displays
            self.expression_label.config(text=expr)
            self.display.config(text=str(result))

            # Log to History
            self.add_to_history(expr, str(result))
            self.step_label.config(text="Status: Evaluation Complete")

            # Try parsing dynamic values for visual rendering
            for op in ["+", "-", "*", "/"]:
                if op in expr:
                    parts = expr.split(op)
                    if len(parts) == 2 and parts[0] and parts[1]:
                        self.visualize_result(parts[0], op, parts[1], result)
                        break

            self.current_expression = str(result)

        except Exception:
            self.display.config(text="Error")
            self.step_label.config(text="Status: Invalid Syntax")

    def add_to_history(self, expr, result):
        log_entry = f"{expr} = {result}"
        self.history.append(log_entry)
        self.history_box.insert(0, log_entry)


if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizerCalculator(root)
    root.mainloop()