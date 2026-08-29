# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tox

Name:           python-%{srcname}
Version:        4.24.1
Release:        %autorelease
Summary:        Virtual environments management and test command line tool
License:        MIT
URL:            https://tox.wiki
VCS:            git:https://github.com/tox-dev/tox.git
#!RemoteAsset:  sha256:083a720adbc6166fff0b7d1df9d154f9d00bfccb9403b8abf6bc0ee435d6a62e
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# The default pyproject check in openRuyi is an import smoke test. Exclude the
# Windows-only helper module and the optional pytest integration module.
BuildOption(check):  -e tox.execute.local_sub_process.read_via_thread_windows
BuildOption(check):  -e tox.pytest
BuildOption(check):  tox
BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hatch-vcs)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
tox is a generic virtual environment management and test command line tool you
can use for:
* checking that your package installs correctly with different Python versions
  and interpreters
* running your tests in each of the environments, configuring your test tool of
  choice
* acting as a frontend to Continuous Integration servers, greatly reducing
  boilerplate and merging CI and shell-based testing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/tox

%changelog
%autochangelog
