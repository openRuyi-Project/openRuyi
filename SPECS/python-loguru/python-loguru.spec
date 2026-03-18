# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname loguru

Name:           python-%{srcname}
Version:        0.7.3
Release:        %autorelease
Summary:        Python logging made (stupidly) simple
License:        MIT
URL:            https://github.com/Delgan/loguru
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  loguru

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Loguru is a library which aims to bring enjoyable logging in Python. It
provides a pre-configured logger with sensible defaults and a simple API
for adding sinks, filtering, and formatting log messages.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%{?autochangelog}
