# -*- coding: utf-8 -*-
from __future__ import division
from art import tprint
VERSION="0.4"
PARAMS_DESCRIPTION={"TPR":"sensitivity, recall, hit rate, or true positive rate","TNR":"specificity or true negative rate",
                   "PPV":"precision or positive predictive value","NPV":"negative predictive value",
                   "FNR":"miss rate or false negative rate","FPR":"fall-out or false positive rate",
                   "FDR":"false discovery rate","FOR":"false omission rate","ACC":"accuracy",
                   "F1":"F1 Score - harmonic mean of precision and sensitivity","MCC":"Matthews correlation coefficient",
                   "BM":"Informedness or Bookmaker Informedness","MK":"Markedness","LR+":"Positive likelihood ratio",
                   "LR-":"Negative likelihood ratio","DOR":"Diagnostic odds ratio","TP":"true positive/hit",
                    "TN":"true negative/correct rejection","FP":"false positive/Type I error/false alarm",
                    "FN":"false negative/miss/Type II error","P":"Condition positive","N":"Condition negative",
                    "TOP":"Test outcome positive","TON":"Test outcome negative","POP":"Population","PRE":"Prevalence",
                    "G":"G-measure geometric mean of precision and sensitivity","RACC":"Random Accuracy",
                    "F0.5":"F0.5 Score","F2":"F2 Score","ERR":"Error Rate"}

def html_init(name):
    '''
    This function return report  file first lines
    :param name: name of file
    :type name : str
    :return: html_init as str
    '''
    result=""
    result+="<html>\n"
    result+="<head>\n"
    result+="<title>"+str(name)+"</title>\n"
    result+="</head>\n"
    result+="<body>\n"
    result+='<h1 style="border-bottom:1px solid black;text-align:center;">Report</h1>'
    return result

def html_table(classes,table):
    '''
    This function return report file confusion matrix
    :param classes: matrix classes
    :type classes: list
    :param table: matrix
    :type table : dict
    :return: html_table as str
    '''
    result=""
    result += "<h2>Confusion Matrix : </h2>\n"
    result+='<table>\n'
    result +='<tr  align="center">' + "\n"
    result +='<td>Actual</td>\n'
    result +='<td>Predict\n'
    result +='<table style="border:1px solid black;border-collapse: collapse;">\n'
    classes.sort()
    result +='<tr align="center">\n<td></td>\n'
    part_2=""
    for i in classes:
        result += '<td style="border:1px solid black;padding:10px;">' + str(i) + '</td>\n'
        part_2+='<tr align="center">\n'
        part_2 +='<td style="border:1px solid black;padding:10px;">' + str(i) + '</td>\n'
        for j in classes:
            part_2 +='<td>' + str(table[i][j]) + '</td>\n'
        part_2 +="</tr>\n"
    result += '</tr>\n'
    part_2 +="</table>\n</td>\n</tr>\n</table>\n"
    result+=part_2
    return result

def html_overall_stat(overall_stat):
    '''
    This function return report file overall stat
    :param overall_stat: overall stat
    :type overall_stat : dict
    :return: html_overall_stat as str
    '''
    result=""
    result+="<h2>Overall Statistics : </h2>\n"
    result +='<table style="border:1px solid black;border-collapse: collapse;">\n'
    for i in overall_stat.keys():
        result +='<tr align="center">\n'
        result +='<td style="border:1px solid black;padding:4px;">' + str(i) + '</td>\n'
        result +='<td style="border:1px solid black;padding:4px;">' + rounder(overall_stat[i]) + '</td>\n'
        result +="</tr>\n"
    result +="</table>\n"
    return result

def html_class_stat(classes,class_stat):
    '''
    This function return report file class_stat
    :param classes: matrix classes
    :type classes: list
    :param class_stat: class stat
    :type class_stat:dict
    :return: html_class_stat as str
    '''
    result=""
    result+="<h2>Class Statistics : </h2>\n"
    result +='<table style="border:1px solid black;border-collapse: collapse;">\n'
    result +='<tr align="center">\n<td>Class</td>\n'
    for i in classes:
        result +='<td style="border:1px solid black;padding:4px;border-collapse: collapse;">' + str(i) + '</td>\n'
    result += '<td>Description</td>\n'
    result +='</tr>\n'
    for i in class_stat.keys():
        result +='<tr align="center" style="border:1px solid black;border-collapse: collapse;">\n'
        result +='<td style="border:1px solid black;padding:4px;border-collapse: collapse;">' + str(i) + '</td>\n'
        for j in classes:
            result +='<td style="border:1px solid black;padding:4px;border-collapse: collapse;">' + rounder(
                class_stat[i][j]) + '</td>\n'
        result += '<td style="border:1px solid black;padding:4px;border-collapse: collapse;">' + \
                  PARAMS_DESCRIPTION[i] + '</td>\n'
        result +="</tr>\n"
    result+="</table>\n"
    return result

