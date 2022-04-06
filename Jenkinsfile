pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('Prepare') {
            steps {
                withPythonEnv('python3') {
                    sh 'pip install pytest'
                    sh 'pytest test_main.py'
                }
            }
        }
    }
}
