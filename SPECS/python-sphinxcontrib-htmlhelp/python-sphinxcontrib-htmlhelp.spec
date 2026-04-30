# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sphinxcontrib-htmlhelp
%global pypi_name sphinxcontrib_htmlhelp

Name:           python-%{srcname}
Version:        2.1.0
Release:        %autorelease
Summary:        Sphinx extension for rendering HTML help files
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-htmlhelp
VCS:            git:https://github.com/sphinx-doc/sphinxcontrib-htmlhelp.git
#!RemoteAsset:  sha256:c9e2916ace8aad64cc13a0d233ee22317f2b9025b9cf3295249fa985cc7082e9
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sphinxcontrib +auto
# No module named 'sphinx'
BuildOption(check):  -e sphinxcontrib.htmlhelp

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sphinxcontrib-htmlhelp is a Sphinx extension which renders HTML help
files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENCE.rst

%changelog
%autochangelog
