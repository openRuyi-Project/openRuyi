# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname durationpy

Name:           python-%{srcname}
Version:        0.10
Release:        %autorelease
Summary:        Module for converting between datetime.timedelta and Go's Duration strings
License:        MIT
URL:            https://github.com/icholy/durationpy
VCS:            git:https://github.com/icholy/durationpy.git
#!RemoteAsset:  sha256:1fa6893409a6e739c9c72334fc65cca1f355dbdd93405d30f726deb5bde42fba
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python module for converting between datetime.timedelta and Go's
Duration strings.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
