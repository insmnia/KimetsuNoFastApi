pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('Prepare') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    sh 'python -m flake8 app/'
                    echo "Done with requirements"
                }
            }
        }
    }
}
