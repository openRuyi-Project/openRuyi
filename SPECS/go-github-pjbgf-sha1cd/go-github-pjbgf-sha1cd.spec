# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sha1cd
%define go_import_path  github.com/pjbgf/sha1cd

Name:           go-github-pjbgf-sha1cd
Version:        0.6.0
Release:        %autorelease
Summary:        SHA-1 implementation with collision detection for Go
License:        Apache-2.0
URL:            https://github.com/pjbgf/sha1cd
#!RemoteAsset:  sha256:dda27d0744ab0e561f24b799a7cc1239e4b5cc17fa7c98cc20101659a1557a47
Source0:        https://github.com/pjbgf/sha1cd/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/cpuid/v2)

Provides:       go(github.com/pjbgf/sha1cd) = %{version}

Requires:       go(github.com/klauspost/cpuid/v2)

%description
sha1cd is a Go implementation of SHA-1 with counter-cryptanalysis support for
detecting known collision attacks.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
