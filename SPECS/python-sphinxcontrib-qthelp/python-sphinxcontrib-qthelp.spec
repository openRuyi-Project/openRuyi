# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sphinxcontrib-qthelp
%global pypi_name sphinxcontrib_qthelp

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Sphinx extension for creating Qt help files
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-qthelp
VCS:            git:https://github.com/sphinx-doc/sphinxcontrib-qthelp.git
#!RemoteAsset:  sha256:4fe7d0ac8fc171045be623aba3e2a8f613f8682731f9153bb2e40ece16b9bbab
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sphinxcontrib +auto
# No module named 'docutils'
BuildOption(check):  -e sphinxcontrib.qthelp

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sphinxcontrib-qthelp is a Sphinx extension which outputs Qt help
documents.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENCE.rst

%changelog
%autochangelog
