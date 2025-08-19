class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_content_item(self, content_item):
        new_node = Node(content_item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search_content_item(self, name):
        current = self.head
        while current is not None:
            if current.data.name == name:
                return current.data
            current = current.next
        return None

    def display_content_items(self):
        current = self.head
        while current is not None:
            print(current.data.name)
            current = current.next

class Node_N:
    def __init__(self, data):
        self.data = data
        self.children = []

class NaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, parent_data, child_data):
        if self.root is None:
            self.root = Node_N(parent_data)
            self.root.children.append(Node_N(child_data))
        else:
            self._add_node(self.root, parent_data, child_data)

    def _add_node(self, node, parent_data, child_data):
        if node.data == parent_data:
            node.children.append(Node_N(child_data))
        else:
            for child in node.children:
                self._add_node(child, parent_data, child_data)

class ContentItem:
    def __init__(self, name, textbooks, links):
        self.name = name
        self.textbooks = textbooks
        self.links = links

class RecommendationSystem:
    def __init__(self):
        self.category_tree = NaryTree()
        self.content_list = DoublyLinkedList()

    def add_category(self, parent_category, child_category):
        self.category_tree.add_node(parent_category, child_category)

    def add_content_item(self, name, textbooks, links):
        content_item = ContentItem(name, textbooks, links)
        self.content_list.add_content_item(content_item)

    def recommend_content(self, user_input, grade_input, subject_input):
    # Traverse the category tree to find the relevant content items
        self._traverse_category_tree(user_input, grade_input, subject_input)

    def _traverse_category_tree(self, user_input, grade_input, subject_input):
        if user_input == "High School":
            if grade_input == "10th" and subject_input == "Mathematics":
                self._recommend_content_items(["Algebra Textbook", "Calculus Textbook", "Linear Algebra Textbook"])
            elif grade_input == "10th" and subject_input == "Physics":
                self._recommend_content_items(["Physics Textbook", "Differential Equations Textbook"])
        elif user_input == "Intermediate":
            if grade_input == "Plus 1" and subject_input == "Mathematics":
                self._recommend_content_items(["Calculus Textbook", "Linear Algebra Textbook"])
            elif grade_input == "Plus 2" and subject_input == "Mathematics":
                self._recommend_content_items(["Differential Equations Textbook"])
        elif user_input == "UG":
            if grade_input == "1":
                if subject_input == "CSE":
                    self._recommend_content_items(["CAD", "System Essentials"])
                elif subject_input == "Mechanical":
                    self._recommend_content_items(["Single Variable Calculus", "Electrical & Electronic Circuits"])
                elif subject_input == "ECE":
                    self._recommend_content_items(["Basic Electrical and Electronics Engineering", "Electronic Devices and Circuits"])
            elif grade_input == "2" and subject_input == "CSE":
                self._recommend_content_items(["Advanced programming", "DATA STRUCTURES AND ALGORITHMS"])

    def _recommend_content_items(self, content_names):
        for name in content_names:
            content_item = self.search_content_by_name(name)
            if content_item:
                print(f"Name: {content_item.name}")
                print(f"Textbooks: {', '.join(content_item.textbooks)}")
                print(f"Links: {', '.join(content_item.links)}")
            else:
                print(f"No content found for '{name}'.")
    
    def search_content_by_key(self, key):
        matching_items = []

        current = self.content_list.head
        while current is not None:
            if key.lower() in current.data.name.lower():
                matching_items.append(current.data)
            current = current.next

        if matching_items:
            print("Matching content item(s) found:")
            for i, item in enumerate(matching_items, start=1):
                print(f"{i}. Name: {item.name}")
                print(f"   Textbooks: {', '.join(item.textbooks)}")
                print(f"   Links: {', '.join(item.links)}")
                print()
        else:
            print("No matching content item found.")


    def display_all_content(self):
        self.content_list.display_content_items()

    def search_content_by_name(self, name):
        return self.content_list.search_content_item(name)


# Example usage
recommendation_system = RecommendationSystem()

