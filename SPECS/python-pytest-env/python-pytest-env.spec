# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest_env

Name:           python-pytest-env
Version:        1.1.5
Release:        %autorelease
Summary:        Pytest plugin that allows you to add environment variables
License:        MIT
URL:            https://github.com/MobileDynasty/pytest-env
#!RemoteAsset:  sha256:91209840aa0e43385073ac464a554ad2947cc2fd663a9debf88d03b01e0cc1cf
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-pytest-env = %{version}-%{release}
%python_provide python3-pytest-env

%description
This is a py.test plugin that enables you to set environment
variables in the pytest.ini file.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
