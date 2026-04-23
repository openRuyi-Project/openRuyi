# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-mock
%global pypi_name pytest_mock

Name:           python-%{srcname}
Version:        3.15.1
Release:        %autorelease
Summary:        Thin-wrapper around the mock package for easier use with py.test
License:        MIT
URL:            https://github.com/pytest-dev/pytest-mock
#!RemoteAsset:  sha256:1849a238f6f396da19762269de72cb1814ab44416fa73a8686deac10b0d87a0f
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pytest_mock +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This plugin installs a mocker fixture which is a thin-wrapper
around the patching API provided by the mock package, but with the
benefit of not having to worry about undoing patches at the end of a test.
The mocker fixture has the same API as mock.patch, supporting the
same arguments.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE

%changelog
%autochangelog
