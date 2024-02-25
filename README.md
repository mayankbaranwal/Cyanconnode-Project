# Cyanconnode-Project
Currently, we can run the uploaded .py files directly! 

However, We can run the file from the terminal in two ways -
1. By creating a Batch File (execution.bat) and running the script in the below manner in the case of Robot Framework - 

CALL pybot.bat --variable ENVIRONMENT:{ENVIRONMENT_NAME} --argumentfile {PATH OF ARGUMENT_FILE.ROBOT FILE}
{PATH OF TEST_FILE.ROBOT FILE}

CALL pybot.bat --variable ENVIRONMENT:usiadvr3912 --argumentfile D:\workspace\SQAAutomation\AutomationTeam\Resources\argFile2.robot
D:\workspace\SQAAutomation\AutomationTeam\TestSuites\GDC\Master\Core\Regression\Security.robot

2. By simply giving the below "python" command in the terminal -
 D:\GitHub\Cyanconnode Project\Problem 1 - File Parsing> python .\readCSVFile.py
