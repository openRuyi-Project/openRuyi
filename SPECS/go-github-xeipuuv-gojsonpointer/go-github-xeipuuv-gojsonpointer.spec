# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gojsonpointer
%define go_import_path  github.com/xeipuuv/gojsonpointer
%define commit_id 02993c407bfbf5f6dae44c4f4b1cf6a39b5fc5bb

Name:           go-github-xeipuuv-gojsonpointer
Version:        0+git20260718.02993c4
Release:        %autorelease
Summary:        An implementation of JSON Pointer - Go language
License:        Apache-2.0
URL:            https://github.com/xeipuuv/gojsonpointer
#!RemoteAsset:  sha256:ac83000a2843d5ac25783b256dda3d12533bc860dafc4c35ba2f5d69dbf9556d
Source0:        https://github.com/xeipuuv/gojsonpointer/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xeipuuv/gojsonpointer) = %{version}

%description
An implementation of JSON Pointer - Go language

%files
%doc README.md
%license LICENSE-APACHE-2.0.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
