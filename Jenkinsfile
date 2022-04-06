pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    echo "done"
                    sh 'dir'
                }
            }
        }
        stage('lint'){
            steps{
                sh 'flake8 app/'
            }
        }
        stage('test'){
            steps{
                sh 'pytest -q'
            }
        }
    }
}