# Add categories
recommendation_system.add_category("High School", "8th Grade")
recommendation_system.add_category("High School", "9th Grade")
recommendation_system.add_category("High School", "10th Grade")
recommendation_system.add_category("8th Grade", "Mathematics")
recommendation_system.add_category("8th Grade", "Physics")
recommendation_system.add_category("8th Grade", "Chemistry")
recommendation_system.add_category("8th Grade", "Biology")
recommendation_system.add_category("8th Grade", "Social Studies")
recommendation_system.add_category("8th Grade", "English")
recommendation_system.add_category("9th Grade", "Mathematics")
recommendation_system.add_category("9th Grade", "Physics")
recommendation_system.add_category("9th Grade", "Chemistry")
recommendation_system.add_category("9th Grade", "Biology")
recommendation_system.add_category("9th Grade", "Social Studies")
recommendation_system.add_category("9th Grade", "English")
recommendation_system.add_category("10th Grade", "Mathematics")
recommendation_system.add_category("10th Grade", "Physics")
recommendation_system.add_category("10th Grade", "Chemistry")
recommendation_system.add_category("10th Grade", "Biology")
recommendation_system.add_category("10th Grade", "Social Studies")
recommendation_system.add_category("10th Grade", "English")
recommendation_system.add_category("Intermediate", "Plus 1")
recommendation_system.add_category("Intermediate", "Plus 2")
recommendation_system.add_category("Plus 1", "Mathematics")
recommendation_system.add_category("Plus 1", "Physics")
recommendation_system.add_category("Plus 1", "Chemistry")
recommendation_system.add_category("Plus 2", "Mathematics")
recommendation_system.add_category("Plus 2", "Physics")
recommendation_system.add_category("Plus 2", "Chemistry")
recommendation_system.add_category("UG", "CSE")
recommendation_system.add_category("UG", "Mechanical")
recommendation_system.add_category("UG", "ECE")
recommendation_system.add_category("CSE", "Year 1")
recommendation_system.add_category("CSE", "Year 2")
recommendation_system.add_category("CSE", "Year 3")
recommendation_system.add_category("CSE", "Year 4")
recommendation_system.add_category("Year 1", "CAD")
recommendation_system.add_category("Year 1", "Manufacturing Lab")
recommendation_system.add_category("Year 1", "System Essentials")
recommendation_system.add_category("Year 1", "PSAT")
recommendation_system.add_category("Year 1", "Physics")
recommendation_system.add_category("Year 1", "UID")
recommendation_system.add_category("Year 2", "Advanced programming")
recommendation_system.add_category("Year 2", "PROGRAM REASONING")
recommendation_system.add_category("Year 2", "DATABASE MANAGEMENT SYSTEMS")
recommendation_system.add_category("Year 2", "OBJECT ORIENTED PARADIGM")
recommendation_system.add_category("Year 2", "DATA STRUCTURES AND ALGORITHMS")
recommendation_system.add_category("Year 2", "THEORY OF COMPUTATION")
recommendation_system.add_category("Year 2", "COMPUTER ORGANIZATION AND ARCHITECTURE")
recommendation_system.add_category("Year 2", "OPERATING SYSTEMS")
recommendation_system.add_category("Year 3", "MACHINE LEARNING")
recommendation_system.add_category("Year 3", "DESIGN AND ANALYSIS OF ALGORITHMS")
recommendation_system.add_category("Year 3", "COMPUTER NETWORKS")
recommendation_system.add_category("Year 3", "FOUNDATIONS OF DATA SCIENCE")
recommendation_system.add_category("Year 3", "EMBEDDED SYSTEMS")
recommendation_system.add_category("Year 3", "SOFTWARE ENGINEERING")
recommendation_system.add_category("Year 3", "PRINCIPLES OF PROGRAMMING LANGUAGES")
recommendation_system.add_category("Year 3", "DISTRIBUTED SYSTEMS")
recommendation_system.add_category("Year 4", "COMPILER DESIGN")
recommendation_system.add_category("Mechanical", "Year 1")
recommendation_system.add_category("Mechanical", "Year 2")
recommendation_system.add_category("Mechanical", "Year 3")
recommendation_system.add_category("Mechanical", "Year 4")
recommendation_system.add_category("Year 1", "Single Variable Calculus")
recommendation_system.add_category("Year 1", "Ordinary Differential Equation")
recommendation_system.add_category("Year 1", "Matrix Algebra")
recommendation_system.add_category("Year 1", "Electrical Engineering Practice")
recommendation_system.add_category("Year 1", "Electrical & Electronic Circuits")
recommendation_system.add_category("Year 1", "Digital Electronics")
recommendation_system.add_category("Year 1", "Fourier Transforms and Complex Analysis")
recommendation_system.add_category("Year 1", "Operating Systems")
recommendation_system.add_category("Year 2", "Electric Machines")
recommendation_system.add_category("Year 2", "Microelectronic Circuits")
recommendation_system.add_category("Year 2", "Sensors and Sensor Circuit Design")
recommendation_system.add_category("Year 2", "Computer Architecture")
recommendation_system.add_category("Year 3", "Machine Learning")
recommendation_system.add_category("Year 3", "Real Time Embedded Systems")
recommendation_system.add_category("Year 3", "Energy Systems")
recommendation_system.add_category("Year 3", "Embedded Digital Signal Processing")
recommendation_system.add_category("Year 3", "Power Electronics and Drives")
recommendation_system.add_category("Year 3", "Data Base Systems and Programming")
recommendation_system.add_category("Year 4", "Theory of Computation and Compiler Design")
recommendation_system.add_category("ECE", "Year 1")
recommendation_system.add_category("ECE", "Year 2")
recommendation_system.add_category("ECE", "Year 3")
recommendation_system.add_category("Year 1", "Biology for Engineers - A")
recommendation_system.add_category("Year 1", "Physics of Electronic Materials")
recommendation_system.add_category("Year 1", "Basic Electrical and Electronics Engineering")
recommendation_system.add_category("Year 1", "Introduction to Internet of Things")
recommendation_system.add_category("Year 1", "Electronic Devices and Circuits")
recommendation_system.add_category("Year 1", "Circuit Theory")
recommendation_system.add_category("Year 2", "Analog Electronic Circuits")
recommendation_system.add_category("Year 2", "Applied Electromagnetics")
recommendation_system.add_category("Year 2", "Digital Electronics and Systems")
recommendation_system.add_category("Year 2", "Signals and Systems")
recommendation_system.add_category("Year 2", "Analog Electronics Lab")
recommendation_system.add_category("Year 3", "Transmission Lines and Radiating Systems")
recommendation_system.add_category("Year 3", "Digital Signal Processing")
recommendation_system.add_category("Year 3", "Linear Integrated Circuits")
recommendation_system.add_category("Year 3", "Communication Theory")
recommendation_system.add_category("Year 3", "Linear Integrated Circuits Lab")


