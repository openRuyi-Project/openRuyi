# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-smtp
%define go_import_path  github.com/emersion/go-smtp

Name:           go-github-emersion-go-smtp
Version:        0.24.0
Release:        %autorelease
Summary:        SMTP client and server library for Go
License:        MIT
URL:            https://github.com/emersion/go-smtp
#!RemoteAsset:  sha256:f6f49bac639a9fd59d7a8b56895f0cdaecaf007e78a75ac76ba2f7ee0ef65b45
Source0:        https://github.com/emersion/go-smtp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Pass dynamically generated authentication commands as data, not formats.
# https://github.com/emersion/go-smtp/pull/302
Patch1:         0001-pass-authentication-commands-as-data.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/emersion/go-sasl)

Provides:       go(github.com/emersion/go-smtp) = %{version}

Requires:       go(github.com/emersion/go-sasl)

%description
Go-smtp implements SMTP and ESMTP clients and servers, including common SMTP
extensions, authentication through go-sasl, UTF-8 messages, and LMTP support.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
