import sys
try:
	import tkinter as tk
except:
	import Tkinter as tk
import datetime
from tkcalendar import DateEntry
	
class QA_CALCULATOR(tk.Tk):

	# size of the screen (width x height)
	init_window_size = '360x250'
	maximized_window = '600x250'

	def __init__(self):
		""" 
      		This app helps to QA_Rating's members to qualify leads
			giving the market median price, the difference between 
			the customer's price and the market price, also 
			helps to know the percentage of the amount 
		"""
			# Setting Window
		self.top = tk.Tk()
		self.top.title('QA CALCULATOR')
		self.top.configure(bd = 3)
		self.top.geometry(self.init_window_size)
		self.top.resizable(0,0)
			# setting menubar
		self.menubar = tk.Menu(self.top)
		self.top.config(menu=self.menubar)

		self.Set_Vars()

			#setting Frame
		self.calculate_frame = tk.Frame( self.top, bg=self.background_color)
		self.calculate_frame.grid(sticky='we')

		self.date_frame = tk.Frame(self.top, bg = self.background_color)

		

		self.Set_Gatgets()
			# setting key blinding
		self.top.bind('<Escape>', self.Reload)
		self.top.bind('<Return>', self.Submit)

		self.top.bind('<Control-d>', self.Set_Date)
		self.top.bind('<Control-c>', self.Set_Calculate)

		self.top.mainloop()

	def Set_Vars(self):
			#setting vaiables 
		self.asking_price = tk.DoubleVar()
		self.median_price = tk.DoubleVar()
		self.difference = tk.DoubleVar()
		self.percentage = tk.DoubleVar()
		self.show_percentage = tk.StringVar()
		self.show_difference = tk.StringVar()
		self.show_median_price = tk.StringVar()
		self.price = []
		self.count = 0.0
		self.cord_x = 360
		self.font2 = ('Time New Roman','12','italic','bold')
		self.background_color = 'light gray'#'dodger blue'
		self.entry_color = 'green'#'deep sky blue'
		self.top.configure(background = self.background_color)
		self.font = ('Comic Sans', '10')
			#setting date variables
		self.day = tk.StringVar() 

	def Set_Gatgets(self):
				# create a menu
		self.file_menu = tk.Menu(self.menubar)
		
		# add a menu item to the menu
		self.file_menu.add_command(label='Calculate', command=self.Set_Calculate)
		self.file_menu.add_command(label='Date', command=self.Set_Date)
		self.file_menu.add_separator()
		self.file_menu.add_command(label='Exit',command=self.top.destroy)
			# add the File menu to the menubar
		self.menubar.add_cascade(label="Options", menu=self.file_menu)
			
				#setting Label 
		self.l_price = tk.Label(self.calculate_frame, text = "Enter asking price", bg = self.background_color, font = self.font)
		self.l1 = tk.Label(self.calculate_frame, text = 'Enter Zillow price', bg = self.background_color, font = self.font)
		self.l2 = tk.Label(self.calculate_frame, text = 'Enter Redfin price', bg = self.background_color, font = self.font)
		self.l3 = tk.Label(self.calculate_frame, text = 'Enter Realtor price', bg = self.background_color, font = self.font)
		self.l4 = tk.Label(self.calculate_frame, text = 'Enter RealtyTrac price', bg = self.background_color, font = self.font)
		self.l5 = tk.Label(self.calculate_frame, text = 'Enter Movoto price', bg = self.background_color, font = self.font)

			# add label for Date section
		self.date = tk.Label(self.date_frame, text='Select a date', bg=self.background_color)
				
			# Labels for show when Submit button has been actived 
		self.l_percentage = tk.Label(self.calculate_frame, textvariable = self.show_percentage, bg = self.background_color, font = ('Time New Roman','16','italic','bold'))
		self.l_median_price = tk.Label(self.calculate_frame, textvariable = self.show_median_price, bg = self.background_color, font = self.font2)
		self.l_difference = tk.Label(self.calculate_frame, textvariable = self.show_difference, bg = self.background_color, font = self.font2)

			# Labels for show date
		self.l_day = tk.Label(self.date_frame, textvariable=self.day, bg=self.background_color, font=self.font2)
			#setting entry
		self.e_price = tk.Entry(self.calculate_frame, bg = self.entry_color, font = self.font, bd = 5)
			#self.e_price.insert(0,0.0)
		self.e1 = tk.Entry(self.calculate_frame, bg = self.entry_color, font = self.font, bd = 5)
		self.e1.insert(0, 0.0)
		self.e2 = tk.Entry(self.calculate_frame, bg = self.entry_color, font = self.font, bd = 5)
		self.e2.insert(0, 0.0)
		self.e3 = tk.Entry(self.calculate_frame, bg = self.entry_color, font = self.font, bd = 5)
		self.e3.insert(0, 0.0)
		self.e4 = tk.Entry(self.calculate_frame, bg = self.entry_color, font = self.font, bd = 5)
		self.e4.insert(0, 0.0)
		self.e5 = tk.Entry(self.calculate_frame, bg = self.entry_color, font = self.font, bd = 5)
		self.e5.insert(0, 0.0)

		# entry for date
		self.cal = DateEntry(self.date_frame, width=12, background='darkblue', foreground='white', borderwidth=2)

				# setting button
		self.submit = tk.Button(self.calculate_frame, text = 'Submit', font = self.font, command = self.Submit, bg = self.entry_color, bd = 2)
		self.reload = tk.Button(self.calculate_frame, text = 'Reload', font = self.font, command = self.Reload, bg = self.entry_color, bd = 2)		

			# Setting Gatget on the Screen
		self.l_price.grid(row = 0, column = 0)
		self.e_price.grid(row = 0, column = 1)
		self.l1.grid(row = 1, column = 0)
		self.e1.grid(row = 1, column = 1)
		self.l2.grid(row = 2, column = 0)
		self.e2.grid(row = 2, column = 1)
		self.l3.grid(row = 3, column = 0)
		self.e3.grid(row = 3, column = 1)
		self.l4.grid(row = 4, column = 0)
		self.e4.grid(row = 4, column = 1)
		self.l5.grid(row = 5, column = 0)
		self.e5.grid(row = 5, column = 1)
			# setting gatget Date
		self.date.grid(row=1, column=0)
		self.cal.grid(row=1, column=1)
		self.l_day.grid(row=3, column=2)
		tk.Button(self.date_frame, text='OK', command=self.Get_user_date).grid(row=3, column=0, columnspan=2)


		tk.Label(self.date_frame,text="",bg=self.background_color).grid(row=6,column=0)

		self.reload.grid(row = 9, column = 0)
		self.submit.grid(row = 9, column = 1)
				# FOCUS ON ENTRY ASKING PRICE
		self.e_price.focus()


