# -*- coding: utf-8 -*-

import calendar
import numpy as np

#  Change these values to generate a new course schedule
year = 2025
# Format is [month, day]
start = [8, 27]
end = [12, 7]

# 0-M, 1-T, 2-W, 3-R, 4-F, 5-S, 6-S
Days = [0, 1, 2, 4]

# Format is (month, day): 'Holiday Name'
# Fall Holidays
Holidays = {
     (9, 1): "Labor Day",
     (10, 13): "Fall Break",
     (10, 14): "Fall Break",
     (11, 24): "Thanksgiving Break",
     (11, 25): "Thanksgiving Break",
     (11, 26): "Thanksgiving Break",
     (11, 27): "Thanksgiving Break",
     (11, 28): "Thanksgiving Break",
 }
# Summer Holidays
# Holidays = {(7, 3): '\\nth{4} July',
#             (7, 24): "\\nth{24} July"
#             }
# Spring Holidays
# Holidays = {
#     (1, 16): "Martin Luther King Day",
#     (2, 20): "President's Day",
#     (2, 27): "Spring Break",
#     (2, 28): "Spring Break",
#     (3, 1): "Spring Break",
#     (3, 2): "Spring Break",
#     (3, 3): "Spring Break",
#     (3, 28): "Festival of Excellence",
# }

# Format is ['title', 'chapter', length] for topics
# Format is ['Exam #'] for midterm exams
Topics = [['Chemistry in Context', '1.1', 0.75],
          ['Phases and Classification of Matter', '1.2', 0.75],
          ['Physical and Chemical Properties', '1.3', 0.75],
          ['Measurements', '1.4', 0.75],
          ['Measurement Uncertainty, Accuracy, and Precision', '1.5', 0.75],
          ['Mathematical Treatment of Measurement Results', '1.6', 0.75],
          ['Early Ideas in Atomic Theory', '2.1', 0.75],
          ['Evolution of Atomic Theory', '2.2', 0.75],
          ['Atomic Structure and Symbolism', '2.3', 0.75],
          ['Chemical Formulas', '2.4', 0.75],
          ['The Periodic Table', '2.5', 0.75],
          ['Ionic and Molecular Compounds', '2.6', 0.75],
          ['Chemical Nomenclature', '2.7', 0.75],
          ['Catch-up/Review Day for Exam 1: Chapters 1 and 2'],
          ['Formula Mass and the Mole Concept', '3.1', 0.75],
          ['Determining Empirical and Molecular Formulas', '3.2', 0.75],
          ['Molarity', '3.3', 0.75],
          ['Other Units for Solution Concentration', '3.4', 0.75],
          ['Writing and Balancing Chemical Equations', '4.1', 0.75],
          ['Classifying Chemical Reactions', '4.2', 0.75],
          ['Reaction Stoichiometry', '4.3', 0.75],
          ['Reaction Yields', '4.4', 0.75],
          ['Quantitative Chemical Analysis', '4.5', 0.75],
          ['Catch-up/Review Day for Exam 2: Chapters 3 and 4'],
          ['Energy Basics', '5.1', 0.75],
          ['Calorimetry', '5.2', 0.75],
          ['Enthalpy', '5.3', 0.75],
          ['Electromagnetic Energy', '6.1', 0.75],
          ['The Bohr Model', '6.2', 0.75],
          ['Development of Quantum Theory', '6.3', 0.75],
          ['Electronic Structure of Atoms (Electron Configurations)', '6.4', 0.75],
          ['Periodic Variations in Element Properties', '6.5', 0.75],
          ['Catch-up/Review Day for Exam 3: Chapters 5 and 6'],
          ['Ionic Bonding', '7.1', 0.75],
          ['Covalent Bonding', '7.2', 0.75],
          ['Lewis Symbols and Structures', '7.3', 0.75],
          ['Formal Charges and Resonance', '7.4', 0.75],
          ['Strengths of Ionic and Covalent Bonds', '7.5', 0.75],
          ['Molecular Structure and Polarity', '7.6', 0.75],
          ['Valence Bond Theory', '8.1', 0.75],
          ['Hybrid Atomic Orbitals', '8.2', 0.75],
          ['Multiple Bonds', '8.3', 0.75],
          ['Molecular Orbital Theory', '8.4', 0.75],
          ['Gas Pressure', '9.1', 0.75],
          ['Relating Pressure, etc.: The Ideal Gas Law', '9.2', 0.75],
          ['Stoichiometry of Gaseous Substances, etc.', '9.3', 0.75],
          ['Effusion and Diffusion of Gases', '9.4', 0.75],
          ['The Kinetic-Molecular Theory', '9.5', 0.75],
          ['Non-Ideal Gas Behavior', '9.6', 0.75],
          ['Catch-up/Review Day for Exam 4: Chapters 7--9'],
          ['Intermolecular Forces', '10.1', 0.75]]

