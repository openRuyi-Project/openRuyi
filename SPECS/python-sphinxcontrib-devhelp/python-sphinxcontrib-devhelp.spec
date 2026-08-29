# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-sphinxcontrib-devhelp
Version:        2.0.0
Release:        %autorelease
Summary:        Sphinx extension for creating Devhelp documents
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-devhelp
#!RemoteAsset:  sha256:411f5d96d445d1d73bb5d52133377b4248ec79db5c793ce7dbe59e074b4dd1ad
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_devhelp/sphinxcontrib_devhelp-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sphinxcontrib +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-sphinxcontrib-devhelp = %{version}-%{release}
%python_provide python3-sphinxcontrib-devhelp

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.

%generate_buildrequires
%pyproject_buildrequires

# We have docutils but we don't have sphinx, so skip the check
%check

%files -f %{pyproject_files}
%doc README.rst
%license LICENCE.rst

%changelog
%autochangelog
