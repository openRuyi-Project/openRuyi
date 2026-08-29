# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname safehttpx

Name:           python-%{srcname}
Version:        0.1.7
Release:        %autorelease
Summary:        A small Python library for SSRF protection
License:        Apache-2.0
URL:            https://github.com/gradio-app/safehttpx
#!RemoteAsset:  sha256:db201c0978c41eddb8bb480f3eee59dd67304fdd91646035e9d9a720049a9d23
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A small Python library created to help developers protect their
applications from Server Side Request Forgery (SSRF) attacks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
