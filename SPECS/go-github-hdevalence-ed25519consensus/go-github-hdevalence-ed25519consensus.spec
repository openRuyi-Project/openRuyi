# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ed25519consensus
%define go_import_path  github.com/hdevalence/ed25519consensus

Name:           go-github-hdevalence-ed25519consensus
Version:        0.2.0
Release:        %autorelease
Summary:        Consensus-compatible Ed25519 verification for Go
License:        BSD-3-Clause
URL:            https://github.com/hdevalence/ed25519consensus
#!RemoteAsset:  sha256:acbfc75768c5808ba79cf425b7f0cc110201e93acafe13ba64db47700050f07b
Source0:        https://github.com/hdevalence/ed25519consensus/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(filippo.io/edwards25519)

%description
Ed25519consensus provides Ed25519 verification compatible with consensus
systems that must preserve historical verification behavior.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
