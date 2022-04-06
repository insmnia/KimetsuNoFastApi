pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'poetry install'
            }
        }
        stage('test') {
            steps {
                sh 'make test'
            }
        }
    }
}