def html_end(version):
    '''
    This function return report file end lines
    :param version: pycm version
    :type version:str
    :return: html_end as str
    '''
    result="</body>\n"
    result+="</html>"
    result+='<p style="text-align:center;position:absoloute;border-top:1px solid black;">Generated By ' \
            '<a href="http://pycm.shaghighi.ir">PYCM</a> Version '+version+'</p>'
    return result

def html_maker(html_file,name,classes,table,overall_stat,class_stat):
    '''
    This function create html report
    :param html_file : file object of html
    :type html_file: file object
    :param name: file name
    :type name : str
    :param classes: matrix classes
    :type classes: list
    :param table: matrix
    :type table: dict
    :param overall_stat: overall stat
    :type overall_stat: dict
    :param class_stat: class stat
    :type class_stat: dict
    :return: None
    '''
    html_file.write(html_init(name))
    html_file.write(html_table(classes,table))
    html_file.write(html_overall_stat(overall_stat))
    html_file.write(html_class_stat(classes,class_stat))
    html_file.write(html_end(VERSION))

def isfloat(value):
    '''
    This function check input for float conversion
    :param value: input value
    :type value:str
    :return: True if input_value is a number and False otherwise
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False

def rounder(input_number,digit=5):
    '''
    This function round input number
    :param input_number: input number
    :type input_number : anything
    :param digit: precision
    :type digit : int
    :return: round number as float
    '''
    if isfloat(input_number)==True:
        return str(round(input_number,digit))
    else:
        return input_number
def pycm_help():
    '''
    This function print pycm details
    :return: None
    '''
    tprint("pycm")
    tprint("V:"+VERSION)
    print("Repo : https://github.com/sepandhaghighi/pycm")
    print("Webpage : http://pycm.shaghighi.ir")


def table_print(classes,table):
    '''
    This function print confusion matrix
    :param classes: classes list
    :type classes:list
    :param table: table
    :type table:dict
    :return: printable table as str
    '''
    classes_len=len(classes)
    result = "Predict" + 10 * " " + "%-9s" * classes_len % tuple(map(str,classes)) + "\n"
    result = result + "Actual\n"
    classes.sort()
    for key in classes:
        row=[table[key][i] for i in classes]
        result += str(key) + " " * (17 - len(str(key))) + "%-9s" * classes_len % tuple(
            map(str, row)) + "\n"
    return result

def normalized_table_print(classes,table):
    '''
    This function print normalized confusion matrix
    :param classes: classes list
    :type classes:list
    :param table: table
    :type table:dict
    :return: printable table as str
    '''
    classes_len=len(classes)
    result = "Predict" + 10 * " " + "%-15s" * classes_len % tuple(map(str,classes)) + "\n"
    result = result + "Actual\n"
    classes.sort()
    for key in classes:
        row=[table[key][i] for i in classes]
        div=sum(row)
        if sum(row)==0:
            div=1
        result += str(key) + " " * (17 - len(str(key))) + "%-15s" * classes_len % tuple(
        map(lambda x:str(round(x/div,5)), row)) + "\n"
    return result

def stat_print(classes,class_stat,overall_stat):
    '''
    This function print statistics
    :param classes: classes list
    :type classes:list
    :param class_stat: statistic result for each class
    :type class_stat:dict
    :param overall_stat : overall statistic result
    :type overall_stat:dict
    :return: printable result as str
    '''
    shift = max(map(len, PARAMS_DESCRIPTION.values())) + 5
    classes_len=len(classes)
    result = "Overall Statistics : "+"\n\n"
    overall_stat_keys = list(overall_stat.keys())
    overall_stat_keys.sort()
    for key in overall_stat_keys:
        result += key + " " * (
        shift - len(key) + 7) + rounder(overall_stat[key]) + "\n"
    result +="\nClass Statistics :\n\n"
    result += "Classes" + shift * " " + "%-24s" * classes_len % tuple(map(str, classes)) + "\n"
    class_stat_keys = list(class_stat.keys())
    class_stat_keys.sort()
    classes.sort()
    for key in class_stat_keys:
        row=[class_stat[key][i] for i in classes]
        result += key + "(" + PARAMS_DESCRIPTION[key] + ")" + " " * (
        shift - len(key) - len(PARAMS_DESCRIPTION[key]) + 5) + "%-24s" * classes_len % tuple(
            map(rounder,row)) + "\n"
    return result