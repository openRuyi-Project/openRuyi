# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
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

BuildOption(check):  -e "fontTools.misc.symfont"
BuildOption(check):  -e "fontTools.pens.freetypePen" -e "fontTools.pens.quartzPen" -e "fontTools.pens.reportLabPen"
BuildOption(check):  -e "fontTools.ttLib.removeOverlaps"
BuildOption(check):  -e "fontTools.varLib.interpolatablePlot" -e "fontTools.varLib.plot"
BuildOption(install):  -l fontTools

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
fontTools is a library for manipulating fonts. It provides tools such as
TTX for converting TrueType and OpenType fonts to and from an XML-based
text format, and also installs utilities for subsetting and merging fonts.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst NEWS.rst
%license LICENSE LICENSE.external
%{_bindir}/fonttools
%{_bindir}/ttx
%{_bindir}/pyftsubset
%{_bindir}/pyftmerge
%{_mandir}/man1/ttx.1*

%changelog
%autochangelog
