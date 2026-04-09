# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golang-pdf417
%define go_import_path  github.com/ruudk/golang-pdf417
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id a7e3863a1245aa774317bb96e6c19640b3a9c99e
# Circular dependencies ahead. - 251
%define go_test_exclude_glob github.com/ruudk/golang-pdf417/examples*

Name:           go-github-ruudk-golang-pdf417
Version:        0+git20260106.a7e3863
Release:        %autorelease
Summary:        Port of pdf417-php by ihabunek in Golang
License:        MIT
URL:            https://github.com/ruudk/golang-pdf417
#!RemoteAsset
Source0:        https://github.com/ruudk/golang-pdf417/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/boombuler/barcode)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/ruudk/golang-pdf417) = %{version}

Requires:       go(github.com/boombuler/barcode)
Requires:       go(github.com/stretchr/testify)

%description
This package is a port of (https://github.com/ihabunek/pdf417-php)

This library encodes data to a PixelGrid that can be used to display the
barcode. You can use the PixelGrid to draw the barcode on anything.
Check pdf417_test.go (/pdf417_test.go) for an example.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
