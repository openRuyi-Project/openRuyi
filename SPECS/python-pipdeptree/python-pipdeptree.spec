# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pipdeptree

Name:           python-%{srcname}
Version:        2.30.0
Release:        %autorelease
Summary:        Command line utility to show dependency tree of packages
License:        MIT
URL:            https://github.com/naiquevin/pipdeptree
#!RemoteAsset:  sha256:0f78fe4bcf36a72d0d006aee0f4e315146cb278e4c4d51621f370a3d6b8861c1
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# remove graphviz test
Patch0:         0001-remove-graphviz-test.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(virtualenv)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pipdeptree is a command line utility for displaying the installed python
packages in form of a dependency tree. It works for packages installed
globally on a machine as well as in a virtualenv.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -vvv -k "not test_console and not test_custom_interpreter"

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pipdeptree

%changelog
%autochangelog
