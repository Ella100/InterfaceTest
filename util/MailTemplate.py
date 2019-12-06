import time
import os
import sys
from basic.testcases_keyword import *
from util.operate_excel import OperateExcel

excelObj = OperateExcel()
colorDict = {"pass":"green","failed":"red","none":"orange"}
class ReportTemplate(object):
    #测试报告模板模板2
    def reportTemplate_2(self,statisticsStr,trData):
        htmlStr = '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>测试报告</title>
        <style>
        *{
            margin: 0px;
            padding: 0px;
        }
        body{  
            background-image: url("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1564399482151&di=38f4666ac2e47385f5a5f3402f2104dd&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F7%2F5822c01f84ed0.jpg");
            background-size: 100%,100%;
            /* opacity: 0.9; */
        }
        .body_style {   
            width: 60%;
            height: 100%;
            margin: 0 auto;
            position:absolute;
            left:20%;
            border-left: solid; border-width: 5px;
            border-right: solid; border-width: 5px;
            border-color: #000;
            background-color: rgba(0,0,0,0.3);
        }
        h1{
            text-align:center;
            color:rgb(197,224,178);
            font-family: 微软雅黑;
            letter-spacing: 12px;
            padding-top: 40px;
        }
        table{
            *border-collapse: collapse; /*合并表格边框*/
            border-spacing: 0;
            width: 100%;
            border-style: inset;
            border-width: 2px;
            border-color: #ffffff;
            background-color: #ffffff;
            opacity: 0.9;
        }
        /* 表头样式 */
        .spread{
            background-color: rgb(169,209,141);
            font-family: "Times New Roman"
        }
        .spread:hover{
            cursor: pointer;
            background-color: rgb(110,168,70);
        }
         /* 标题样式 */
        .td_title{
            color: #333;
            font-size: 25px;
        }
        /* 副标题样式 */
        .detail{
            color: red;
            font-family: arial;
            font-size: 5px;
            margin-top: 5px;

        }
        table td,table th{
            border-left: solid 1px  #ccc;
            border-top: 1px solid  #ccc;
            padding: 15px;
            text-align: center;
            font-family: "Courier New";
        }
        /* 下拉标题样式 */
        .title{
            padding: 15px;
            background-color: rgb(169,209,141);
        }
        #distance{
            height: 100px;
        }
        #logo{
            text-align: center;
            position: absolute;
            bottom: 30px;
            right: 0px;
            color: #ffffff;
            font-family: "KaiTi";
        }
        </style>
        <script src="http://libs.baidu.com/jquery/2.1.4/jquery.min.js"></script>
        <script>
            $(function(){
                $(".hide").hide();
                var window_h=$(window).height();//获取窗口大小
                function addWindowHeight() {
                    var h =$(document).height(); //获取当前窗口可视操作区域高度
                    var $bodyHeight = $(".body_style"); //获取body_style盒子的对象
                    $bodyHeight.css("height",h+"px"); //自适应窗口
                }
                function minusWindowHeight(){
                    var h=$("#distance").offset().top+100;//获取当前内容的高度
                    var $bodyHeight = $(".body_style");//获取body_style盒子的高度
                    window_h>h?$bodyHeight.css("height",window_h+"px"):$bodyHeight.css("height",h+"px");//自适应窗口
                }
                $(".spread").attr("flag","true");
                    $(".spread").on("click",function(){
                        if($(this).attr("flag")=="true"){ 
                            $(this).css("background-color","rgb(110,168,70)");
                            $(this).closest(".part").find(".hide").stop().slideDown();
                            $(this).attr("flag","flase");
                            addWindowHeight();
                        }
                        else{
                            $(this).attr("flag","true");
                            $(this).css({"background-color":"rgb(107,167,67)"});
                            $(this).closest(".part").find(".hide").stop().hide();
                            minusWindowHeight(); 
                        }    
                    });

            });
        </script>
        </head>
        <body>
            <div class="body_style">
                <h1>H5自动化测试报告</h1>
                <br>
        '''
        endStr = '''
        <div id="distance"></div> 
                <div id="logo">联云科技·质控部
                    <br/>
                    %s
                </div>        
            </div>  
        </body>
        </html>'''%(time.strftime("%Y-%m-%d"))
        html = htmlStr + statisticsStr + trData + endStr
        with open(parentDirPath+"//testReport_H5_"+time.strftime("%Y%m%d_%H%M%S")+".html","w",encoding="utf-8") as fp:
            fp.write(html)
        return html
    
    #获取结果表格模板2
    def getResult_2(self,excel_files):
        global colorDict
        trDatas = []
        trData = ''
        for excel in excel_files:
            excelObj.loadWorkBook(excel)
            caseSheet = excelObj.getSheetByName("测试用例")
            tableTotal = 0
            tableExecuteNum = 0
            tablePassNum = 0
            passRate = ''
            tableTotal += excelObj.getRowsNumber(caseSheet)-1
            resultCols = excelObj.getColumn(caseSheet,testCase_testResult)
            executeCols = excelObj.getColumn(caseSheet,testCase_isExecute)
            for idx,result in enumerate(resultCols[1:]):
                if result.value == "pass":
                    tablePassNum += 1
            for idx,execute in enumerate(executeCols[1:]):
                if execute.value == "y":
                    tableExecuteNum += 1
            if tableExecuteNum != 0:
                passRate = str(tablePassNum/tableExecuteNum*100)+'%'
            else:
                passRate = '0%'
            excel_name = excel.split('\\')[-1].split('.')[0]
            tbHead = '''
            <table class="part">
                    <tr>
                        <td colspan="5" class="spread">
                            <div class="td_title ">
                                %s测试报告
                            </div>
                            <div class="detail">
                                (总用例数：%s&emsp;&emsp;执行用例总数：%s&emsp;&emsp;通过用例：%s&emsp;&emsp;通过率：%s)
                            </div>
                        </td>
                        <!-- <td class="spread result_col" colspan="1">展开</td> -->
                    </tr>                
                    <tr class="title hide">
                            <td>名称</td>
                            <td>用例描述</td>
                            <td>是否执行</td>
                            <td>执行结束时间</td>
                            <td>结果</td>
                    </tr>
                '''%(excel_name,tableTotal,tableExecuteNum,tablePassNum,passRate)
            trData += tbHead
            for rowNo in range(2,excelObj.getRowsNumber(caseSheet)+1):
                trDatas.append('''
                <tr class="hide">
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td style="color:%s">%s</td>
                </tr> 
                '''% (str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testCaseName)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testCaseName+1)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_isExecute)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_runTime)),\
                        colorDict[excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testResult)],\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testResult)))
                        )
            for data in trDatas:
                trData += data
            trDatas.clear()
            trData += "</table>"
        return trData
    
    #统计用例执行情况
    def statistics(self,excel_files):
        global colorDict
        total = 0
        executeNum = 0
        passNum = 0
        for excel in excel_files:
            excelObj.loadWorkBook(excel)
            caseSheet = excelObj.getSheetByName("测试用例")
            total += excelObj.getRowsNumber(caseSheet)-1
            resultCols = excelObj.getColumn(caseSheet,testCase_testResult)
            executeCols = excelObj.getColumn(caseSheet,testCase_isExecute)
            for idx,result in enumerate(resultCols[1:]):
                if result.value == "pass":
                    passNum += 1
            for idx,execute in enumerate(executeCols[1:]):
                if execute.value == "y":
                    executeNum += 1
        statisticsStr = '''
        <p style="text-align:center;color: red;">用例总数：%s&emsp;&emsp;执行用例数：%s&emsp;&emsp;成功用例数：%s&emsp;&emsp;通过率：%s</p>
        <br>
        '''%(total,executeNum,passNum,str(passNum/executeNum*100)+'%')
        return statisticsStr