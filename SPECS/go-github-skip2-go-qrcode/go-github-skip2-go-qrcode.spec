# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-qrcode
%define go_import_path  github.com/skip2/go-qrcode
%global commit_id da1b6568686e89143e94f980a98bc2dbd5537f13

Name:           go-github-skip2-go-qrcode
Version:        0+git20260911.da1b656
Release:        %autorelease
Summary:        QR Code encoder for Go
License:        MIT
URL:            https://github.com/skip2/go-qrcode
#!RemoteAsset:  sha256:35460d655e1bef07615a38d47295bfa39d08310440d2b4a19cd5b0bedd2c8fd9
Source0:        https://github.com/skip2/go-qrcode/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix go vet: conversion from int to string yields a string of one rune.
Patch2000:      2000-tests-make-rune-conversion-explicit.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/skip2/go-qrcode) = %{version}

%description
Go library for encoding text and binary data as QR Codes with configurable
size and error correction levels.

%prep
%autosetup -n %{_name}-%{commit_id}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
