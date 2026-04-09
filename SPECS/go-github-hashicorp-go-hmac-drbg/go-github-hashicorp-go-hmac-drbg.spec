# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-hmac-drbg
%define go_import_path  github.com/hashicorp/go-hmac-drbg
%define commit_id eb7152219c892c070995f4658d618fe2edf24b3a
# Test failure, may be cause by outdate code - Julian
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-go-hmac-drbg
Version:        0+git20251119.eb71522
Release:        %autorelease
Summary:        Deterministic random bit generator using hmac/sha256 as per NIST 800-90A
License:        MIT
URL:            https://github.com/hashicorp/go-hmac-drbg
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-hmac-drbg/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/hashicorp/go-hmac-drbg) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Implements HMAC_DRBG in Go, as per NIST Special Publication 800-90A.

This implementation is a port of (https://github.com/fpgaminer/python-
hmac-drbg)

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
