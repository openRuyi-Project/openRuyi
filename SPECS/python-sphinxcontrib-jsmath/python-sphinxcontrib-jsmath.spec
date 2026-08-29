# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sphinxcontrib-jsmath

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        Sphinx extension which renders display math in HTML via JavaScript
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-jsmath
VCS:            git:https://github.com/sphinx-doc/sphinxcontrib-jsmath.git
#!RemoteAsset:  sha256:a9925e4a4587247ed2191a22df5f6970656cb8ca2bd6284309578f2153e0c4b8
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sphinxcontrib +auto
# No module named 'docutils'
BuildOption(check):  -e "sphinxcontrib.jsmath*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sphinxcontrib-jsmath is a Sphinx extension which renders display math in
HTML via JavaScript.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
