import json
import shutil
import os

treeJsonPath = "tree.json"
occSrcPath = "opencascade-7.7.0"
occTarPath = "occ_src"


def getTreeJson():
    srcContent = ""
    with open(treeJsonPath, 'r', encoding='utf-8') as treeInfo:
        for line in treeInfo.readlines():
            srcContent += line
    jsonObject = json.loads(srcContent)
    return jsonObject


def removeTarDir():
    if (os.path.exists(occTarPath)):
        shutil.rmtree(occTarPath)
        print('geTool clean target dir')
    else:
        os.mkdir(occTarPath)
        print('geTool create target dir')


def copyInc():
    srcPath = os.path.join(occSrcPath, 'inc')
    tarPath = os.path.join(occTarPath, 'inc')
    shutil.copytree(srcPath, tarPath)
    print('geTool copy include to target dir')


def getPackageList(path):
    packageList = []
    srcPath = os.path.join(occSrcPath, 'src')
    srcPath = os.path.join(srcPath, path)
    srcPath = os.path.join(srcPath, 'PACKAGES')
    with open(srcPath, 'r', encoding='utf-8') as packages:
        for line in packages.readlines():
            packageList.append(line)
    return packageList


def copySrc():
    jsonObject = getTreeJson()
    for moduleDir in jsonObject:
        moduleTarPath = os.path.join(occTarPath, moduleDir)
        os.mkdir(moduleTarPath)
        for toolKit in jsonObject[moduleDir]:
            toolKitPath = os.path.join(moduleTarPath, toolKit)
            os.mkdir(toolKitPath)
            packages = getPackageList(toolKit)
            for package in packages:
                pStr = package.replace('\n', '')
                srcPath = os.path.join(occSrcPath, 'src')
                srcPath = os.path.join(srcPath, pStr)
                tarPath = os.path.join(toolKitPath, pStr)
                shutil.copytree(srcPath, tarPath)
    print('geTool copy src to target dir')


def generate():
    removeTarDir()
    copyInc()
    copySrc()
    return


generate()
