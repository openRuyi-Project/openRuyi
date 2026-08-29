# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tempora

Name:           python-%{srcname}
Version:        5.9.0
Release:        %autorelease
Summary:        Objects and routines pertaining to date and time
License:        MIT
URL:            https://github.com/jaraco/tempora
VCS:            git:https://github.com/jaraco/tempora.git
#!RemoteAsset:  sha256:66e6ddee320c38f4b253a7d8039337424c699916451b9271e0ccce770a4e8f62
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l tempora +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Objects and routines pertaining to date and time, such as timing, scheduling
and rate-limiting utilities.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
