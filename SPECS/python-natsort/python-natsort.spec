# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname natsort

Name:           python-%{srcname}
Version:        8.4.0
Release:        %autorelease
Summary:        Simple yet flexible natural sorting in Python
License:        MIT
URL:            https://github.com/SethMMorton/natsort
VCS:            git:https://github.com/SethMMorton/natsort.git
#!RemoteAsset:  sha256:45312c4a0e5507593da193dedd04abb1469253b601ecaf63445ad80f0a1ea581
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
When you try to sort a list of strings that contain numbers, the normal
python sort algorithm sorts lexicographically, which is often not what
you want. natsort provides a function natsorted that helps sort lists
"naturally" ("naturally" is rather ill-defined, but in general it means
sorting based on meaning and not computer code point).

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/natsort

%changelog
%autochangelog