Day_Letters = ['M', 'T', 'W', 'R', 'F', 'S', 'S']
#%%
Class_Days = []
Total_Days = 0
for month in range(start[0], end[0] + 1):
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if month is start[0] and max(week) < start[1]:
            pass
        elif month is end[0] and week[0] > end[1]:
            pass
        elif (0 not in week) or (week[-1] == 0):
            Class_Days.append('New Week')
        for day, date in enumerate(week):
            if month is start[0] and date < start[1]:
                pass
            elif month is end[0] and date > end[1]:
                pass
            elif day not in Days:
                pass
            elif date == 0:
                pass
            elif (month, date) not in Holidays:
                today = '{}, {}. {}'.format(Day_Letters[day],
                                            calendar.month_abbr[month],
                                            date)
                Class_Days.append(today)
                Total_Days += 1
            else:
                today = '{}, {}. {}'.format(Day_Letters[day],
                                            calendar.month_abbr[month],
                                            date)
                Class_Days.append([today, Holidays[(month, date)]])

shortfall = len(Topics) - Total_Days
print('Shortfall is {}'.format(shortfall))
#%%
combined_times = np.ones(len(Topics))*5
for i in range(len(Topics)-1):
    try:
        combined_times[i] = Topics[i][2] + Topics[i+1][2]
    except:
        pass
#%%
combined_indexes = []
i = 0
j = 0
while i < len(combined_times) and j < shortfall:
    if combined_times[i] < 1.75:
        answer = input('Combine {} with {}?'.format(Topics[i][0], Topics[i+1][0]))
        if answer == 'y':
            combined_indexes.append(i)
            i += 2
            j += 1
        else:
            i += 1
    else:
        i += 1
print('Made up {} of the shortfall of {}.'.format(j, shortfall))
#%%
schedule = '\\begin{tabular}{rcccc}\n\
& Date && Topic & Chapter\\\\\n'
topic_num = 0
week_num = 1
day_num = 0
while day_num < len(Class_Days):
    if Class_Days[day_num] == 'New Week':
        schedule = schedule + '\\midrule\nWeek {} '.format(week_num)
        week_num += 1
        day_num += 1
    if len(Class_Days[day_num]) == 2:
        schedule = schedule + '& {}'.format(Class_Days[day_num][0])
        schedule = schedule + '& \\multicolumn{{3}}{{l}}{{\\textbf{{{} - No Class!}}}}\\\\\n'.format(Class_Days[day_num][1])
    elif topic_num in combined_indexes:
        schedule = schedule + '& \\multirow{{2}}{{*}}{{{}}}'.format(Class_Days[day_num])
        schedule = schedule + '& & {} & {}\\\\\n'.format(Topics[topic_num][0], Topics[topic_num][1])
        topic_num += 1
        schedule = schedule + '& & & {} & {}\\\\\n'.format(Topics[topic_num][0], Topics[topic_num][1])
        topic_num += 1
    elif len(Topics[topic_num]) > 1:
        schedule = schedule + '& {}'.format(Class_Days[day_num])
        schedule = schedule + '&& {} & {}\\\\\n'.format(Topics[topic_num][0], Topics[topic_num][1])
        topic_num += 1
    else:
        schedule = schedule + '& {}'.format(Class_Days[day_num])
        schedule = schedule + '& \\multicolumn{{3}}{{l}}{{\\textbf{{{}}}}}\\\\\n'.format(Topics[topic_num][0])
        topic_num +=1
    day_num += 1
schedule = schedule + '\\midrule\n\\midrule\n'
schedule = schedule + 'Finals Week & X, XXX. X & \\multicolumn{3}{l}{\\textbf{Final Exam} ~ X:00-X:50 ~ Bring a pencil and a scantron sheet}\\\\\n'
schedule = schedule + '\\end{tabular}'
print('Here is your schedule')
print('---------------------')
print(schedule)
with open('schedule.tex', 'w') as f:
    f.write(schedule)

