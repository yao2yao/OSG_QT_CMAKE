cmake_minimum_required (VERSION 3.8)

# 项目信息
set (PROJECT_NAME "QTCMAKE")
project (${PROJECT_NAME})

# c++ 11
set (CMAKE_CXX_STANDARD 11)

# osg
set (OSG_DIR ${CMAKE_CURRENT_SOURCE_DIR}/thirdpart/OpenSceneGraph-3.6.5-VC2019-64-Debug)
include_directories (${OSG_DIR}/include)
link_directories (${OSG_DIR}/lib)

# qt
set (CMAKE_AUTOMOC ON)
set (CMAKE_AUTORCC ON)
set (CMAKE_AUTOUIC ON)

set (CMAKE_PREFIX_PATH ${CMAKE_CURRENT_SOURCE_DIR}/thirdpart/qt5.15/msvc2019_64)
message ("pre_path: ${CMAKE_PREFIX_PATH}")

# 自动寻找QT5
find_package (Qt5 COMPONENTS Widgets Core Gui OpenGL REQUIRED)

include_directories (${CMAKE_CURRENT_BINARY_DIR})

# 源文件
set (SRC_FILE
	main.cpp
	QTTEST.cpp
)

# 头文件
set (HEADER_FILE
	QTTEST.h
)

# ui文件
set (UI_FILE
	QTTEST.ui
)

# 资源文件
set (QRC_FILE
	QTTEST.qrc
)

add_executable (${PROJECT_NAME}
	${SRC_FILE}
	${HEADER_FILE}
	${UI_FILE}
	${QRC_FILE}
)

target_link_libraries (${PROJECT_NAME} Qt5::Widgets Qt5::Core Qt5::Gui Qt5::OpenGL)
target_link_libraries(${PROJECT_NAME} debug OpenThreadsd)
target_link_libraries(${PROJECT_NAME} debug osgd)
target_link_libraries(${PROJECT_NAME} debug osgViewerd)
target_link_libraries(${PROJECT_NAME} debug osgDBd)
target_link_libraries(${PROJECT_NAME} debug osgGAd)
target_link_libraries(${PROJECT_NAME} debug osgUtild)
target_link_libraries(${PROJECT_NAME} debug osgQt5d)

set_target_properties (${PROJECT_NAME} PROPERTIES 
    VS_DEBUGGER_ENVIRONMENT "PATH=${CMAKE_CURRENT_SOURCE_DIR}/thirdpart/qt5.15/msvc2019_64/bin;${OSG_DIR}/bin"
)

# 拷贝data到运行目录
file (COPY ${CMAKE_CURRENT_SOURCE_DIR}/data DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/)