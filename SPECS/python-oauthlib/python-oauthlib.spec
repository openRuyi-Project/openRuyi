# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname oauthlib

Name:           python-%{srcname}
Version:        4.0.1
Release:        %autorelease
Summary:        An implementation of the OAuth request-signing logic
License:        BSD-3-Clause
URL:            https://github.com/oauthlib/oauthlib
#!RemoteAsset:  sha256:3d73febdb6faa00f277c81fb04be7b7586fb96fc3b7f0b9c772dada69a25ede7
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(blinker)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pyjwt)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise OAuth request validation, grant handling and token issuance.
%pytest tests

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
