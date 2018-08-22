#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */
pipeline {
    agent any
    options {
        buildDiscarder(
            // Only keep the 10 most recent builds
            logRotator(numToKeepStr:'10'))
    }
    environment {
        projectName = 'ProjectTemplate'
        emailTo = 'prem1pre@gmail.com'
        emailFrom = 'premjenkins@gmail.com'
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }

    stages {

        /*
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        */

        stage ('Install_Requirements') {
            steps {
                sh """
                    echo ${SHELL}
                    PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
                    if [ ! -d "venv" ]; then
                        virtualenv venv
                    fi
                    #. venv/bin/activate
                    [ -d venv ] && rm -rf venv
                    #virtualenv --python=python2.7 venv
                    virtualenv venv
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pip install --upgrade pip
                    #pip install -r requirements.txt -r dev-requirements.txt
                    pip install -r requirements.txt
                    make clean
                """
            }
        }

        stage ('Check_style') {
            steps {

                sh """
                    #. venv/bin/activate
                    [ -d report ] || mkdir report
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    make check || true
                """
                }
            }


        stage ('Unit Tests') {
            steps {
                sh """
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    make unittest || true
                """
            }

            post {
                always {
                    junit keepLongStdio: true, testResults: 'report/nosetests.xml'
                    publishHTML target: [
                        reportDir: 'cover/',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report - Unit Test'
                    ]
                }
            }
        }
        /*
        stage ('System Tests') {
            steps {
                sh """
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    // Write file containing test node connection information if needed.
                    // writeFile file: "test/fixtures/nodes.yaml", text: "---\n- node: <some-ip>\n"
                    make systest || true
                """
            }

            post {
                always {
                    junit keepLongStdio: true, testResults: 'report/nosetests.xml'
                    publishHTML target: [
                        reportDir: 'report/coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report - System Test'
                    ]
                }
            }
        }


        stage ('Docs') {
            steps {
                sh """
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    PYTHONPATH=. pdoc --html --html-dir docs --overwrite env.projectName
                """
            }

            post {
                always {
                    publishHTML target: [
                        reportDir: 'docs/*',
                        reportFiles: 'index.html',
                        reportName: 'Module Documentation'
                    ]
                }
            }
        }

        */


        stage ('Cleanup') {
            steps {
                sh 'rm -rf venv'
            }
        }
    }
    /*
    post {
        failure {
            mail body: "${env.JOB_NAME} (${env.BUILD_NUMBER}) ${env.projectName} build error " +
                       "is here: ${env.BUILD_URL}\nStarted by ${env.BUILD_CAUSE}" ,
                 from: env.emailFrom,
                 //replyTo: env.emailFrom,
                 subject: "${env.projectName} ${env.JOB_NAME} (${env.BUILD_NUMBER}) build failed",
                 to: env.emailTo
        }
        success {
            mail body: "${env.JOB_NAME} (${env.BUILD_NUMBER}) ${env.projectName} build successful\n" +
                       "Started by ${env.BUILD_CAUSE}",
                 from: env.emailFrom,
                 //replyTo: env.emailFrom,
                 subject: "${env.projectName} ${env.JOB_NAME} (${env.BUILD_NUMBER}) build successful",
                 to: env.emailTo
        }
    }
    */
}