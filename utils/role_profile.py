ROLE_SKILLS = {
    "Physician": {
        "clinical_skills": [
            "Diagnosis and Treatment (Common Illnesses)",
            "Preventive Care",
            "Chronic Disease Management",
            "Patient Assessment",
            "Medical History Taking",
            "Physical Examination",
            "Referral Management (to specialists)",
            "Clinical Reasoning",
            "Pharmacology",
            "Basic Procedures (e.g., wound care, minor suturing, basic fracture care)",
            "Diagnostic Test Interpretation (Labs, Imaging)"
        ],
        "technical_skills": [
            "Documentation (EHR/EMR proficiency)"
        ],
        "soft_skills": [
            "Medical Ethics",
            "Communication (Patient, Family, Peers)",
            "Empathy",
            "Problem-Solving",
            "Interdisciplinary Collaboration",
            "Time Management",
            "Health Promotion"
        ],
        "certifications": [
            "Medical Doctor (MD) or Doctor of Osteopathy (DO) Degree",
            "State Medical License",
            "Board Certification in Family Medicine or Internal Medicine (e.g., ABFM, ABIM)",
            "Basic Life Support (BLS)",
            "Advanced Cardiovascular Life Support (ACLS)"
        ]
    },
    "Registered Nurse": {
        "clinical_skills": [
            "Patient Care (Holistic)",
            "Medication Administration",
            "Vital Signs Monitoring",
            "Wound Care",
            "Patient Education",
            "Health Assessment",
            "Care Planning",
            "IV Insertion and Management",
            "Aseptic Technique",
            "Infection Control",
            "Emergency Response"
        ],
        "technical_skills": [
            "Electronic Health Record (EHR) Documentation"
        ],
        "soft_skills": [
            "Communication (Verbal, Written)",
            "Critical Thinking",
            "Problem-Solving",
            "Compassion",
            "Attention to Detail",
            "Teamwork"
        ],
        "certifications": [
            "Associate's Degree in Nursing (ADN) or Bachelor of Science in Nursing (BSN)",
            "National Council Licensure Examination (NCLEX-RN)",
            "State Nursing License",
            "Basic Life Support (BLS)",
            "Advanced Cardiovascular Life Support (ACLS)",
            "Pediatric Advanced Life Support (PALS)",
            "Specialty Certifications (e.g., CCRN, CEN, OCN)"
        ]
    },
    "Medical Laboratory Scientist": {
        "clinical_skills": [
            "Laboratory Testing (Hematology, Chemistry, Microbiology, Immunohematology/Blood Bank, Urinalysis)",
            "Specimen Collection and Processing",
            "Microscopic Analysis"
        ],
        "technical_skills": [
            "Instrumentation Operation and Maintenance",
            "Quality Control and Assurance",
            "Data Analysis and Interpretation",
            "Troubleshooting (equipment, results)",
            "Record Keeping and Documentation",
            "Laboratory Safety (OSHA, CLIA)",
            "Medical Terminology"
        ],
        "soft_skills": [
            "Accuracy and Precision",
            "Attention to Detail",
            "Critical Thinking",
            "Problem-Solving",
            "Communication (Lab staff, clinicians)"
        ],
        "certifications": [
            "Bachelor's Degree in Medical Laboratory Science/Technology or related science field",
            "Certification from American Society for Clinical Pathology (ASCP) Board of Certification (e.g., MLS(ASCP)CM, MT(ASCP))",
            "Specialty Certifications (e.g., SBB, SM)"
        ]
    },
    "Pharmacist": {
        "clinical_skills": [
            "Medication Dispensing",
            "Drug Interaction and Adverse Effect Monitoring",
            "Dosage Calculation",
            "Patient Counseling on Medication Use",
            "Pharmacology and Pharmacokinetics",
            "Drug Information Retrieval",
            "Immunization Administration"
        ],
        "technical_skills": [
            "Compounding (Sterile and Non-sterile)",
            "Inventory Management",
            "Regulatory Compliance (DEA, FDA, State Boards)",
            "Pharmacy Software Proficiency (e.g., EHR integration)"
        ],
        "soft_skills": [
            "Patient Safety",
            "Attention to Detail",
            "Analytical Skills",
            "Communication (Patients, Physicians, Nurses)",
            "Problem-Solving",
            "Customer Service"
        ],
        "certifications": [
            "Doctor of Pharmacy (Pharm.D.) Degree",
            "State Pharmacist License",
            "Board Certification in Pharmacotherapy (BCPS), Ambulatory Care (BCACP), Oncology (BCOP) (Board of Pharmacy Specialties - BPS)",
            "Immunization Certification"
        ]
    },
    "Radiologist": {
        "clinical_skills": [
            "Medical Imaging Interpretation (X-ray, CT, MRI, Ultrasound, Nuclear Medicine, Mammography)",
            "Image Analysis and Reporting",
            "Diagnostic Accuracy",
            "Pathology Knowledge (as it relates to imaging findings)",
            "Anatomy and Physiology",
            "Interventional Radiology Techniques (for Interventional Radiologists)"
        ],
        "technical_skills": [
            "Radiation Safety and Protection",
            "PACS (Picture Archiving and Communication System) and RIS (Radiology Information System) Proficiency",
            "Contrast Media Knowledge"
        ],
        "soft_skills": [
            "Communication (Referring Physicians)",
            "Attention to Detail",
            "Critical Thinking",
            "Problem-Solving"
        ],
        "certifications": [
            "Medical Doctor (MD) or Doctor of Osteopathy (DO) Degree",
            "State Medical License",
            "Residency Training in Diagnostic Radiology",
            "Board Certification from the American Board of Radiology (ABR)",
            "Fellowship Training and Board Certification in Subspecialties (e.g., Neuroradiology, Interventional Radiology)"
        ]
    },
    "Emergency Medical Technician": { # Grouping EMT and Paramedic for skill categorization
        "clinical_skills": [
            "Emergency Patient Assessment",
            "Basic Life Support (BLS)",
            "Advanced Life Support (ALS)",
            "Cardiopulmonary Resuscitation (CPR)",
            "Trauma Care (Bleeding control, Fracture immobilization)",
            "Airway Management",
            "Medication Administration (Paramedics)",
            "IV Insertion (Paramedics)",
            "Defibrillation",
            "Spinal Immobilization",
            "Patient Extrication and Transport",
            "Vital Signs Monitoring"
        ],
        "technical_skills": [], # Most technical skills here are inherent to the clinical practice
        "soft_skills": [
            "Rapid Decision-Making",
            "Stress Management",
            "Communication (Patients, Families, Hospital Staff)",
            "Problem-Solving",
            "Compassion",
            "Physical Stamina"
        ],
        "certifications": [
            "National Registry of Emergency Medical Technicians (NREMT) certification (EMT-Basic, Advanced EMT, Paramedic)",
            "State EMT/Paramedic License",
            "Basic Life Support (BLS)",
            "Advanced Cardiovascular Life Support (ACLS) (Paramedics)",
            "Pediatric Advanced Life Support (PALS) (Paramedics)",
            "Prehospital Trauma Life Support (PHTLS) or International Trauma Life Support (ITLS)"
        ]
    },
    "Physical Therapist": {
        "clinical_skills": [
            "Patient Assessment (Musculoskeletal, Neurological)",
            "Therapeutic Exercise Prescription",
            "Manual Therapy Techniques",
            "Modality Application (e.g., ultrasound, electrical stimulation, heat/cold therapy)",
            "Gait Training",
            "Balance Training",
            "Functional Training",
            "Pain Management",
            "Rehabilitation Planning",
            "Patient Education (Home exercise programs, injury prevention)",
            "Equipment Knowledge (Assistive devices, exercise equipment)"
        ],
        "technical_skills": [
            "Documentation (SOAP notes, progress reports)"
        ],
        "soft_skills": [
            "Communication (Patients, Families, Physicians)",
            "Empathy",
            "Clinical Reasoning",
            "Problem-Solving",
            "Goal Setting (Patient-centered)"
        ],
        "certifications": [
            "Doctor of Physical Therapy (DPT) Degree",
            "State Physical Therapy License",
            "Board Certification in Specialty Areas (e.g., OCS, NCS, GCS, SCS)",
            "CPR/First Aid"
        ]
    },
    "Physician Assistant": {
        "clinical_skills": [
            "Patient History Taking and Physical Exams",
            "Diagnosis and Treatment of Common Illnesses",
            "Ordering and Interpreting Diagnostic Tests (Labs, Imaging)",
            "Medication Prescription and Management",
            "Surgical Assistance (First-assist role in surgery)",
            "Minor Procedures (e.g., suturing, splinting, aspirations)",
            "Patient Education and Counseling",
            "Clinical Reasoning"
        ],
        "technical_skills": [
            "Medical Documentation (EHR/EMR)"
        ],
        "soft_skills": [
            "Problem-Solving",
            "Communication (Patients, Supervising Physician, Healthcare Team)",
            "Interdisciplinary Collaboration",
            "Ethical Practice",
            "Adaptability (across specialties)"
        ],
        "certifications": [
            "Master's Degree from an ARC-PA accredited PA Program",
            "Physician Assistant National Certifying Examination (PANCE)",
            "Physician Assistant-Certified (PA-C) credential from NCCPA",
            "State PA License",
            "Basic Life Support (BLS)",
            "Advanced Cardiovascular Life Support (ACLS)"
        ]
    },
    "Anesthesiologist": {
        "clinical_skills": [
            "Anesthesia Administration (General, Regional, Local)",
            "Patient Monitoring (Vital Signs, ECG, Hemodynamics)",
            "Airway Management (Intubation, LMA)",
            "Pain Management (Acute and Chronic)",
            "Resuscitation Techniques (CPR, ACLS)",
            "Pharmacology (Anesthetic Agents, Analgesics)",
            "Preoperative Patient Assessment",
            "Postoperative Management",
            "Crisis Management in OR",
            "Surgical Anesthesia Planning"
        ],
        "technical_skills": [
            "Anesthesia Equipment Operation"
        ],
        "soft_skills": [
            "Critical Thinking",
            "Rapid Decision-Making under Pressure",
            "Attention to Detail",
            "Communication (Surgeons, OR Staff, Patients)",
            "Teamwork"
        ],
        "certifications": [
            "Medical Doctor (MD) or Doctor of Osteopathy (DO) Degree",
            "State Medical License",
            "Residency Training in Anesthesiology",
            "Board Certification from the American Board of Anesthesiology (ABA)",
            "Fellowship Training and Board Certification in Subspecialties (e.g., Pain Medicine, Critical Care Medicine)",
            "Advanced Cardiovascular Life Support (ACLS)"
        ]
    },
    "Medical and Health Services Manager": { # Grouping Manager and Administrator
        "clinical_skills": [], # Not direct patient care/clinical
        "technical_skills": [
            "Healthcare Operations Management",
            "Financial Management (Budgeting, Billing, Revenue Cycle)",
            "Personnel Management (Staffing, HR, Performance Evaluation)",
            "Strategic Planning",
            "Project Management",
            "Quality Improvement (QI) / Patient Safety Initiatives",
            "Regulatory Compliance (HIPAA, JCAHO, State Regulations)",
            "Data Analysis and Reporting (Healthcare Metrics)",
            "Healthcare Information Technology (EHR implementation, Cybersecurity basics)"
        ],
        "soft_skills": [
            "Leadership",
            "Communication (Staff, Stakeholders, Board)",
            "Problem-Solving",
            "Organizational Skills",
            "Decision-Making",
            "Negotiation",
            "Marketing (Healthcare services)"
        ],
        "certifications": [
            "Bachelor's Degree (Healthcare Administration, Business Administration, Public Health)",
            "Master's Degree (MHA, MBA with Healthcare Concentration, MPH)",
            "Certified Medical Manager (CMM)",
            "Fellow of the American College of Healthcare Executives (FACHE)",
            "Project Management Professional (PMP)",
            "Certified Professional in Healthcare Quality (CPHQ)",
            "Certified Revenue Cycle Representative (CRCR)"
        ]
    }
}