# Other classes' Topics
#1210 #BLMB?
Topics = [['The Study of Chemistry', '1.1', 0.5],
          ['Classifications of Matter', '1.2', 0.5],
          ['Properties of Matter', '1.3', 0.75],
          ['Units of Measure', '1.4', 0.75],
          ['Uncertainty in Measurement', '1.5', 0.75],
          ['Dimensional Analysis', '1.6', 1],
          ['The Atomic Theory of Matter', '2.1', 0.3],
          ['The Discovery of Atomic Structure', '2.2', 0.3],
          ['The Modern View of Atomic Structure', '2.3', 0.3],
          ['Atomic Weights', '2.4', 0.3],
          ['The Periodic Table', '2.5', 0.3],
          ['Molecules and Molecular Compounds', '2.6', 0.3],
          ['Ions and Ionic Compounds', '2.7', 0.3],
          ['Naming Inorganic Compounds', '2.8', 0.3],
          ['Some Simple Organic Compounds', '2.9', 0.3],
          ['Midterm Exam 1 (Ch. 1--2)'],
          ['Chemical Equations', '3.1', 0.3],
          ['Some Simple Patterns of Chemical Reactivity', '3.2', 0.3],
          ['Formula Weights', '3.3', 0.5],
          ["Avogadro's Number and the Mole", '3.4', 0.5],
          ['Empirical Formulas from Analyses', '3.5', 0.5],
          ['Quantitative Information from Balanced Equations', '3.6', 0.5],
          ['Limiting Reactants', '3.7', 1],
          ['General Properties of Aqueous Solutions', '4.1', 0.75],
          ['Precipitation Reactions', '4.2', 0.75],
          ['Acids, Bases, and Neutralization Reactions', '4.3', 0.75],
          ['Oxidation-Reduction Reactions', '4.4', 1],
          ['Concentrations of Solutions', '4.5', 0.75],
          ['Solution Stoichiometry and Chemical Analysis', '4.6', 1],
          ['The Nature of Energy', '5.1', 0.5],
          ['The First Law of Thermodynamics', '5.2', 0.75],
          ['Enthalpy', '5.3', 0.75],
          ['Enthalpies of Reaction', '5.4', 0.75],
          ['Calorimetry', '5.5', 1],
          ["Hess's Law", "5.6", 1],
          ['Enthalpies of Formation', '5.7', 0.75],
          ['Foods and Fuels', '5.8', 0.75],
          ['Midterm Exam 2 (Ch. 3--5)'],
          ['The Wave Nature of Light', '6.1', 0.5],
          ['Quantized Energy and Photons', '6.2', 0.5],
          ['Line Spectra and the Bohr Model', '6.3', 0.75],
          ['The Wave Behavior of Matter', '6.4', 0.75],
          ['Quantum Mechanics and Atomic Orbitals', '6.5', 0.75],
          ['Representations of Orbitals', '6.6', 0.5],
          ['Many-Electron Atoms', '6.7', 0.5],
          ['Electron Configurations', '6.8', 0.5],
          ['Electron Configurations and the Periodic Table', '6.9', 0.5],
          ['Development of the Periodic Table', '7.1', 0.5],
          ['Effective Nuclear Charge', '7.2', 0.5],
          ['Sizes of Atoms and Ions', '7.3', 0.3],
          ['Ionization Energy', '7.4', 0.3],
          ['Electron Affinities', '7.5', 0.3],
          ['Metals, Nonmetals, and Metalloids', '7.6', 0.5],
          ['Trends for Groups 1A and 2A Metals', '7.7', 0.5],
          ['Trends for Selected Nonmetals', '7.8', 0.3],
          ['Lewis Symbols and the Octet Rule', '8.1', 0.75],
          ['Ionic Bonding', '8.2', 1],
          ['Covalent Bonding', '8.3', 1],
          ['Bond Polarity and Electronegativity', '8.4', 0.75],
          ['Drawing Lewis Structures', '8.5', 0.75],
          ['Resonance Structures', '8.6', 1],
          ['Exceptions to the Octet Rule', '8.7', 0.5],
          ['Strengths of Covalent Bonds', '8.8', 0.5],
          ['Midterm Exam 3 (Ch. 6--8)'],
          ['Molecular Shapes', '9.1', 0.75],
          ['The VSEPR Model', '9.2', 0.75],
          ['Molecular Shape and Molecular Polarity', '9.3', 0.75],
          ['Covalent Bonding and Orbital Overlap', '9.4', 1],
          ['Hybrid Orbitals', '9.5', 1],
          ['Multiple Bonds', '9.6', 1],
          ['Molecular Orbitals', '9.7', 1],
          ['Period 2 Diatomic Molecules', '9.8', 1],
          ['Characteristics of Gases', '10.1', 0.5],
          ['Pressure', '10.2', 0.5],
          ['The Gas Laws', '10.3', 0.75],
          ['The Ideal Gas Equation', '10.4', 0.75],
          ['Further Applicaions of the Ideal Gas Equation', '10.5', 0.75],
          ['Gas Mixtures and Partial Pressures', '10.6', 0.5],
          ['The Kinetic Molecular Theory of Gases', '10.7', 0.75],
          ['Molecular Effusion and Diffusion', '10.8', 0.75],
          ['Real Gases: Deviations from Ideal Behavior', '10.9', 0.75],
          ['A Molecular Comparison of Gases, Liquids, and Solids', '11.1', 0.75],
          ['Intermolecular Forces', '11.2', 1],
          ['Midterm Exam 4 (Ch. 9--11)'],]
          
