# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gojsonreference
%define go_import_path  github.com/xeipuuv/gojsonreference
%define commit_id bd5ef7bd5415a7ac448318e64f11a24cd21e594b

Name:           go-github-xeipuuv-gojsonreference
Version:        0+git20260718.bd5ef7b
Release:        %autorelease
Summary:        An implementation of JSON Reference - Go language
License:        Apache-2.0
URL:            https://github.com/xeipuuv/gojsonreference
#!RemoteAsset:  sha256:641833c200235d14732c9705ab636d3ef33a52d924b0ab5702fe98a08cf6339e
Source0:        https://github.com/xeipuuv/gojsonreference/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/xeipuuv/gojsonpointer)

Provides:       go(github.com/xeipuuv/gojsonreference) = %{version}

Requires:       go(github.com/xeipuuv/gojsonpointer)

%description
An implementation of JSON Reference - Go language

%files
%doc README.md
%license LICENSE-APACHE-2.0.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