# DEF MAIN FUNTIONS 
	def Submit(self,event=None):
		self.Set_Median_Price()
		self.Set_Persentage()
		self.Set_Difference()

		self.show_percentage.set('{}%'.format(self.percentage.get()))
		self.show_median_price.set('The median price: {}'.format(self.median_price.get()))
		self.show_difference.set('The difference: {}'.format(self.difference.get()))
		
		if (self.percentage.get() < 0.0):
			self.l_percentage.configure(fg='green')
			self.l_percentage.grid(row=1, column=3)

		else:
			self.l_percentage.configure(fg='red')
			self.l_percentage.grid(row=1, column=3)

		# self.l_median_price.place(x= self.cord_x, y = 70 )
		self.l_median_price.grid(row=2, column=3)
		# self.l_difference.place(x= self.cord_x, y = 140 )
		self.l_difference.grid(row=3, column=3)


		self.top.geometry(self.maximized_window)

	def Reload(self,event=None):

			# set labels to empty string
		self.show_percentage.set('')
		self.show_median_price.set('')
		self.show_difference.set('')


		self.top.geometry(self.init_window_size) # change the size of the main window

			# reset the main variables 
		self.percentage.set(0.0)
		self.median_price.set(0.0)
		self.difference.set(0.0)
		self.asking_price.set(0.0)
		self.count = 0.0

			# reset entries 
		self.e_price.delete(0,'end')
		self.e1.delete(0,'end')
		self.e1.insert(0,0.0)
		self.e2.delete(0,'end')
		self.e2.insert(0,0.0)
		self.e3.delete(0,'end')
		self.e3.insert(0,0.0)
		self.e4.delete(0,'end')
		self.e4.insert(0, 0.0)
		self.e5.delete(0,'end')
		self.e5.insert(0, 0.0)

		self.e_price.focus() #Focus on main entry

# DEF SECONDARY FUNTIONS 
	def Set_Median_Price(self): #works 
		
		#get all values of the entry and put them into the price array
		self.price.insert(0,float(self.e1.get()))
		self.price.insert(1,float(self.e2.get()))
		self.price.insert(2,float(self.e3.get()))
		self.price.insert(3,float(self.e4.get()))
		self.price.insert(4,float(self.e5.get()))
		self.price.insert(5,0.0)

		#check the values and + variables
		for i in range(0,6):
			if(i<5):
				self.price[5] += self.price[i]
				 
			if (self.price[i] != 0 and i<5):
				self.count += 1
		try:
			self.median_price.set(round(self.price[5] / self.count, 2))
		except ZeroDivisionError:
			self.median_price.set(0.0)		
		self.count= 0.0
	
	def Set_Persentage(self): #works
		self.asking_price.set(self.e_price.get())
		try:
			self.percentage.set(round((((self.asking_price.get()/self.median_price.get())-1)*100),2))
		except ZeroDivisionError:
			self.percentage.set(0.0)
	
	def Set_Difference(self): #works
		self.difference.set(round(self.asking_price.get() - self.median_price.get(),2))

	# handling menu options 
	def Set_Calculate(self, event=None):
		self.date_frame.grid_forget()
		self.calculate_frame.grid(sticky='ew')

	def Set_Date(self, event=None):
		self.calculate_frame.grid_forget()
		self.date_frame.grid(sticky='ew')

	def Get_user_date(self):
		now = datetime.date.today()
		date = self.cal.get_date()
		days = now - date
		result = self.get_days(date, now)
		self.day.set('{} years, {} months'.format(result['year'], result['month']))

	def get_days(self,fecha1, fecha2):
		""" Convert days in it's representation in years and months"""
		formato = "%d-%m-%Y"  
		fecha_objeto1 = fecha1 #.strptime(fecha1, formato)
		fecha_objeto2 = fecha2 # datetime.strptime(fecha2, formato)

		diferencia = fecha_objeto2 - fecha_objeto1
		dias = diferencia.days

		annos_completos = dias // 365
		residuo_annos = dias % 365

		meses_completos = residuo_annos // 30
		residuo_meses = residuo_annos % 30

		return {'year':annos_completos, 'month':meses_completos, 'days':residuo_meses}