# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname configshell-fb
%global pypi_name configshell_fb

Name:           python-%{srcname}
Version:        2.0.3
Release:        %autorelease
Summary:        A framework to implement simple but nice CLIs
License:        Apache-2.0
URL:            https://github.com/open-iscsi/configshell-fb
#!RemoteAsset:  sha256:dbb086c16c1603a230f9017ef85baccabfd5d87439a01e963377e50f10220f53
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l configshell configshell_fb

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
configshell is a Python library that provides a framework for building
simple but nice CLI-based applications, such as targetcli and spdk-cli.

%prep -a
# the sdist lacks the configshell_fb symlink the wheel ships
ln -s configshell configshell_fb

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
