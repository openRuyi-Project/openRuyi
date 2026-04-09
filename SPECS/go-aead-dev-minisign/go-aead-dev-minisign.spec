# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           minisign
%define go_import_path  aead.dev/minisign

Name:           go-aead-dev-minisign
Version:        0.3.0
Release:        %autorelease
Summary:        A dead simple tool to sign files and verify digital signatures.
License:        MIT
URL:            https://github.com/aead/minisign
#!RemoteAsset
Source0:        https://github.com/aead/minisign/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(aead.dev/minisign) = %{version}

%description
minisign is a dead simple tool to sign files and verify signatures.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
