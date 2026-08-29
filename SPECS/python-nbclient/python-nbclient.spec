# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nbclient

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        Client library for executing Jupyter notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbclient
#!RemoteAsset:  sha256:04a134a5b087f2c5887f228aca155db50169b8cd9334dee6942c8e927e56081a
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l nbclient

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(jupyter-core)
BuildRequires:  python3dist(nbformat)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(traitlets)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
nbclient is a client library for executing Jupyter notebooks and handling
their kernel messages.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jupyter-execute

%changelog
%autochangelog
