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
        stage('test'){
            steps{
                bash 'pytest test_main.py'
            }
        }
    }
}
