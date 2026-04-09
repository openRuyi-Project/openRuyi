# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mtls
%define go_import_path  aead.dev/mtls

Name:           go-aead-dev-mtls
Version:        0.3.0
Release:        %autorelease
Summary:        A Go library for TLS/HTTPS using public key pinning instead of certificate authorities.
License:        MIT
URL:            https://github.com/aead/mtls
#!RemoteAsset
Source0:        https://github.com/aead/mtls/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(aead.dev/mtls) = %{version}

%description
A Go library for TLS/HTTPS using public key pinning instead of
certificate authorities.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
