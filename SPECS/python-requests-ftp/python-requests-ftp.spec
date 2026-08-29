# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname requests-ftp

Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
Summary:        FTP transport adapter for python-requests
License:        Apache-2.0
URL:            https://github.com/Lukasa/requests-ftp
#!RemoteAsset:  sha256:7504ceb5cba8a5c0135ed738596820a78c5f2be92d79b29f96ba99b183d8057a
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  requests_ftp

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the awesome Requests Python library.

%generate_buildrequires
%pyproject_buildrequires

# pypi release does not have tests
%check

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
