# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bokeh

Name:           python-%{srcname}
Version:        3.9.0
Release:        %autorelease
Summary:        Interactive plots and applications in the browser from Python
License:        BSD-3-Clause
URL:            https://bokeh.org
VCS:            git:https://github.com/bokeh/bokeh.git
#!RemoteAsset:  sha256:775219714a8496973ddbae16b1861606ba19fe670a421e4d43267b41148e07a3
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# No module named 'selenium'
BuildOption(check):  -e 'bokeh.io.webdriver'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(bokeh-sampledata)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(contourpy)
BuildRequires:  python3dist(icalendar)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(narwhals)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools-git-versioning)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(xyzservices)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Bokeh is an interactive visualization library for modern web browsers.
It provides elegant, concise construction of versatile graphics.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/typings/
%{_bindir}/bokeh

%changelog
%autochangelog
