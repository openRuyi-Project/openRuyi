# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-secure-stdlib
%define go_import_path  github.com/hashicorp/go-secure-stdlib
%define ver_parseutil   0.1.8
%define ver_strutil     0.1.2
# The legacy aggregate still contains modules whose dependencies are not all
# packaged. Required parseutil/strutil checks below fail on any error.
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-go-secure-stdlib
Version:        0.1.0
Release:        %autorelease
Summary:        Stdlib for HashiCorp Secure products
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-secure-stdlib
#!RemoteAsset:  sha256:b247a695f7e3c3bbd7f3869855a3f9b3dddc0d67a3c777df6e773698f823e61f
Source0:        https://github.com/hashicorp/go-secure-stdlib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:8ab3306fa8c0b7f737a3996d8b3558c7d69062e85d0d43453a1f59658edbb9d0
Source1:        https://github.com/hashicorp/go-secure-stdlib/archive/refs/tags/parseutil/v%{ver_parseutil}.tar.gz#/%{_name}-parseutil-%{ver_parseutil}.tar.gz
#!RemoteAsset:  sha256:c9973177d8b8c46d64038cfba05643f42d523b2bac40b7505bbbe5a551e1eb69
Source2:        https://github.com/hashicorp/go-secure-stdlib/archive/refs/tags/strutil/v%{ver_strutil}.tar.gz#/%{_name}-strutil-%{ver_strutil}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/go-sockaddr)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/ryanuber/go-glob)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/hashicorp/go-secure-stdlib) = %{version}
Provides:       go(github.com/hashicorp/go-secure-stdlib/parseutil) = %{ver_parseutil}
Provides:       go(github.com/hashicorp/go-secure-stdlib/strutil) = %{ver_strutil}

Requires:       go(github.com/hashicorp/go-sockaddr)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/ryanuber/go-glob)

%description
These libraries are maintained by engineers in the HashiCorp's Secure
division as a stdlib for its projects -- Vault, Vault plugins, Boundary,
etc. -- to reduce code duplication and increase consistency.

Each library is its own Go module, although some of them may have
dependencies on others within the repo. The libraries follow Go module
versioning rules.

Most of the libraries in here were originally pulled from
vault/helper/metricsutil, vault/sdk/helper, and vault/internalshared;
see there for contribution and change history prior to their move here.

All modules are licensed according to MPLv2 as contained in the LICENSE
file; this file is duplicated in each module.

%prep -a
# Replace only the two required modules; retain the existing aggregate payload.
mkdir .parseutil .strutil
%{__tar} -xf %{SOURCE1} --strip-components=1 -C .parseutil
%{__tar} -xf %{SOURCE2} --strip-components=1 -C .strutil
rm -rf parseutil strutil
mv .parseutil/parseutil parseutil
mv .strutil/strutil strutil
rm -rf .parseutil .strutil

%check
# Preserve the legacy aggregate's attempted checks and existing tolerance.
%buildsystem_golangmodules_check
# These two modules are required by Vault API and KES and must pass.
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
%__go test %{go_test_flags_default} ./parseutil/... ./strutil/...

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
