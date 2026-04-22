# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mccabe

Name:           python-%{srcname}
Version:        0.7.0
Release:        %autorelease
Summary:        McCabe checker, plugin for flake8
License:        MIT
URL:            https://github.com/PyCQA/mccabe
#!RemoteAsset:  sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides a Flake8 plug-in to compute the McCabe cyclomatic
complexity of Python source code.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
