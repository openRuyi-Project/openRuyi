# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-secure-stdlib
%define go_import_path  github.com/hashicorp/go-secure-stdlib
# TODO: reenable it after adding dependencies - Julian
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-go-secure-stdlib
Version:        0.1.0
Release:        %autorelease
Summary:        Stdlib for HashiCorp Secure products
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-secure-stdlib
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-secure-stdlib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-secure-stdlib) = %{version}

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

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
