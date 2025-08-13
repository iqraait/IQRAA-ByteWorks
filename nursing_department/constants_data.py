# from enum import Enum

# class RatingScale(Enum):
#     NOVICE = 1
#     ADVANCED_BEGINNER = 2
#     COMPETENT = 3
#     PROFICIENT = 4

# FORM1_CRITERIA = {
#     "I": {
#         "name": "Appearance and Behaviour",
#         "items": {
#             1: "Punctual and regular in attendance, has a positive attitude towards work & is receptive to corrections",
#             2: "Meets professional grooming standards nails short, hair done, professionalism in uniform, shaved and smiles appropriately",
#             3: "Takes initiative in updating knowledge and demonstrates improvement progressively."
#         },
#         "scale": (1, 4),  # 1-4 scale
#         "type": "frequency"
#     },
#     "II": {
#         "name": "Communication skill",
#         "items": {
#             4: "Friendly and courteous/Introduce self to patient/family and caregiver.",
#             5: "Good listening skill",
#             6: "Communicates clearly and effectively with team members and patient/patient's attendants and reports back to nursing officer/TL/ shift incharge as required",
#             7: "Shift handoff communication is done effectively."
#         },
#         "scale": (1, 4),
#         "type": "frequency"
#     },
#     "III": {
#         "name": "Proactiveness and promptness",
#         "items": {
#             8: "Anticipates needs of patient and/or potential complications and takes corrective/preventive action on time",
#             9: "Asks for help from senior staff nurse/TL, whenever required",
#             10: "Carries out instructions given by doctors/shift incharge/supervisors timely and correctly"
#         },
#         "scale": (1, 4),
#         "type": "frequency"
#     },
#     "IV": {
#         "name": "Prioritizing Capabilities",
#         "items": {
#             11: "Ability to prioritize activities of the patients assigned",
#             12: "Ability to accomplish her task on time",
#             13: "Able to assess the need of time & act instantly"
#         },
#         "scale": (1, 4),
#         "type": "frequency"
#     }
# }

# FORM1_RATING_SCALE_CRITERIA = {
#     "V": {
#         "name": "Adherence to hospital policy (Infection control & isolation)",
#         "items": {
#             14: [
#                 "Has inadequate knowledge & does not follow infection control practices & isolation protocols",
#                 "Follows infection control practices & isolation protocols only when supervised",
#                 "Confidently adheres to all infection control practices including hand hygiene, following aseptic measures in procedures, segregates biomedical waste appropriately & prevents needle stick injury & isolation protocol including barrier nursing precautions",
#                 "In addition to score 3, keeps herself updated about infection control practices and motives other staff to follow them"
#             ]
#         },
#         "scale": RatingScale,
#         "type": "rating"
#     },
#     "VI": {
#         "name": "Training Aptitude",
#         "items": {
#             15: [
#                 "Barely participates in training & development",
#                 "Participates in training & development only after frequent reminders",
#                 "Takes initiative in participating in training & development voluntarily including attending various training modules, in-service education, briefing sessions & unit meetings",
#                 "In addition to score 3, helps in motivates others to participate in training"
#             ]
#         },
#         "scale": RatingScale,
#         "type": "rating"
#     },
#     "VII": {
#         "name": "IT Competency",
#         "items": {
#             16: [
#                 "Unable to use HIS efficiently",
#                 "Operates HIS only with assistance of nursing officer/TL/ unit In charge",
#                 "Confidently operates HIS",
#                 "In addition to score 3, Perform & guides other ANM staff to operate HIS effectively"
#             ]
#         },
#         "scale": RatingScale,
#         "type": "rating"
#     },
#     "VIII": {
#         "name": "Equipment",
#         "items": {
#             17: [
#                 "Unable to operate & cleans any biomedical equipment",
#                 "Operates & cleans most of the biomedical equipment with assistance of nursing officer/TL/ unit Incharge only",
#                 "Confidently operates & cleans most biomedical equipment correctly including Suction apparatus, multipara monitor, pulse oxymeter, glucometer, AMBU Bag, oxygen cylinder,weighing mechine, radient warmer, ventilator, syringe pumb, infusion pumb, laminar flow, incubator, portable warmer, & Sonosite etc",
#                 "In addition to score 3, guides other ANM staff to use & cleaning of biomedical equipment effectively"
#             ]
#         },
#         "scale": RatingScale,
#         "type": "rating"
#     },
#     "IX": {
#         "name": "Assist in assessment of neonates",
#         "items": {
#             18: [
#                 "Unable to assist neonatal assessment",
#                 "Assist in neonatal assessment with supervision of TL/ unit Incharge only",
#                 "Confidently assist in neonatal assessment including vitalsigns monitoring, checking anthropometric measurements, weight and RBS",
#                 "In addition to score 3, Performs & guides other ANM staff to assist in neonatal assessment effectively"
#             ]
#         },
#         "scale": RatingScale,
#         "type": "rating"
#     },
#     "X": {
#         "name": "Neonatal competency",
#         "items": {
#             19: [
#                 "Unable to complete neonatal competency",
#                 "Is able to take care of neonates with the guidance of nursing officer,TL/unit Incharge only",
#                 "Confidently takes care of neonates by safeguarding against fall and is competent to perform neonatal competency effectively",
#                 "In addition to score 3, Is able to perform & train other ANM staff to take care of neonates, assist mothers to do direct breast feeding, Collect expressed breast milk from carers after identifying correctly with ID card, guide parents to visit the babies while visiting in NICU after identifying with ID card &after collecting expressed breast milk- empty the bowl, clean, and return to carer."
#             ]

