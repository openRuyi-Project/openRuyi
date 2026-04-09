# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hil
%define go_import_path  github.com/hashicorp/hil
%define commit_id 0985b598d4331dc17d97f62c1bfa9bbc3f3eb5ae

Name:           go-github-hashicorp-hil
Version:        0+git20260202.0985b59
Release:        %autorelease
Summary:        HIL is a small embedded language for string interpolations.
License:        MPL-2.0
URL:            https://github.com/hashicorp/hil
#!RemoteAsset
Source0:        https://github.com/hashicorp/hil/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)

Provides:       go(github.com/hashicorp/hil) = %{version}

Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/mitchellh/reflectwalk)

%description
HIL (HashiCorp Interpolation Language) is a lightweight embedded
language used primarily for configuration interpolation. The goal of HIL
is to make a simple language for interpolations in the various
configurations of HashiCorp tools.

HIL is built to interpolate any string, but is in use by HashiCorp
primarily with HCL (https://github.com/hashicorp/hcl). HCL is *not
required* in any way for use with HIL.

HIL isn't meant to be a general purpose language. It was built for basic
configuration interpolations. Therefore, you can't currently write
functions, have conditionals, set intermediary variables, etc. within
HIL itself. It is possible some of these may be added later but the
right use case must exist.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