# Add content items
#10th grade 
recommendation_system.add_content_item("RS Agarwal Textbook", ["Mathematics for Class 10 by R.S. Aggarwal (Bharati Bhawan)"], ["https://byjus.com/rs-textbook"])
recommendation_system.add_content_item("Physics Textbook", ["Physics for Dummies"], ["https://toppr.com/physics-textbook"])
recommendation_system.add_content_item("Physics Textbook", ["Physics for Dummies"], ["https://toppr.com/physics-textbook"])
recommendation_system.add_content_item("Chemistry Textbook", ["Chemistry Essentials"], ["https://toppr.com/chemistry-textbook"])
recommendation_system.add_content_item("Biology Textbook", ["Biology Fundamentals"], ["https://toppr.com/biology-textbook"])
recommendation_system.add_content_item("Social Studies Textbook", ["World History"], ["https://toppr.com/social-studies-textbook"])
recommendation_system.add_content_item("English Textbook", ["Grammar and Composition"], ["https://byjus.com/english-textbook"])
recommendation_system.add_content_item("NCERT maths Textbook", ["NCERT Mathematics: Textbook for Class 10"], ["https://apnaclass.com/ncert-textbook"])
recommendation_system.add_content_item("Linear Algebra Textbook", ["Linear Algebra for Beginners"], ["https://maths.com/linear-algebra-textbook"])
recommendation_system.add_content_item("Differential Equations Textbook", ["Differential Equations Made Easy"], ["https://byjus.com/diff-eq-textbook"])
recommendation_system.add_content_item("ICSE 10th Textbook", ["ICSE Class 10 Mathematics by Selina Publishers"],["https://selinapublishers.com/icse10-textbook"])
recommendation_system.add_content_item("Secondary school Textbook", ["Secondary School Mathematics for Class 10 by S. L. Loney (Goyal Brothers Prakashan)"],["https://goyalbros.com/textbook"])
recommendation_system.add_content_item("Cengage 10th grade Textbook", ["Mathematics - VIII (Eighth) by Cengage Learning India"],["https://cengage.com/textbook"])
recommendation_system.add_content_item("biology pdf1", ["Life processes"], ["https://biologyunit.com/lifeprocesses.pdf"])
recommendation_system.add_content_item("biology pdf2", ["Control and Coordination"], ["https://biologyunit.com/controlandcoordination.pdf"])
recommendation_system.add_content_item("NCERT Biology 10", ["NCERT Science: Biology for Class 10"], ["https://toppr.com/ncert-biology-textbook"])
recommendation_system.add_content_item("NCERT Biology 10", ["NCERT Science: Biology for Class 10"], ["https://toppr.com/ncert-biology-textbook"])


