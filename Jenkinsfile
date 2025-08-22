pipeline {
  agent {
    docker { image 'python:3.12' }
  }
  options { timestamps() }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install deps') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt -r requirements-dev.txt'
      }
    }
    stage('Lint') {
      steps { sh 'flake8 .' }
    }
    stage('Test') {
      steps {
        sh 'pytest -q --junitxml=test-results/junit.xml --cov=.'
      }
    }
    stage('Package (wheel)') {
      steps {
        sh 'python -m pip install build'
        sh 'python -m build'
      }
    }
  }
  post {
    always {
      junit 'test-results/*.xml'
      archiveArtifacts artifacts: 'dist/*', fingerprint: true, allowEmptyArchive: true
    }
  }
}
