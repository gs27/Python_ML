# Python_ML


Software Defect Prediction

Software Defect Prediction (SDP) is the line of research that concerned with building prediction models, which leverage software metrics to predict defect-prone areas of a software.

A bug indicates the unexpected behavior of system for some given requirements. The unexpected behavior is identified during software testing and marked as a bug. A software bug can be referred to as” Imperfection in software development process that would cause software to fail to meet the desired expectation.

p..Ground Reality The more complex (software like ours), the more defect prone Some code works well Some code creates issues again and again => HOT SPOT Hot spot Inadequate (unit) test coverage Resistant to (unit) testing ? We are smart Diligent, experienced, and fearless code reviewers, who are able to spot any issues and resolve them Still Bugs… Challenges Tracking changes in a hot spot versus generally harmless code. Huge code base, as well as team size

Bug prediction

Identify hot spots, and warn developers. Uses machine-learning and statistical analysis Simple algorithm, simply ranking files by the number of times they've been changed with a bug-fixing commit Adapt to changes, weighting each bug-fixing commit by its age i.e.

p..Machine learning techniques can be used to analyse data from different perspectives and enable developers to retrieve useful information. The machine learning techniques that can be used to detect bugs in software datasets can be classification and clustering. Classification is a data mining and machine learning approach, useful in software bug prediction. It involves categorization of software modules into defective or non-defective that is denoted by a set of software complexity metrics by utilizing a classification model that is derived from earlier development projects data.

For comparative study, performance indicators such as accuracy, mean absolute error and F measure based on precision and recall were used. Accuracy can be defined as the total number of correctly identified bugs divided by the total number of bugs, and is calculated by the equations listed below: Accuracy = (TP + TN) / (TP+TN+FP+FN) (1) Accuracy (%) = (correctly classified software bugs/ Total software bugs) * 100 (2) Precision is a measure of correctness and it is a ratio between correctly classified software bugs and actual number of software bugs assigned to their category. It is calculated by the equation below: Precision = TP / (TP+FP)
