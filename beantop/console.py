class Console:
    def __init__(self,  time,  char_reader,  screen_printer,  screen):
        self._time = time
        self._char_reader = char_reader
        self._screen_printer = screen_printer
        self._screen = screen
        self._finished = False

    def main_loop(self):
        try:
            self._char_reader.setup_terminal_for_char_read()
            while not self._finished:
                self._run_loop_once()
        finally:
            self._char_reader.reset_terminal_options()

    def _run_loop_once(self):
        time_limit = self._time.gmtime()+5
        scr = self._screen.render_screen()
        self._screen_printer.clear()
        time = self._time.get_printable_time()
        self._screen_printer.print_lines([time]+scr)
        self._loop_finished=False
        while self._time.gmtime()<time_limit and not self._loop_finished:
            self._process_char_queue()
            self._time.sleep(0.1)

    def _process_char(self):
        char_read = self._char_reader.get_char()
        if char_read is None:
            return False
        if char_read == 'q': 
            self._finished = True
            self._loop_finished=True
        if char_read == 'r': 
            self._loop_finished=True
        return True
       
    def _process_char_queue(self):
        found_char = self._process_char()
        while found_char and not self._finished:
            found_char = self._process_char()
