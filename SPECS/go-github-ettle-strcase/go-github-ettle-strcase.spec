# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           strcase
%define go_import_path  github.com/ettle/strcase

Name:           go-github-ettle-strcase
Version:        0.2.0
Release:        %autorelease
Summary:        String case conversion library for Go
License:        MIT
URL:            https://github.com/ettle/strcase
#!RemoteAsset:  sha256:353ad93d666b5f464d62da992b2874363d2862e581d5f3fd9151ab103aaa31a1
Source0:        https://github.com/ettle/strcase/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/asaskevich/govalidator)
BuildRequires:  go(github.com/fatih/camelcase)
BuildRequires:  go(github.com/iancoleman/strcase)
BuildRequires:  go(github.com/segmentio/go-camelcase)
BuildRequires:  go(github.com/stoewer/go-strcase)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/ettle/strcase) = %{version}

%description
Strcase converts strings between snake, camel, Pascal, kebab, and custom word
case formats, with Unicode and Go initialism support.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
