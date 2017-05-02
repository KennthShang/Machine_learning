def NBAccuracy(features_train, labels_train, features_test, labels_test):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    from sklearn.naive_bayes import GaussianNB
	
	
	### create classifier
    clf = GuassianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)


    ### calculate and return the accuracy on the test data
    accuracy = clf.score(pred, labels_test)
    return clf, accuracy
    
    