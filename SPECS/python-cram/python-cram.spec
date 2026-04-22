# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cram

Name:           python-%{srcname}
Version:        0.7
Release:        %autorelease
Summary:        Simple testing framework for command line applications
License:        GPL-2.0-or-later
URL:            https://bitheap.org/cram/
VCS:            git:https://github.com/aiiie/cram
#!RemoteAsset:  sha256:7da7445af2ce15b90aad5ec4792f857cef5786d71f14377e9eb994d8b8337f2f
Source:         https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Cram is a functional testing framework for command line applications. Cram
tests look like snippets of interactive shell sessions. Cram runs each command
and compares the command output in the test with the command's actual output.

%prep -a
%py3_shebang_fix scripts/cram

%generate_buildrequires
%pyproject_buildrequires

%check -a
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHON=%{__python3} scripts/cram -v tests

%files -f %{pyproject_files}
%license COPYING.txt
%doc NEWS.rst README.rst TODO.md
%{_bindir}/cram

%changelog
%autochangelog
