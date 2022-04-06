pipeline {
    agent { any }
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