#plus one 
recommendation_system.add_content_item("University Physics", ["University Physics by Young and Freedman"], ["UniversityPhysics.html"])
recommendation_system.add_content_item("Fundamentals of Physics", ["Fundamentals of Physics by Halliday, Resnick, and Walker"], ["FundamentalsOfPhysics.html"])
recommendation_system.add_content_item("Introduction to Electrodynamics", ["Introduction to Electrodynamics by David J. Griffiths"], ["IntroductionToElectrodynamics.html"])
recommendation_system.add_content_item("Electricity and Magnetism", ["Electricity and Magnetism by Edward M. Purcell"], ["ElectricityAndMagnetism.html"])
recommendation_system.add_content_item("Optics", ["Optics by Eugene Hecht"], ["Optics.html"])
recommendation_system.add_content_item("Engineering Thermodynamics", ["Engineering Approach by Yunus A. Çengel", "Engineering Thermodynamics by Michael A. Boles"], ["EngineeringThermodynamics.html"])
recommendation_system.add_content_item("Modern Physics for Scientists and Engineers", ["Modern Physics for Scientists and Engineers by John Morrison", "Serway"], ["ModernPhysicsForScientistsAndEngineers.html"])
recommendation_system.add_content_item("Chemistry: The Central Science", ["Chemistry: The Central Science by Brown, LeMay, Bursten, Murphy, Woodward, and Stoltzfus"], ["ChemistryTheCentralScience.html"])
recommendation_system.add_content_item("Organic Chemistry", ["Organic Chemistry by Paula Bruice"], ["OrganicChemistry.html"])
recommendation_system.add_content_item("Inorganic Chemistry", ["Inorganic Chemistry by Gary L. Miessler and Paul J. Fischer"], ["InorganicChemistry.html"])
recommendation_system.add_content_item("Physical Chemistry", ["Physical Chemistry by Peter Atkins and Julio de Paula"], ["PhysicalChemistry.html"])
recommendation_system.add_content_item("Principles of Instrumental Analysis", ["Principles of Instrumental Analysis by Douglas A. Skoog, F. James Holler, and Stanley R. Crouch"], ["PrinciplesOfInstrumentalAnalysis.html"])
recommendation_system.add_content_item("Calculus: Early Transcendentals", ["Calculus: Early Transcendentals by James Stewart"], ["CalculusEarlyTranscendentals.html"])
recommendation_system.add_content_item("Calculus", ["Calculus by Michael Spivak"], ["Calculus.html"])
recommendation_system.add_content_item("Linear Algebra and Its Applications", ["Linear Algebra and Its Applications by David C. Lay"], ["LinearAlgebraAndItsApplications.html"])
recommendation_system.add_content_item("Elementary Differential Equations and Boundary Value Problems", ["Elementary Differential Equations and Boundary Value Problems by William E. Boyce and Richard C. DiPrima"], ["ElementaryDifferentialEquationsAndBoundaryValueProblems.html"])
recommendation_system.add_content_item("Introduction to Probability and Statistics", ["Introduction to Probability and Statistics by William Mendenhall, Robert J. Beaver, and Barbara M. Beaver"], ["IntroductionToProbabilityAndStatistics.html"])
recommendation_system.add_content_item("Discrete Mathematics and Its Applications", ["Discrete Mathematics and Its Applications by Kenneth H. Rosen"], ["DiscreteMathematicsAndItsApplications.html"])

#plus two
recommendation_system.add_content_item("Electricity and Magnetism", ["University Physics by Young & Freedman"], ["https://www.amazon.com/University-Physics-13th-Young-Freedman/dp/0321696867"])
recommendation_system.add_content_item("Modern Physics", ["Modern Physics by R. Eisberg and R. Resnick"], ["https://www.amazon.com/Modern-Physics-Robert-Eisberg/dp/0471873130"])
recommendation_system.add_content_item("Mechanics", ["Fundamentals of Physics by Halliday, Resnick, and Walker"], ["https://www.amazon.com/Fundamentals-Physics-David-Halliday/dp/1118230809"])
recommendation_system.add_content_item("Physical Chemistry", ["Physical Chemistry by Atkins & de Paula"], ["https://www.amazon.com/Physical-Chemistry-Peter-Atkins/dp/1429218126"])
recommendation_system.add_content_item("Organic Chemistry", ["Organic Chemistry by Jonathan Clayden, Nick Greeves, and Stuart Warren"], ["https://www.amazon.com/Organic-Chemistry-Jonathan-Clayden/dp/0199270295"])
recommendation_system.add_content_item("Inorganic Chemistry", ["Inorganic Chemistry by Gary L. Miessler and Paul J. Fischer"], ["https://www.amazon.com/Inorganic-Chemistry-Gary-L-Miessler/dp/0134143332"])
recommendation_system.add_content_item("Calculus", ["Calculus: Early Transcendentals by James Stewart"], ["https://www.amazon.com/Calculus-Early-Transcendentals-James-Stewart/dp/1285741552"])
recommendation_system.add_content_item("Algebra", ["Linear Algebra and Its Applications by David C. Lay"], ["https://www.amazon.com/Linear-Algebra-Its-Applications-5th/dp/032198238X"])
recommendation_system.add_content_item("Statistics", ["Introduction to Probability and Statistics by William Mendenhall"], ["https://www.amazon.com/Introduction-Probability-Statistics-William-Mendenhall/dp/1305032942"])

