import sys
import GDocs
import Configuration
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)


class GUIManager():
	"""Provides an interface to access the GUI functionality
	"""
	
	def __init__(self):
		"""
		"""
		#TODO: Find an elegant way to do this.
		self._confMan=Configuration.ConfigurationManager()
		account=self._confMan.get_account()
		self._gdcm=GDocs.GDClientManager()
		self._gdam=GDocs.GDActionsManager(self._gdcm)
		self._gdcm.authenticate_client(account)


	def show_import_window(self):
		"""Shows the import Google Documents window"""

                window=ImportGDocsWindow(self._gdam)
		#window=MainWindow()
		

	


class ImportGDocsWindow():
	"""Shows the import Google Docs windows
	"""
	
	def __init__(self, gdam):
		"""
		
                Arguments:
                - `gdam`:GDocs.GDActionsManager
                """
		self._gdam = gdam

                #load and setup the GUI components

                #TODO: Create a good way to get the file locations.From the
		#ConfigurationManager may be?
		filename = "/home/ishan/4sep/1.glade"
		builder = gtk.Builder()
		builder.add_from_file(filename)
		builder.connect_signals(self)
		
		DocTreeView=builder.get_object('DocTreeView')
		

                
		col_type=gtk.TreeViewColumn('Type')
		col_type.set_resizable(True)
		DocTreeView.append_column(col_type)

                col_name=gtk.TreeViewColumn('Name',gtk.CellRendererText(),text=1)
		col_name.set_resizable(True)
		DocTreeView.append_column(col_name)

                col_folders=gtk.TreeViewColumn('In Folders',gtk.CellRendererText(),text=2)
		col_folders.set_resizable(True)
		DocTreeView.append_column(col_folders)

                DocList=gtk.ListStore(str,str,str)
		DocTreeView.set_model(DocList)
		
		for doc in self._gdam.get_all_documents().entry:
			data= self._gdam.get_doc_data(doc)
			#print dir(data)
			
			DocList.append([data[0],data[1],"Folder"])

			#itr=DocList.append([1,'2','3'])
		#DocList.insert_after(itr,[2,"2",'2'])
		#DocList.append([2,"ssssss2"])
		

                cell = gtk.CellRendererText()
		col_type.pack_start(cell,False)
		col_type.add_attribute(cell,"text",0)

	def destroy_all(self,arg):
		"""Destroy everything
		"""
		gtk.main_quit()

	def on_row_activated(self, treeview,path,column):
		"""
		
                Arguments:
                - `treeview`:
                - `path`:
                - `column`:
                """
		print "O.o"




class MainWindow:
        """This is an Hello World GTK application"""

        def __init__(self):
		
                # #Set the Glade file
                # self.gladefile = "hello.glade"  
	        # self.wTree = gtk.glade.XML("1.glade") 
		
		# #Get the Main Window, and connect the "destroy" event
		# self.window = self.wTree.get_widget("MainWindow")
		# if (self.window):
		# 	self.window.connect("destroy", gtk.main_quit)
                #text.insertString( cursor, "in class\n", 0 )
                #load the 1.glade
                filename = "/home/ishan/4sep/1.glade"
		builder = gtk.Builder()
		builder.add_from_file(filename)
		builder.connect_signals(self)
		#DocList=builder.get_object('DocList')
		DocList=gtk.ListStore(str)
		DocTreeView=builder.get_object('DocTreeView')
		DocTreeView.set_model(DocList)
		#DocTreeView=gtk.ListStore(str)
                DocList.append(["TypeHi"])
		col_type=gtk.TreeViewColumn('Type')
		col_type.set_resizable(True)
		DocTreeView.append_column(col_type)

                col_name=gtk.TreeViewColumn('Name')
		col_name.set_resizable(False)
		DocTreeView.append_column(col_name)

                cell = gtk.CellRendererText()
		col_type.pack_start(cell,False)
		col_type.add_attribute(cell,"text",0)
		
		#comment the following lines
		#window=builder.get_object('window')
		#window.show_all()

	def on_buttonGenerate_clicked(self, widget):
		print "You clicked the button"

	def destroy_all(self,arg):
		"""Destroy everything
		"""
		gtk.main_quit()

	def on_row_activated(self, treeview,path,column):
		"""
		
                Arguments:
                - `treeview`:
                - `path`:
                - `column`:
                """
		print "O.o"



if __name__ == "__main__":
	#hwg = MainWindow()
	guiM=GUIMaanger()
	guiM.show_import_window()
	gtk.main()