# IGC
Topics = [['Classification and Properties of Matter and Energy', '1.1-1.3', 0.5],
          ['The Scientific Method', '1.4', 0.75],
          ['Units and Significang Digits', '1.5-1.6', 0.75],
          ['Dimensional Analysis, Density, and Temperature', '1.7-1.9',1],
          ['Chemical Symbols and Chemical Combination', '2.1-2.2', 0.3],
          ['The History of the Atom and Atomic Structure', '2.3-2.4', 0.3],
          ['Atomic Masses and the Periodic Table', '2.5-2.6', 0.3],
          ['Formulas and Names -- Binary Covalent Compounds', '3.1-3.2', 0.3],
          ['Formulas and Names -- Ionic Compounds', '3.3-3.4', 0.5],
          ['Naming Acids and Nomenclature Review', '3.5-3.6', 0.5],
          ['The Mole and Molar Mass', '3.7-3.8', 1],
          ['Percent Composition and Empirical Formulas', '3.9-3.10', 1],
          ['Molecular Formulas and Combustion Analysis', '3.11-3.12', 1],
          ['Chemical Equations and Reactions', '4.1-4.2', 0.75],
          ['Compounds in Aqueous Solution and Precipitation Reactions', '4.3-4.4', 0.75],
          ['Acid-Base Reactions', '4.5', 0.75],
          ['Oxidation States and Reox Reactions', '4.6-4.7', 1],
          ['Calculations for Chemical Reactions', '5.1-5.2', 0.5],
          ['Limiting Quantities and Yields', '5.3-5.4', 0.75],
          ['Definition and Uses of Molarity', '5.5-5.6', 1],
          ['Calculations Involving Other Quantities', '5.7', 0.75],
          ['Calculations with Net Ionic Equations', '5.8', 0.75],
          ['Titration', '5.9', 1],
          ['Energy, Heat, and Work', '6.1-6.3', 0.5],
          ['Enthalpy and Specific Heat', '6.4-6.5', 0.75],
          ['Calorimetry: Measuring Energy Changes', '6.6', 0.5],
          ['Enthalpy in Chemical Reactions', '6.7', 0.5],
          ['Standard Enthalpies of Formation', '6.8', 0.5],
          ['Gas Pressure and Simple Gas Laws', '7.1-7.3', 0.5],
          ['The Combined Gas Law and the Ideal Gas Law', '7.4-7.6', 0.3],
          ['Partial Pressures, Molar Mass, and Density of gases', '7.7-7.8', 0.3],
          ['Gas Reactions and the Kinetic Molecular Theory', '7.9-7.10', 0.3],
          ['Movement of Gas Particles', '7.11', 0.3],
          ['Behavior of Real Gases', '7.12', 0.3],
          ['Light and the Bohr Model of the Atom', '8.1-8.2', 0.75],
          ['Electron Shells, Subshells, and Orbitals', '8.3', 1],
          ['Energy-Level Diagrams and Electron Configurations', '8.4-8.5', 0.75],
          ['Quantum Numbers', '8.6', 1],
          ['Valence Electrons and Atomic/Ionic Sizes', '9.1-9.2', 0.75],
          ['Ionization Energy and Electron Affinity', '9.3', 0.75],
          ['Ionic Bonding and Lattice Energy', '9.4-9.5', 1],       
          ['Formation of Covalent Bonds', '10.1', 0.5],
          ['Lewis Structures', '10.2', 0.5],
          ['Resonance and Formal Charges', '10.3', 0.75],
          ['Exceptions to the Octet Rule', '10.4', 0.75],
          ['Polar Bonds and Bond Enthalpy', '10.5-10.6', 0.75],
          ['VSEPR and Molecular Geometry', '11.1', 0.75],
          ['Polar and Nonpolar Molecules', '11.2', 0.75],
          ['Valence Bond Theory', '11.3', 0.75],
          ['Using Valence Bond Theory', '11.4', 0.75],
          ['Molecular Orbital Theory', '11.5', 1]]

Topics = [[' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75]]