#ece 1st year 
recommendation_system.add_content_item("19BIO101 BIOLOGY FOR ENGINEERS - A", ["Leslie Cromwell, Biomedical Instrumentation, Prentice Hall 2011"], ["https://www.amazon.com/Biomedical-Instrumentation-Technology-Applications-Cromwell/dp/0131964709"])
recommendation_system.add_content_item("19BIO101 BIOLOGY FOR ENGINEERS - A", ["Thyagarajan S., Selvamurugan N., Rajesh M.P., Nazeer R.A., Thilagaraj R. W., Barathi S., and Jaganthan M.K., Biology for Engineers, Tata McGraw-Hill, New Delhi, 2012"], ["https://www.mheducation.co.in/biology-for-engineers-9789339213572-india"])
recommendation_system.add_content_item("19PHY103 PHYSICS OF ELECTRONIC MATERIALS", ["S O Kasap, Principles of Electronic Materials and Devices, 4thEdition, McGraw Hill Education, 2018"], ["https://www.mheducation.com/highered/product/principles-electronic-materials-devices-kasap/M9780073380643.html"])
recommendation_system.add_content_item("19EEE100 BASIC ELECTRICAL AND ELECTRONICS ENGINEERING", ["Edward Hughes. Electrical and Electronic Technology, 10th Edition, Pearson Education Asia, 2019"], ["https://www.pearson.com/en-gb/subject-catalog/p/hughes-electrical-and-electronic-technology/P200000005535/9781292317748"])
recommendation_system.add_content_item("19ECE101 INTRODUCTION TO INTERNET OF THINGS", ["Sylvia Libow Martinez, Gary S Stager, Invent To Learn: Making, Tinkering, and Engineering in the Classroom, Constructing Modern Knowledge Press, 2016"], ["https://www.amazon.com/Invent-Learn-Making-Tinkering-Engineering/dp/0985342116"])
recommendation_system.add_content_item("19ECE101 INTRODUCTION TO INTERNET OF THINGS", ["Michael Margolis, Arduino Cookbook, Oreilly, 2011"], ["https://www.oreilly.com/library/view/arduino-cookbook/9781449313876/"])
recommendation_system.add_content_item("19ECE112 ELECTRONIC DEVICES AND CIRCUITS", ["Robert L Boylestad and Louis Nashelsky, Electronic Devices and Circuit Theory, Eleventh Edition, Pearson India Education Services Pvt. Ltd., 2015"], ["https://www.pearson.com/en-in/subject-catalog/p/robert-l-boylestad-louis-nashelsky-electronic-devices-and-circuit-theory/P200000005191/9789332582231"])
recommendation_system.add_content_item("19ECE111 CIRCUIT THEORY", ["Charles K Alexander, Mathew N. O. Sadiku, Fundamentals of Electric circuits, Tata McGraw Hill, 2003"], ["https://www.mheducation.co.in/fundamentals-of-electric-circuits-9780071326056-india"])

#ece 2nd year 
recommendation_system.add_content_item("19ECE201 ANALOG ELECTRONIC CIRCUITS", ["S. Sedra, K. C. Smith and A. N. Chandorkar, Microelectronic Circuits - Theory and Applications, Seventh Edition, Oxford University Press, 2017"], ["https://global.oup.com/academic/product/microelectronic-circuits-9780190698379?cc=in&lang=en&"])

recommendation_system.add_content_item("19ECE201 ANALOG ELECTRONIC CIRCUITS", ["R. L. Boylestad and L. Nashelsky, Electronic Devices and Circuit Theory, Eleventh Edition, Pearson India Education Services Pvt. Ltd., 2015"], ["https://www.pearson.com/en-in/subject-catalog/p/robert-l-boylestad-louis-nashelsky-electronic-devices-and-circuit-theory/P200000005191/9789332582231"])

recommendation_system.add_content_item("19ECE201 ANALOG ELECTRONIC CIRCUITS", ["D. A. Neamen, Electronic Circuits - Analysis and Design, Third Edition, McGraw Hill Education, 2006"], ["https://www.mheducation.com/highered/product/electronic-circuits-analysis-design-neamen/M9780073529608.html"])

recommendation_system.add_content_item("19ECE202 APPLIED ELECTROMAGNETICS", ["David K.Cheng, Field and Wave Electromagnetics, Pearson Education, Second Edition, 2002"], ["https://www.pearson.com/en-us/subject-catalog/p/david-k-cheng-field-and-wave-electromagnetics/P200000005195/9780201128192"])

recommendation_system.add_content_item("19ECE202 APPLIED ELECTROMAGNETICS", ["Clayton R. Paul, Keith W. Whites, Syed A. Nasar, Introduction to Electromagnetic Fields, Tata McGraw-Hill Education Private Limited, Third Edition (Fifth Reprint), 2009"], ["https://www.mheducation.co.in/introduction-to-electromagnetic-fields-9780070144439-india"])

recommendation_system.add_content_item("19ECE204 DIGITAL ELECTRONICS AND SYSTEMS", ["Stephen Brown, Zvonko Vranesic, Fundamentals of Digital logic with Verilog Design, Tata McGraw Hill Publishing Company Limited, Special Indian Edition, 2007"], ["https://www.mheducation.co.in/fundamentals-of-digital-logic-with-verilog-design-9780070144446-india"])

recommendation_system.add_content_item("19ECE204 DIGITAL ELECTRONICS AND SYSTEMS", ["M Morris Mano and Michael D Ciletti, Digital Design with Introduction to the Verilog HDL, Pearson Education, Fifth Edition, Fifth Edition, 2015"], ["https://www.pearson.com/en-us/subject-catalog/p/m-morris-mano-michael-d-ciletti-digital-design-with-an-introduction-to-the-verilog-hdl/P200000005184/9780133072989"])

