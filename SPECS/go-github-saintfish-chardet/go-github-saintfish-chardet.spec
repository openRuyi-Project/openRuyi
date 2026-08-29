# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           chardet
%define go_import_path  github.com/saintfish/chardet
%define commit_id       5e3ef4b5456d

Name:           go-github-saintfish-chardet
Version:        0+git20260719.5e3ef4b
Release:        %autorelease
Summary:        Charset detector library for golang derived from ICU
License:        MIT
URL:            https://github.com/saintfish/chardet
#!RemoteAsset:  sha256:7a0eb7ca17da0d98132dfc4fab1541c082dc290980dea73449431c408bf214a8
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/saintfish/chardet/pull/12 - Jvle
Patch2000:      2000-test-fix-text-detector-example-name.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/saintfish/chardet) = %{version}

%description
chardet is library to automatically detect charset of texts for
Go programming language. It's based on the algorithm and data
in ICU's implementation.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
