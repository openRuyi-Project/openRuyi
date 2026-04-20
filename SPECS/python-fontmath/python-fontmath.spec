# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fontmath

Name:           python-%{srcname}
Version:        0.10.0
Release:        %autorelease
Summary:        Math operations on font data
License:        MIT
URL:            https://pypi.org/project/fontMath/
VCS:            git:https://github.com/robotools/fontMath
#!RemoteAsset:  sha256:7b0b39336d83d7fc03fb9dc3c662ef7d26b2c15355a34c643d1cfbd03f89fb74
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l fontMath +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
fontMath provides objects for performing math operations on font data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license License.txt

%changelog
%autochangelog