recommendation_system.add_content_item("19ECE203 SIGNALS AND SYSTEMS", ["Simon Haykin, Barry Van Veen, Signals and Systems, Second Edition, John Wiley and Sons, 2007"], ["https://www.wiley.com/en-us/Signals+and+Systems%2C+2nd+Edition-p-9780471164746"])

recommendation_system.add_content_item("19ECE203 SIGNALS AND SYSTEMS", ["Alan V. Oppenheim, Alan S. Wilsky, S. Hamid Nawab, Signals and Systems. Prentice Hall India private Limited, Second Edition, 1997"], ["https://www.pearsoned.co.in/web/books/signals-and-systems_9780133814293.aspx"])

recommendation_system.add_content_item("19ECE281 ANALOG ELECTRONICS LAB", ["S. Sedra, K. C. Smith and A. N. Chandorkar, Microelectronic Circuits - Theory and Applications, Seventh Edition, Oxford University Press, 2017"], ["https://global.oup.com/academic/product/microelectronic-circuits-9780190698379?cc=in&lang=en&"])
recommendation_system.add_content_item("19ECE281 ANALOG ELECTRONICS LAB", ["R. L. Boylestad and L. Nashelsky, Electronic Devices and Circuit Theory, Eleventh Edition, Pearson India Education Services Pvt. Ltd., 2015"], ["https://www.pearson.com/en-in/subject-catalog/p/robert-l-boylestad-louis-nashelsky-electronic-devices-and-circuit-theory/P200000005191/9789332582231"])
recommendation_system.add_content_item("19ECE281 ANALOG ELECTRONICS LAB", ["D. A. Neamen, Electronic Circuits - Analysis and Design, Third Edition, McGraw Hill Education, 2006"], ["https://www.mheducation.com/highered/product/electronic-circuits-analysis-design-neamen/M9780073529608.html"])
#ece 3rd year 
recommendation_system.add_content_item("19ECE313 TRANSMISSION LINES AND RADIATING SYSTEMS", ["David K.Cheng, Field and Wave Electromagnetics, Pearson Education, Second Edition, 2002"], ["https://www.pearson.com/en-us/subject-catalog/p/david-k-cheng-field-and-wave-electromagnetics/P200000005195/9780201128192"])

recommendation_system.add_content_item("19ECE313 TRANSMISSION LINES AND RADIATING SYSTEMS", ["Clayton R. Paul, Keith W. Whites, Syed A. Nasar, Introduction to Electromagnetic Fields, Tata McGraw-Hill Education Private Limited, Third Edition (Fifth Reprint), 2009"], ["https://www.mheducation.co.in/introduction-to-electromagnetic-fields-9780070144439-india"])

recommendation_system.add_content_item("19ECE313 TRANSMISSION LINES AND RADIATING SYSTEMS", ["Kraus, Fleisch, Electromagnetics with Applications, Tata McGraw Hill Education Private Limited, Fifth Edition"], ["https://www.mheducation.co.in/electromagnetics-with-applications-9780070284968-india"])

recommendation_system.add_content_item("19ECE313 TRANSMISSION LINES AND RADIATING SYSTEMS", ["Constantine A. Balanis, Antenna Theory: Analysis and Design, Wiley-Interscience, Third Edition, 2005"], ["https://www.wiley.com/en-us/Antenna+Theory%3A+Analysis+and+Design%2C+3rd+Edition-p-9780471667827"])

recommendation_system.add_content_item("19ECE311 DIGITAL SIGNAL PROCESSING", ["John G Proakis, G. Manolakis, Digital Signals Processing Principles, Algorithms, Applications, Prentice Hall India Private Limited, Fourth Edition, 2007"], ["https://www.pearson.com/en-in/subject-catalog/p/john-g-proakis-g-manolakis-digital-signal-processing/P200000005229/9788120325388"])

recommendation_system.add_content_item("19ECE311 DIGITAL SIGNAL PROCESSING", ["Sanjit K. Mitra, Digital Signal Processing, A computer based approach, Tata McGraw Hill Publishing Company Limited, Fourth Edition, 2010"], ["https://www.mheducation.co.in/digital-signal-processing-9789339205171-india"])

recommendation_system.add_content_item("19ECE312 LINEAR INTEGRATED CIRCUITS", ["A S. Sedra, K. C. Smith and A. N. Chandorkar, Microelectronic Circuits -Theory and Applications, Seventh Edition, Oxford University Press, 2017"], ["https://global.oup.com/academic/product/microelectronic-circuits-9780190698379?cc=in&lang=en&"])

recommendation_system.add_content_item("19ECE312 LINEAR INTEGRATED CIRCUITS", ["D. A. Neamen, Electronic Circuit -Analysis and Design, Third Edition, McGraw Hill Education, 2006"], ["https://www.mheducation.com/highered/product/electronic-circuits-analysis-design-neamen/M9780073529608.html"])

