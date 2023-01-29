#include "QTTEST.h"
#include <QtWidgets/QApplication>
#include <osgQt/GraphicsWindowQt>
#include <osgViewer/Viewer>
#include <osg/Geode>
#include <osg/Node>
#include <osg/Group>
#include <osgGA/StateSetManipulator>
#include <osgGA/TrackballManipulator>
#include <osgDB/ReadFile>
#include <QGridLayout>
#include <QGLWidget>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
	QTTEST w;

	osg::ref_ptr<osgViewer::Viewer> viewer = new osgViewer::Viewer;
	osg::ref_ptr<osg::Group> root = new osg::Group;
	osg::ref_ptr<osg::Node> node = osgDB::readNodeFile("data\\cow.osg");
	root->addChild(node);

	viewer->setSceneData(root.get());
	viewer->setCameraManipulator(new osgGA::TrackballManipulator);

	osgQt::setViewer(viewer.get());
	osgQt::GLWidget* glw = new osgQt::GLWidget;
	osgQt::GraphicsWindowQt* graphicswin = new osgQt::GraphicsWindowQt(glw);
	graphicswin->setCursor(osgQt::GraphicsWindowQt::MouseCursor::HandCursor);
	viewer->getCamera()->setViewport(new osg::Viewport(0, 0, glw->width(), glw->height()));
	viewer->getCamera()->setGraphicsContext(graphicswin);
	viewer->setThreadingModel(osgViewer::ViewerBase::SingleThreaded);

	QGridLayout* grid = new QGridLayout;
	grid->addWidget(glw);
	grid->setSpacing(0);
	grid->setContentsMargins(0, 0, 0, 0);

	w.ui.listWidget->setLayout(grid);
	w.show();
    return a.exec();
}
