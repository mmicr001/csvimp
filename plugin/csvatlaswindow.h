/*
 * This file is part of the xTuple ERP: PostBooks Edition, a free and
 * open source Enterprise Resource Planning software suite,
 * Copyright (c) 1999-2009 by OpenMFG LLC, d/b/a xTuple.
 * It is licensed to you under the Common Public Attribution License
 * version 1.0, the full text of which (including xTuple-specific Exhibits)
 * is available at www.xtuple.com/CPAL.  By using this software, you agree
 * to be bound by its terms.
 */

#ifndef CSVATLASWINDOW_H
#define CSVATLASWINDOW_H

#include "ui_csvatlaswindow.h"

class CSVAtlas;

class CSVAtlasWindow : public QMainWindow, public Ui::CSVAtlasWindow
{
  Q_OBJECT

  public:
    CSVAtlasWindow(QWidget *parent = 0);
    ~CSVAtlasWindow();

    virtual void        closeEvent(QCloseEvent *e);

  public slots:
    virtual void        fileNew();
    virtual void        fileOpen();
    virtual void        filePrint();
    virtual void        fileSave();
    virtual void        fileSaveAs();
    virtual CSVAtlas   *getAtlas();
    virtual void        helpAbout();
    virtual void        helpContents();
    virtual void        helpIndex();
    virtual void        sAddMap();
    virtual void        sDeleteMap();
    virtual void        sMapChanged( int );
    virtual void        sRenameMap();

  protected slots:
    virtual void languageChange();

  protected:
    CSVAtlas *_atlas;
    QString   _filename;
    QString   _selectedMap;
};

#endif