recommendation_system.add_content_item("19ECE314 COMMUNICATION THEORY", ["John. G. Proakis, Masoud Salehi, Fundamentals of Communication Systems, Pearson Education, 6th edition, 2011"], ["https://www.pearson.com/en-us/subject-catalog/p/john-g-proakis-masoud-salehi-fundamentals-of-communication-systems/P200000005194/9780132213950"])

recommendation_system.add_content_item("19ECE383 LINEAR INTEGRATED CIRCUITS LAB", ["A.S. Sedra, K. C. Smith and A. N. Chandorkar, Microelectronic Circuits - Theory and Applications, Seventh Edition, Oxford University Press, 2017"], ["https://global.oup.com/academic/product/microelectronic-circuits-9780190698379?cc=in&lang=en&"])

recommendation_system.add_content_item("19ECE383 LINEAR INTEGRATED CIRCUITS LAB", ["D. A. Neamen, Electronic Circuit -Analysis and Design, Third Edition, McGraw Hill Education, 2006"], ["https://www.mheducation.com/highered/product/electronic-circuits-analysis-design-neamen/M9780073529608.html"])

recommendation_system.add_content_item("19ECE383 LINEAR INTEGRATED CIRCUITS LAB", ["Sergio Franco, Design with Operational Amplifiers and Analog Integrated Circuits, Fourth Edition, Tata McGraw Hill Publishing Company Limited, 2015"], ["https://www.mheducation.co.in/design-with-operational-amplifiers-and-analog-integrated-circuits-9789339217730-india"])

recommendation_system.add_content_item("19ECE383 LINEAR INTEGRATED CIRCUITS LAB", ["J. Millman and A.Grabel, Microelectronics, Second Edition, McGraw-Hill, 2001"], ["https://www.mheducation.com/highered/product/microelectronics-millman-grabel/M9780070426627.html"])
#cse 1st year 
recommendation_system.add_content_item("Computer Programming", ["C for All-in-One for Dummies"], ["https://www.wiley.com/en-us/C+All+in+One+For+Dummies-p-9781119247791"])

recommendation_system.add_content_item("User Interface Design", ["The Essential Guide to user Interface Design"], ["https://www.wiley.com/en-us/The+Essential+Guide+to+User+Interface+Design%3A+An+Introduction+to+GUI+Design+Principles+and+Techniques%2C+4th+Edition-p-9781119038108"])

recommendation_system.add_content_item("Fundamentals of Data Structures", ["Fundamentals of Data Structures"], [""])

recommendation_system.add_content_item("Engineering Physics - A", ["Halliday & Resnick Principles of Physics"], ["https://www.wiley.com/en-us/Fundamentals+of+Physics%2C+10th+Edition-p-9781118230718"])

recommendation_system.add_content_item("Problem Solving and Algorithmic Thinking", ["Think Like a Programmer: An Introduction to Creative Problem Solving"], ["https://nostarch.com/thinklikeaprogrammer"])

recommendation_system.add_content_item("Engineering Graphics - CAD", ["CAD/CAM : Theory and Practice: Special Indian Edition"], [""])

recommendation_system.add_content_item("Computer Systems Essentials", ["ESSENTIAL OF OPERATING SYSTEM"], [""])

recommendation_system.add_content_item("Linear algebra", ["Linear Algebra and its Applications"], ["https://www.pearson.com/us/higher-education/product/Lay-Linear-Algebra-and-Its-Applications-5th-Edition/9780321982384.html"])

