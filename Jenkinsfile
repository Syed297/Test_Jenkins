pipeline {
    agent any 

    stages {
        stage('Fetch from Git') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Syed297/Test_Jenkins'
            }
        }
        
        stage('Prepare Environment') {
            steps {
                sh '''
                python3 -m venv mlops_demo
                source mlops_demo/bin/activate
                pip install sklearn
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                source mlops_demo/bin/activate
                python3 model_training.py
                '''
            }
        }

        stage('Test Model') {
            steps {
                sh '''
                source mlops_demo/bin/activate
                python3 model_testing.py
                '''
            }
        }

        stage('Deploy Model') {
            steps {
                sh 'python3 model_deployment.py'
            }
        }
    }
}
