pipeline {
  agent any
  stages {
    stage('Setup Python Env') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }
    stage('Run Python Tests') {
      steps {
        sh '''
          . venv/bin/activate
          pytest tests/
        '''
      }
    }
    stage('Deploy with Ansible') {
      steps {
        sh '''
          . venv/bin/activate
          ansible-playbook playbook.yml
        '''
      }
    }
  }
}
