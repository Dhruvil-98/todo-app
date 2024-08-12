pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                script {
                    def python = tool name: 'Python 3.x', type: 'PythonInstallation'
                    env.PATH = "${python}/bin:${env.PATH}"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }

        stage('Lint Code') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 .'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
