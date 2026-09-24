# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname azure-identity
%global pypi_name azure_identity

Name:           python-%{srcname}
Version:        1.25.3
Release:        %autorelease
Summary:        Azure Identity client library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity
#!RemoteAsset:  sha256:ab23c0d63015f50b630ef6c6cf395e7262f439ce06e5d07a64e874c724f8d9e6
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l azure +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(azure-core) >= 1.31
BuildRequires:  python3dist(cryptography) >= 2.5
BuildRequires:  python3dist(msal) >= 1.35.1
BuildRequires:  python3dist(msal-extensions) >= 1.2
BuildRequires:  python3dist(setuptools) >= 77.0.3
BuildRequires:  python3dist(typing-extensions) >= 4
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Azure Identity provides Azure Active Directory token credentials for Python
applications using the Azure SDK.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
