# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname termcolor

Name:           python-%{srcname}
Version:        3.3.0
Release:        %autorelease
Summary:        ANSI color formatting for output in terminal
License:        MIT
URL:            https://github.com/termcolor/termcolor
#!RemoteAsset:  sha256:348871ca648ec6a9a983a13ab626c0acce02f515b9e1983332b17af7979521c5
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ANSI color formatting for output in terminal.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license COPYING.txt

%changelog
%autochangelog
