# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           seed
%define go_import_path  github.com/sean-/seed
%define commit_id       e2103e2c35297fb7e17febb81e49b312087a2372

Name:           go-github-sean--seed
Version:        0+git20260615.e2103e2
Release:        %autorelease
Summary:        Securely seed Go's random number generator
License:        MIT
URL:            https://github.com/sean-/seed
#!RemoteAsset:  sha256:b29a1625653c2b8eb31a4386890d68170e96049d6e8965fd2f1d883ef4fdaafb
Source0:        https://github.com/sean-/seed/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/sean-/seed) = %{version}

%description
seed provides a helper to securely seed Go's math/rand global generator
from a cryptographically strong source, falling back to a time-based seed.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
