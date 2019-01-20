import tkinter as tk
from tkinter import font  as tkfont
import person_group


class SampleApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (StartPage,):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("StartPage")

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


class StartPage(tk.Frame):  # url input

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Enter the URL of the query image", font=controller.title_font)
		label.pack()

		e = tk.Entry(self)
		e.pack()

		labelText2 = tk.StringVar()
		labelText3 = tk.StringVar()

		def button_func(e_):
			image_url = e_.get()
			test_results = person_group.test_person(image_url, 0.4)
			if test_results[0]:
				labelText2.set("Wanted person alert!!!")
				labelText3.set("Confidence: {}".format(test_results[1]))
			else:
				labelText2.set('This person is probably not wanted')
				labelText3.set('')

		button1 = tk.Button(self, text="Query image",
							command=lambda: button_func(e))
		button1.pack()

		label2 = tk.Label(self, textvariable=labelText2)
		label3 = tk.Label(self, textvariable=labelText3)

		label2.pack()
		label3.pack()


if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()


