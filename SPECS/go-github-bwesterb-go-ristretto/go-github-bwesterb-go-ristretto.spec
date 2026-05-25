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
Summary:        Pure Go implementation of the Ristretto prime-order group over Edwards25519
License:        MIT
URL:            https://github.com/bwesterb/go-ristretto
#!RemoteAsset:  sha256:e4b102e50780181e36918afe9009397b63cddfd89771ce37de2d40ece82f2683
Source0:        https://github.com/bwesterb/go-ristretto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-ristretto-1.2.3

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bwesterb/go-ristretto) = %{version}
Provides:       go(github.com/bwesterb/go-ristretto/cref) = %{version}
Provides:       go(github.com/bwesterb/go-ristretto/edwards25519) = %{version}


%description
go-ristretto

Many cryptographic schemes need a group of prime order.  Popular and
efficient elliptic curves like (Edwards25519 of ed25519 fame) are rarely
of prime order.  There is, however, a convenient method to construct a
prime order group from such curves, called Ristretto
(https://ristretto.group) proposed by Mike Hamburg
(https://www.shiftleft.org).

This is a pure Go implementation of the group operations on the
Ristretto prime-order group built from Edwards25519. Documentation is on

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
