pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install poetry'
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
