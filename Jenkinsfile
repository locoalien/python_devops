node('master'){
    stage("Obtener codigo fuente"){
        git 'https://github.com/locoalien/python_devops.git'
    }
    dir(''){
        printMessage('Ejecutando Pipeline')
        
        stage('Testing'){
            sh 'python test_functions.py'
        }
        
        stage("Testing"){
            if(env.BRANCH_NAME == 'master'){
                printMessage('Desplegando master Branch')
            }else{
                printMessage('No desplegado el Branch configurado')
            }
        }
        
        printMessage('Pipeline Completado')
    }
}

def printMessage(message){
    echo '${message}'
}