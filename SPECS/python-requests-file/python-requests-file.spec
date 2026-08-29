# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname requests_file

Name:           python-requests-file
Version:        3.0.1
Release:        %autorelease
Summary:        Transport adapter for using file:// URLs with python-requests
License:        Apache-2.0
URL:            https://codeberg.org/dashea/requests-file
#!RemoteAsset:  sha256:f14243d7796c588f3521bd423c5dea2ee4cc730e54a3cac9574d78aca1272576
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python)

Provides:       python3-requests-file = %{version}-%{release}
%python_provide python3-requests-file

%description
Requests-File is a transport adapter for use with the Requests Python
library to allow local file system access via file:// URLs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
