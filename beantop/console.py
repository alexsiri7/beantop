class Console:
    def __init__(self,  time,  char_reader,  screen_printer,  screen):
        self.time = time
        self.char_reader = char_reader
        self.screen_printer = screen_printer
        self.screen = screen
        self.finished = False

    def main_loop(self):
        try:
            self.char_reader.setup_terminal_for_char_read()
            while not self.finished:
                self._run_loop_once()
        finally:
            self.char_reader.reset_terminal_options()


    def _run_loop_once(self):
        time_limit = self.time.gmtime()+5
        scr = self.screen.render_screen()
        self.screen_printer.clear()
        time = self.time.get_printable_time()
        self.screen_printer.print_lines([time]+scr)
        while self.time.gmtime()<time_limit and not self.finished:
            self._process_char_queue()
            self.time.sleep(0.1)
               

    def _process_char(self):
        char_read = self.char_reader.get_char()
        if char_read is None:
            return False
        if char_read == 'q': 
            self.finished = True
        return True
       
    def _process_char_queue(self):
        found_char = self._process_char()
        while found_char and not self.finished:
            found_char = self._process_char()
