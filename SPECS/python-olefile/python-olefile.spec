# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname olefile

Name:           python-%{srcname}
Version:        0.47
Release:        %autorelease
Summary:        Parse, read and write Microsoft OLE2 files
License:        BSD-2-Clause AND HPND
URL:            https://github.com/decalage2/olefile
#!RemoteAsset:  sha256:599383381a0bf3dfbd932ca0ca6515acd174ed48870cbf7fee123d698c192c1c
Source0:        https://files.pythonhosted.org/packages/69/1b/077b508e3e500e1629d366249c3ccb32f95e50258b231705c09e3c7a4366/olefile-0.47.zip
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
olefile reads and writes Microsoft OLE2 structured storage files, including
legacy Office documents and image formats containing OLE compound storage.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md doc/
%license LICENSE.txt

%changelog
%autochangelog
