# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sphinxcontrib-applehelp
%global pypi_name sphinxcontrib_applehelp

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Sphinx extension for creating Apple help books
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-applehelp
VCS:            git:https://github.com/sphinx-doc/sphinxcontrib-applehelp.git
#!RemoteAsset:  sha256:2f29ef331735ce958efa4734873f084941970894c6090408b079c61b2e1c06d1
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sphinxcontrib +auto
# No module named 'sphinx'
BuildOption(check):  -e sphinxcontrib.applehelp

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sphinxcontrib-applehelp is a Sphinx extension which outputs Apple help
books.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENCE.rst

%changelog
%autochangelog
