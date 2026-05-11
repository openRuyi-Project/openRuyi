# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname polib

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Library to manipulate gettext files
License:        MIT
URL:            https://github.com/izimobil/polib/
VCS:            git:https://github.com/izimobil/polib.git
#!RemoteAsset:  sha256:f3ef94aefed6e183e342a8a269ae1fc4742ba193186ad76f175938621dbfc26b
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
polib is a library to manipulate, create, and modify gettext files such as
POT, PO, and MO files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGELOG
%license LICENSE

%changelog
%autochangelog
