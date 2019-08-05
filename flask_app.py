
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request



from disease import getRankings
from disease import getRecommendation

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])

def adder_page():
    errors = ""
    if request.method == "POST":
        disease = None
        try:
            age = str(request.form["age"])
            gender = str(request.form["gender"])
            disease = str(request.form["disease"])
            symptoms = str(request.form["smp"])
            print("HI")
        except:
            errors += "<p>{!r} is not a disease.</p>\n".format(request.form["disease"])
        if symptoms:
            array = symptoms.split(',')
            conditions = getRecommendation(array)
            return '''
                    <html>
                        <head>
                            <meta charset="utf-8" />
                            <meta name="viewport" content="width=device-width, initial-scale=1" />
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                            <link href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.css" rel="stylesheet">
                            <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                            <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js"></script>
                            <title>DrugRec</title>

                            <style>
                                body,
                              html {{
                                margin: 0;
                                size: 17px;
                                font-family: Avenir;
                                /* position: absolute; */
                              }}
                              .tablink {{
                                margin: 80;
                                background-color: #FF5733;
                                color: black;
                                float: left;
                                border: none;
                                outline: none;
                                cursor: pointer;
                                padding: 14px 16px;
                                font-size: 17px;
                                width: 25%;
                                font-family: Avenir;
                              }}
                            </style>
                        </head>
                        <body style="background-color: #e0ffff">
                            {errors}


                              <h2 style="text-align: center; font-weight: 600; font-family: Avenir">
                                Drug Recommendation
                              </h2>
                              <br>
                              <br>





                              <form id="input" method="post" action=".">
                                <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
                                      <link rel="stylesheet" href="/resources/demos/style.css">
                                      <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
                                      <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
                                      <script>

                                      $( function() {{
                                        var availableTags = [
                                            "Upper abdominal pain","Lower abdominal pain","Abscess (Collection of pus)","Alcohol abuse","Anxiety (Nervousness)","Arm ache or pain","Back ache or pain","Bleeding tendency","Blood in vomit","Bloody diarrhea","Pain or soreness of breast","Calf pain","Chest pressure","Chills","Change in behavior","Constipation","Cough","Dark stools","Depressed","Diarrhea","Dizziness","Double vision (Diplopia)","Ear pressure","Pain in the ear","Elbow ache or pain","Eye pain (Irritation)","Facial pain","Fainting","Fever","Fever in the returning traveler","Fever of unknown origin","Flank pain","Frequent urination (Frequency)","Foot pain","Cranky, crying, fussy, irritable child","Groin pain","Delusions or hallucinations","Hand, finger ache or pain","Head injury","Headache","Heel pain","Heat illness","Hip pain","Hives","Hoarse voice","Hypothermia (Low temperature)","Incontinence (leaking urine)","Insect sting","Insomnia (Trouble sleeping)","Skin itching","Joint pain","Kidney pain (Flank pain)","Knee pain","Laceration","Leg ache or pain","Swelling of both legs","Lethargy (Sluggishness)","Mouth pain","Muscle pain","Nail Injury","Nasal bleeding","Nasal injury","Nausea","Neck ache or pain","Neck swelling","Numbness","Obesity","Overdose","Painful urination","Heart pulsations and palpitations","Pelvic pain","Penile discharge","Penis pain","Poisoning","Pregnancy problem","Psychiatric problem","Puncture wound","Rash","Rectal pain","Rectal swelling","Scrotal pain","Scrotal swelling","Seizure","Shortness of breath","Shoulder ache or pain","Sinus pain and pressure","Skin trauma","Snake bite","Sore throat","Speech problem","Spider bite","Substance abuse (Drug abuse)","Suicidal tendencies","Swallowing problem (Dysphagia)","Swelling","Toe pain","Tooth pain","Trauma","Traveler's diarrhea","Unsteady gait (Trouble walking)","Vaginal bleeding","Vaginal bleeding after menopause","Vaginal bleeding during pregnancy","Vaginal discharge","Vaginal itching","Vaginal pain","Vertigo (Room spinning)","Visual problems","Vomiting","General weakness","Weakness (Muscle localized)","Tired","Wrist pain","Throat pain","Tremors","Weight loss, unexplained","Tongue swelling","Inconsolable baby","Wheezing (Noisy breathing)","Swollen lymph nodes (Large lymph nodes)","Failure to thrive","Behavioral problem","Itchy rash (Pruritic rash)","Headache after trauma","Learning difficulties","Blood in urine (Hematuria)","Urinary retention (Inability to urinate)","Liver failure (Cirrhosis)","Choking","Painful rash","Ingestion","Melena (Black stools from blood)","Vomiting coffee ground material","Ringing in ears (Tinnitus)","Mouth ulcers","Mouth swelling","Eye redness","Sneezing","Bleeding gums","Loss of balance","Bleeding in brain","Cyanosis (Blue skin coloration)","Muscle spasm","Drooling","Abdominal swelling (Stomach swelling)","Skin growths","Hand numbness (paresthesias)","Ankle pain","Hemoptysis (Coughing blood)","Jaundice (Yellowing skin)","Night sweats","Flatulence (Passing gas)","Blister (Pocket of fluid)","Hair loss (Baldness)","Jaw pain","Impotence","Heart murmur (Abnormal heart sound)","Pustule (Collection of pus)","Skin pain","Hot skin","Skin swelling","Lip swelling","Eye swelling","Foot swelling","Visual flashing lights","Eye floaters","Amenorrhea (No menstruation)","Blurry vision","Painful gums","Swollen gums","Low blood sugar","Low blood pressure","Darkening of the skin (Hyperpigmentation)","Low heart rate","Foot itching","Hot flashes","Infertility (Female)","Increased facial hair","Arm swelling","Calf swelling","Ear swelling","Wrist swelling","Maroon stools","Arm cut (laceration)","Hand cut (laceration)","Leg cut (laceration)","Foot cut (laceration)","Arm itching","Hand redness","Foot redness","Arm redness","Leg redness","Hand itching","Leg itching","Steatorrhea (Excess fat in stool)","Upper leg pain","Armpit pain","Sweating","Nasal congestion","Joint stiffness","Skin sores","Chest burning","Memory loss","Arm numbness (paresthesias)","Leg numbness (paresthesias)","Foot numbness (paresthesias)","Face numbness (paresthesias)","Dementia","Facial droop (weakness)","Limping in a child","Increased thirst","Increased urination (polyuria)","Shin pain","Stings","Sleep disorders","Drooping eyelid (Ptosis)","Snoring","Dry skin","Itchy eyes","Elbow swelling","Chest pain","Skin infection","Stomach and abdominal pain","Anger","Hurts to breathe","Difficulty breathing","Pulling at ears","Skin bumps","Congestion in chest or lungs","Discharge from ear","Low back ache or pain","Unusual color or odor of urine","Penis inflammation or swelling","Excessive appetite","Retaining fluid","Lump or mass of breast","Neck stiffness or tightness","Agitated","Confusion","Headache and weakness","Confusion and headache","Nipple discharge","Shoulder stiffness or tightness","Arm stiffness or tightness","High blood pressure","High blood sugar"
                                          ];
                                        var arr = [];
                                        var array = [];
                                        $( "#symptoms" ).autocomplete({{
                                          source: availableTags,
                                          minLength: 3,
                                          select: function(e, ui) {{
                                                arr.push(" " + ui.item.value);
                                                array.push(ui.item.value);
                                                document.getElementById("disp").innerHTML = "Symptoms:" + arr.join();
                                                document.getElementById("smp").innerHTML = array.join();

                                            }}

                                        }});
                                      }} );
                                      </script>

                                      <div class="ui-widget">
                                          <label for="symptoms" style = "margin: 20px; font-size: 17px; font-weight: bold; font-family: Avenir">Enter Symptoms: </label>
                                          <input id="symptoms" style="float: right; display: inline; font-size: 15px">
                                        </div>
                                    <p name = "disp" id = "disp" style = "text-align: center">Symptoms:</p>
                                    <textarea name="smp" id = "smp" style = "text-align: center; display:none;"></textarea>

                                  <div style="text-align: center">
                                        <button type="submit" class="btn btn-primary" style="text-align: center" >Get Diseases</button>

                                    </div>
                                <p style="margin: 20px; font-size: 17px; text-align: center";> Predicted Conditions are: {conditions} </p>
                                <h5 style="margin: 20px; font-size: 17px; font-weight: bold";>
                                  Age:
                                  <span style="float: right; display: inline; font-size: 15px">
                                    <input
                                      name="age"
                                      type="number"
                                      pattern="\d*"
                                      autocomplete="off"
                                      style="width: 40px"
                                    />
                                  </span>
                                </h5>
                                <h5 style="margin: 20px; font-size: 17px; font-weight: bold">
                                  Gender:
                                  <select name="gender" id="gender" style="float: right; display: inline; width: 100px; background: white; font-size: 15px">
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                      </select>
                                </h5>
                                <script>

                                                  $( function() {{
                                                    var availableTags = [
                                                        'Diabetes Insipidus', 'Cold Symptoms', 'Herpes Simplex, Suppression', 'Angina', 'Bladder Infection', 'Constipation, Chronic', 'Endoscopy or Radiology Premedication', 'Nausea/Vomiting of Pregnancy', 'Gastroparesis', 'Osteoarthritis', 'Plaque Psoriasis', 'Hypogonadism, Male', 'Actinic Keratosis', 'Light Anesthesia', 'Hypersomnia', 'Osteolytic Bone Metastases of Solid Tumors', 'Agitated State', 'Hemorrhoids', "Tourette's Syndrome", 'Chronic Myelogenous Leukemia', 'Acne', 'Uveitis', 'Alopecia', 'ADHD', 'Biliary Cirrhosis', 'Light Sedation', 'Glaucoma, Open Angle', 'Menorrhagia', 'Vitamin D Deficiency', 'Systemic Lupus Erythematosus', 'Tonsillitis/Pharyngitis', 'Hypoestrogenism', 'Basal Cell Carcinoma', 'Tinea Versicol', 'Chlamydia Infection', "Alzheimer's Disease", 'Bacterial Skin Infection', 'Atrial Fibrillation', 'Cold Sores', 'Burns, External', 'Prevention of Thromboembolism in Atrial Fibrillation', 'Borderline Personality Disorder', 'Osteoporosis', 'Malaria Prevention', 'Ulcerative Colitis', 'Eye Redness', 'Epilepsy', 'Allergic Reactions', 'Cancer', 'Allergic Rhinitis', 'Opiate Dependence', 'Human Papillomavirus Prophylaxis', 'Hypertensive Emergency', 'Dermatitis', 'Status Epilepticus', 'Birth Control', 'Sarcoidosis', 'Insomnia', 'Malaria', 'Onychomycosis, Toenail', 'Asthma, acute', 'Constipation, Drug Induced', 'Stomach Ulce', 'Asthma', 'Bowel Preparation', 'Cough and Nasal Congestion', 'Rosacea', 'Nocturnal Leg Cramps', 'Extrapyramidal Reaction', 'Benign Essential Trem', 'Labor Pain', 'Sexual Dysfunction, SSRI Induced', 'Abnormal Uterine Bleeding', 'Surgical Prophylaxis', 'Cerebral Spasticity', 'Pseudotumor Cerebri', 'Anxiety and Stress', 'Ovarian Cysts', 'Asperger Syndrome', 'Migraine Prevention', 'Fatigue', 'HIV Infection', 'Candida Urinary Tract Infection', 'Bronchiectasis', 'Hyperhidrosis', 'Sore Throat', 'Undifferentiated Connective Tissue Disease', 'Eye Redness/Itching', 'Allergies', 'Swine Flu', 'Erosive Esophagitis', 'Nausea/Vomiting, Postoperative', 'Benign Prostatic Hyperplasia', 'Autism', 'Anxiety', 'Migraine', 'Atrial Flutte', 'Pneumococcal Disease Prophylaxis', 'Impetig', 'Edema', 'High Blood Pressure', 'Indigestion', 'Panic Disorder', 'Bronchitis', "Crohn's Disease", 'Diaper Rash', 'Conjunctivitis, Allergic', 'Androgenetic Alopecia', 'Eczema', 'Shift Work Sleep Disorder', 'Back Pain', 'Reversal of Opioid Sedation', 'Headache', 'Peripheral Neuropathy', 'COPD, Maintenance', 'Diverticulitis', 'Pain', 'Herbal Supplementation', 'Colorectal Cancer', 'Narcolepsy', 'Menstrual Disorders', 'Tinea Corporis', 'Multiple Myeloma', 'Dietary Supplementation', "Sjogren's Syndrome", 'Prostate Cancer', 'Premenstrual Dysphoric Disorder', 'Chronic Idiopathic Constipation', 'Facial Wrinkles', 'Postoperative Pain', 'Tendonitis', 'Lipodystrophy', 'Prevention of Hypokalemia', 'Kidney Infections', 'Seasonal Allergic Conjunctivitis', 'Sinus Symptoms', 'Atopic Dermatitis', 'Endometrial Hyperplasia, Prophylaxis', 'Pupillary Dilation', 'Folic Acid Deficiency', 'Dermatitis Herpetiformis', 'Keratoconjunctivitis Sicca', 'Hypothyroidism, After Thyroid Removal', 'Mitral Valve Prolapse', 'High Cholesterol', 'Opiate Withdrawal', 'Pulmonary Embolism, Recurrent Event', 'Bacterial Vaginitis', 'Tinnitus', 'Emergency Contraception', 'Inflammatory Conditions', 'Urinary Retention', 'Oral Thrush', 'Supraventricular Tachycardia', 'Social Anxiety Disorder', 'Reflex Sympathetic Dystrophy Syndrome', 'Vulvodynia', 'Diabetes, Type 1', 'Sinusitis', 'Xerostomia', 'Acute Lymphoblastic Leukemia', 'Thyroid Suppression Test', 'Hypertriglyceridemia', 'Formoterol', 'Lyme Disease', 'Nasal Polyps', "Crohn's Disease, Maintenance", 'Pharyngitis', 'Opioid Overdose', 'Bipolar Disorder', 'Restless Legs Syndrome', 'Hemangioma', 'Spondyloarthritis', 'Cataplexy', 'Trichotillomania', 'Diabetes, Type 2', 'Opiate Adjunct', 'Immunosuppression', 'New Daily Persistent Headache', 'Computed Tomography', 'Obstructive Sleep Apnea/Hypopnea Syndrome', 'Weight Loss', 'Cluster Headaches', 'Hereditary Angioedema', 'Metformin / sitagliptin', 'Pneumonia', 'Dental Abscess', 'Angina Pectoris Prophylaxis', 'Strep Throat', 'Dystonia', 'Seizure Prevention', 'Binge Eating Disorder', 'Breast Cancer, Metastatic', 'Ankylosing Spondylitis', 'Cough', 'Rhinitis', 'Opioid-Induced Constipation', 'Ulcerative Colitis, Active', 'Schistosoma japonicum', 'Anaplastic Oligodendroglioma', "Parkinson's Disease", 'Pruritus', 'Otitis Media', 'Constipation', "Barrett's Esophagus", 'COPD', 'Influenza Prophylaxis', 'Nausea/Vomiting', 'Trichomoniasis', 'Mucositis', 'Non-Small Cell Lung Cancer', 'Left Ventricular Dysfunction', 'Period Pain', 'Bacterial Endocarditis Prevention', 'Diarrhea', 'Hirsutism', 'Breast Cancer, Adjuvant', 'Temporomandibular Joint Disorder', 'Breast Cancer', 'Hyperprolactinemia', 'Periodic Limb Movement Disorder', 'Perimenopausal Symptoms', 'Dermatomyositis', 'Muscle Pain', 'Keratosis', 'Warts', 'TSH Suppression', 'Psoriatic Arthritis', 'Premature Ventricular Depolarizations', 'Interstitial Cystitis', 'Neuropathic Pain', 'Helicobacter Pylori Infection', 'Clostridial Infection', 'Vaginal Yeast Infection', 'Dysuria', 'Schizophrenia', 'Psoriasis', 'Anorexia', 'Uterine Fibroids', 'Polycystic Ovary Syndrome', "Addison's Disease", 'Female Infertility', 'Chronic Pain', 'Asthma, Maintenance', 'Hyperthyroidism', 'Seizures', 'Myasthenia Gravis', 'Obesity', 'Fibromyalgia', 'Heart Attack', 'High Cholesterol, Familial Homozygous', 'Burning Mouth Syndrome', 'Sedation', 'Influenza', 'Renal Cell Carcinoma', 'Urticaria', 'Skin Rash', 'Nausea/Vomiting, Chemotherapy Induced', 'Post Traumatic Stress Disorder', 'Hyperlipoproteinemia', 'Prevention of Dental Caries', 'Deep Vein Thrombosis, First Event', 'Breakthrough Pain', 'Spondylolisthesis', 'Head Lice', 'Vitamin/Mineral Supplementation during Pregnancy/Lactation', 'Dysautonomia', 'Ophthalmic Surgery', 'Obsessive Compulsive Disorder', 'Hepatitis C', 'Paranoid Disorder', 'Primary Immunodeficiency Syndrome', 'Skin and Structure Infection', 'Herpes Simplex', 'Condylomata Acuminata', 'Dry Skin', "Hashimoto's disease", 'Postpartum Depression', 'Lennox-Gastaut Syndrome', 'Heart Failure', 'Bacterial Infection', 'Amenorrhea', 'Systemic Mastocytosis', 'Chronic Fatigue Syndrome', 'Schizoaffective Disorder', 'Anesthesia', 'Alcohol Dependence', 'Streptococcal Infection', 'Hot Flashes', 'Night Terrors', 'Generalized Anxiety Disorder', 'Sciatica', 'Muscle Twitching', 'Pulmonary Embolism', 'Neutropenia Associated with Chemotherapy', 'Nasal Congestion', 'Progesterone Insufficiency', "Behcet's Disease", 'Seborrheic Dermatitis', 'Carcinoid Tum', 'moterol / mometasone)', 'NSAID-Induced Ulcer Prophylaxis', 'Trigeminal Neuralgia', 'Constipation, Acute', 'Smoking Cessation', 'Urinary Tract Infection', 'Gout', 'Upper Respiratory Tract Infection', 'Avian Influenza', 'Pseudobulbar Affect', 'Erectile Dysfunction', 'GERD', 'Bursitis', 'Irritable Bowel Syndrome', 'Depression', 'Endometriosis', 'Conjunctivitis, Bacterial', 'Women (oxybutynin)', 'Deep Vein Thrombosis', 'High Cholesterol, Familial Heterozygous', 'Methicillin-Resistant Staphylococcus Aureus Infection', 'Gout, Acute', 'Glioblastoma Multiforme', 'Underactive Thyroid', 'Hepatitis B', 'Multiple Sclerosis', 'Urinary Tract Stones', 'Overactive Bladder', 'Major Depressive Disorder', 'Vertig', 'Glaucoma', "Non-Hodgkin's Lymphoma", 'Psychosis', 'Dry Eye Disease', 'Atrophic Vaginitis', 'Postmenopausal Symptoms', 'Arrhythmia', 'Pulmonary Hypertension', 'Giardiasis', 'Performance Anxiety', "Raynaud's Syndrome", 'Alcohol Withdrawal', 'Anemia, Sickle Cell', 'Urinary Incontinence', 'Not Listed / Othe', 'Diabetic Peripheral Neuropathy', 'Pain/Feve', 'Mania', 'Adult Human Growth Hormone Deficiency', 'Hypokalemia', 'Bulimia', 'Diarrhea, Chronic', 'Muscle Spasm', 'Melanoma, Metastatic', 'Rheumatoid Arthritis', 'Prostatitis', 'Juvenile Idiopathic Arthritis', 'Motion Sickness', 'Skin or Soft Tissue Infection', 'Primary Ovarian Failure'
                                                      ];
                                                    var array = [];
                                                    $( "#fake" ).autocomplete({{
                                                      source: availableTags,
                                                      minLength: 3,
                                                      select: function(e, ui) {{



                                                        document.getElementById("disease").innerHTML = ui.item.value;
                                                    }}
                                                    }});
                                                  }} );
                                                  </script>
                                                  <textarea hidden name="disease" id = "disease"></textarea>
                                <h5 style="margin: 20px; font-size: 17px; margin-top: 5px; font-weight: bold">
                                  Disease:
                                  <span style="float: right; display: inline; font-size: 15px">
                                    <div class="ui-widget" style = "margin-left: 40">
                                          <label for="fake"></label>
                                          <input id="fake">
                                        </div>
                                  </span>
                                </h5>
                                <br>

                                <div style="text-align: center">
                                    <button type="submit" class="btn btn-primary" style="text-align: center">Submit</button>
                                </div>
                              </form>

                        </body>
                    </html>
                '''.format(errors=errors, symptoms = symptoms, array = array, conditions = conditions)

        if disease is not None or disease is not "":
            result = dict(getRankings(disease))


            return '''
                <html>
                <head>
                    <meta charset="utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                    <link href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.css" rel="stylesheet">
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js"></script>
                    <title>DrugRec</title>

                    <style>
                        body,
                      html {{
                        margin: 0;
                        size: 17px;
                        font-family: Avenir;
                        /* position: absolute; */
                      }}
                      .tablink {{
                        margin: 80;
                        background-color: #FF5733;
                        color: black;
                        float: left;
                        border: none;
                        outline: none;
                        cursor: pointer;
                        padding: 14px 16px;
                        font-size: 17px;
                        width: 25%;
                        font-family: Avenir;
                      }}
                    </style>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
                </head>

                    <body style="background-color: #e0ffff">

                        <h2 style="text-align: center; margin-left: 17px;font-weight: 600">
                        Drug Recommendation
                        </h2>
                        <h5 style="margin: 20px; font-size: 17px; font-weight: bold">
                        Age
                        <div id="output-age" style="float: right">{age}</div>
                      </h5>
                <h5 style="margin: 20px; font-size: 17px; font-weight: bold">
                        Gender
                        <div id="output-gender" style="float: right">{gender}</div>
                      </h5>
                <h5 style="margin: 20px; font-size: 17px; font-weight: bold">
                        Condition
                        <div id="output-condition" style="float: right">{disease}</div>
                      </h5>

                      <div><canvas id="myChart" width="650" height="350"></canvas></div>

                          <script>


                            function getKeyByValue(object, value) {{
                                return Object.keys(object).find(key => object[key] === value);
                            }}
                            dict = {result};
                            baked = Object.values(dict);



                            stuff = [];
                            for(var i = 0; i < baked.length; i++){{
                                stuff[i] = getKeyByValue(dict, baked[i]);
                            }}



                            new Chart(document.getElementById("myChart"), {{
                                type: 'horizontalBar',
                                data: {{
                                  labels: stuff,
                                  datasets: [
                                    {{
                                      label: "Percent Match: ",
                                      backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                                      data: baked
                                    }}
                                  ]
                                }},
                                options: {{
                                  legend: {{ display: false }},
                                  title: {{
                                    display: true,
                                    text: 'Treatment Recommendations'
                                  }},
                                  scales: {{
                                    xAxes: [{{
                                        scaleLabel: {{
                                            display: true,
                                            labelString: 'Percent Match (%)'
                                        }},
                                        ticks: {{
                                            beginAtZero: true,
                                            max: 100,
                                            stepSize: 10
                                        }}
                                    }}]
                                  }}
                                }}
                            }});
                          </script>


                    <p><a href="/">Click here to calculate again</a>
                      </div>
                    </body>
                </html>
            '''.format(age = age, gender = gender, disease = disease, result=result)
    return '''
        <html>
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.css" rel="stylesheet">
                <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js"></script>
                <title>DrugRec</title>

                <style>
                    body,
                  html {{
                    margin: 0;
                    size: 17px;
                    font-family: Avenir;
                    /* position: absolute; */
                  }}
                  .tablink {{
                    margin: 80;
                    background-color: #FF5733;
                    color: black;
                    float: left;
                    border: none;
                    outline: none;
                    cursor: pointer;
                    padding: 14px 16px;
                    font-size: 17px;
                    width: 25%;
                    font-family: Avenir;
                  }}
                </style>
            </head>
            <body style="background-color: #e0ffff">
                {errors}


                  <h2 style="text-align: center; font-weight: 600; font-family: Avenir">
                    Drug Recommendation
                  </h2>
                  <br>
                  <br>





                  <form id="input" method="post" action=".">
                    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
                          <link rel="stylesheet" href="/resources/demos/style.css">
                          <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
                          <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
                          <script>

                          $( function() {{
                            var availableTags = [
                                "Upper abdominal pain","Lower abdominal pain","Abscess (Collection of pus)","Alcohol abuse","Anxiety (Nervousness)","Arm ache or pain","Back ache or pain","Bleeding tendency","Blood in vomit","Bloody diarrhea","Pain or soreness of breast","Calf pain","Chest pressure","Chills","Change in behavior","Constipation","Cough","Dark stools","Depressed","Diarrhea","Dizziness","Double vision (Diplopia)","Ear pressure","Pain in the ear","Elbow ache or pain","Eye pain (Irritation)","Facial pain","Fainting","Fever","Fever in the returning traveler","Fever of unknown origin","Flank pain","Frequent urination (Frequency)","Foot pain","Cranky, crying, fussy, irritable child","Groin pain","Delusions or hallucinations","Hand, finger ache or pain","Head injury","Headache","Heel pain","Heat illness","Hip pain","Hives","Hoarse voice","Hypothermia (Low temperature)","Incontinence (leaking urine)","Insect sting","Insomnia (Trouble sleeping)","Skin itching","Joint pain","Kidney pain (Flank pain)","Knee pain","Laceration","Leg ache or pain","Swelling of both legs","Lethargy (Sluggishness)","Mouth pain","Muscle pain","Nail Injury","Nasal bleeding","Nasal injury","Nausea","Neck ache or pain","Neck swelling","Numbness","Obesity","Overdose","Painful urination","Heart pulsations and palpitations","Pelvic pain","Penile discharge","Penis pain","Poisoning","Pregnancy problem","Psychiatric problem","Puncture wound","Rash","Rectal pain","Rectal swelling","Scrotal pain","Scrotal swelling","Seizure","Shortness of breath","Shoulder ache or pain","Sinus pain and pressure","Skin trauma","Snake bite","Sore throat","Speech problem","Spider bite","Substance abuse (Drug abuse)","Suicidal tendencies","Swallowing problem (Dysphagia)","Swelling","Toe pain","Tooth pain","Trauma","Traveler's diarrhea","Unsteady gait (Trouble walking)","Vaginal bleeding","Vaginal bleeding after menopause","Vaginal bleeding during pregnancy","Vaginal discharge","Vaginal itching","Vaginal pain","Vertigo (Room spinning)","Visual problems","Vomiting","General weakness","Weakness (Muscle localized)","Tired","Wrist pain","Throat pain","Tremors","Weight loss, unexplained","Tongue swelling","Inconsolable baby","Wheezing (Noisy breathing)","Swollen lymph nodes (Large lymph nodes)","Failure to thrive","Behavioral problem","Itchy rash (Pruritic rash)","Headache after trauma","Learning difficulties","Blood in urine (Hematuria)","Urinary retention (Inability to urinate)","Liver failure (Cirrhosis)","Choking","Painful rash","Ingestion","Melena (Black stools from blood)","Vomiting coffee ground material","Ringing in ears (Tinnitus)","Mouth ulcers","Mouth swelling","Eye redness","Sneezing","Bleeding gums","Loss of balance","Bleeding in brain","Cyanosis (Blue skin coloration)","Muscle spasm","Drooling","Abdominal swelling (Stomach swelling)","Skin growths","Hand numbness (paresthesias)","Ankle pain","Hemoptysis (Coughing blood)","Jaundice (Yellowing skin)","Night sweats","Flatulence (Passing gas)","Blister (Pocket of fluid)","Hair loss (Baldness)","Jaw pain","Impotence","Heart murmur (Abnormal heart sound)","Pustule (Collection of pus)","Skin pain","Hot skin","Skin swelling","Lip swelling","Eye swelling","Foot swelling","Visual flashing lights","Eye floaters","Amenorrhea (No menstruation)","Blurry vision","Painful gums","Swollen gums","Low blood sugar","Low blood pressure","Darkening of the skin (Hyperpigmentation)","Low heart rate","Foot itching","Hot flashes","Infertility (Female)","Increased facial hair","Arm swelling","Calf swelling","Ear swelling","Wrist swelling","Maroon stools","Arm cut (laceration)","Hand cut (laceration)","Leg cut (laceration)","Foot cut (laceration)","Arm itching","Hand redness","Foot redness","Arm redness","Leg redness","Hand itching","Leg itching","Steatorrhea (Excess fat in stool)","Upper leg pain","Armpit pain","Sweating","Nasal congestion","Joint stiffness","Skin sores","Chest burning","Memory loss","Arm numbness (paresthesias)","Leg numbness (paresthesias)","Foot numbness (paresthesias)","Face numbness (paresthesias)","Dementia","Facial droop (weakness)","Limping in a child","Increased thirst","Increased urination (polyuria)","Shin pain","Stings","Sleep disorders","Drooping eyelid (Ptosis)","Snoring","Dry skin","Itchy eyes","Elbow swelling","Chest pain","Skin infection","Stomach and abdominal pain","Anger","Hurts to breathe","Difficulty breathing","Pulling at ears","Skin bumps","Congestion in chest or lungs","Discharge from ear","Low back ache or pain","Unusual color or odor of urine","Penis inflammation or swelling","Excessive appetite","Retaining fluid","Lump or mass of breast","Neck stiffness or tightness","Agitated","Confusion","Headache and weakness","Confusion and headache","Nipple discharge","Shoulder stiffness or tightness","Arm stiffness or tightness","High blood pressure","High blood sugar"
                              ];
                            var array = [];
                            var arr = [];
                            $( "#symptoms" ).autocomplete({{
                                          source: availableTags,
                                          minLength: 3,
                                          select: function(e, ui) {{
                                                arr.push(" " + ui.item.value);
                                                array.push(ui.item.value);
                                                document.getElementById("disp").innerHTML = "Symptoms:" + arr.join();
                                                document.getElementById("smp").innerHTML = array.join();

                                            }}

                                        }});
                                      }} );
                                      </script>

                                      <div class="ui-widget">
                                          <label for="symptoms" style = "margin: 20px; font-size: 17px; font-weight: bold; font-family: Avenir">Enter Symptoms: </label>
                                          <input id="symptoms" style="float: right; display: inline; font-size: 15px">
                                        </div>
                                    <p name = "disp" id = "disp" style = "text-align: center">Symptoms:</p>
                                    <textarea name="smp" id = "smp" style = "text-align: center; display:none;"></textarea>

                                  <div style="text-align: center">
                                        <button type="submit" class="btn btn-primary" style="text-align: center" >Get Diseases</button>

                                    </div>
                    <h5 style="margin: 20px; font-size: 17px; font-weight: bold";>
                      Age:
                      <span style="float: right; display: inline; font-size: 15px">
                        <input
                          name="age"
                          type="number"
                          pattern="\d*"
                          autocomplete="off"
                          style="width: 40px"
                        />
                      </span>
                    </h5>
                    <h5 style="margin: 20px; font-size: 17px; font-weight: bold">
                      Gender:
                      <select name="gender" id="gender" style="float: right; display: inline; width: 100px; background: white; font-size: 15px">
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                          </select>
                    </h5>
                    <script>

                                      $( function() {{
                                        var availableTags = [
                                            'Diabetes Insipidus', 'Cold Symptoms', 'Herpes Simplex, Suppression', 'Angina', 'Bladder Infection', 'Constipation, Chronic', 'Endoscopy or Radiology Premedication', 'Nausea/Vomiting of Pregnancy', 'Gastroparesis', 'Osteoarthritis', 'Plaque Psoriasis', 'Hypogonadism, Male', 'Actinic Keratosis', 'Light Anesthesia', 'Hypersomnia', 'Osteolytic Bone Metastases of Solid Tumors', 'Agitated State', 'Hemorrhoids', "Tourette's Syndrome", 'Chronic Myelogenous Leukemia', 'Acne', 'Uveitis', 'Alopecia', 'ADHD', 'Biliary Cirrhosis', 'Light Sedation', 'Glaucoma, Open Angle', 'Menorrhagia', 'Vitamin D Deficiency', 'Systemic Lupus Erythematosus', 'Tonsillitis/Pharyngitis', 'Hypoestrogenism', 'Basal Cell Carcinoma', 'Tinea Versicol', 'Chlamydia Infection', "Alzheimer's Disease", 'Bacterial Skin Infection', 'Atrial Fibrillation', 'Cold Sores', 'Burns, External', 'Prevention of Thromboembolism in Atrial Fibrillation', 'Borderline Personality Disorder', 'Osteoporosis', 'Malaria Prevention', 'Ulcerative Colitis', 'Eye Redness', 'Epilepsy', 'Allergic Reactions', 'Cancer', 'Allergic Rhinitis', 'Opiate Dependence', 'Human Papillomavirus Prophylaxis', 'Hypertensive Emergency', 'Dermatitis', 'Status Epilepticus', 'Birth Control', 'Sarcoidosis', 'Insomnia', 'Malaria', 'Onychomycosis, Toenail', 'Asthma, acute', 'Constipation, Drug Induced', 'Stomach Ulce', 'Asthma', 'Bowel Preparation', 'Cough and Nasal Congestion', 'Rosacea', 'Nocturnal Leg Cramps', 'Extrapyramidal Reaction', 'Benign Essential Trem', 'Labor Pain', 'Sexual Dysfunction, SSRI Induced', 'Abnormal Uterine Bleeding', 'Surgical Prophylaxis', 'Cerebral Spasticity', 'Pseudotumor Cerebri', 'Anxiety and Stress', 'Ovarian Cysts', 'Asperger Syndrome', 'Migraine Prevention', 'Fatigue', 'HIV Infection', 'Candida Urinary Tract Infection', 'Bronchiectasis', 'Hyperhidrosis', 'Sore Throat', 'Undifferentiated Connective Tissue Disease', 'Eye Redness/Itching', 'Allergies', 'Swine Flu', 'Erosive Esophagitis', 'Nausea/Vomiting, Postoperative', 'Benign Prostatic Hyperplasia', 'Autism', 'Anxiety', 'Migraine', 'Atrial Flutte', 'Pneumococcal Disease Prophylaxis', 'Impetig', 'Edema', 'High Blood Pressure', 'Indigestion', 'Panic Disorder', 'Bronchitis', "Crohn's Disease", 'Diaper Rash', 'Conjunctivitis, Allergic', 'Androgenetic Alopecia', 'Eczema', 'Shift Work Sleep Disorder', 'Back Pain', 'Reversal of Opioid Sedation', 'Headache', 'Peripheral Neuropathy', 'COPD, Maintenance', 'Diverticulitis', 'Pain', 'Herbal Supplementation', 'Colorectal Cancer', 'Narcolepsy', 'Menstrual Disorders', 'Tinea Corporis', 'Multiple Myeloma', 'Dietary Supplementation', "Sjogren's Syndrome", 'Prostate Cancer', 'Premenstrual Dysphoric Disorder', 'Chronic Idiopathic Constipation', 'Facial Wrinkles', 'Postoperative Pain', 'Tendonitis', 'Lipodystrophy', 'Prevention of Hypokalemia', 'Kidney Infections', 'Seasonal Allergic Conjunctivitis', 'Sinus Symptoms', 'Atopic Dermatitis', 'Endometrial Hyperplasia, Prophylaxis', 'Pupillary Dilation', 'Folic Acid Deficiency', 'Dermatitis Herpetiformis', 'Keratoconjunctivitis Sicca', 'Hypothyroidism, After Thyroid Removal', 'Mitral Valve Prolapse', 'High Cholesterol', 'Opiate Withdrawal', 'Pulmonary Embolism, Recurrent Event', 'Bacterial Vaginitis', 'Tinnitus', 'Emergency Contraception', 'Inflammatory Conditions', 'Urinary Retention', 'Oral Thrush', 'Supraventricular Tachycardia', 'Social Anxiety Disorder', 'Reflex Sympathetic Dystrophy Syndrome', 'Vulvodynia', 'Diabetes, Type 1', 'Sinusitis', 'Xerostomia', 'Acute Lymphoblastic Leukemia', 'Thyroid Suppression Test', 'Hypertriglyceridemia', 'Formoterol', 'Lyme Disease', 'Nasal Polyps', "Crohn's Disease, Maintenance", 'Pharyngitis', 'Opioid Overdose', 'Bipolar Disorder', 'Restless Legs Syndrome', 'Hemangioma', 'Spondyloarthritis', 'Cataplexy', 'Trichotillomania', 'Diabetes, Type 2', 'Opiate Adjunct', 'Immunosuppression', 'New Daily Persistent Headache', 'Computed Tomography', 'Obstructive Sleep Apnea/Hypopnea Syndrome', 'Weight Loss', 'Cluster Headaches', 'Hereditary Angioedema', 'Metformin / sitagliptin', 'Pneumonia', 'Dental Abscess', 'Angina Pectoris Prophylaxis', 'Strep Throat', 'Dystonia', 'Seizure Prevention', 'Binge Eating Disorder', 'Breast Cancer, Metastatic', 'Ankylosing Spondylitis', 'Cough', 'Rhinitis', 'Opioid-Induced Constipation', 'Ulcerative Colitis, Active', 'Schistosoma japonicum', 'Anaplastic Oligodendroglioma', "Parkinson's Disease", 'Pruritus', 'Otitis Media', 'Constipation', "Barrett's Esophagus", 'COPD', 'Influenza Prophylaxis', 'Nausea/Vomiting', 'Trichomoniasis', 'Mucositis', 'Non-Small Cell Lung Cancer', 'Left Ventricular Dysfunction', 'Period Pain', 'Bacterial Endocarditis Prevention', 'Diarrhea', 'Hirsutism', 'Breast Cancer, Adjuvant', 'Temporomandibular Joint Disorder', 'Breast Cancer', 'Hyperprolactinemia', 'Periodic Limb Movement Disorder', 'Perimenopausal Symptoms', 'Dermatomyositis', 'Muscle Pain', 'Keratosis', 'Warts', 'TSH Suppression', 'Psoriatic Arthritis', 'Premature Ventricular Depolarizations', 'Interstitial Cystitis', 'Neuropathic Pain', 'Helicobacter Pylori Infection', 'Clostridial Infection', 'Vaginal Yeast Infection', 'Dysuria', 'Schizophrenia', 'Psoriasis', 'Anorexia', 'Uterine Fibroids', 'Polycystic Ovary Syndrome', "Addison's Disease", 'Female Infertility', 'Chronic Pain', 'Asthma, Maintenance', 'Hyperthyroidism', 'Seizures', 'Myasthenia Gravis', 'Obesity', 'Fibromyalgia', 'Heart Attack', 'High Cholesterol, Familial Homozygous', 'Burning Mouth Syndrome', 'Sedation', 'Influenza', 'Renal Cell Carcinoma', 'Urticaria', 'Skin Rash', 'Nausea/Vomiting, Chemotherapy Induced', 'Post Traumatic Stress Disorder', 'Hyperlipoproteinemia', 'Prevention of Dental Caries', 'Deep Vein Thrombosis, First Event', 'Breakthrough Pain', 'Spondylolisthesis', 'Head Lice', 'Vitamin/Mineral Supplementation during Pregnancy/Lactation', 'Dysautonomia', 'Ophthalmic Surgery', 'Obsessive Compulsive Disorder', 'Hepatitis C', 'Paranoid Disorder', 'Primary Immunodeficiency Syndrome', 'Skin and Structure Infection', 'Herpes Simplex', 'Condylomata Acuminata', 'Dry Skin', "Hashimoto's disease", 'Postpartum Depression', 'Lennox-Gastaut Syndrome', 'Heart Failure', 'Bacterial Infection', 'Amenorrhea', 'Systemic Mastocytosis', 'Chronic Fatigue Syndrome', 'Schizoaffective Disorder', 'Anesthesia', 'Alcohol Dependence', 'Streptococcal Infection', 'Hot Flashes', 'Night Terrors', 'Generalized Anxiety Disorder', 'Sciatica', 'Muscle Twitching', 'Pulmonary Embolism', 'Neutropenia Associated with Chemotherapy', 'Nasal Congestion', 'Progesterone Insufficiency', "Behcet's Disease", 'Seborrheic Dermatitis', 'Carcinoid Tum', 'moterol / mometasone)', 'NSAID-Induced Ulcer Prophylaxis', 'Trigeminal Neuralgia', 'Constipation, Acute', 'Smoking Cessation', 'Urinary Tract Infection', 'Gout', 'Upper Respiratory Tract Infection', 'Avian Influenza', 'Pseudobulbar Affect', 'Erectile Dysfunction', 'GERD', 'Bursitis', 'Irritable Bowel Syndrome', 'Depression', 'Endometriosis', 'Conjunctivitis, Bacterial', 'Women (oxybutynin)', 'Deep Vein Thrombosis', 'High Cholesterol, Familial Heterozygous', 'Methicillin-Resistant Staphylococcus Aureus Infection', 'Gout, Acute', 'Glioblastoma Multiforme', 'Underactive Thyroid', 'Hepatitis B', 'Multiple Sclerosis', 'Urinary Tract Stones', 'Overactive Bladder', 'Major Depressive Disorder', 'Vertig', 'Glaucoma', "Non-Hodgkin's Lymphoma", 'Psychosis', 'Dry Eye Disease', 'Atrophic Vaginitis', 'Postmenopausal Symptoms', 'Arrhythmia', 'Pulmonary Hypertension', 'Giardiasis', 'Performance Anxiety', "Raynaud's Syndrome", 'Alcohol Withdrawal', 'Anemia, Sickle Cell', 'Urinary Incontinence', 'Not Listed / Othe', 'Diabetic Peripheral Neuropathy', 'Pain/Feve', 'Mania', 'Adult Human Growth Hormone Deficiency', 'Hypokalemia', 'Bulimia', 'Diarrhea, Chronic', 'Muscle Spasm', 'Melanoma, Metastatic', 'Rheumatoid Arthritis', 'Prostatitis', 'Juvenile Idiopathic Arthritis', 'Motion Sickness', 'Skin or Soft Tissue Infection', 'Primary Ovarian Failure'
                                          ];
                                        var array = [];
                                        $( "#fake" ).autocomplete({{
                                          source: availableTags,
                                          minLength: 3,
                                          select: function(e, ui) {{



                                            document.getElementById("disease").innerHTML = ui.item.value;
                                        }}
                                        }});
                                      }} );
                                      </script>
                                      <textarea hidden name="disease" id = "disease"></textarea>
                    <h5 style="margin: 20px; font-size: 17px; margin-top: 5px; font-weight: bold">
                      Condition:
                      <span style="float: right; display: inline; font-size: 15px">
                        <div class="ui-widget" style = "margin-left: 40">
                              <label for="fake"></label>
                              <input id="fake">
                            </div>
                      </span>
                    </h5>
                    <br>

                    <div style="text-align: center">
                        <button type="submit" class="btn btn-primary" style="text-align: center">Submit</button>
                    </div>
                  </form>

            </body>
        </html>
    '''.format(errors=errors)
