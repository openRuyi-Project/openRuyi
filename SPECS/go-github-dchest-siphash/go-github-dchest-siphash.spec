# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           siphash
%define go_import_path  github.com/dchest/siphash

Name:           go-github-dchest-siphash
Version:        1.2.3
Release:        %autorelease
Summary:        Go implementation of SipHash-2-4, a fast short-input PRF created by Jean-Philippe Aumasson and Daniel J. Bernstein.
License:        CC0-1.0
URL:            https://github.com/dchest/siphash
#!RemoteAsset
Source0:        https://github.com/dchest/siphash/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dchest/siphash) = %{version}

%description
Go implementation of SipHash-2-4, a fast short-input PRF created by Jean-
Philippe Aumasson and Daniel J. Bernstein

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
