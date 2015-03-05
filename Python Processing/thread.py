from interface import Interface
import wx

class CustomThread(Thread):
	"""Worker Thread Class."""
    def __init__(self, notify_window, interface):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.interface = interface
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()

    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread. Simulation of
        # a long process (well, 10s here) as a simple loop - you will
        # need to structure your processing so that you periodically
        # peek at the abort variable
        for i in range(10):
            time.sleep(1)
            if self._want_abort:
                # Use a result of None to acknowledge the abort (of
                # course you can use whatever you'd like or even
                # a separate event type)
                wx.PostEvent(self._notify_window, ResultEvent(None))
                return
        # Here's where the result would be returned (this is an
        # example fixed result of the number 10, but it could be
        # any Python object)
        wx.PostEvent(self._notify_window, ResultEvent(10))

    def abort(self):
        """abort worker thread."""
        # Method for use by main thread to signal an abort
        self._want_abort = 1

if __name__ == "__main__":
#inizialitzem interface
# inicilitzem classe radar
# preguntem dades
# fem un show de la interface
# loop mostrant dades

	
	app = wx.App(False)
	i = Interface(None)

	t = CustomThread()

	i.Show(True)
	app.MainLoop()


	speed = 1.0
	while True:
		time.sleep(1)
		speed += 1
		i.update_speed(speed)
		print speed
