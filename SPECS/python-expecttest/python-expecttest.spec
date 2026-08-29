# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname expecttest

Name:           python-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        A python test utility
License:        MIT
URL:            https://github.com/ezyang/expecttest
#!RemoteAsset:  sha256:6e8512fb86523ada1f94fd1b14e280f924e379064bb8a29ee399950e513eeccd
Source:         https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-scm)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This library implements expect tests (also known as "golden" tests).
Expect tests are a method of writing tests where instead of hard-coding
the expected output of a test, you run the test to get the output, and
the test framework automatically populates the expected output. If the
output of the test changes, you can rerun the test with the environment
variable EXPECTTEST_ACCEPT=1 to automatically update the expected output.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
