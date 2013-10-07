import csv, run_count_importer, count_import



def initialize_out_file():
	global output
	global outfile

	outfile = open('..\Outputs\count_output.csv','wb')
	output = csv.writer(outfile)

def reconstruct_inputs():
	output.writerow([''])
	output.writerow(['Start_Time'])


def reconstruct_intervals():
	pass


def reconstruct_data():
	pass


def create_summary():
	pass


#run_count_importer.run_importer()

count_import.initialize(run_count_importer.travel_modes)
count_import.import_intervals(run_count_importer.travel_modes)
count_import.import_mode_volume(run_count_importer.travel_modes,'All Vehicles')
count_import.import_legs(run_count_importer.Directory+run_count_importer.VEH_FILE,run_count_importer.VEH_TAB,run_count_importer.LEGS)
	
initialize_out_file()
reconstruct_inputs()

outfile.close()