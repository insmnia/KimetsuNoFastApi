pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    echo "done"
                }
            }
        }
        stage('test'){
            steps{
                sh 'make test'
            }
        }
    }
}
