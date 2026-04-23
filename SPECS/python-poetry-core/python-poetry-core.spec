# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname poetry_core

Name:           python-poetry-core
Version:        2.1.2
Release:        %autorelease
Summary:        Poetry PEP 517 build back-end
License:        MIT
URL:            https://github.com/python-poetry/poetry-core
#!RemoteAsset:  sha256:f9dbbbd0ebf9755476a1d57f04b30e9aecf71ca9dc2fcd4b17aba92c0002aa04
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  poetry +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-poetry-core = %{version}-%{release}
%python_provide python3-poetry-core

%description
The poetry-core module provides a PEP 517 build back-end
implementation developed for Poetry.  This project is intended to be
a light weight, fully compliant, self-contained package allowing PEP 517
compatible build front-ends to build Poetry managed projects.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE

%changelog
%autochangelog
