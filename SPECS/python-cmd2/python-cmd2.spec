# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cmd2

Name:           python-%{srcname}
Version:        2.5.11
Release:        %autorelease
Summary:        Tool for building interactive command line applications in Python
License:        MIT
URL:            https://pypi.org/project/cmd2
VCS:            git:https://github.com/python-cmd2/cmd2.git
#!RemoteAsset:  sha256:30a0d385021fbe4a4116672845e5695bbe56eb682f9096066776394f954a7429
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cmd2 is a tool for building interactive command line applications in Python.
It extends the Python standard library's cmd module so applications gain
features such as command-line history, tab completion, multi-line commands,
shell-like piping/redirection, scripting, and more, while still letting
developers focus on application-specific logic.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