#         },
#         "scale": RatingScale,
#         "type": "rating"
#     }
# }












# PROCEDURAL_COMPETENCE_CRITERIA = {
#     "XI": {
#         "name": "Procedural competence",
#         "items": {
#             20: {
#                 "name": "Basic Nursing/Hygiene Care of neonates",
#                 "options": [
#                     "Not able to meet basic hygienic needs of the neonates",
#                     "Able to meet hygienic needs of the baby with assistance of senior nurse/TL/incharge",
#                     "Able to meet basic nursing/hygiene care of the neonates independently",
#                     "In addition to score 3, Is able to takes initiative and helps other staff to perform basic nursing/hygiene care (baby care, nesting, oil massaging, etc), Help nursing officers for routine care of babies,change bed linens, remove linen from bed after baby discharge & also maintain baby and bedside always neat and clean"
#                 ]
#             },
#             21: {
#                 "name": "Assist in NICU procedures",
#                 "options": [
#                     "Not able to assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse",
#                     "Able to meet assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse with assistance/supervision of senior nurse/TL/incharge",
#                     "Able to assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse.",
#                     "In addition to score 3, Is able to perform & helps other staff to assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse."
#                 ]
#             },
#             # Continue with all other procedural competence items...
#             28: {
#                 "name": "Care of Dead",
#                 "options": [
#                     "Unable to perform dead body care & carry out death formalities",
#                     "Performs dead body care & carry out death formalities with assistance of staff nurse/unit TL/Incharge",
#                     "Performs dead body care & carries out death formalities independently including cleaning & packing of body, getting the death forms filled in appropriate copies & shifting the body to mortuary/hearse van",
#                     "In addition to score 3, Is also able to guide other ANM staff in care of dead"
#                 ]
#             }
#         },
#         "scale": RatingScale,
#         "type": "procedural"
#     }
# }



# # Combined structure for easy access
# FORM1_FULL_STRUCTURE = {
#     **FORM1_CRITERIA,
#     **FORM1_RATING_SCALE_CRITERIA,
#     **PROCEDURAL_COMPETENCE_CRITERIA
# }








