import ast
import re

data = """105,Panic disorder,[{"symptoms":"Anxiety and nervousness"},{"symptoms":"88"},{"symptoms":"Depression"},{"symptoms":"55"},{"symptoms":"Shortness of breath"},{"symptoms":"40"},{"symptoms":"Depressive or psychotic symptoms"},{"symptoms":"33"},{"symptoms":"Sharp chest pain"},{"symptoms":"33"},{"symptoms":"Dizziness"},{"symptoms":"24"},{"symptoms":"Insomnia"},{"symptoms":"18"},{"symptoms":"Abnormal involuntary movements"},{"symptoms":"16"},{"symptoms":"Chest tightness"},{"symptoms":"14"},{"symptoms":"Palpitations"},{"symptoms":"13"},{"symptoms":"Irregular heartbeat"},{"symptoms":"11"},{"symptoms":"Breathing fast"},{"symptoms":"10"}],Panic disorder 	 		 	Panic disorder is an anxiety disorder characterized by recurring severe panic attacks. It may also include significant behavioral changes lasting at least a month and of ongoing worry about the implications or concern about having other attacks. The latter are called anticipatory attacks (DSM-IVR). Panic disorder is not the same as agoraphobia (fear of public places), although many afflicted with panic disorder also suffer from agoraphobia. Panic attacks cannot be predicted, therefore an individual may become stressed, anxious or worried wondering when the next panic attack will occur. Panic disorder may be differentiated as a medical condition, or chemical imbalance. The DSM-IV-TR describes panic disorder and anxiety differently. Whereas anxiety is preceded by chronic stressors which build to reactions of moderate intensity that can last for days, weeks or months, panic attacks are acute events triggered by a sudden, out-of-the-blue cause: duration is short and symptoms are more intense. Panic attacks can occur in children, as well as adults. Panic in young people may be particularly distressing because children tend to have less insight about what is happening, and parents are also likely to experience distress when attacks occur. 		 Source: Wikipedia,Patients with panic disorder often receive 			 			 psychotherapy, 			 						 			 mental health counseling, 			 						 			 electrocardiogram, 			 						 			 depression screen, 			 						 			 toxicology screen, 			 						 			 psychological and psychiatric evaluation and therapy and 			 						 			 occupational therapy assessment 			 			.,[{"commonTestsAndProcedures":"Psychotherapy"},{"commonTestsAndProcedures":"Mental health counseling"},{"commonTestsAndProcedures":"Electrocardiogram"},{"commonTestsAndProcedures":"Depression screen (Depression screening)"},{"commonTestsAndProcedures":"Toxicology screen"},{"commonTestsAndProcedures":"Psychological and psychiatric evaluation and therapy"},{"commonTestsAndProcedures":"Occupational therapy assessment (Speech therapy)"}],The most commonly prescribed drugs for patients with panic disorder include 		 		 lorazepam, 		 		 		 alprazolam (xanax), 		 		 		 clonazepam, 		 		 		 paroxetine (paxil), 		 		 		 venlafaxine (effexor), 		 		 		 mirtazapine, 		 		 		 buspirone (buspar), 		 		 		 fluvoxamine (luvox), 		 		 		 imipramine, 		 		 		 desvenlafaxine (pristiq), 		 		 		 clomipramine, 		 		 		 acamprosate (campral) and 		 		 		 disulfiram (antabuse) 		 	.,[{"commonMedications":"Lorazepam"},{"commonMedications":"Alprazolam (Xanax)"},{"commonMedications":"Clonazepam"},{"commonMedications":"Paroxetine (Paxil)"},{"commonMedications":"Venlafaxine (Effexor)"},{"commonMedications":"Mirtazapine"},{"commonMedications":"Buspirone (Buspar)"},{"commonMedications":"Fluvoxamine (Luvox)"},{"commonMedications":"Imipramine"},{"commonMedications":"Desvenlafaxine (Pristiq)"},{"commonMedications":"Clomipramine"},{"commonMedications":"Acamprosate (Campral)"},{"commonMedications":"Disulfiram (Antabuse)"}],Groups of people at highest risk for panic disorder include 		 	age 30-44 years. 		On the other hand, age 1-4 years and age < 1 years almost never get panic disorder.,Within all the people who go to their doctor with panic disorder, 88% report having anxiety and nervousness, 55% report having depression, and 40% report having shortness of breath. 		The symptoms that are highly suggestive of panic disorder are anxiety and nervousness and breathing fast, although you may still have panic disorder without those symptoms.
106,Vocal cord polyp,[{"symptoms":"Hoarse voice"},{"symptoms":"91"},{"symptoms":"Sore throat"},{"symptoms":"47"},{"symptoms":"Difficulty speaking"},{"symptoms":"27"},{"symptoms":"Cough"},{"symptoms":"27"},{"symptoms":"Nasal congestion"},{"symptoms":"27"},{"symptoms":"Throat swelling"},{"symptoms":"19"},{"symptoms":"Diminished hearing"},{"symptoms":"19"},{"symptoms":"Lump in throat"},{"symptoms":"19"},{"symptoms":"Throat feels tight"},{"symptoms":"11"},{"symptoms":"Difficulty in swallowing"},{"symptoms":"11"},{"symptoms":"Skin swelling"},{"symptoms":"11"},{"symptoms":"Retention of urine"},{"symptoms":"11"}],Vocal cord polyp 	 	 		Vocal cord polyp is encountered rarely on Symcat. We will add more content to this page if enough people like you show interest.,Patients with vocal cord polyp often receive 			 			 tracheoscopy and laryngoscopy with biopsy, 			 						 			 occupational therapy assessment, 			 						 			 other diagnostic procedures (interview; evaluation; consultation), 			 						 			 physical therapy exercises, 			 						 			 diagnostic procedures on nose; mouth and pharynx, 			 						 			 other physical therapy and rehabilitation, 			 						 			 ophthalmologic and otologic diagnosis and treatment and 			 						 			 other diagnostic procedures of respiratory tract and mediastinum 			 			.,[{"commonTestsAndProcedures":"Tracheoscopy and laryngoscopy with biopsy"},{"commonTestsAndProcedures":"Occupational therapy assessment (Speech therapy)"},{"commonTestsAndProcedures":"Other diagnostic procedures (interview; evaluation; consultation)"},{"commonTestsAndProcedures":"Physical therapy exercises (Exercises)"},{"commonTestsAndProcedures":"Diagnostic procedures on nose; mouth and pharynx"},{"commonTestsAndProcedures":"Other physical therapy and rehabilitation"},{"commonTestsAndProcedures":"Ophthalmologic and otologic diagnosis and treatment"},{"commonTestsAndProcedures":"Other diagnostic procedures of respiratory tract and mediastinum"}],The most commonly prescribed drugs for patients with vocal cord polyp include 		 		 esomeprazole (nexium), 		 		 		 beclomethasone nasal product, 		 		 		 nicotine, 		 		 		 azelastine nasal, 		 		 		 phenylephrine (duramax), 		 		 		 rabeprazole (aciphex), 		 		 		 vinorelbine (navelbine), 		 		 		 trandolapril / verapamil, 		 		 		 vitamin a, 		 		 		 adalimumab (humira), 		 		 		 acetaminophen / diphenhydramine, 		 		 		 rituximab and 		 		 		 aprepitant (emend) 		 	.,[{"commonMedications":"Esomeprazole (Nexium)"},{"commonMedications":"Beclomethasone Nasal Product"},{"commonMedications":"Nicotine"},{"commonMedications":"Azelastine Nasal"},{"commonMedications":"Phenylephrine (Duramax)"},{"commonMedications":"Rabeprazole (Aciphex)"},{"commonMedications":"Vinorelbine (Navelbine)"},{"commonMedications":"Vitamin A"},{"commonMedications":"Adalimumab (Humira)"},{"commonMedications":"Rituximab"},{"commonMedications":"Aprepitant (Emend)"}],Groups of people at highest risk for vocal cord polyp include 		 	age 60-74 years		 	age 45-59 years.,Within all the people who go to their doctor with vocal cord polyp, 91% report having hoarse voice, 47% report having sore throat, and 27% report having difficulty speaking. 		The symptoms that are highly suggestive of vocal cord polyp are hoarse voice, difficulty speaking, throat swelling, and lump in throat, although you may still have vocal cord polyp without those symptoms.
107,Turner syndrome,[{"symptoms":"Groin mass"},{"symptoms":"27"},{"symptoms":"Leg pain"},{"symptoms":"27"},{"symptoms":"Hip pain"},{"symptoms":"27"},{"symptoms":"Suprapubic pain"},{"symptoms":"27"},{"symptoms":"Blood in stool"},{"symptoms":"27"},{"symptoms":"Lack of growth"},{"symptoms":"27"},{"symptoms":"Diminished hearing"},{"symptoms":"27"},{"symptoms":"Depression"},{"symptoms":"27"},{"symptoms":"Emotional symptoms"},{"symptoms":"2"},{"symptoms":"Elbow weakness"},{"symptoms":"2"},{"symptoms":"Back weakness"},{"symptoms":"2"},{"symptoms":"Pus in sputum"},{"symptoms":"2"}],Turner syndrome 	 Also known as Gonadal Dysgenesis, XO Syndrome, and Bonnevie-ullrich Syndrome 	 		 	Turner syndrome or Ullrich–Turner syndrome (also known as "Gonadal dysgenesis":550), 45,X, encompasses several conditions in human females, of which monosomy X (absence of an entire sex chromosome, the Barr body) is most common. It is a chromosomal abnormality in which all or part of one of the sex chromosomes is absent or has other abnormalities (unaffected humans have 46 chromosomes, of which two are sex chromosomes). In some cases, the chromosome is missing in some cells but not others, a condition referred to as mosaicism or "Turner mosaicism". 		 Source: Wikipedia,Patients with turner syndrome often receive 			 			 complete physical skin exam performed (ml), 			 						 			 ultrasonography, 			 						 			 other diagnostic procedures (interview; evaluation; consultation), 			 						 			 echocardiography, 			 						 			 depression screen, 			 						 			 examination of breast, 			 						 			 ophthalmologic and otologic diagnosis and treatment and 			 						 			 corneal transplant 			 			.,[{"commonTestsAndProcedures":"Complete physical skin exam performed (ML)"},{"commonTestsAndProcedures":"Ultrasonography (Ultrasound)"},{"commonTestsAndProcedures":"Other diagnostic procedures (interview; evaluation; consultation)"},{"commonTestsAndProcedures":"Echocardiography"},{"commonTestsAndProcedures":"Depression screen (Depression screening)"},{"commonTestsAndProcedures":"Examination of breast"},{"commonTestsAndProcedures":"Ophthalmologic and otologic diagnosis and treatment"},{"commonTestsAndProcedures":"Corneal transplant"}],The most commonly prescribed drugs for patients with turner syndrome include 		 		 somatropin, 		 		 		 ethinyl estradiol / norgestrel, 		 		 		 drospirenone / ethinyl estradiol, 		 		 		 sulfamethoxazole (bactrim), 		 		 		 pimecrolimus topical, 		 		 		 hyoscyamine (a-spas), 		 		 		 ortho cyclen, 		 		 		 carbamazepine, 		 		 		 ascorbic acid, 		 		 		 nystatin topical product, 		 		 		 phenazopyridine (azo), 		 		 		 nifedipine and 		 		 		 levetiracetam (keppra) 		 	.,[{"commonMedications":"Somatropin"},{"commonMedications":"Sulfamethoxazole (Bactrim)"},{"commonMedications":"Pimecrolimus Topical"},{"commonMedications":"Hyoscyamine (A-Spas)"},{"commonMedications":"Ortho Cyclen"},{"commonMedications":"Carbamazepine"},{"commonMedications":"Ascorbic Acid"},{"commonMedications":"Nystatin Topical Product"},{"commonMedications":"Phenazopyridine (Azo)"},{"commonMedications":"Nifedipine"},{"commonMedications":"Levetiracetam (Keppra)"}],Groups of people at highest risk for turner syndrome include 		 	race/ethnicity = other,		 	age 5-14 years,		 	age 1-4 years and		 	sex == female. 		On the other hand, age 75+ years and age 60-74 years almost never get turner syndrome.,Within all the people who go to their doctor with turner syndrome, 27% report having groin mass, 27% report having lack of growth, and 27% report having blood in stool. 		The symptoms that are highly suggestive of turner syndrome are groin mass, blood in stool, lack of growth, diminished hearing, emotional symptoms, elbow weakness, back weakness, and pus in sputum, although you may still have turner syndrome without those symptoms.
"""
line_separated = data.split("\n")
line_separated.pop()

disease_index = []
symptoms = []  # array of values stored in the form of {"symptoms":"Leg pain"}. symptoms[0] will give symptoms for the first disease.
'''takes out the symptoms string'''
# for line in line_separated:
#     ind_pos = line.find(",")
#     symptom_start, symptom_end = line.find("["), line.find("]")
#     str_int = int(line[:ind_pos])
#     symptoms.append(line[symptom_start + 1: symptom_end])
#     disease_index.append(str_int)
# print(symptoms[0])

for line in line_separated:
    line.replace(',,', ',')
    line.replace('  ', ' ')
    print(line)