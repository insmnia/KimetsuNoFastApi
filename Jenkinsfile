pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('Prepare') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    echo "Done with requirements"
                    sh 'pytest'
                    sh 'flake8 app/'
                    sh 'dir'
                }
            }
        }
    }
}