FORM1_FULL_STRUCTURE = {"Appearance and Behaviour":["Punctual and regular in attendance, has a positive attitude towards work & is receptive to corrections","Meets professional grooming standards nails short, hair done, professionalism in uniform, shaved and smiles appropriately","Takes initiative in updating knowledge and demonstrates improvement progressively."] ,

    "Communication skill":["Friendly and courteous/Introduce self to patient/family and caregiver.","Good listening skill","Communicates clearly and effectively with team members and patient/patient's attendants and reports back to nursing officer/TL/ shift incharge as required","Shift handoff communication is done effectively."],
    
     "Proactiveness and promptness":["Anticipates needs of patient and/or potential complications and takes corrective/preventive action on time","Asks for help from senior staff nurse/TL, whenever required","Carries out instructions given by doctors/shift incharge/supervisors timely and correctly"],
     
    "Prioritizing Capabilities":["Ability to prioritize activities of the patients assigned",
    "Ability to accomplish her task on time",
    "Able to assess the need of time & act instantly"],
    
    "Adherence to hospital policy (Infection control & isolation)":["Has inadequate knowledge & does not follow infection control practices & isolation protocols",
                "Follows infection control practices & isolation protocols only when supervised",
                "Confidently adheres to all infection control practices including hand hygiene, following aseptic measures in procedures, segregates biomedical waste appropriately & prevents needle stick injury & isolation protocol including barrier nursing precautions",
                "In addition to score 3, keeps herself updated about infection control practices and motives other staff to follow them"],
                
    
    "Training Aptitude":["Barely participates in training & development","Participates in training & development only after frequent reminders",
                "Takes initiative in participating in training & development voluntarily including attending various training modules, in-service education, briefing sessions & unit meetings",
                "In addition to score 3, helps in motivates others to participate in training"],
                
    "IT Competency":["Unable to use HIS efficiently",
                "Operates HIS only with assistance of nursing officer/TL/ unit In charge",
                "Confidently operates HIS",
                "In addition to score 3, Perform & guides other ANM staff to operate HIS effectively"
            ],
    "Equipment":["Unable to operate & cleans any biomedical equipment",
                "Operates & cleans most of the biomedical equipment with assistance of nursing officer/TL/ unit Incharge only",
                "Confidently operates & cleans most biomedical equipment correctly including Suction apparatus, multipara monitor, pulse oxymeter, glucometer, AMBU Bag, oxygen cylinder,weighing mechine, radient warmer, ventilator, syringe pumb, infusion pumb, laminar flow, incubator, portable warmer, & Sonosite etc",
                "In addition to score 3, guides other ANM staff to use & cleaning of biomedical equipment effectively"
            ],
    "Assist in assessment of neonates":[
                "Unable to assist neonatal assessment",
                "Assist in neonatal assessment with supervision of TL/ unit Incharge only",
                "Confidently assist in neonatal assessment including vitalsigns monitoring, checking anthropometric measurements, weight and RBS",
                "In addition to score 3, Performs & guides other ANM staff to assist in neonatal assessment effectively"
            ],
    
    "Neonatal competency":["Unable to complete neonatal competency",
                "Is able to take care of neonates with the guidance of nursing officer,TL/unit Incharge only",
                "Confidently takes care of neonates by safeguarding against fall and is competent to perform neonatal competency effectively",
                "In addition to score 3, Is able to perform & train other ANM staff to take care of neonates, assist mothers to do direct breast feeding, Collect expressed breast milk from carers after identifying correctly with ID card, guide parents to visit the babies while visiting in NICU after identifying with ID card &after collecting expressed breast milk- empty the bowl, clean, and return to carer."
            ],
            
    "Basic Nursing/Hygiene Care of neonates":["Not able to meet basic hygienic needs of the neonates",
                    "Able to meet hygienic needs of the baby with assistance of senior nurse/TL/incharge",
                    "Able to meet basic nursing/hygiene care of the neonates independently",
                    "In addition to score 3, Is able to takes initiative and helps other staff to perform basic nursing/hygiene care (baby care, nesting, oil massaging, etc), Help nursing officers for routine care of babies,change bed linens, remove linen from bed after baby discharge & also maintain baby and bedside always neat and clean"
                ],
                 
                 
    "Assist in NICU procedures":["Not able to assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse",
                    "Able to meet assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse with assistance/supervision of senior nurse/TL/incharge",
                    "Able to assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse.",
                    "In addition to score 3, Is able to perform & helps other staff to assist in procedures, such as IV cannulization, ET suction, blood transfusion, etc as directed by a physician or staff nurse."
                ],
                
    
    "Care of Dead":[
                    "Unable to perform dead body care & carry out death formalities",
                    "Performs dead body care & carry out death formalities with assistance of staff nurse/unit TL/Incharge",
                    "Performs dead body care & carries out death formalities independently including cleaning & packing of body, getting the death forms filled in appropriate copies & shifting the body to mortuary/hearse van",
                    "In addition to score 3, Is also able to guide other ANM staff in care of dead"
                ]}           
                
