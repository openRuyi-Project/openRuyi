# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fonttools

Name:           python-%{srcname}
Version:        4.62.1
Release:        %autorelease
Summary:        Tools to manipulate font files
License:        MIT
URL:            https://github.com/fonttools/fonttools
VCS:            git:https://github.com/fonttools/fonttools
#!RemoteAsset:  sha256:e54c75fd6041f1122476776880f7c3c3295ffa31962dc6ebe2543c00dca58b5d
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l fontTools +auto
BuildOption(check):  -e "fontTools.misc.symfont"
BuildOption(check):  -e "fontTools.pens.freetypePen"
BuildOption(check):  -e "fontTools.pens.quartzPen"
BuildOption(check):  -e "fontTools.pens.reportLabPen"
BuildOption(check):  -e "fontTools.ttLib.removeOverlaps"
BuildOption(check):  -e "fontTools.varLib.interpolatablePlot"
BuildOption(check):  -e "fontTools.varLib.plot"

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
FontTools is a library for manipulating fonts, written in Python.

%pyproject_extras_subpkg -n python3-%{srcname} all graphite interpolatable lxml pathops plot repacker symfont type1 ufo unicode woff

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%license LICENSE.external

%changelog
%autochangelog
