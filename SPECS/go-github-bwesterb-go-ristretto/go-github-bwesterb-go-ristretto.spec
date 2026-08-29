# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ristretto
%define go_import_path  github.com/bwesterb/go-ristretto

Name:           go-github-bwesterb-go-ristretto
Version:        1.2.3
Release:        %autorelease
Summary:        Pure Go implementation of the Ristretto prime-order group
License:        MIT
URL:            https://github.com/bwesterb/go-ristretto
#!RemoteAsset:  sha256:e4b102e50780181e36918afe9009397b63cddfd89771ce37de2d40ece82f2683
Source0:        https://github.com/bwesterb/go-ristretto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bwesterb/go-ristretto) = %{version}

%description
Pure Go implementation of the Ristretto prime-order group built from
Edwards25519.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
