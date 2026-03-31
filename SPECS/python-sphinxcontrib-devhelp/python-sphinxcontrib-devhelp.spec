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
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_devhelp/sphinxcontrib_devhelp-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sphinxcontrib +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-sphinxcontrib-devhelp
%python_provide python3-sphinxcontrib-devhelp

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.

%generate_buildrequires
%pyproject_buildrequires

%check

%files -f %{pyproject_files}
%license LICENCE.rst
%doc README.rst

%changelog
%{?autochangelog}
