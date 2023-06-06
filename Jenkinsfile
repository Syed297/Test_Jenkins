pipeline {
    agent any 

    stages {
        stage('Fetch from Git') {
            steps {
                git 'https://github.com/Syed297/Test_Jenkins'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 model_training.py'
            }
        }

        stage('Test Model') {
            steps {
                sh 'python3 model_testing.py'
            }
        }

        stage('Deploy Model') {
            steps {
                sh 'python3 model_deployment.py'
            }
        }
    }
}