# Python_ML
Machine Learning Perdictions on selected features for Software Bug Data Sets

A detailed comparative performance analysis of different machine learning techniques is being
explored for software bug prediction on public available data sets. Machine learning techniques 
are proven to be useful in terms of software bug prediction. The data from software repository 
contains lots of information in assessing software quality; and machine learning techniques can be applied on them in order to extract software bugs information. The machine learning techniques are classified into two broad categories in order to compare their performance; such as supervised learning versus unsupervised learning. In supervised learning algorithms such as ensemble classifier like bagging and boosting, Multilayer perceptron, Naive Bayes classifier, Support vector machine, Random Forest and Decision Trees are compared. In case of unsupervised learning methods like Radial base network function, clustering techniques such as K-means algorithm, K nearest neighbor are compared against each other

Performance Indicators 
For comparative study, performance indicators such as accuracy, mean absolute error and F-
measure based on precision and recall were used. Accuracy can be defined as the total number of 
correctly identified bugs divided by the total number of bugs, and is calculated by the equations 
listed below: Accuracy = (TP + TN) / (TP+TN+FP+FN) (1) 
Accuracy (%) = (correctly classified software bugs/ Total software bugs) * 100 (2) 
Precision is a measure of correctness and it is a ratio between correctly classified software bugs 
and actual number of software bugs assigned to their category. It is calculated by the equation 
below: 
Precision = TP / (TP+FP) 

		Performance Measure	Supervised Learning		
Data Set	Naye Bayes	MLP	SVM	J48	Bagging	Decision Tree	Random Forest
AR1	83.45	89.55	91.97	90.15	92.23	89.32	90.15	

Data Source	Algotihim	Attributes	Infogain	Correlation_C	Gain Ratio	Infogain	Correlation_P	Gain Ratio
Defect ar1	J48	29	90.08	90.08	90.08		93.9	93.9	95.7
		25	90.08	91.37	90.08		93.9	93.9	93.9
		20	87.6	88.42	90.08		92.2	93	93.9
		15	88.42	89.25	88.42		92.2	93	92.2
		10	90.9	90.08	90.08		93.2	93.1	93.1
		5	90.9	90.9	90.9		93.2	93.2	93.2
									
Defect ar1	Random Forest	29	90.08	90.08	90.08		92.4	92.4	92.4
		25	90.08	90.08	90.08		92.4	92.4	92.4
		20	89.25	90.08	99.17		92.3	92.4	92.3
		15	89.25	90.08	89.25		92.3	92.4	92.3
		10	89.25	89.29	88.42		92.3	92.3	92.2
		5	89.25	88.42	89.25		93	92.2	92.3
									
Defect ar1	Random Tree	29	89.25	89.25	89.25		93.8	93.8	93.8
		25	87.6	88.42	87.6		92.2	92.2	92.2
		20	87.6	86.77	99.17		93.7	93.6	92.3
		15	87.6	87.6	90.08		92.9	92.9	93.1
		10	87.6	85.95	84.29		92.2	94.4	91.9
		5	87.6	87.6	89.25		93.7	92.9	93.8
									
Defect ar1	LMT	29	91.73	91.73	91.73		92.5	92.5	92.5
		25	91.73	91.73	91.73		92.5	92.5	92.5
		20	91.73	91.73	91.73		92.5	92.5	92.5
		15	91.73	91.73	91.73		92.5	92.5	92.5
		10	91.73	91.73	91.73		92.5	92.5	92.5
		5	91.73	91.73	91.73		92.5	92.5	92.5
									
Defect ar1	Decision stump	29	90.91	90.91	90.91		92.6	92.6	92.4
		25	90.9	92.56	90.91		92.4	92.4	92.4
		20	90.9	92.56	90.91		92.4	92.4	92.4
		15	90.9	90.91	90.91		92.4	92.4	92.4
		10	90.9	90.9	90.91		92.4	92.4	92.4
		5	90.9	90.9	90.91		92.4	92.4	92.4
									
Defect ar1	svm.svc	29	91.73	91.73			93	93	
		25	91.73	91.73			93	93	
		20	91.73	91.73			94	93	
		15	91.73	91.73			93	93	
		10	91.73	91.73			93	93	
		5	91.73	91.73			93	93	
									
Defect ar1	LinearSVC	29	80.99	80.99			92	92	
		25	78.51	80.16			95	92	
		20	75.2	78.51			95	93	
		15	76.03	63.63			94	94	
		10	76.03	85.95			93	95	
		5	79.33	90.9			94	95	
									
Defect ar1	NuSVC	29	28.09	28.09			93	93	
		25	28.09	28.09			93	93	
		20	28.09	28.09			93	93	
		15	83.47	28.09			93	93	
		10	32.23	28.09			92	93	
		5	91.73	28.09			93	93	
									
Glass Multi class	MLPClassfier	15		16.49			20		
		10		11.14			5		
		5		18			43		
									
Glass Multi Class, crossval=5	svm.svc	15		96.24			97		
		10		53.7			66.8		
		5		66.66			63		
									
Glass Multi Class crossval=5	LinearSVC	15		69.95			71		
		10		64.81			71		
		5		53.7			47		
									
Glass Multi Class crossval=5	NuSVC	15		97.65			98		
		10		52.33			53		
		5		40.65			43		
									
									
Letter Multi Class, crossval=5	svm.svc	15		97.2			97		
		10		96.96			97		
		5		81.92			83		
									
Letter Multi Class, crossval=5	LinearSVC	15		64.78			70		
		10		58.94			63		
		5		46.98			45		
									
Letter Multi Class, crossval=5	NuSVC	15		97.92			98		
		10		97.12			97		
		5		79.54			80		
									
 			Correctness				precision	



