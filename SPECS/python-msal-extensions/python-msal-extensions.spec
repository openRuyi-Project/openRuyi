# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname msal-extensions
%global pypi_name msal_extensions

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        Extensions for Microsoft Authentication Library
License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-extensions-for-python
#!RemoteAsset:  sha256:c5b0fd10f65ef62b5f1d62f4251d51cbcaf003fcedae8c91b040a488614be1a4
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} +auto
BuildOption(check):    -e %{pypi_name}.libsecret -e %{pypi_name}.osx -e %{pypi_name}.windows

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(msal) >= 1.29
BuildRequires:  python3dist(portalocker) >= 1.4
BuildRequires:  python3dist(portalocker) < 4
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
MSAL Extensions supplies cross-platform token cache persistence helpers for
the Microsoft Authentication Library.

%pyproject_extras_subpkg -n python-%{srcname} portalocker

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
