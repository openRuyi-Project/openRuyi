# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bottle

Name:           python-%{srcname}
Version:        0.13.4
Release:        %autorelease
Summary:        Fast and simple WSGI-framework for small web-applications
License:        MIT
URL:            https://bottlepy.org/
VCS:            git:https://github.com/bottlepy/bottle.git
#!RemoteAsset:  sha256:787e78327e12b227938de02248333d788cfe45987edca735f8f88e03472c3f47
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Bottle is a fast, simple and lightweight WSGI micro web-framework for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/bottle
%{_bindir}/bottle.py

%changelog
%autochangelog
