# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname service_identity

Name:           python-service-identity
Version:        24.2.0
Release:        %autorelease
Summary:        Service identity verification for pyOpenSSL
License:        MIT
URL:            https://github.com/pyca/service-identity
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-service-identity = %{version}-%{release}
%python_provide python3-service-identity

%description
service_identity aspires to give you all the tools you need for
verifying whether a certificate is valid for the intended purposes.

In the simplest case, this means host name verification. However,
service_identity implements RFC 6125 fully and plans to add other
relevant RFCs too.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%{?autochangelog}
