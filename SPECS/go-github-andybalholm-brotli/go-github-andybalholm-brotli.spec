# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           brotli
%define go_import_path  github.com/andybalholm/brotli

Name:           go-github-andybalholm-brotli
Version:        1.2.1
Release:        %autorelease
Summary:        Pure Go Brotli encoder and decoder
License:        MIT
URL:            https://github.com/andybalholm/brotli
#!RemoteAsset:  sha256:cf15899856d1d95d1c2ad2d0fe8fb5bd028bf2fa7eb1e13c80ccbb73b3c12170
Source0:        https://github.com/andybalholm/brotli/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/xyproto/randomstring)

Provides:       go(github.com/andybalholm/brotli) = %{version}

Requires:       go(github.com/xyproto/randomstring)

%description
This package is a brotli compressor and decompressor implemented in Go.
It was translated from the reference implementation
((https://github.com/google/brotli)) with the c2go tool at
(https://github.com/andybalholm/c2go).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
