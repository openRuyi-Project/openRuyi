# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sphinx

Name:           python-%{srcname}
Version:        9.1.0
Release:        %autorelease
Summary:        Python documentation generator
License:        BSD-2-Clause
URL:            https://www.sphinx-doc.org/
VCS:            git:https://github.com/sphinx-doc/sphinx.git
#!RemoteAsset:  sha256:7741722357dd75f8190766926071fed3bdc211c74dd2d7d4df5404da95930ddb
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# No module named 'pytest'
BuildOption(check):  -e "%{srcname}.testing*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources).  Sphinx uses reStructuredText as
its markup language, and many of its strengths come from the power and
straightforwardness of reStructuredText and its parsing and translating
suite, the Docutils.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst AUTHORS.rst CHANGES.rst
%license LICENSE.rst

%changelog
%autochangelog
