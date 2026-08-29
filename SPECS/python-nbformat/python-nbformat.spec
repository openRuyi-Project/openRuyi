# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nbformat

Name:           python-%{srcname}
Version:        5.10.4
Release:        %autorelease
Summary:        Jupyter Notebook format implementation
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbformat
#!RemoteAsset:  sha256:322168b14f937a5d11362988ecac2a4952d3d8e3a2cbeb2319584631226d5b3a
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l nbformat

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(fastjsonschema)
BuildRequires:  python3dist(hatch-nodejs-version)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(jupyter-core)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(traitlets)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Nbformat contains the base implementation and Python APIs for the Jupyter
Notebook file format.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/jupyter-trust

%changelog
%autochangelog
