pipeline {
  agent any
  stages {
    stage('Install Requirements') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run Python Tests') {
      steps {
        sh 'pytest tests/'
      }
    }
    stage('Deploy with Ansible') {
      steps {
        sh 'ansible-playbook playbook.yml'
      }
    }
  }
}
