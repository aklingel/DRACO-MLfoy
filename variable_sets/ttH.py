variables = {}
variables["ge4j_ge3t"] = [
	"Jet_Pt[0]",
	"Jet_Pt[1]",
	"Jet_Pt[2]",
	"Jet_Pt[3]",
	"Jet_Pt[4]",
	"Jet_Pt[5]",
	"Jet_Pt[6]",
	"Jet_Pt[7]",
	"Jet_Pt[8]",
	"Jet_Pt[9]",
	"Jet_Pt[10]",
	"Jet_Pt[11]",
	"Jet_Pt[12]",
	"Jet_Eta[0]",
	"Jet_Eta[1]",
	"Jet_Eta[2]",
	"Jet_Eta[3]",
	"Jet_Eta[4]",
	"Jet_Eta[5]",
	"Jet_Eta[6]",
	"Jet_Eta[7]",
	"Jet_Eta[8]",
	"Jet_Eta[9]",
	"Jet_Eta[10]",
	"Jet_Eta[11]",
	"Jet_Eta[12]",
	"Jet_Phi[0]",
	"Jet_Phi[1]",
	"Jet_Phi[2]",
	"Jet_Phi[3]",
	"Jet_Phi[4]",
	"Jet_Phi[5]",
	"Jet_Phi[6]",
	"Jet_Phi[7]",
	"Jet_Phi[8]",
	"Jet_Phi[9]",
	"Jet_Phi[10]",
	"Jet_Phi[11]",
	"Jet_Phi[12]",
	"Jet_M[0]",
	"Jet_M[1]",
	"Jet_M[2]",
	"Jet_M[3]",
	"Jet_M[4]",
	"Jet_M[5]",
	"Jet_M[6]",
	"Jet_M[7]",
	"Jet_M[8]",
	"Jet_M[9]",
	"Jet_M[10]",
	"Jet_M[11]",
	"Jet_M[12]",
	"Jet_E[0]",
	"Jet_E[1]",
	"Jet_E[2]",
	"Jet_E[3]",
	"Jet_E[4]",
	"Jet_E[5]",
	"Jet_E[6]",
	"Jet_E[7]",
	"Jet_E[8]",
	"Jet_E[9]",
	"Jet_E[10]",
	"Jet_E[11]",
	"Jet_E[12]",
	"Jet_CSV[0]",
	"Jet_CSV[1]",
	"Jet_CSV[2]",
	"Jet_CSV[3]",
	"Jet_CSV[4]",
	"Jet_CSV[5]",
	"Jet_CSV[6]",
	"Jet_CSV[7]",
	"Jet_CSV[8]",
	"Jet_CSV[9]",
	"Jet_CSV[10]",
	"Jet_CSV[11]",
	"Jet_CSV[12]",
	"N_TightMuons",
	"N_TightElectrons",
#	"Muon_Pt[0]",	
#	"Muon_Eta[0]",
#	"Muon_Phi[0]",
#	"Muon_E[0]",
#	"Electron_Pt[0]",
#	"Electron_Eta[0]",
#	"Electron_Phi[0]",
#	"Electron_E[0]",
#	"LooseLepton_Pt[0]",
#	"LooseLepton_Eta[0]",
#	"LooseLepton_Phi[0]",
#	"LooseLepton_E[0]",
#	"Evt_MET_Pt",
#	"Evt_MET_Phi",
#	"GenTopLep_Eta",
#	"GenTopLep_Phi",
#	"GenTopHad_Eta",
#	"GenTopHad_Phi",
#	"GenTopHad_B_Eta",
#	"GenTopHad_B_Phi",
#	"GenTopLep_B_Eta",
#	"GenTopLep_B_Phi",
#	"GenTopHad_Q1_Eta",
#	"GenTopHad_Q1_Phi",
#	"GenTopHad_Q2_Eta",
#	"GenTopHad_Q2_Phi",
	"Evt_Odd",
	"Evt_HT",

	"GenHiggs_B1_Phi",
	"GenHiggs_B2_Phi",
	"GenHiggs_B1_Eta",
	"GenHiggs_B2_Eta",

	"GenHiggs_B1_Pt",
	"GenHiggs_B1_E",
	"GenHiggs_B2_Pt",
	"GenHiggs_B2_E",
	"GenHiggs_Pt",
	"GenHiggs_Eta",
	"GenHiggs_Phi",
	"GenHiggs_E",
	#"GenHiggs_logM"
	]


all_variables = list(set( [v for key in variables for v in variables[key] ] ))