while True:
    print("Enter 'key' if you want to search for a content by keyword, 'category' if you want to search by category")
    x = input ()
    if x == "category":
        user_input = input("Enter your category (High School, Intermediate, UG): ")
        if user_input == "High School":
            grade_input = input("Enter your grade (8th, 9th, 10th): ")
            subject_input = input("Enter your subject (Mathematics, Physics, Chemistry, Biology, Social Studies, English): ")
            print("Recommended Content:")
            print() 
            if grade_input == "10th" and subject_input == "Mathematics":
                content_item = recommendation_system.search_content_by_name("RS Agarwal Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()        
                content_item = recommendation_system.search_content_by_name("NCERT maths Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print() 
                content_item = recommendation_system.search_content_by_name("Linear Algebra Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print() 
                content_item = recommendation_system.search_content_by_name("ICSE 10th Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print() 
                content_item = recommendation_system.search_content_by_name("Secondary school Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print() 
                content_item = recommendation_system.search_content_by_name("Cengage 10th grade Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print() 
            elif grade_input == "10th" and subject_input == "Physics":
                content_item = recommendation_system.search_content_by_name("Physics Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                content_item = recommendation_system.search_content_by_name("Differential Equations Textbook")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
            else:
                print("No recommended content found.")
        
        elif user_input == "Intermediate":
            grade_input = input("Enter your grade (Plus 1, Plus 2): ")
            subject_input = input("Enter your subject (Mathematics, Physics, Chemistry): ")
            print("Recommended Content:")
            print()
            #plus one 
            if grade_input == "Plus 1" and subject_input == "Physics":
                content_item = recommendation_system.search_content_by_name("University Physics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Fundamentals of Physics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Introduction to Electrodynamics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Electricity and Magnetism")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Optics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Engineering Thermodynamics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Modern Physics for Scientists and Engineers")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
            if grade_input == "Plus 1" and subject_input == "Chemistry":
                content_item = recommendation_system.search_content_by_name("Chemistry: The Central Science")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Organic Chemistry")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Inorganic Chemistry")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Physical Chemistry")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Principles of Instrumental Analysis")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
            if grade_input == "Plus 1" and subject_input == "Mathematics":
                content_item = recommendation_system.search_content_by_name("Calculus: Early Transcendentals")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Calculus")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Linear Algebra and Its Applications")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Elementary Differential Equations and Boundary Value Problems")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Introduction to Probability and Statistics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Discrete Mathematics and Its Applications")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
            #plus two
            if grade_input == "Plus 2" and subject_input == "Physics":
                content_item = recommendation_system.search_content_by_name("Electricity and Magnetism")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Modern Physics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Mechanics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
            if grade_input == "Plus 2" and subject_input == "Chemistry":
                content_item = recommendation_system.search_content_by_name("Physical Chemistry")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Organic Chemistry")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Inorganic Chemistry")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
            if grade_input == "Plus 2" and subject_input == "Mathematics":
                content_item = recommendation_system.search_content_by_name("Calculus: Early Transcendentals")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Linear Algebra and Its Applications")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Introduction to Probability and Statistics")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Material: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
        elif user_input == "UG":
            program_input = input("Enter your program (CSE, Mechanical, ECE): ")
            year_input = input("Enter your year (1, 2, 3, 4): ")
            print("Recommended Content:")
            if program_input == "CSE" and year_input == "1":
                content_item = recommendation_system.search_content_by_name("CAD")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                content_item = recommendation_system.search_content_by_name("System Essentials")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
            if program_input == "CSE" and year_input == "2":
                content_item = recommendation_system.search_content_by_name("Advanced programming")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                content_item = recommendation_system.search_content_by_name("DATA STRUCTURES AND ALGORITHMS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
            if program_input == "Mechanical" and year_input == "1":
                content_item = recommendation_system.search_content_by_name("Single Variable Calculus")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                content_item = recommendation_system.search_content_by_name("Electrical & Electronic Circuits")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
            #ece 1st year 
            if program_input == "ECE" and year_input == "1":
                content_item = recommendation_system.search_content_by_name("Basic Electrical and Electronics Engineering")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("Electronic Devices and Circuits")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("19BIO101 BIOLOGY FOR ENGINEERS - A")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("19PHY103 PHYSICS OF ELECTRONIC MATERIALS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("19EEE100 BASIC ELECTRICAL AND ELECTRONICS ENGINEERING")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("19ECE101 INTRODUCTION TO INTERNET OF THINGS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("19ECE112 ELECTRONIC DEVICES AND CIRCUITS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
                content_item = recommendation_system.search_content_by_name("19ECE111 CIRCUIT THEORY")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
            #ece 2nd year 
            if program_input == "ECE" and year_input == "2":
                content_item = recommendation_system.search_content_by_name("19ECE201 ANALOG ELECTRONIC CIRCUITS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("19ECE202 APPLIED ELECTROMAGNETICS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
                content_item = recommendation_system.search_content_by_name("19ECE204 DIGITAL ELECTRONICS AND SYSTEMS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
                content_item = recommendation_system.search_content_by_name("19ECE203 SIGNALS AND SYSTEMS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
                content_item = recommendation_system.search_content_by_name("19ECE281 ANALOG ELECTRONICS LAB")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
            #ece 3rd year 
            if program_input == "ECE" and year_input == "3":
                content_item = recommendation_system.search_content_by_name("19ECE313 TRANSMISSION LINES AND RADIATING SYSTEMS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
                content_item = recommendation_system.search_content_by_name("19ECE311 DIGITAL SIGNAL PROCESSING")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
                content_item = recommendation_system.search_content_by_name("19ECE312 LINEAR INTEGRATED CIRCUITS")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
                content_item = recommendation_system.search_content_by_name("19ECE314 COMMUNICATION THEORY")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
                content_item = recommendation_system.search_content_by_name("19ECE383 LINEAR INTEGRATED CIRCUITS LAB")
                if content_item:
                    print(f"Name: {content_item.name}")
                    print(f"Textbooks: {', '.join(content_item.textbooks)}")
                    print(f"Links: {', '.join(content_item.links)}")
                    print()
        
            else:
                print("No recommended content found.")
    elif x=="key":
        key=input("Enter the subject of which you would like the content\n")
        recommendation_system.search_content_by_key(key)

    else:
        break
