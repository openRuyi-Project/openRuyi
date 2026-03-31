# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sphinxcontrib-serializinghtml

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Sphinx extension to serialize HTML files
License:        BSD-2-clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-serializinghtml
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/sphinxcontrib_serializinghtml-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sphinxcontrib +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
@code{sphinxcontrib-serializinghtml} is a Sphinx extension which outputs
"serialized" HTML files.

%generate_buildrequires
%pyproject_buildrequires

%check

%files -f %{pyproject_files}
%doc README*

%changelog
%{?autochangelog}
