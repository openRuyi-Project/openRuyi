# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fontpens

Name:           python-%{srcname}
Version:        0.4.0
Release:        %autorelease
Summary:        A collection of classes implementing the pen protocol for manipulating glyphs
License:        BSD-3-Clause
URL:            https://pypi.org/project/fontPens/
VCS:            git:https://github.com/robotools/fontPens.git
#!RemoteAsset:  sha256:69be9a81087dd59f1b8dee3f1fc8f7cd4693980ab45852feb496cbb28fbd93cb
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l fontPens

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A collection of classes implementing the pen protocol for manipulating glyph outlines.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
